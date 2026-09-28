---
name: 09-measure-evolution
description: "Phase 8 orchestrator. Determines whether the transformation created sustained business value and evolves the system from evidence: evaluates Outcome, Capability, operating, AI-quality and economic effects against baselines, pre-registers new evaluations (skill 26) and records their results, assesses value state and attribution (skill 33), and promotes or demotes AI authority from evidence (skill 34); stops before value is declared realized (HG-VALUE) or authority is increased (HG-AUTHORITY). Use after rollout or operation has produced evidence. Produces the Transformation Scorecard, the Value Realization Report and updated evaluations, authority and design records. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "8"
human_gate: true
gates: [HG-VALUE, HG-AUTHORITY]
---

# Skill 09: Orchestrate Measurement & Evolution

## Purpose

Evaluate business effect, capability effect, economics, and AI quality, and update the architecture and AI authority from evidence.

## Required inputs

The Required inputs of `methodology/08-measurement-evolution.md` (Outcome and Metric records with baselines, evaluation and pilot results, rollout and operating data, cost data, incident history, Autonomy Assessments where AI is used).

## Normative sources

- `methodology/08-measurement-evolution.md` and the modules in its Method

## Produces

Only what the active profile requires (`APPLICATION_PROFILES.md`):

- `artifacts/transformation-scorecard.md` — Metric records (`MET-###`), observations, and the effect conclusion
- `artifacts/value-realization-report.md` — value state and value conclusion, where the profile requires it (skill 33)
- `artifacts/evaluation-plan.md` — `results` of post-rollout evaluations; new EVL plans (skill 26)
- `artifacts/execution-gate.md` — Gate G (skill 33); Governed
- `artifacts/autonomy-assessment.md` — updates after promotion or demotion (skill 34)
- `artifacts/decision-assumption-log.md` — gate Decisions, revised Assumptions
- updates to diagnosis, Capability Target States, Target Operating Architecture, or Roadmap where Evidence disproves an assumption (`EXECUTION_MODEL.md` §3)

## Specialist skills

- `skills/26-design-evaluation/SKILL.md` — to pre-register new evaluations (new EVL records) for post-rollout measurement; 09 records their results; never to rewrite pre-registered success criteria
- `skills/33-assess-value-realization/SKILL.md` — where the profile requires a Value Realization Report
- `skills/34-manage-authority-promotion/SKILL.md` — where AI is used: promote, retain, or demote from evidence

## Procedure

1. Load the active profiles (`AGENT_CONTEXT_POLICY.md`) and `methodology/08-measurement-evolution.md`.
2. Verify the phase's Required inputs; stop with `BLOCKED` when no baseline or evidence period exists.
3. Execute the phase Activities, invoking 26, 33, and 34 where their conditions hold.
4. Record evaluation `results` against the pre-registered plans, the effect conclusion in the scorecard, and, where required, the value state and value conclusion (skill 33).
5. Decide per Initiative (phase Activity 11); scaling goes back through Phase 7 rollout gates (skill 08).
6. Keep stable IDs and the `TRACEABILITY.md` §4 trace; validate the phase Exit condition (`EXECUTION_MODEL.md` §2) and each produced contract.
7. Stop with `INSUFFICIENT_EVIDENCE` when a conclusion would rest on invented facts; report negative and failed results.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-VALUE` (value state REALIZED or SUSTAINED, or conclusion `VALUE_CONFIRMED`) and `HG-AUTHORITY` (AI authority increased or restored); the approval is recorded as a DEC with `gate:` set, listing the `VRL-###` or `AUT-###` in `subject_ids`. Demotion needs no gate. Any other `STANDARD.md` §8 gate applies whenever its trigger occurs.

## MUST NOT

- treat deployment, adoption, or AI quality as business value;
- hide negative or failed results;
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
