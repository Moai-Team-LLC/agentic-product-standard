---
name: 16-validate-root-cause
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: diagnostic-specialist
---

# Skill: Validate Root Cause

## Required inputs

- Gap
- Cause hypotheses
- available evidence

## Produces

- `artifacts/diagnostic-record.md`

## Procedure

1. For each cause identify supporting and falsifying evidence.
2. Identify alternative causes.
3. Apply counterfactual test.
4. Determine whether evidence is sufficient for intervention design.
5. If not sufficient, define the cheapest useful validation method.

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
