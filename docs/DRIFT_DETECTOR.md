# Documentation Drift Detector — v0.1

## Current behavior
The initial deterministic analyzer accepts changed repository paths and emits conservative findings for API contracts, database/model/migration files, implementation code, and test assets. It intentionally returns `UNKNOWN` because path-based heuristics cannot establish semantic consistency.

## Not yet supported
- Reading Git diffs or compare API directly.
- Parsing OpenAPI schemas or database migrations.
- Mapping files to FR/BR/NFR/ERR identifiers.
- Suppression files, severity policy and CI annotations.
- AI-assisted semantic analysis.

## Safety invariant
No changed path without a known mapping may be treated as proof that no documentation impact exists. AI-generated impact suggestions must remain separate from deterministic findings.