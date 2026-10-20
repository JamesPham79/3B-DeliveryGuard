# 3B-DeliveryGuard

**Status:** Architecture blueprint / scaffold — not production-ready.

3B-DeliveryGuard is an evidence-based software delivery assurance layer for solo developers and AI coding agents. It is designed to complement [OpenBA-Kit](https://github.com/spmtitsolution/OpenBA-Kit) by validating traceability, detecting documentation drift, enforcing evidence-based quality gates, packaging acceptance evidence, analyzing change impact, and providing agent-neutral project context.

## Product principles
1. Evidence over assertion: generated artifacts do not prove that software works.
2. Deterministic checks first; AI explanations second.
3. `UNKNOWN` is a valid state. Missing evidence must never become `PASS`.
4. Keep upstream BA skills replaceable and avoid dependence on one AI agent.
5. Preserve upstream copyright and license notices for copied or adapted material.
6. Do not include secrets or private customer data in evidence bundles.

## Six capabilities
1. Requirement-to-Code Traceability
2. Documentation Drift Detector
3. Evidence-Based Quality Gate
4. Acceptance Evidence Pack
5. Change Impact Analyzer
6. Agent-Agnostic Project Context

## Architecture
See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [roadmap](docs/ROADMAP.md), [acceptance criteria](docs/ACCEPTANCE_CRITERIA.md), [security](docs/SECURITY.md), and [upstream/license notes](docs/UPSTREAM_AND_LICENSE.md).

## Initial workflow
Requirements -> canonical model -> traceability graph -> deterministic validators and impact analyzers -> quality gate -> versioned evidence pack.

## Status
This repository currently defines architecture and acceptance criteria. Features must not be advertised as implemented until code and automated tests exist.
