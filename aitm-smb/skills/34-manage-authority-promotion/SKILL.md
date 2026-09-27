---
name: 34-manage-authority-promotion
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: execution-governance
---

# Skill: Manage AI Authority Promotion

## Required inputs

- Autonomy Assessment
- Evaluation results
- Incident history
- Governance controls

## Produces

- `artifacts/autonomy-assessment.md`

## Procedure

1. Check quality stability.
2. Check observability and verification.
3. Check policy enforcement.
4. Check recovery and permission boundaries.
5. Check business value.
6. Recommend promote, retain, or demote authority.
7. Stop for explicit human approval.

## Execution controls

- Evidence gates must be explicit.
- Success criteria must not be rewritten after results are known.
- Technical deployment does not equal transformation success.
- Business effect, operating effect, and AI quality must remain separate.
- Human approval is required for material authority increases.
- Failed pilots may be stopped.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
