"""Heuristic documentation drift detection from changed paths.

This first version is deterministic and intentionally conservative: it flags
potentially affected artifact categories; it does not claim semantic mismatch.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import PurePosixPath
from typing import Iterable

@dataclass(frozen=True)
class DriftFinding:
    rule_id: str
    severity: str
    status: str
    changed_path: str
    affected_artifact: str
    reason: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

API_SUFFIXES = (".yaml", ".yml", ".openapi.json")
DB_MARKERS = ("migration", "migrations", "schema", "models", "entity", "entities")
TEST_MARKERS = ("test_", "_test.", "/tests/")

def _is_api_contract(path: str) -> bool:
    p = path.lower()
    return p.endswith(API_SUFFIXES) and ("openapi" in p or "swagger" in p or "api" in p)

def analyze_changed_paths(paths: Iterable[str]) -> list[DriftFinding]:
    """Return potential drift findings for a list of changed repository paths."""
    findings: list[DriftFinding] = []
    normalized = sorted({str(PurePosixPath(p)).replace("\\", "/").lstrip("./") for p in paths if str(p).strip()})
    for path in normalized:
        low = path.lower()
        if low.startswith(("docs/", "doc/")) or "/docs/" in low:
            continue
        if _is_api_contract(low):
            findings.append(DriftFinding("DG-DRIFT-API-001", "warning", "UNKNOWN", path,
                "API documentation and contract tests",
                "API/OpenAPI contract changed; review linked API docs, generated clients and contract tests."))
        elif any(marker in low for marker in DB_MARKERS) and ("/" in low or low.endswith((".sql", ".py", ".prisma"))):
            findings.append(DriftFinding("DG-DRIFT-DB-001", "warning", "UNKNOWN", path,
                "ERD, data dictionary and migration guide",
                "Database/model/migration path changed; review data model documentation and migration notes."))
        elif low.endswith((".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".java", ".rs", ".cs")) and not any(m in low for m in TEST_MARKERS):
            findings.append(DriftFinding("DG-DRIFT-CODE-001", "info", "UNKNOWN", path,
                "Requirements, design docs and regression tests",
                "Implementation code changed; impact is unknown until requirement links and test evidence are evaluated."))
        elif any(m in low for m in TEST_MARKERS):
            findings.append(DriftFinding("DG-DRIFT-TEST-001", "info", "UNKNOWN", path,
                "Test plan and acceptance evidence",
                "Test asset changed; review test coverage, execution result and acceptance evidence."))
    return findings
