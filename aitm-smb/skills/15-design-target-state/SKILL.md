---
name: 15-design-target-state
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: diagnostic-specialist
---

# Skill: Design Target Capability State

## Required inputs

- selected intervention
- Capability Diagnosis
- approved constraints

## Produces

- `artifacts/capability-target-state.md`

## Procedure

1. Write target capability statement.
2. Design people and decision rights first.
3. Design process and information flow.
4. Define data and knowledge requirements.
5. Define application and automation boundaries.
6. Add AI only where justified.
7. Define controls, metrics, and operating ownership.
8. Validate that every target-state element addresses a diagnosed Gap.

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
