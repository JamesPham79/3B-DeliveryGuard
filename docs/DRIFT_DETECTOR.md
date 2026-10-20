# Documentation Drift Detector — v0.1

## Current behavior
The deterministic analyzer accepts changed repository paths and emits conservative findings for API contracts, database/model/migration files, implementation code and test assets. It intentionally returns `UNKNOWN` because path heuristics cannot establish semantic consistency.

Run it with `deliveryguard-drift src/auth.py api/openapi.yaml db/migrations/001.sql`, or pass a newline-delimited list using `--paths-file paths.txt`. Use `--json-out report.json` for machine-readable output.

## Not yet supported
- Reading Git diffs or GitHub compare API directly.
- Parsing OpenAPI schemas or database migrations.
- Mapping files to FR/BR/NFR/ERR identifiers.
- Suppression files, severity policy and CI annotations.
- AI-assisted semantic analysis.

## Safety invariant
No changed path without a known mapping may be treated as proof that no documentation impact exists. AI-generated impact suggestions must remain separate from deterministic findings.