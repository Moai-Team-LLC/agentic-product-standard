---
artifact_type: incident-record
framework_version: 1.1.0
status: canonical
entity: Incident
id_prefix: INC
owner_module: operations/INCIDENT_MODEL.md
produced_by: [40-handle-incident]
---

# Incident Record

## Purpose

Record one incident of an AI-enabled capability: what happened, how it was contained and recovered, and what it changed (`operations/INCIDENT_MODEL.md`). Incident history feeds evaluation datasets, authority reviews, and Phase 8.

## Record

```yaml
incident:
  id: INC-###
  capability_id:            # CAP-###
  initiative_id:            # INI-###
  class:                    # operations/INCIDENT_MODEL.md §2
  severity: high | medium | low   # operations/INCIDENT_MODEL.md §3
  status: open | contained | recovered | closed
  detected_at:
  impact:
  affected_state:           # business state affected: records, transactions, customers
  trace_ids: []             # operation traces (operations/OBSERVABILITY_MODEL.md §4)
  containment:
  recovery:
  root_cause:
  corrective_action:
  authority_change:         # AUT-### and the new level when authority was reduced; empty otherwise
  feedback_updates: []      # one entry per operations/INCIDENT_MODEL.md §4 target updated: target and change
  eval_case_added:          # eval case added to the evaluation dataset (<dataset id>/<case id>)
  evidence_ids: []
  owner:
```

## Rules

When the incident matches a demotion trigger (`governance/AUTHORITY_ESCALATION_MODEL.md` §4), authority MAY be reduced at once and is recorded in `authority_change` and the Autonomy Assessment. Restoring it requires `HG-AUTHORITY` (`STANDARD.md` §8).

## Validation

- [ ] linked to a Capability, with class and severity per `operations/INCIDENT_MODEL.md` §2–§3
- [ ] detection time, impact, affected state, containment, and recovery are recorded
- [ ] root cause and corrective action are stated before `status: closed`
- [ ] a material incident lists its feedback updates (`operations/INCIDENT_MODEL.md` §4)
- [ ] any authority reduction is recorded, and no authority is restored without `HG-AUTHORITY`
