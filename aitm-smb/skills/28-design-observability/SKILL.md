---
name: 28-design-observability
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: execution-governance
---

# Skill: Design Observability

## Required inputs

- Target Operating Architecture
- Pilot/Rollout Plan
- governance requirements

## Produces

- `artifacts/observability-plan.md`

## Procedure

1. Identify business and capability signals.
2. Identify workflow and decision traces.
3. Identify AI/agent traces and tool actions.
4. Identify cost and risk signals.
5. Define alerts and review cadence.
6. Assign operational owner.

## Execution controls

- Evidence gates must be explicit.
- Success criteria must not be rewritten after results are known.
- Technical deployment does not equal transformation success.
- Business effect, operating effect, and AI quality must remain separate.
- Human approval is required for material authority increases.
- Failed pilots may be stopped.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
