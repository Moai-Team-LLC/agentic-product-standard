---
name: 14-assess-autonomy
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: diagnostic-specialist
---

# Skill: Assess Agentic Autonomy

## Required inputs

- AI-suitable intervention
- governance context

## Produces

- `artifacts/autonomy-assessment.md`

## Procedure

1. Evaluate reversibility, financial/customer/legal/security impact, ambiguity, policy clarity, observability, verification, exception detection, recovery, and permissions.
2. Recommend autonomy level L0–L5.
3. Define maximum authority ceiling.
4. Define prohibited actions and approval boundaries.

## Mandatory controls

- Separate evidence from inference.
- Preserve stable AITM identifiers.
- Do not silently widen scope.
- Surface uncertainty.
- Do not recommend AI before simpler intervention classes are considered.

## Stop conditions

Stop when proceeding would require invented business facts or when a human gate is reached.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
