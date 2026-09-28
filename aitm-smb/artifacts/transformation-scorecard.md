---
artifact_type: transformation-scorecard
framework_version: 1.1.0
status: canonical
entity: Metric
id_prefix: MET
owner_module: METRICS.md
produced_by: [01-discover-transformation, 09-measure-evolution]
---

# Transformation Scorecard

## Purpose

Determine whether the transformation changed the intended business system. Holds the engagement's Metric records (`MET-###`) from the moment each is defined (any phase), and the effect conclusion per evidence period.

## Record

Record contract: Metric `METRICS.md` §6.

```yaml
metrics: []                 # Metric records (MET-###)

scorecard:
  outcome_ids: []           # OUT-###
  initiative_ids: []        # INI-###
  owner:
  evidence_period:
  outcome_metric_ids: []    # MET-### by class (METRICS.md §6 `class`)
  capability_metric_ids: []
  operating_metric_ids: []
  ai_evaluation_metric_ids: []
  economic_metric_ids: []
  risk_governance_metric_ids: []
  observations:             # extension: one entry per metric read in the period
    - metric_id:
      observed:
      as_of:
      evidence_ids: []
  unexpected_effects: []
  evidence_ids: []
  conclusion: EFFECT_CONFIRMED | PARTIAL_EFFECT | NO_EFFECT | NEGATIVE_EFFECT | INSUFFICIENT_EVIDENCE
```

## Rules

Skill 01 records the baseline Metrics in Phase 0; any skill that defines a Metric MAY append its record to `metrics`.

Adoption alone cannot produce EFFECT_CONFIRMED.

The scorecard carries the effect conclusion: whether the metrics moved against baseline in the evidence period. Whether that effect is attributable, sustained value is the value conclusion of the Value Realization Report (`measurement/VALUE_REALIZATION.md` §6). `INSUFFICIENT_EVIDENCE` is a result value, not an agent status (`PUBLIC_API.md` §8).

Lower-level metrics explain performance but do not replace Outcome metrics (`STANDARD.md` §9).

## Validation

- [ ] every Metric has definition, owner, source, baseline or explicit baseline gap, and cadence (`METRICS.md` §7)
- [ ] the scorecard links its Outcomes and Initiatives, and every listed metric resolves to a Metric record of that class
- [ ] each material Initiative has at least one Outcome or Capability metric (`STANDARD.md` §9)
- [ ] every observation cites Evidence, and missing readings stay visible (`TRACEABILITY.md` §4)
- [ ] the conclusion does not rest on adoption or AI-quality metrics alone
