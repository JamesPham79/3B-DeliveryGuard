# Architecture

## System boundaries
- **Project model:** canonical identifiers and metadata.
- **Requirement registry:** FR/BR/NFR/ERR and acceptance criteria.
- **Evidence registry:** references to test results, CI runs, commit SHA, environment and timestamps.
- **Validators:** deterministic checks returning structured findings.
- **Analyzers:** risk-based inference about change impact; inferred findings must be labelled.
- **Integrations:** thin adapters; core must not depend on a specific agent.
- **Delivery:** versioned report and offline package.

## Six capabilities
### 1. Requirement-to-Code Traceability
Inputs: requirements, acceptance criteria, source references, test definitions/results. Outputs: bidirectional traceability matrix, uncovered items, dangling references. ID links alone do not prove semantic correctness.

### 2. Documentation Drift Detector
Inputs: Git base/head, changed paths, OpenAPI schemas, migrations, documentation references. Outputs: likely stale artifacts, reasons, confidence and review actions. Deterministic path/schema rules first; AI may rank or explain but must not silently rewrite approved requirements.

### 3. Evidence-Based Quality Gate
Inputs: policy, validator findings, CI/test results, required-artifact checklist. Outputs: PASS / FAIL / UNKNOWN with reasons and evidence references. UNKNOWN fails closed for mandatory release gates unless an explicit override is approved and recorded.

### 4. Acceptance Evidence Pack
Inputs: pinned commit, approved requirements, test results, unresolved defects and environment metadata. Outputs: self-contained HTML report plus machine-readable manifest. Never bundle secrets or private customer data by default.

### 5. Change Impact Analyzer
Inputs: proposed change, requirement links, dependency graph, code diff, API/database changes. Outputs: impacted requirements, modules, tests and docs; risk and questions needing human approval. Do not invent cost/time estimates without project-specific evidence.

### 6. Agent-Agnostic Project Context
Inputs: canonical project model and adapter configuration. Outputs: compact context files and task packets for supported agents. Adapters remain optional and vendor-specific syntax never becomes the source of truth.

## Data flow
Source requirements -> canonical model -> traceability graph -> validators/analyzers -> quality gate -> evidence pack.

## Constraints
- Core validators are deterministic and unit-testable.
- Findings include rule ID, severity, status, source reference and explanation.
- Outputs are reproducible for a pinned commit and configuration.
- AI-generated content is labelled; human approvals are recorded separately.
- Offline reports do not require external network access.