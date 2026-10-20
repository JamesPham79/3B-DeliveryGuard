# Acceptance Criteria

## Traceability
- Given valid requirements, the validator reports each requirement with linked acceptance criteria and tests.
- Duplicate IDs produce FAIL and identify all locations.
- Missing links are reported; the tool does not silently create links.
- A test without execution evidence has status UNKNOWN, not PASS.

## Drift detection
- Changed API schemas flag mapped API docs and contract tests when relevant.
- Changed source files with no known mapping are reported as unmapped/unknown, not as having no impact.
- Deterministic matches and AI-inferred suggestions are distinguishable.

## Quality gate
- PASS requires every mandatory check to pass with evidence references.
- FAIL is emitted for a failed mandatory check.
- UNKNOWN is emitted when mandatory evidence is missing, stale or unreadable.
- Overrides require approver, reason and timestamp.

## Acceptance pack
- Manifest records repository, commit SHA, generation time, policy version and test evidence references.
- No environment secrets or credentials are included.
- Offline report opens without external network dependencies.
- Unresolved defects and skipped checks remain visible.

## Change impact
- Proposed changes list impacted requirements, code paths, tests and docs where graph links exist.
- Directly observed and inferred impacts are distinct.
- Cost/time estimates are omitted unless supported by historical project data.

## Agent-neutral context
- Canonical project data remains readable without a supported agent installed.
- Adapter failure cannot corrupt canonical data.
- Agent-specific files are generated from canonical records, not maintained as conflicting sources of truth.