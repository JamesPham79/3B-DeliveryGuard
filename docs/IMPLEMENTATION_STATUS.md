# Implementation Status

## Implemented in the initial scaffold
- Canonical requirement JSON Schema.
- Deterministic requirement structure checks: ID format, duplicate IDs, required fields, missing acceptance criteria, missing code/test references, and inferred/unknown sources.
- JSON CLI for requirement validation.
- Conservative changed-path drift analyzer for API contracts, database/model/migration paths, implementation code and test assets.
- JSON CLI for changed-path drift findings.
- Unit tests and GitHub Actions CI workflow.

## Not implemented yet
- Git diff ingestion directly from Git or GitHub compare API.
- OpenAPI schema parsing and semantic database migration analysis.
- Requirement-to-code graph with semantic verification.
- Test/CI evidence ingestion and immutable evidence registry.
- Release policy configuration and approval records.
- Acceptance evidence HTML pack.
- Dependency graph and change impact analysis.
- Coding-agent adapters.

## Important limitations
Current validators check structure and path heuristics, not semantic correctness. A linked test is not proof that it ran or passed. Path-based drift findings are intentionally UNKNOWN until stronger mappings and evidence exist. Do not advertise unimplemented capabilities as production-ready.