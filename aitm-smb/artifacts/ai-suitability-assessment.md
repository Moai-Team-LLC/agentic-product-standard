---
artifact_type: ai-suitability-assessment
framework_version: 1.1.0
status: canonical
entity: AI Suitability Assessment
id_prefix: AIS
owner_module: diagnostics/AI_SUITABILITY.md
produced_by: [04-design-interventions, 13-assess-ai-suitability]
---

# AI Suitability Assessment

## Purpose

Record whether probabilistic intelligence adds more value than process redesign, deterministic software, or automation for one `AI_*` candidate Intervention.

## Record

```yaml
ai_suitability:
  id: AIS-###
  intervention_id:                     # INT-### (type AI_*)
  gap_ids: []
  simpler_alternatives_considered: []  # INT-### or short statements
  non_ai_alternative:                  # the best non-AI option and why it is or is not enough
  # dimensions (diagnostics/AI_SUITABILITY.md §2): low | medium | high | not_relevant, with a note (for not_relevant: the reason)
  semantic_load:
  input_variability:
  judgment_requirement:
  knowledge_intensity:
  interaction_requirement:
  prediction_requirement:
  generation_requirement:
  probabilistic_tolerance:             # Tolerance for Probabilistic Output
  verification_feasibility:
  recoverability:                      # Error Recoverability
  context_readiness:                   # Context Availability
  data_sensitivity:
  execution_risk:
  economic_frequency:                  # economic value goes in rationale
  classification: A | B | C | D | E
  rationale:
  evidence_ids: []
  assumption_ids: []
```

Classes and what each implies for selection: [`diagnostics/AI_SUITABILITY.md`](../diagnostics/AI_SUITABILITY.md) §5.

## Rules

This assessment does not set authority; autonomy is assessed separately ([`artifacts/autonomy-assessment.md`](autonomy-assessment.md)).

## Validation

- [ ] linked to one `AI_*` Intervention and its Gaps
- [ ] every dimension ([`diagnostics/AI_SUITABILITY.md`](../diagnostics/AI_SUITABILITY.md) §2) is rated, or marked `not_relevant` with a reason
- [ ] simpler alternatives and the non-AI alternative are recorded
- [ ] `rationale` explains the classification, and its consequence ([`diagnostics/AI_SUITABILITY.md`](../diagnostics/AI_SUITABILITY.md) §5) is respected: C and D need a recorded justification; E is rejected
