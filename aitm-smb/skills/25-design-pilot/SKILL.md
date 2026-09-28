---
name: 25-design-pilot
description: "Designs a bounded pilot that tests a transformation Hypothesis under real or production-representative conditions: pilot type and autonomy level within the Authority Ceiling, smallest sufficient scope and duration, baseline and comparison method, success and stop criteria fixed before execution, risks, guardrails, rollback, evidence plan, owner and post-pilot decision owner, checked against the pilot validity rules; updates Execution Gate C. Use in Phase 6 when material uncertainty remains before an Initiative scales (INV-11). Produces a PLT record per artifacts/pilot-plan.md and stops where the pilot accepts material risk; a pilot above the approved AI level starts only after the HG-AUTHORITY grant (skill 34). Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: execution-governance
phase: "6"
human_gate: true
gates: [HG-RISK, HG-AUTHORITY]
---

# Skill 25: Design Pilot

## Purpose

Design a pilot whose result can justify, or stop, promotion to rollout. Invoked by [`skills/07-build-roadmap/SKILL.md`](../07-build-roadmap/SKILL.md) where a pilot is required.

## Required inputs

- selected Initiative (INI) and the Hypotheses it tests (HYP);
- Capability Target State and, where they exist, Transition States;
- baseline Metrics (MET), or Evidence Debt recorded for a missing baseline;
- Autonomy Assessment with approved Authority Ceiling, where AI takes part;
- material Uncertainties ([`artifacts/evidence-register.md`](../../artifacts/evidence-register.md)).

## Normative sources

- [`execution/PILOT_MODEL.md`](../../execution/PILOT_MODEL.md)
- [`execution/EXPERIMENT_MODEL.md`](../../execution/EXPERIMENT_MODEL.md)
- [`execution/EXECUTION_GATE_MODEL.md`](../../execution/EXECUTION_GATE_MODEL.md) (Gate C)

## Produces

- [`artifacts/pilot-plan.md`](../../artifacts/pilot-plan.md) — PLT record with every field of its contract;
- [`artifacts/execution-gate.md`](../../artifacts/execution-gate.md) — Gate C record of the Initiative (created by skill 07): `evidence_provided` and a proposed status (Governed).

## Procedure

1. Confirm a pilot is needed: a test whose result is the evidence for promotion is a Pilot; a bounded question answered more cheaply is an Experiment ([`execution/EXPERIMENT_MODEL.md`](../../execution/EXPERIMENT_MODEL.md) §1, §4, §5), recorded per its §3 instead.
2. State the Hypotheses tested and the Outcomes targeted.
3. Choose `pilot_type` ([`execution/PILOT_MODEL.md`](../../execution/PILOT_MODEL.md) §3) and, separately, `autonomy_level`; the type does not set authority, and the level stays within the Authority Ceiling. A level above the currently approved level (AUT `current_level`) needs a grant: plan the pilot-grant criteria ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../../governance/AUTHORITY_ESCALATION_MODEL.md) §3 (a)) and return a `{gate: HG-AUTHORITY, subject_ids: [AUT-###]}` entry for the Initiative's `decision_gates` (skill 07).
4. Choose the smallest scope capable of testing the Hypotheses (§4) and a `duration_or_volume`.
5. Record the baseline and the `control_or_comparison` method; a missing baseline is recorded as Evidence Debt.
6. Fix success and stop criteria, and have [`skills/26-design-evaluation/SKILL.md`](../26-design-evaluation/SKILL.md) pre-register the evaluations (`pilot_id` set), before execution.
7. Define guardrails, rollback, evidence plan, owner, and the human `decision_owner` for promotion; record the pilot's risks as Risk records (RSK-###, [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md)) and list them in `risks`.
8. Check that no invalidity condition of [`execution/PILOT_MODEL.md`](../../execution/PILOT_MODEL.md) §5 holds.
9. Governed: update Gate C with `evidence_provided`, the `human_gates` it needs (`HG-AUTHORITY`, `HG-RISK` where they apply), and a proposed status; its approver decides it.
10. Validate against the Validation of [`artifacts/pilot-plan.md`](../../artifacts/pilot-plan.md); review aid: [`rubrics/PILOT_QUALITY_RUBRIC.md`](../../rubrics/PILOT_QUALITY_RUBRIC.md).
11. Stop with `INSUFFICIENT_EVIDENCE` when proceeding would require invented business facts, `HUMAN_DECISION_REQUIRED` while a required upstream gate is still open (gate in `open_gates`), or `BLOCKED` when a required input is missing.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-RISK` when the pilot accepts material risk, before the pilot starts; record the gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing the PLT-### and the accepted RSK-### in `subject_ids`; the named human's approval updates it to `approved`. A pilot above AUT `current_level` starts only after `HG-AUTHORITY` closes: [`skills/34-manage-authority-promotion/SKILL.md`](../34-manage-authority-promotion/SKILL.md) performs the grant before the pilot starts (Phase 7, invoked by skill 08), with a Decision that lists the AUT-### (the PLT-### as context) and states the new level and scope in `statement`.

## MUST NOT

- run a demo or prototype as a pilot, or observe only AI-quality metrics;
- define or change success and stop criteria after results are known;
- let the pilot type imply authority, or exceed the Authority Ceiling;
- pass Gate C, or record an approval the named human has not explicitly given.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
