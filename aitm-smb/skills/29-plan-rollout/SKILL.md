---
name: 29-plan-rollout
description: "Plans a progressive rollout after an approved promotion: stages along the rollout dimensions, each stage's autonomy level within the Authority Ceiling, the rollout gates verified before every stage, monitoring, support, rollback versus recovery, legacy-path retirement, change capacity and completion criteria, linked to the pilot, its evaluations and the promotion Decision. Use in Phase 7 only after a material pilot's HG-PROMOTION Decision is approved, or for an Initiative that needed no pilot. Produces a ROL record per artifacts/rollout-plan.md and stops where a stage accepts material risk; a stage that raises AI authority starts only after the HG-AUTHORITY grant (skill 34). Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: execution-governance
phase: "7"
human_gate: true
gates: [HG-AUTHORITY, HG-RISK]
---

# Skill 29: Plan Progressive Rollout

## Purpose

Expand a validated transformation in controlled stages, each entered only after its gates hold (evidence before scale, INV-11). Invoked by [`skills/08-design-operating-model/SKILL.md`](../08-design-operating-model/SKILL.md) after `HG-PROMOTION`.

## Required inputs

- for a material pilot: the approved Decision closing `HG-PROMOTION` (DEC-###) for the pilot (it records any waiver of unmet success criteria), and the pilot's EVL results and `pilot_result` ([`artifacts/evaluation-plan.md`](../../artifacts/evaluation-plan.md)); while that gate is open, stop with `HUMAN_DECISION_REQUIRED` (`HG-PROMOTION` in `open_gates`);
- Initiative (INI), target scope, and the Pilot Plan (PLT) where a pilot preceded the rollout;
- Autonomy Assessment with approved Authority Ceiling and `current_level`, where AI is used;
- Observability Plan and Adoption Plan, where they exist.

## Normative sources

- [`execution/ROLLOUT_MODEL.md`](../../execution/ROLLOUT_MODEL.md)
- [`execution/EXECUTION_GATE_MODEL.md`](../../execution/EXECUTION_GATE_MODEL.md) (Gate E)
- [`governance/AUTHORITY_ESCALATION_MODEL.md`](../../governance/AUTHORITY_ESCALATION_MODEL.md)

## Produces

- [`artifacts/rollout-plan.md`](../../artifacts/rollout-plan.md) — ROL record, created or updated.

## Procedure

1. Where a pilot preceded the rollout, verify the promotion Decision is approved and names the PLT-### in `subject_ids`; set `pilot_id`, `promotion_decision_id`, and `evaluation_ids`.
2. Choose stages along the rollout dimensions ([`execution/ROLLOUT_MODEL.md`](../../execution/ROLLOUT_MODEL.md) §2), following the progressive pattern (§4).
3. Set each stage's `autonomy_level` within the Authority Ceiling. A stage above the currently approved level (AUT `current_level`) is an authority increase: [`skills/34-manage-authority-promotion/SKILL.md`](../34-manage-authority-promotion/SKILL.md) performs the grant through `HG-AUTHORITY` before the stage starts. A stage that only widens scope at the approved level, for the same action class and ceiling, is rollout, not an authority increase.
4. Set `entry_gates` to at least the §3 rollout gates plus stage-specific gates; Governed: link each stage's Gate E record (`gate_id`).
5. Define monitoring from the Observability Plan, support model, rollback and recovery (§5), and legacy-path retirement.
6. Check organizational change capacity (Portfolio: `change_capacity` and `wip_limit` in the Transformation Portfolio).
7. Define completion criteria covering §6.
8. Validate against the Validation of [`artifacts/rollout-plan.md`](../../artifacts/rollout-plan.md).
9. Stop with `INSUFFICIENT_EVIDENCE` when proceeding would require invented business facts, `HUMAN_DECISION_REQUIRED` while a required upstream gate is still open (gate in `open_gates`), or `BLOCKED` when a required input is missing.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-RISK` when a stage or the completion accepts a material known risk (a Risk record, RSK-###, with its owner); record the gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing the ROL-### (naming the stage) and the accepted RSK-### in `subject_ids`; the named human's approval updates it to `approved`. A stage whose autonomy level is above AUT `current_level` starts only after `HG-AUTHORITY` closes: skill 34's Decision lists the AUT-### (the ROL-### and stage as context) and states the new level and scope in `statement`.

## MUST NOT

- plan the rollout of a material pilot without an approved `HG-PROMOTION` Decision;
- raise autonomy through a stage outside skill 34 and `HG-AUTHORITY`, or above the Authority Ceiling;
- declare the rollout complete while a completion criterion of [`execution/ROLLOUT_MODEL.md`](../../execution/ROLLOUT_MODEL.md) §6 is unmet;
- record an approval the named human has not explicitly given.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
