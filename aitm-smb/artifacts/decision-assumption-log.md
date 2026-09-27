---
artifact_type: decision-assumption-log
framework_version: 1.0.0
status: canonical
---

# Decision & Assumption Log

## Decision record

```yaml
decision:
  id: DEC-###
  statement:
  owner:
  rationale:
  evidence_ids: []
  alternatives: []
  consequences: []
  status:
  date:
```

## Assumption record

```yaml
assumption:
  id: ASM-###
  statement:
  impact_if_wrong:
  validation_path:
  owner:
  status: open | validated | invalidated
```

## Hypothesis record

```yaml
hypothesis:
  id: HYP-###
  statement:
  related_gap_ids: []
  evidence_for: []
  evidence_against: []
  test:
  status:
```

## Rule

Decisions, assumptions, and hypotheses are different object types and MUST NOT be merged.
