# Implementation Status

## Implemented in the initial scaffold
- Canonical requirement JSON Schema (structural contract).
- Deterministic requirement structure/traceability checks for ID format, duplicate IDs, required fields, missing acceptance criteria, missing code/test references, and inferred/unknown sources.
- JSON CLI output and basic unit tests.

## Not implemented yet
- Git diff-based documentation drift detection.
- Test/CI evidence ingestion and cryptographic or immutable evidence registry.
- Release policy configuration and approvals.
- Acceptance evidence HTML pack.
- Dependency graph and change impact analysis.
- Coding-agent adapters.

## Important limitations
The current validator checks presence and shape, not semantic correctness. A linked test is not proof that it ran or passed. The CLI currently returns non-zero for structural error-severity FAIL findings; warning-level findings remain visible in the report and should be enforced by policy in a later release.