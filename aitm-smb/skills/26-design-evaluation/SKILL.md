---
name: 26-design-evaluation
description: "Pre-registers how a pilot, rollout, or operating Capability will be evaluated: one Evaluation record per relevant layer, from business Outcome to risk and governance, including human-AI interaction and technical reliability where AI is used, with metrics, method, sample, threshold and owner fixed before execution, and AI evaluations that strengthen as autonomy rises. Use in Phase 6 before a pilot runs, in Phase 7 before a rollout stage whose evaluation must be extended, and in Phase 8 when new evaluations are needed. Produces the plan section (EVL plan fields) of artifacts/evaluation-plan.md. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: execution-governance
phase: "6-8"
human_gate: false
---

# Skill 26: Design Evaluation

## Purpose

Fix what counts as success before evidence exists, so results cannot reshape the criteria. Invoked by [`skills/07-build-roadmap/SKILL.md`](../07-build-roadmap/SKILL.md) (pilots), [`skills/08-design-operating-model/SKILL.md`](../08-design-operating-model/SKILL.md) (before a rollout stage whose evaluation must be extended), and [`skills/09-measure-evolution/SKILL.md`](../09-measure-evolution/SKILL.md) (evaluation updates).

## Required inputs

- Initiative (INI) and the Pilot Plan or Rollout Plan being evaluated, or the operating Capability;
- Metric records with baselines ([`artifacts/transformation-scorecard.md`](../../artifacts/transformation-scorecard.md));
- AI components and their target autonomy levels, if any.

## Normative sources

- [`evaluation/EVALUATION_SYSTEM.md`](../../evaluation/EVALUATION_SYSTEM.md)
- [`evaluation/AI_EVALS.md`](../../evaluation/AI_EVALS.md)
- [`METRICS.md`](../../METRICS.md)

## Produces

- [`artifacts/evaluation-plan.md`](../../artifacts/evaluation-plan.md) — `evaluation_plan` with EVL records (plan fields only) and `registered_on`. Datasets: skill 27. Results: skill 32 (pilots) or skill 09.

## Procedure

1. Select the relevant layers ([`evaluation/EVALUATION_SYSTEM.md`](../../evaluation/EVALUATION_SYSTEM.md) §2); where AI is used, include human-AI interaction and technical reliability; list each other layer in `not_evaluated` with a reason.
2. Write one EVL record per evaluation with its plan fields (§4): layer, metric_ids, method, sample, threshold, owner. Business-facing layers use business Metrics.
3. For AI components, choose reference-based or calibrated reference-free evaluation ([`evaluation/AI_EVALS.md`](../../evaluation/AI_EVALS.md) §3), and shift toward trajectory quality, action correctness, policy compliance and state integrity as autonomy increases (§5).
4. Name the evaluation datasets needed; [`skills/27-build-eval-dataset/SKILL.md`](../27-build-eval-dataset/SKILL.md) builds them.
5. Check that AI metrics do not substitute for business metrics ([`evaluation/EVALUATION_SYSTEM.md`](../../evaluation/EVALUATION_SYSTEM.md) §5).
6. Set `registered_on` before execution. Later changes add new EVL records; registered plan fields never change.
7. Validate against the Validation of [`artifacts/evaluation-plan.md`](../../artifacts/evaluation-plan.md).
8. Stop with `INSUFFICIENT_EVIDENCE` when a threshold or baseline would have to be invented (record Evidence Debt), or `BLOCKED` when a required input is missing.

## MUST NOT

- change plan fields or thresholds after results are known;
- let an AI evaluation stand in for a business evaluation;
- invent business facts; renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
