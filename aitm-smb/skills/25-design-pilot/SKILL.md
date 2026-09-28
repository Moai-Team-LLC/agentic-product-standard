---
name: 25-design-pilot
description: "Designs a bounded pilot that tests a transformation Hypothesis under real or production-representative conditions: pilot type and autonomy level within the Authority Ceiling, smallest sufficient scope and duration, baseline and comparison method, success and stop criteria fixed before execution, risks, guardrails, rollback, evidence plan, owner and post-pilot decision owner, checked against the pilot validity rules; updates Execution Gate C. Use in Phase 6 when material uncertainty remains before an Initiative scales (INV-11). Produces a PLT record per artifacts/pilot-plan.md and stops where the pilot grants AI authority or accepts material risk. Part of AITM-SMB; paths are relative to the AITM-SMB root."
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

Design a pilot whose result can justify, or stop, promotion to rollout. Invoked by `skills/07-build-roadmap/SKILL.md` where a pilot is required.

## Required inputs

- selected Initiative (INI) and the Hypotheses it tests (HYP);
- Capability Target State and, where they exist, Transition States;
- baseline Metrics (MET), or Evidence Debt recorded for a missing baseline;
- Autonomy Assessment with approved Authority Ceiling, where AI takes part;
- material Uncertainties (`artifacts/evidence-register.md`).

## Normative sources

- `execution/PILOT_MODEL.md`
- `execution/EXPERIMENT_MODEL.md`
- `execution/EXECUTION_GATE_MODEL.md` (Gate C)

## Produces

- `artifacts/pilot-plan.md` — PLT record with every field of its contract;
- `artifacts/execution-gate.md` — Gate C record of the Initiative (created by skill 07): `evidence_provided` and a proposed status (Governed).

## Procedure

1. Confirm a pilot is needed: a test whose result is the evidence for promotion is a Pilot; a bounded question answered more cheaply is an Experiment (`execution/EXPERIMENT_MODEL.md` §1, §4, §5), recorded per its §3 instead.
2. State the Hypotheses tested and the Outcomes targeted.
3. Choose `pilot_type` (`execution/PILOT_MODEL.md` §3) and, separately, `autonomy_level`; the type does not set authority, and the level stays within the Authority Ceiling.
4. Choose the smallest scope capable of testing the Hypotheses (§4) and a `duration_or_volume`.
5. Record the baseline and the `control_or_comparison` method; a missing baseline is recorded as Evidence Debt.
6. Fix success and stop criteria, and have `skills/26-design-evaluation/SKILL.md` pre-register the evaluations (`pilot_id` set), before execution.
7. Define guardrails, rollback, evidence plan, owner, and the human `decision_owner` for promotion; record the pilot's risks as Risk records (RSK-###, `artifacts/decision-assumption-log.md`) and list them in `risks`.
8. Check that no invalidity condition of `execution/PILOT_MODEL.md` §5 holds.
9. Governed: update Gate C with the evidence provided and a proposed status; its approver decides it.
10. Validate against the Validation of `artifacts/pilot-plan.md`; review aid: `rubrics/PILOT_QUALITY_RUBRIC.md`.
11. Stop with `INSUFFICIENT_EVIDENCE` when proceeding would require invented business facts, or `BLOCKED` when a required input is missing.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-AUTHORITY` when the pilot's `autonomy_level` is above the currently approved level, and at `HG-RISK` when the pilot accepts material risk, before the pilot starts; the approval is recorded as a DEC with `gate:` set that lists the PLT-### (for `HG-RISK`, also the accepted RSK-###) in `subject_ids` (`artifacts/decision-assumption-log.md`).

## MUST NOT

- run a demo or prototype as a pilot, or observe only AI-quality metrics;
- define or change success and stop criteria after results are known;
- let the pilot type imply authority, or exceed the Authority Ceiling;
- pass Gate C, or record an approval the named human has not explicitly given.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
