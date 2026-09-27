---
artifact_type: diagnostic-record
framework_version: 1.0.0
status: canonical
---

# Diagnostic Record

```yaml
diagnostic:
  id: DIA-###
  outcome_ids: []
  capability_id:
  observations:
    - evidence_id:
      statement:
  symptoms: []
  current_behavior:
  required_behavior:
  gap_id:
  cause_hypotheses:
    - hypothesis_id:
      cause_class:
      confidence:
  validated_causes: []
  evidence_debt: []
  next_action:
```

## Rule

A Diagnostic Record does not contain solution selection unless the diagnosis has reached intervention readiness.
