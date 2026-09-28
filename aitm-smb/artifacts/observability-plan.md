---
artifact_type: observability-plan
framework_version: 1.1.0
status: canonical
owner_module: operations/OBSERVABILITY_MODEL.md
produced_by: [08-design-operating-model, 28-design-observability]
---

# Observability Plan

## Purpose

Make one transformed Capability observable as a business system, with trace depth proportional to its authority and risk ([`operations/OBSERVABILITY_MODEL.md`](../operations/OBSERVABILITY_MODEL.md)).

## Record

```yaml
observability:
  capability_id:            # CAP-###
  initiative_ids: []        # INI-###
  owner:
  # signals by layer (operations/OBSERVABILITY_MODEL.md §2)
  business_signals: []
  capability_signals: []
  workflow_signals: []
  decision_signals: []
  ai_signals: []            # AI / Agent layer, including tool actions
  technical_signals: []     # Application and Infrastructure layers, where relevant
  cost_signals: []          # Economics layer
  risk_signals: []
  trace_depth:              # chosen depth and why (operations/OBSERVABILITY_MODEL.md §5)
  traces:                   # operation_trace fields captured (operations/OBSERVABILITY_MODEL.md §4)
  alerts: []                # signal, threshold, recipient; which alerts open an Incident (operations/OBSERVABILITY_MODEL.md §7)
  review_cadence:
```

## Validation

- [ ] every relevant layer has at least one signal, and each material state change is logged
- [ ] the minimum observable questions ([`operations/OBSERVABILITY_MODEL.md`](../operations/OBSERVABILITY_MODEL.md) §3) can be answered for production AI-enabled work
- [ ] trace depth is justified by authority, risk, and impact ([`operations/OBSERVABILITY_MODEL.md`](../operations/OBSERVABILITY_MODEL.md) §5)
- [ ] no dark-automation pattern remains ([`operations/OBSERVABILITY_MODEL.md`](../operations/OBSERVABILITY_MODEL.md) §6)
- [ ] alerts, review cadence, and an owner are set
