"""Deterministic traceability checks for a project requirements manifest."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any
import re

ID_PATTERN = re.compile(r"^(FR|BR|NFR|ERR)-[0-9]{3,}$")

@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    status: str
    item_id: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

def validate_requirements(requirements: list[dict[str, Any]]) -> list[Finding]:
    """Check IDs, required fields, acceptance criteria and test/code references.

    This validates structural traceability only; it does not prove semantic correctness
    or that referenced tests have actually passed.
    """
    findings: list[Finding] = []
    seen: dict[str, int] = {}
    for index, req in enumerate(requirements):
        item_id = str(req.get("id", f"<row:{index + 1}>"))
        if not ID_PATTERN.fullmatch(item_id):
            findings.append(Finding("DG-TR-001", "error", "FAIL", item_id,
                                    "Requirement ID must match FR-/BR-/NFR-/ERR- followed by at least three digits."))
        seen[item_id] = seen.get(item_id, 0) + 1
        for field in ("type", "title", "status", "source"):
            if field not in req or req[field] in (None, "", [], {}):
                findings.append(Finding("DG-TR-002", "error", "FAIL", item_id,
                                        f"Required field is missing or empty: {field}."))
        if not req.get("acceptance_criteria"):
            findings.append(Finding("DG-TR-003", "warning", "FAIL", item_id,
                                    "No acceptance criteria are linked."))
        if not req.get("test_refs"):
            findings.append(Finding("DG-TR-004", "warning", "FAIL", item_id,
                                    "No test references are linked."))
        if not req.get("code_refs"):
            findings.append(Finding("DG-TR-005", "info", "UNKNOWN", item_id,
                                    "No code references are linked; implementation coverage is unknown."))
        source = req.get("source")
        if isinstance(source, dict) and source.get("kind") in ("inferred", "unknown"):
            findings.append(Finding("DG-GOV-001", "warning", "UNKNOWN", item_id,
                                    "Requirement source is inferred or unknown; human confirmation is needed."))
    for item_id, count in seen.items():
        if count > 1:
            findings.append(Finding("DG-TR-006", "error", "FAIL", item_id,
                                    f"Duplicate requirement ID appears {count} times."))
    return findings
