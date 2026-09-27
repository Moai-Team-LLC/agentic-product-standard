# AITM-SMB Traceability

**Version:** 1.0.0

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

Where relevant, system-level trace also includes:

```text
CPN-### Capability Network
CST-### System Constraint
TOA-### Target Operating Architecture
STA-### Transition State
PLT-### Pilot
EVL-### Evaluation
```

---

## 2. Canonical relations

| Source | Relation | Target |
|---|---|---|
| Outcome | REQUIRES | Capability |
| Capability | HAS_STATE | State |
| Capability | HAS_GAP | Gap |
| Gap | EXPLAINED_BY | Cause / Hypothesis |
| Gap | ADDRESSED_BY | Intervention |
| Intervention | IMPLEMENTED_BY | Initiative |
| Initiative | MOVES_TOWARD | Target State |
| Initiative | MEASURED_BY | Metric |
| Outcome | MEASURED_BY | Metric |
| Claim | SUPPORTED_BY | Evidence |
| Capability | DEPENDS_ON | Capability |
| Target States | COMPOSE_INTO | Target Operating Architecture |

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
```

Missing links MUST remain visible.

---

## 5. Stability

Entity identifiers SHOULD remain stable across artifact revisions and framework upgrades.
