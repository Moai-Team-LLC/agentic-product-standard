---
name: 25-design-pilot
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: execution-governance
---

# Skill: Design Pilot

## Required inputs

- approved Initiative
- Target State
- uncertainties
- baseline metrics

## Produces

- `artifacts/pilot-plan.md`

## Procedure

1. State the transformation hypothesis being tested.
2. Select the smallest operational scope capable of testing it.
3. Choose shadow, assisted, controlled execution, or limited autonomous mode.
4. Define baseline and comparison method.
5. Define success and stop criteria before execution.
6. Define guardrails, rollback, and owner.
7. Define evidence to collect.

## Execution controls

- Evidence gates must be explicit.
- Success criteria must not be rewritten after results are known.
- Technical deployment does not equal transformation success.
- Business effect, operating effect, and AI quality must remain separate.
- Human approval is required for material authority increases.
- Failed pilots may be stopped.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
