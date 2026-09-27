---
artifact_type: transformation-scorecard
framework_version: 1.0.0
status: canonical
---

# Transformation Scorecard

## Purpose

Determine whether the transformation changed the intended business system.

## Scorecard structure

```yaml
scorecard:
  outcome_metrics: []
  capability_metrics: []
  operating_metrics: []
  ai_evaluation_metrics: []
  economic_metrics: []
  unexpected_effects: []
  evidence_period:
  conclusion:
```

## Conclusion values

```text
EFFECT_CONFIRMED
PARTIAL_EFFECT
NO_EFFECT
NEGATIVE_EFFECT
INSUFFICIENT_EVIDENCE
```

## Rule

Adoption alone cannot produce EFFECT_CONFIRMED.
