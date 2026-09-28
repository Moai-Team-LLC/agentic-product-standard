---
artifact_type: autonomy-assessment
framework_version: 1.1.0
status: canonical
entity: Autonomy Assessment
id_prefix: AUT
owner_module: diagnostics/AUTONOMY_SUITABILITY.md
produced_by: [04-design-interventions, 08-design-operating-model, 09-measure-evolution, 14-assess-autonomy, 34-manage-authority-promotion]
---

# Autonomy Assessment

## Purpose

Record how much authority AI may hold for one action class of a Capability: the assessment, the recommended level, the Authority Ceiling, and the level in operation after promotion or demotion.

## Record

```yaml
autonomy:
  id: AUT-###
  capability_id:              # CAP-###
  intervention_id:            # INT-### (type AI_*)
  action_class:               # the action class assessed; levels are per action class
  recommended_level: L0 | L1 | L2 | L3 | L4 | L5
  current_level: L0 | L1 | L2 | L3 | L4 | L5   # level in operation; L0 before any AI runs
  # dimensions (diagnostics/AUTONOMY_SUITABILITY.md §3): low | medium | high, with a note
  reversibility:              # Action Reversibility
  financial_impact:
  customer_impact:
  legal_impact:
  security_impact:
  safety_impact:
  decision_ambiguity:
  policy_clarity:
  observability:
  verification:               # Verification Quality
  exception_detectability:
  recovery:                   # Recovery Quality
  permission_precision:       # Identity / Permission Precision
  # Authority Ceiling (diagnostics/AUTONOMY_SUITABILITY.md §6)
  maximum_allowed_level: L0 | L1 | L2 | L3 | L4 | L5
  prohibited_actions: []
  approval_required: []
  escalation_conditions: []
  owner:                      # accountable role for this ceiling
  promotion_recommendation: promote | retain | demote   # skill 34; criteria: governance/AUTHORITY_ESCALATION_MODEL.md
  rationale:
  evidence_ids: []
  assumption_ids: []
```

Level meanings: `diagnostics/AUTONOMY_SUITABILITY.md` §2.

## Rules

`maximum_allowed_level`, `prohibited_actions`, `approval_required`, `escalation_conditions`, and `owner` are the Authority Ceiling for this action class.

Setting or raising the ceiling, and each increase of `current_level` above L0, takes effect only when a Decision closing `HG-AUTHORITY` (`STANDARD.md` §8) lists this `AUT-###` in `subject_ids` and states the level. Until then it is a proposal.

`recommended_level` and `current_level` MUST NOT exceed `maximum_allowed_level`; a higher level requires re-assessing the ceiling first.

Demotion needs no gate: the operating owner lowers `current_level` (or the ceiling) and records why in `rationale`.

## Validation

- [ ] linked to one Capability, action class, and `AI_*` Intervention
- [ ] every dimension (`diagnostics/AUTONOMY_SUITABILITY.md` §3) is rated
- [ ] prohibited actions, approval boundaries, and escalation conditions are explicit, and an owner is named
- [ ] recommended and current level do not exceed `maximum_allowed_level`
- [ ] the ceiling and every increase of `current_level` are approved through `HG-AUTHORITY` before use
