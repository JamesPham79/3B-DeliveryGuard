"""CLI for conservative changed-path drift analysis."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .drift import analyze_changed_paths

def main() -> int:
    parser = argparse.ArgumentParser(prog="deliveryguard-drift", description="Flag likely documentation impact from changed paths.")
    parser.add_argument("paths", nargs="*", help="Changed repository paths.")
    parser.add_argument("--paths-file", type=Path, help="Optional newline-delimited changed-path file.")
    parser.add_argument("--json-out", type=Path, help="Optional JSON output file.")
    args = parser.parse_args()
    paths = list(args.paths)
    if args.paths_file:
        try:
            paths.extend(line.strip() for line in args.paths_file.read_text(encoding="utf-8").splitlines() if line.strip())
        except OSError as exc:
            parser.error(f"Cannot read paths file: {exc}")
    findings = [f.to_dict() for f in analyze_changed_paths(paths)]
    output = {"status": "UNKNOWN" if findings else "UNKNOWN", "findings_count": len(findings), "findings": findings,
              "note": "Path heuristics cannot prove absence of documentation drift; UNKNOWN is intentional."}
    rendered = json.dumps(output, ensure_ascii=False, indent=2)
    print(rendered)
    if args.json_out:
        args.json_out.write_text(rendered + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
