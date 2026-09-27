---
name: 29-plan-rollout
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: execution-governance
---

# Skill: Plan Progressive Rollout

## Required inputs

- passed Pilot
- Evaluation results
- Target scope

## Produces

- `artifacts/rollout-plan.md`

## Procedure

1. Choose rollout dimensions and stages.
2. Define entry gates for each stage.
3. Define monitoring and support.
4. Define rollback/recovery.
5. Define legacy-path retirement.
6. Check organizational change capacity.

## Execution controls

- Evidence gates must be explicit.
- Success criteria must not be rewritten after results are known.
- Technical deployment does not equal transformation success.
- Business effect, operating effect, and AI quality must remain separate.
- Human approval is required for material authority increases.
- Failed pilots may be stopped.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
