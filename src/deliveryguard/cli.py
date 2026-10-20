"""Small JSON-manifest CLI for deterministic requirement checks."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .traceability import validate_requirements

def main() -> int:
    parser = argparse.ArgumentParser(prog="deliveryguard", description="Validate requirement traceability structure.")
    parser.add_argument("manifest", type=Path, help="Path to JSON file containing a list of requirements or {requirements: [...]}.")
    parser.add_argument("--json-out", type=Path, help="Optional path for machine-readable findings.")
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(f"Cannot read valid JSON manifest: {exc}")
    requirements = data if isinstance(data, list) else data.get("requirements") if isinstance(data, dict) else None
    if not isinstance(requirements, list):
        parser.error("Manifest must be a list or an object with a 'requirements' list.")
    findings = [f.to_dict() for f in validate_requirements(requirements)]
    output = {"status": "FAIL" if any(f["status"] == "FAIL" and f["severity"] == "error" for f in findings) else ("UNKNOWN" if any(f["status"] == "UNKNOWN" for f in findings) else "PASS"), "findings_count": len(findings), "findings": findings}
    rendered = json.dumps(output, ensure_ascii=False, indent=2)
    print(rendered)
    if args.json_out:
        args.json_out.write_text(rendered + "\n", encoding="utf-8")
    return 1 if output["status"] == "FAIL" else 0

if __name__ == "__main__":
    raise SystemExit(main())
