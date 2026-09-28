---
artifact_type: adoption-plan
framework_version: 1.1.0
status: canonical
owner_module: change/CHANGE_ADOPTION_MODEL.md
produced_by: [08-design-operating-model, 30-design-adoption]
---

# Adoption Plan

## Purpose

Make the human side of the transformation explicit: the behavior each affected role must change, what it needs to do so, and how each role's tasks, responsibilities, and decision rights move (`change/CHANGE_ADOPTION_MODEL.md`, `change/ROLE_TRANSITION_MODEL.md`).

## Record

```yaml
adoption:
  capability_id:            # CAP-###
  initiative_ids: []        # INI-###
  affected_roles: []
  behavior_changes: []
  skills_required: []
  training_required: []
  incentive_changes: []
  trust_risks: []
  workflow_fit_risks: []
  communication: []
  support_model:
  feedback_channel:
  adoption_metrics: []      # MET-###
  owner:

role_transitions:           # one per affected role
  - role:
    capability_id:          # CAP-###
    initiative_id:          # INI-###
    current_responsibilities: []
    target_responsibilities: []
    task_dispositions: []   # task and disposition: RETAIN | ASSIST | AUTOMATE | TRANSFER | ELIMINATE | CREATE_NEW
    removed_tasks: []
    new_tasks: []
    decision_right_changes: []   # BDS-### entries changed
    skill_changes: []
    performance_metric_changes: []
    risks: []
```

Dispositions: `change/ROLE_TRANSITION_MODEL.md` §2. Adoption dimensions: `change/CHANGE_ADOPTION_MODEL.md` §2.

## Rules

Role changes are explicit before rollout (`change/ROLE_TRANSITION_MODEL.md` §5). Material `decision_right_changes` require `HG-DECISION-RIGHTS` (`STANDARD.md` §8).

Adoption metrics do not substitute for Outcome metrics. Resistance is evidence, not only a people problem (`change/CHANGE_ADOPTION_MODEL.md` §5).

## Validation

- [ ] every affected role has a role transition with task dispositions
- [ ] decision-right changes match the Decision Rights Map where one exists, and material ones are approved through `HG-DECISION-RIGHTS`
- [ ] every `change/CHANGE_ADOPTION_MODEL.md` §2 dimension the change touches is addressed, including trust and workflow-fit risks
- [ ] training, support model, feedback channel, and owner are defined
- [ ] adoption metrics are Metric records and sit alongside, not in place of, Outcome metrics
