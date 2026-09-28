---
artifact_type: operating-model
framework_version: 1.1.0
status: canonical
owner_module: methodology/07-operating-model-governance.md
produced_by: [08-design-operating-model]
---

# Operating Model

## Purpose

Define who operates the target system and how decisions are made after transformation.

## Record

```yaml
operating_model:
  capability_ids: []        # CAP-###
  roles: []
  responsibilities: []
  decision_rights: []       # BDS-### or statements
  human_ai_boundaries: []
  service_ownership: []
  support_model: []
  change_ownership: []      # who approves AI changes (governance/AI_CHANGE_CONTROL.md)
  governance_cadence: []    # governance/GOVERNANCE_OPERATING_MODEL.md §4, §6
  incident_ownership: []    # who records and handles incidents (operations/INCIDENT_MODEL.md)
  skill_requirements: []
```

Role transitions are recorded in the Adoption Plan (`artifacts/adoption-plan.md`).

## Required questions

1. Who owns each transformed capability?
2. Which role owns each material decision?
3. What work disappears, changes, or is created?
4. What AI output is reviewed by humans?
5. Who improves prompts, policies, knowledge, and evaluations?
6. Who responds when AI behavior degrades?
7. Who decides whether autonomy may increase?

## Validation

- [ ] every transformed Capability and material decision has an owner (`governance/GOVERNANCE_OPERATING_MODEL.md` §3; roles MAY be combined)
- [ ] human-AI boundaries match the Decision Rights Map and approved Authority Ceilings, where they exist
- [ ] support model, change ownership, and incident ownership are explicit
- [ ] governance cadence and review triggers are set
- [ ] the owner of autonomy decisions is named; increases still require `HG-AUTHORITY`
