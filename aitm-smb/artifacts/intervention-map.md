---
artifact_type: intervention-map
framework_version: 1.0.0
status: canonical
entity: Intervention
id_prefix: INT
---

# Intervention Map

## Purpose

Map candidate interventions against diagnosed Capability Gaps.

AI interventions are a subset of interventions.

## Contract

```yaml
intervention:
  id: INT-###
  gap_ids: []
  type:
  description:
  expected_effect:
  simpler_alternatives_considered: []
  non_ai_alternative:
  required_context:
  required_actions:
  required_permissions:
  verification:
  risks: []
  assumptions: []
```

## Intervention types

```text
ELIMINATE
SIMPLIFY
STANDARDIZE
INSTRUMENT
INTEGRATE
PROCESS
ROLE
DECISION
DATA
KNOWLEDGE
SOFTWARE
AUTOMATION
AI_ASSIST
AI_AUTOMATE
AI_AUGMENT
AI_AUTONOMIZE
CONTROL
FEEDBACK
```

## Rule

An AI intervention MUST NOT be selected before plausible simpler intervention classes are considered.
