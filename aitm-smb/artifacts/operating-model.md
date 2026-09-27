---
artifact_type: operating-model
framework_version: 1.0.0
status: canonical
---

# Operating Model

## Purpose

Define who operates the target system and how decisions are made after transformation.

## Structure

```yaml
operating_model:
  capability_ids: []
  roles: []
  responsibilities: []
  decision_rights: []
  human_ai_boundaries: []
  service_ownership: []
  support_model: []
  change_ownership: []
  governance_cadence: []
  incident_ownership: []
  skill_requirements: []
```

## Required questions

1. Who owns each transformed capability?
2. Which role owns each material decision?
3. What work disappears, changes, or is created?
4. What AI output is reviewed by humans?
5. Who improves prompts, policies, knowledge, and evaluations?
6. Who responds when AI behavior degrades?
7. Who decides whether autonomy may increase?
