---
name: 32-evaluate-pilot
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: execution-governance
---

# Skill: Evaluate Pilot

## Required inputs

- Pilot Plan
- pilot evidence
- Evaluation Plan

## Produces

- `artifacts/evaluation-plan.md`

## Procedure

1. Compare evidence against pre-defined thresholds.
2. Separate business, operating, AI, economic, and governance results.
3. Record limitations and attribution uncertainty.
4. Classify result as PROMOTE, REVISE, REPEAT, STOP, or INSUFFICIENT_EVIDENCE.
5. Identify architecture or diagnosis updates required.

## Execution controls

- Evidence gates must be explicit.
- Success criteria must not be rewritten after results are known.
- Technical deployment does not equal transformation success.
- Business effect, operating effect, and AI quality must remain separate.
- Human approval is required for material authority increases.
- Failed pilots may be stopped.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
