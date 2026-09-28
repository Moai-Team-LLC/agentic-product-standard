---
name: 32-evaluate-pilot
description: "Evaluates a pilot against its pre-registered Evaluation Plan: checks the plan was fixed before execution and the pilot is valid, appends the result fields (actual, conclusion, limitations, Evidence) of each Evaluation record to the plan's results section with layers kept separate, derives the pilot result (PROMOTE, REVISE, REPEAT, STOP, INSUFFICIENT_EVIDENCE) from the pre-defined success and stop criteria, and updates Execution Gate D. Use in Phase 7 when a pilot has run. PROMOTE is a recommendation: the skill stops for the HG-PROMOTION decision. Produces results in artifacts/evaluation-plan.md. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: execution-governance
phase: "7"
human_gate: true
gates: [HG-PROMOTION]
---

# Skill 32: Evaluate Pilot

## Purpose

Judge a pilot only by the criteria fixed before it ran, and put the promotion decision in human hands. Invoked by `skills/08-design-operating-model/SKILL.md` after a pilot has run.

## Required inputs

- Pilot Plan (PLT) with success and stop criteria;
- the pre-registered Evaluation Plan (`registered_on` before the pilot ran);
- pilot Evidence (EVD) and operating data;
- Incident records (INC-###) from the pilot period, where any.

## Normative sources

- `execution/PILOT_MODEL.md`
- `evaluation/EVALUATION_SYSTEM.md`
- `execution/EXECUTION_GATE_MODEL.md` (Gate D)

## Produces

- `artifacts/evaluation-plan.md` — `results` entries (one per EVL record) and `pilot_result`; plan fields and the Pilot Plan are read-only;
- `artifacts/execution-gate.md` — Gate D record (created by skill 07): `evidence_provided` and a proposed status (Governed).

## Procedure

1. Verify the plan fields were registered before execution and are unchanged, and that no invalidity condition of `execution/PILOT_MODEL.md` §5 holds; an invalid pilot cannot yield PROMOTE.
2. For each EVL record, append one result entry: actual against threshold, conclusion (`evaluation/EVALUATION_SYSTEM.md` §5), limitations, `evidence_ids`. Keep layers separate.
3. Record limitations and attribution uncertainty, including incidents during the pilot.
4. Derive `pilot_result` (`execution/PILOT_MODEL.md` §6) from the results against the pre-defined success and stop criteria. Promotion despite unmet criteria needs a Gate D waiver Decision (`execution/EXECUTION_GATE_MODEL.md` §4).
5. Identify the diagnosis, design, or roadmap updates the results require (`EXECUTION_MODEL.md` §3).
6. Governed: update Gate D with the EVL and EVD provided and a proposed status.
7. Validate against the Validation of `artifacts/evaluation-plan.md`.
8. Stop with `INSUFFICIENT_EVIDENCE` when results cannot be established without invented facts (record Evidence Debt), or `BLOCKED` when a required input is missing.

## Human gates

On PROMOTE for a material pilot, stop with status `HUMAN_DECISION_REQUIRED` at `HG-PROMOTION`: list the gate in `open_gates` and the promotion question, with the PLT-### and EVL-### in `subject_ids`, in `decisions_needed`. The approval is recorded as a DEC with `gate:` set (`artifacts/decision-assumption-log.md`) only after the named human gives it; `skills/29-plan-rollout/SKILL.md` then plans the rollout.

## MUST NOT

- change thresholds, success criteria, or other plan fields after results are known;
- overwrite a result; a repeated evaluation gets a new EVL record;
- let a passing AI evaluation stand in for business effect, or hide negative results;
- record the promotion Decision or pass Gate D itself.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
