---
name: 09-measure-evolution
description: "Phase 8 orchestrator. Determines whether the transformation created sustained business value and evolves the system from evidence: evaluates Outcome, Capability, operating, AI-quality and economic effects against baselines, pre-registers new evaluations (skill 26) and records their results, assesses value state and attribution (skill 33), and promotes or demotes AI authority from evidence (skill 34); stops before value is declared realized (HG-VALUE) or authority is increased (HG-AUTHORITY). Use after rollout or operation has produced evidence. Produces the Transformation Scorecard, the Value Realization Report and updated evaluation and authority records; returns disproved diagnosis or design to its phase. Part of AITM-SMB; paths are relative to the AITM-SMB root."
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

Evaluate business effect, capability effect, economics, and AI quality; update AI authority from evidence and return disproved diagnosis or design to its phase.

## Required inputs

The Required inputs of [`methodology/08-measurement-evolution.md`](../../methodology/08-measurement-evolution.md) (Outcome and Metric records with baselines or recorded baseline gaps, evaluation and pilot results, rollout and operating data, cost data and economic hypotheses, incident history, Autonomy Assessments where AI is used).

## Normative sources

- [`methodology/08-measurement-evolution.md`](../../methodology/08-measurement-evolution.md) and the modules in its Method

## Produces

Only what the active profile requires ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md)):

- [`artifacts/transformation-scorecard.md`](../../artifacts/transformation-scorecard.md) — Metric records (`MET-###`), observations, and the effect conclusion
- [`artifacts/value-realization-report.md`](../../artifacts/value-realization-report.md) — value state and value conclusion, where the profile requires it (skill 33)
- [`artifacts/evaluation-plan.md`](../../artifacts/evaluation-plan.md) — `results` of post-rollout evaluations; new EVL plans (skill 26)
- [`artifacts/execution-gate.md`](../../artifacts/execution-gate.md) — Gate G (skill 33); Governed
- [`artifacts/autonomy-assessment.md`](../../artifacts/autonomy-assessment.md) — updates after promotion or demotion (skill 34)
- [`artifacts/ai-governance-canvas.md`](../../artifacts/ai-governance-canvas.md) — AI Change (`CHG-###`) records for those promotions or demotions (skill 34), where AI Change Control applies
- [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md) — gate Decisions, revised Assumptions

## Specialist skills

- [`skills/26-design-evaluation/SKILL.md`](../26-design-evaluation/SKILL.md) — to pre-register new evaluations (new EVL records) for post-rollout measurement; 09 records their results; never to rewrite pre-registered success criteria
- [`skills/33-assess-value-realization/SKILL.md`](../33-assess-value-realization/SKILL.md) — where the profile requires a Value Realization Report
- [`skills/34-manage-authority-promotion/SKILL.md`](../34-manage-authority-promotion/SKILL.md) — where AI is used: promote, retain, or demote from evidence

## Procedure

1. Load the active profiles ([`AGENT_CONTEXT_POLICY.md`](../../AGENT_CONTEXT_POLICY.md)) and [`methodology/08-measurement-evolution.md`](../../methodology/08-measurement-evolution.md).
2. Verify the phase's Required inputs; stop with `BLOCKED` only when no evidence period exists. Without a measured baseline, continue: the scorecard effect conclusion is `INSUFFICIENT_EVIDENCE`, the value state stays HYPOTHESIZED (skill 33), Evidence Debt is recorded, and the status is `PARTIAL` or `INSUFFICIENT_EVIDENCE`.
3. Execute the phase Activities, invoking 26, 33, and 34 where their conditions hold.
4. Record evaluation `results` against the pre-registered plans, the effect conclusion in the scorecard, and, where required, the value state and value conclusion (skill 33).
5. Where Evidence disproves an assumption, return the work to its phase ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §3) and name the orchestrator in `next_skill`: diagnosis to skill 03, Capability Target State or Target Operating Architecture to skill 06, roadmap to skill 07. This skill does not edit those records.
6. Decide per Initiative (phase Activity 11); scaling goes back through Phase 7 rollout gates (skill 08).
7. Keep stable IDs and the [`TRACEABILITY.md`](../../TRACEABILITY.md) §4 trace; validate the phase Exit condition ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §2) and each produced contract.
8. Stop with `INSUFFICIENT_EVIDENCE` when a conclusion would rest on invented facts; report negative and failed results.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-VALUE` (value state REALIZED or SUSTAINED, or conclusion `VALUE_CONFIRMED`) and `HG-AUTHORITY` (AI authority increased or restored); record each gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing in `subject_ids` the `AUT-###` (`HG-AUTHORITY`) or the `HG-VALUE` subject ([`measurement/VALUE_REALIZATION.md`](../../measurement/VALUE_REALIZATION.md) §2: the `VRL-###`, or without a report the `INI-###` and Outcome `MET-###`); the named human's approval updates it to `approved`. Demotion needs no gate. Any other [`STANDARD.md`](../../STANDARD.md) §8 gate applies whenever its trigger occurs.

## MUST NOT

- treat deployment, adoption, or AI quality as business value;
- hide negative or failed results;
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
