# Phase 7 — Operationalize (Operating Model & Governance)

## Objective

Make the transformed system operable, governable, observable, and adoptable; run and evaluate pilots, decide promotion, and expand scope only through verified rollout gates and approved AI authority.

The Operating Model is who operates the transformed system and how it is run, decided, observed, supported, and governed after transformation.

## Required inputs

- approved Target Operating Architecture (Compact: Capability Target States) and Decision Rights Map, where the profile requires it;
- Transformation Roadmap (Initiative records with decision gates) and Transition States, where the profile requires them;
- Autonomy Assessments with approved Authority Ceilings, where AI is used;
- Pilot Plans and their pre-registered Evaluation Plans, where a pilot is required (Phase 6);
- Execution Gate records (Governed);
- Evidence Register; Decision & Assumption Log.

## Method

Use:

1. [`governance/GOVERNANCE_OPERATING_MODEL.md`](../governance/GOVERNANCE_OPERATING_MODEL.md)
2. [`governance/AI_CHANGE_CONTROL.md`](../governance/AI_CHANGE_CONTROL.md)
3. [`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md)
4. [`operations/OBSERVABILITY_MODEL.md`](../operations/OBSERVABILITY_MODEL.md)
5. [`operations/INCIDENT_MODEL.md`](../operations/INCIDENT_MODEL.md)
6. [`change/CHANGE_ADOPTION_MODEL.md`](../change/CHANGE_ADOPTION_MODEL.md)
7. [`change/ROLE_TRANSITION_MODEL.md`](../change/ROLE_TRANSITION_MODEL.md)
8. [`execution/PILOT_MODEL.md`](../execution/PILOT_MODEL.md)
9. [`evaluation/EVALUATION_SYSTEM.md`](../evaluation/EVALUATION_SYSTEM.md) (with [`evaluation/AI_EVALS.md`](../evaluation/AI_EVALS.md) for AI components)
10. [`execution/ROLLOUT_MODEL.md`](../execution/ROLLOUT_MODEL.md)
11. [`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md) (Governed)

## Activities

1. assign business and operational ownership;
2. define observability and make it active;
3. define incident handling;
4. define AI change control;
5. define authority promotion and demotion;
6. define role transitions;
7. define training, support, feedback, and adoption metrics;
8. define governance cadence and triggers;
9. run each pilot; record results against its pre-registered evaluation; classify the pilot result;
10. obtain the promotion decision (`HG-PROMOTION`) for each material pilot;
11. plan rollout: stages, per-stage gates, rollback or recovery, completion criteria; pre-register new evaluations (EVL) before a stage whose scope the pilot's evaluations do not cover;
12. verify the rollout gates before each rollout stage;
13. change AI authority only by an approved promotion (`HG-AUTHORITY`, criteria [`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3; a planned increase closes the `decision_gates` entry naming its AUT-### that Phase 6 placed on its Initiative when the increase is due) or by demotion.

## Outputs

- Operating Model ([`artifacts/operating-model.md`](../artifacts/operating-model.md));
- Observability Plan ([`artifacts/observability-plan.md`](../artifacts/observability-plan.md));
- Adoption Plan with role transitions ([`artifacts/adoption-plan.md`](../artifacts/adoption-plan.md));
- AI Governance Canvas with AI Change records (`CHG-###`) ([`artifacts/ai-governance-canvas.md`](../artifacts/ai-governance-canvas.md)), where AI is used;
- Evaluation Plan results (`EVL-###`) and pilot result ([`artifacts/evaluation-plan.md`](../artifacts/evaluation-plan.md)), where piloted; new pre-registered evaluations for rollout stages, where needed;
- Rollout Plan (`ROL-###`, [`artifacts/rollout-plan.md`](../artifacts/rollout-plan.md)), where rolling out;
- Autonomy Assessment updates after promotion or demotion ([`artifacts/autonomy-assessment.md`](../artifacts/autonomy-assessment.md)), where AI is used;
- Execution Gate records D, E, F ([`artifacts/execution-gate.md`](../artifacts/execution-gate.md)), Governed;
- Incident records (`INC-###`, [`artifacts/incident-record.md`](../artifacts/incident-record.md)) as incidents occur, Governed;
- Evidence Register and Decision & Assumption Log updates, including gate Decisions and Risk records (`RSK-###`).

Compact: the Phase 7 minimum (operating owner, observability signal, support path, role changes, failure or rollback path, adoption) MAY sit on the Initiative as `operation:` in [`artifacts/transformation-roadmap.md`](../artifacts/transformation-roadmap.md) instead of the Operating Model, Observability Plan, and Adoption Plan; the exit condition still holds.

## Human gates

- `HG-PROMOTION` — before a material pilot is promoted to rollout; the Decision lists the `PLT-###` in `subject_ids` and records any waiver of unmet success criteria ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md) §4).
- `HG-AUTHORITY` — before a pilot, rollout stage, or operation uses a level above the approved one (AUT `current_level`), and before authority is restored after a demotion; the Decision lists the `AUT-###` in `subject_ids` and states the new level and scope.
- `HG-RISK` — before a material Risk (`RSK-###`) is accepted, e.g. for a pilot or a rollout stage.
- `HG-DECISION-RIGHTS` — before material Decision Rights change through role transitions.

Record the gate Decision as `proposed` and stop with `HUMAN_DECISION_REQUIRED` until the human approves it ([`STANDARD.md`](../STANDARD.md) §8). Demotion needs no gate. Any other gate applies whenever its trigger occurs. Governed profile: Execution Gates D, E, F ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md)).

## Exit condition

Matches [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2:

```text
ownership explicit
AND observability active
AND failure path and support model defined
AND role changes explicit
AND adoption defined (training, support, feedback, adoption metrics)
AND governance controls executable
AND where piloted: pilot evaluated and promotion decided
AND where rolling out: rollout gates (execution/ROLLOUT_MODEL.md §3) verified before each stage
```

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` ([`AGENTS.md`](../AGENTS.md) §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

```text
promising pilot or demo → wider scope or higher AI authority
```

without a pre-registered evaluation, a promotion decision, verified rollout gates, and approved authority.
