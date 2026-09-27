---
name: 31-operationalize-governance
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: execution-governance
---

# Skill: Operationalize Governance

## Required inputs

- AI Governance Canvas
- Operating Model
- Observability Plan

## Produces

- `artifacts/ai-governance-canvas.md`
- `artifacts/operating-model.md`

## Procedure

1. Assign governance responsibilities.
2. Define review cadence and event triggers.
3. Define AI change-control classes.
4. Define authority promotion/demotion process.
5. Define incident review loop.
6. Define evidence required for material decisions.

## Execution controls

- Evidence gates must be explicit.
- Success criteria must not be rewritten after results are known.
- Technical deployment does not equal transformation success.
- Business effect, operating effect, and AI quality must remain separate.
- Human approval is required for material authority increases.
- Failed pilots may be stopped.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
