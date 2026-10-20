# Roadmap

## Phase 0 — Foundation
- Preserve upstream attribution and review MIT obligations.
- Define canonical schemas and stable IDs.
- Add sample fixtures and CI baseline.
- Add threat model and secret-handling rules.

## Phase 1 — Traceability core
- Parse requirements, acceptance criteria, code references and test manifests.
- Validate duplicate IDs, dangling references, missing acceptance criteria and missing tests.
- Export JSON and Markdown/HTML matrix.
- Test positive and negative fixtures.

## Phase 2 — Drift detection
- Compare base/head Git changes.
- Map changed paths to docs, API contracts, migrations and tests.
- Emit findings with confidence and deterministic reasons.
- Never silently change approved requirements.

## Phase 3 — Quality gate
- Define policy configuration and mandatory checks.
- Report PASS / FAIL / UNKNOWN.
- Require evidence references for PASS.
- Add documented override mechanism with approver and reason.

## Phase 4 — Acceptance pack
- Generate self-contained HTML and JSON manifest.
- Pin commit SHA, test run identifiers, environment and unresolved defects.
- Scan output for secrets and disallowed files.

## Phase 5 — Change impact
- Build a requirement/module/API/database/test dependency graph.
- Report direct and probable impacts separately.
- Add regression-test recommendations.

## Phase 6 — Agent-neutral context
- Define stable task packet format.
- Add adapters incrementally, starting with file-based instructions.
- Test operation without an agent-specific CLI.

## Release criteria
- Automated tests pass.
- Sample fixtures demonstrate all status types.
- Generated suggestions are distinct from verified facts.
- Security review completed for evidence-pack contents.