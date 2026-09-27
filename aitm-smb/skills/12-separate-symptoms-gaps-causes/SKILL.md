---
name: 12-separate-symptoms-gaps-causes
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: diagnostic-specialist
---

# Skill: Separate Symptoms, Gaps, and Causes

## Required inputs

- observations
- Capability Map

## Produces

- `artifacts/diagnostic-record.md`
- `artifacts/capability-diagnosis.md`

## Procedure

1. Convert raw observations into explicit Symptoms.
2. Link each Symptom to affected Outcomes and Capabilities.
3. Describe current behavior and required behavior.
4. Create GAP records.
5. Generate competing cause hypotheses.
6. Classify cause hypotheses by cause class and confidence.

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
