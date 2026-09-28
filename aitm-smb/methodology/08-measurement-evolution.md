# Phase 8 — Measure & Evolve (Measurement & Evolution)

## Objective

Determine whether the transformation created sustained business value and evolve the system based on evidence.

## Required inputs

- Outcome and Metric records with baselines (`artifacts/transformation-intent.md`, `artifacts/transformation-scorecard.md`);
- Evaluation Plans with Phase 7 results and pilot results, where piloted;
- Rollout Plans and operating data from the Observability Plan, where rolled out;
- cost data;
- incident history (`INC-###`), where incidents occurred;
- Autonomy Assessments with current levels and Authority Ceilings, where AI is used;
- Evidence Register; Decision & Assumption Log.

## Method

Use:

1. `evaluation/EVALUATION_SYSTEM.md`
2. `evaluation/AI_EVALS.md`
3. `METRICS.md`
4. `economics/TRANSFORMATION_ECONOMICS.md`
5. `measurement/VALUE_REALIZATION.md`
6. `measurement/BENEFIT_EVIDENCE_CHAIN.md` (Measured)
7. `operations/INCIDENT_MODEL.md`
8. `governance/AUTHORITY_ESCALATION_MODEL.md`

## Activities

1. evaluate business Outcomes;
2. evaluate Capability performance;
3. evaluate operating performance;
4. evaluate AI quality where relevant;
5. evaluate economics against the economic hypothesis;
6. assess attribution confidence and competing explanations;
7. assess value sustainability;
8. incorporate incident and exception evidence;
9. record the effect conclusion and, where required, the value state and value conclusion;
10. update diagnosis, Capability Target State, Target Operating Architecture, or Roadmap where evidence disproves assumptions;
11. decide per Initiative: promote authority, revise, scale, reduce authority, or stop. Scaling goes through Phase 7 rollout gates; promoting authority requires `HG-AUTHORITY`; reducing authority is a demotion.

## Outputs

- Transformation Scorecard (`artifacts/transformation-scorecard.md`): Metric records, observations, effect conclusion;
- Value Realization Report (`VRL-###`, `artifacts/value-realization-report.md`): value state, value conclusion, and, under Measured, the benefit chain; where the profile requires it;
- updated Evaluation records (`artifacts/evaluation-plan.md`);
- Autonomy Assessment updates after promotion or demotion (`artifacts/autonomy-assessment.md`), where AI is used;
- Execution Gate G (`artifacts/execution-gate.md`), Governed;
- revised assumptions and decisions (`artifacts/decision-assumption-log.md`), including gate Decisions;
- Evidence Register updates;
- architecture/roadmap updates where required.

## Human gates

- `HG-VALUE` — before a value state REALIZED or SUSTAINED, or the conclusion `VALUE_CONFIRMED`, is declared.
- `HG-AUTHORITY` — before AI authority is increased or restored.

Stop with `HUMAN_DECISION_REQUIRED` until a Decision closing the gate is recorded (`STANDARD.md` §8). Demotion needs no gate. Any other gate applies whenever its trigger occurs. Governed profile: Execution Gate G (`execution/EXECUTION_GATE_MODEL.md`).

## Exit condition

Matches `EXECUTION_MODEL.md` §2:

```text
effect evaluated against baseline
AND value state recorded with Evidence, where the profile requires a Value Realization Report
AND diagnosis, target, roadmap and authority updated from Evidence
```

An Initiative is value-confirmed only when the conditions in `measurement/VALUE_REALIZATION.md` §6 hold and `HG-VALUE` is approved.

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` (`AGENTS.md` §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

```text
deployed or adopted → value realized
```
