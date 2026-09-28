---
artifact_type: value-realization-report
framework_version: 1.1.0
status: canonical
entity: Value Realization
id_prefix: VRL
owner_module: measurement/VALUE_REALIZATION.md
produced_by: [09-measure-evolution, 33-assess-value-realization]
---

# Value Realization Report

## Purpose

Record whether an Initiative created attributable, sustained business value against its Outcome, with the value state and value conclusion it has reached ([`measurement/VALUE_REALIZATION.md`](../measurement/VALUE_REALIZATION.md)).

## Record

```yaml
value_realization:
  id: VRL-###
  initiative_id:            # INI-###
  outcome_id:               # OUT-###
  metric_id:                # MET-### measuring the Outcome
  baseline:
  target:
  observed:
  business_effect:
  capability_effect:
  economic_effect:          # gross economic effect of the change
  implementation_cost:
  operating_cost:
  realized_value:           # economic effect net of implementation and operating cost
  attribution_confidence: LOW | MEDIUM | HIGH   # measurement/VALUE_REALIZATION.md §4
  competing_explanations: []
  unexpected_effects: []
  sustainability_period:    # measurement/VALUE_REALIZATION.md §5
  value_state: HYPOTHESIZED | OBSERVED | ATTRIBUTED | REALIZED | SUSTAINED   # measurement/VALUE_REALIZATION.md §2
  conclusion: VALUE_CONFIRMED | PARTIAL_VALUE | NO_VALUE | NEGATIVE_VALUE | INSUFFICIENT_EVIDENCE   # measurement/VALUE_REALIZATION.md §6
  evaluation_ids: []        # EVL-### used, including risk / governance evaluations
  evidence_ids: []
  benefit_chain:            # Measured: record per measurement/BENEFIT_EVIDENCE_CHAIN.md §3
```

State entry criteria and conclusion meanings: [`measurement/VALUE_REALIZATION.md`](../measurement/VALUE_REALIZATION.md) §2, §6.

## Rules

`value_state: REALIZED` or `SUSTAINED` and `conclusion: VALUE_CONFIRMED` take effect only when a Decision closing `HG-VALUE` ([`STANDARD.md`](../STANDARD.md) §8) lists this `VRL-###` in `subject_ids`. Until then they are proposals. Governed: Gate G ([`artifacts/execution-gate.md`](execution-gate.md)).

This report carries the value conclusion; the Transformation Scorecard carries the effect conclusion.

## Validation

- [ ] linked to one Initiative, Outcome, and Outcome metric, with baseline, target, and observed value
- [ ] realized value is stated net of implementation and operating cost
- [ ] attribution confidence is recorded with competing explanations
- [ ] value state and conclusion meet [`measurement/VALUE_REALIZATION.md`](../measurement/VALUE_REALIZATION.md) §2 and §6, and every claim cites Evidence
- [ ] REALIZED, SUSTAINED, or VALUE_CONFIRMED is backed by an approved `HG-VALUE` Decision
- [ ] Measured: a benefit chain links change, behavior, capability, Outcome, and economic value
