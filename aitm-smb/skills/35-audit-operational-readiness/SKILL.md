---
name: 35-audit-operational-readiness
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: execution-governance
---

# Skill: Audit Operational Readiness

## Required inputs

- Rollout Plan
- Observability Plan
- Governance
- Support model
- Recovery plan

## Produces

- no persistent artifact required; return findings through `AGENT_OUTPUT_STANDARD.md`

## Procedure

1. Check ownership.
2. Check monitoring and alerts.
3. Check incident path.
4. Check rollback/recovery.
5. Check eval coverage.
6. Check cost controls.
7. Check support and adoption readiness.
8. Identify blocking gaps.

## Execution controls

- Evidence gates must be explicit.
- Success criteria must not be rewritten after results are known.
- Technical deployment does not equal transformation success.
- Business effect, operating effect, and AI quality must remain separate.
- Human approval is required for material authority increases.
- Failed pilots may be stopped.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
