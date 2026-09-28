# AITM-SMB Traceability

**Version:** 1.1.0

Traceability prevents AI transformation from degrading into a disconnected list of tools, automations, or experiments.

---

## 1. Required semantic trace

```text
OUT-###
  └── CAP-###
       ├── STA-### CURRENT
       └── GAP-###
            └── HYP-### / validated Cause
                 └── INT-###
                      └── INI-###
                           ├── STA-### TARGET
                           ├── MET-###
                           └── EVD-###
```

A validated Cause keeps its `HYP-###` ID.

Where relevant, system-level trace also includes:

```text
CPN-### Capability Network
CST-### System Constraint
TOA-### Target Operating Architecture
STA-### Transition State
PLT-### Pilot
EVL-### Evaluation
VRL-### Value Realization
```

---

## 2. Canonical relations

| Source | Relation | Target | Recorded in |
|---|---|---|---|
| Outcome | REQUIRES | Capability | Capability `outcome_ids` |
| Capability | HAS_STATE | State | Capability `current_state_id`, `target_state_id`; State `capability_id` |
| Capability | HAS_GAP | Gap | Gap `capability_id` |
| Gap | EXPLAINED_BY | Cause / Hypothesis | Gap `hypothesis_ids`; Hypothesis `gap_ids` |
| Gap | ADDRESSED_BY | Intervention | Intervention `gap_ids` |
| Intervention | ADDRESSES | Cause / Hypothesis | Intervention `hypothesis_ids` |
| Intervention | IMPLEMENTED_BY | Initiative | Initiative `intervention_ids` |
| Initiative | SERVES | Outcome | Initiative `expected_outcome_ids` |
| Initiative | MOVES_TOWARD | Target State | Initiative `entry_state_id`, `exit_state_id` |
| Initiative | MEASURED_BY | Metric | Initiative `success_metric_ids`; Metric `initiative_ids` |
| Outcome | MEASURED_BY | Metric | Outcome `metric_ids`; Metric `outcome_ids` |
| Claim | SUPPORTED_BY | Evidence | `evidence_ids` of the claiming record; Evidence `claim_supported` |
| Capability | DEPENDS_ON | Capability | Capability Dependency `DEP-###` ([`artifacts/capability-network.md`](artifacts/capability-network.md)) |
| Target States | COMPOSE_INTO | Target Operating Architecture | TOA `target_state_ids`; each Capability's `target_state_id` points to the same STA records |
| Decision | DECIDES | any registered object | Decision `subject_ids` |

Record contracts: [`CORE_MODEL.md`](CORE_MODEL.md) §1–§7 and the sources named in [`CANONICAL_CONCEPTS.md`](CANONICAL_CONCEPTS.md).

---

## 3. Invalid orphan patterns

Invalid without upstream business trace:

```text
build AI assistant
implement vector database
deploy agent
adopt model provider
automate workflow
```

Such items MAY exist as technical tasks inside a traced Initiative.

---

## 4. Trace record

```yaml
trace:
  outcome_ids: []
  capability_ids: []
  state_ids: []
  gap_ids: []
  hypothesis_ids: []
  intervention_ids: []
  initiative_ids: []
  metric_ids: []
  evidence_ids: []
  other_ids: []         # any other registered IDs (ontology/ONTOLOGY.md)
```

The agent handoff carries this record as `aitm_output.trace` ([`AGENT_OUTPUT_STANDARD.md`](AGENT_OUTPUT_STANDARD.md)).

Missing links MUST remain visible:

- An empty list means no applicable link.
- A required link that is not yet established is recorded as the entry `MISSING:<reason>` in the list that should hold it (e.g. `evidence_ids: ["MISSING:no baseline data yet"]`); a required single-value field holds `MISSING:<reason>` the same way.
- When the missing link is Evidence, it is also recorded as Evidence Debt ([`evidence/EVIDENCE_STANDARD.md`](evidence/EVIDENCE_STANDARD.md) §5).

---

## 5. Stability

Entity identifiers SHOULD remain stable across artifact revisions and framework upgrades.

Identifier format, uniqueness, allocation, and supersession: [`ontology/ONTOLOGY.md`](ontology/ONTOLOGY.md).
