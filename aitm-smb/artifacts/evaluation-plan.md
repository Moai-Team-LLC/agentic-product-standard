---
artifact_type: evaluation-plan
framework_version: 1.1.0
status: canonical
entity: Evaluation
id_prefix: EVL
owner_module: evaluation/EVALUATION_SYSTEM.md
produced_by: [07-build-roadmap, 08-design-operating-model, 09-measure-evolution, 26-design-evaluation, 27-build-eval-dataset, 32-evaluate-pilot]
---

# Evaluation Plan

## Purpose

Pre-register how a pilot, rollout, or operating Capability will be evaluated across the evaluation layers, then record the results against that registration. Holds the Evaluation records (`EVL-###`) and, for AI components, the evaluation datasets.

## Record

Record contracts: Evaluation [`evaluation/EVALUATION_SYSTEM.md`](../evaluation/EVALUATION_SYSTEM.md) §4; evaluation dataset [`evaluation/EVALUATION_DATASET.md`](../evaluation/EVALUATION_DATASET.md) §3.

```yaml
evaluation_plan:
  initiative_id:            # INI-###
  pilot_id:                 # PLT-###, when the plan evaluates a pilot
  rollout_id:               # ROL-###, when it evaluates a rollout
  owner:
  registered_on:            # date the plan fields were fixed, before execution
  evaluations: []           # EVL records, plan fields only (layer, metric_ids, method, sample, threshold, owner); each inherits initiative_id from the plan
  not_evaluated: []         # optional: {layer, reason} for each evaluation/EVALUATION_SYSTEM.md §2 layer judged not relevant
  datasets: []              # eval_dataset records, for AI components

results: []                 # append-only; written after execution
  # - evaluation_id:        # EVL-### from `evaluations`
  #   actual:
  #   conclusion:           # PASS | PASS_WITH_LIMITATIONS | FAIL | INSUFFICIENT_EVIDENCE
  #   limitations:
  #   evidence_ids: []
  #   recorded_on:          # extension: date the result was recorded

pilot_result:               # PROMOTE | REVISE | REPEAT | STOP | INSUFFICIENT_EVIDENCE (execution/PILOT_MODEL.md §6); pilots only
```

A `results` entry holds the result fields of one EVL record; the record is its planned entry plus its result entry.

## Rules

Plan fields are fixed before execution and MUST NOT be changed after results are known ([`execution/PILOT_MODEL.md`](../execution/PILOT_MODEL.md) §5). Results are appended, never overwritten; a repeated evaluation gets a new EVL record.

`pilot_result` is derived from the results against the pilot's pre-defined success and stop criteria; unmet success criteria never yield PROMOTE. PROMOTE is a recommendation until a Decision closes `HG-PROMOTION` ([`STANDARD.md`](../STANDARD.md) §8). Promotion despite unmet criteria is waived only in that Decision ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md) §4); `pilot_result` stays as derived.

A passing AI evaluation does not imply a passing business evaluation ([`evaluation/EVALUATION_SYSTEM.md`](../evaluation/EVALUATION_SYSTEM.md) §5).

## Validation

- [ ] linked to an Initiative, and to the pilot or rollout it evaluates
- [ ] every layer of [`evaluation/EVALUATION_SYSTEM.md`](../evaluation/EVALUATION_SYSTEM.md) §2 has at least one evaluation with a threshold, or is listed in `not_evaluated` with a reason; where AI is used, human-AI interaction and technical reliability are evaluated
- [ ] plan fields were registered before execution and are unchanged in the results
- [ ] every result states actual, conclusion, limitations, and Evidence
- [ ] Governed: each AI component has a dataset covering [`evaluation/EVALUATION_DATASET.md`](../evaluation/EVALUATION_DATASET.md) §2, with leakage tracked per its §4
