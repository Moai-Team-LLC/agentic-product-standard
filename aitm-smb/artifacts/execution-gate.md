---
artifact_type: execution-gate
framework_version: 1.1.0
status: canonical
entity: Execution Gate
id_prefix: GAT
owner_module: execution/EXECUTION_GATE_MODEL.md
produced_by: [05-prioritize-initiatives, 06-design-target-system, 07-build-roadmap, 08-design-operating-model, 09-measure-evolution, 25-design-pilot, 32-evaluate-pilot, 33-assess-value-realization, 35-audit-operational-readiness]
---

# Execution Gate

## Purpose

Record one evidence checkpoint on an Initiative: what evidence the gate requires, what was provided, and who decided ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md)).

## Record

```yaml
gate:
  id: GAT-###
  initiative_id:            # INI-###
  type: A | B | C | D | E | F | G   # execution/EXECUTION_GATE_MODEL.md §2, or a named custom gate
  subject_ids: []           # records the gate guards, e.g. GAP-### (A), TOA-### (B), PLT-###, ROL-### (and stage), VRL-###
  human_gates: []           # HG-* needed to pass this gate (execution/EXECUTION_GATE_MODEL.md §2 gate map); empty if none
  required_evidence: []
  evidence_provided: []     # EVD-###, EVL-###, and other records
  approver:                 # human who decides the gate
  status: open | passed | failed | waived
  decision_ids: []          # DEC-### that close its human gates, or fail or waive the gate
  rationale:
  review_trigger:
```

Skill 05 records Gate A per Initiative at selection (evidence: the Initiative's Gaps meet the Phase 2 readiness condition); skill 06 records Gate B after `HG-TOA`; skill 07 creates the Gate C–G records an Initiative needs; skill 35 creates a rollout stage's Gate E record when the stage has none; the skills that check a gate (25: C, 32: D, 35: E, 08: F, 33: G) update `evidence_provided` and propose a status.

## Rules

Only the `approver` passes, fails, or waives a gate. `status: passed` requires `decision_ids` to name an approved Decision closing each gate in `human_gates` ([`STANDARD.md`](../STANDARD.md) §8).

`status: waived` requires `decision_ids` to name an approved Decision that records reason, risk, owner, and expiration or review trigger ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md) §4); for Gate D, the `HG-PROMOTION` Decision.

## Validation

- [ ] linked to one Initiative and to the records it guards
- [ ] `type` is a gate of [`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md) §2 or a named custom gate, and `human_gates` matches that section's gate map
- [ ] required evidence is stated before the gate is checked, and evidence provided cites records
- [ ] every passed gate names an approved Decision in `decision_ids` for each of its `human_gates`, and every waived gate names its waiver Decision
- [ ] the approver is a named human
