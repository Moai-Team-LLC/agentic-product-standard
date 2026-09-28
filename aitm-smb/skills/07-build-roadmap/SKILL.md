---
name: 07-build-roadmap
description: "Phase 6 orchestrator. Turns the approved target into an executable transition: sequences Initiatives, designs operable Transition States (skill 21), Transformation Slices, decision and execution gates, rollback, the Transformation Portfolio under the Portfolio profile (skill 22), and, where material uncertainty remains, Pilots with pre-registered evaluation and evaluation datasets (skills 25, 26, 27); stops for budget approval (HG-BUDGET). Use after the target system is approved, before operationalization. Produces the Transformation Roadmap, Transition States, Pilot and Evaluation Plans, Execution Gate records and the Portfolio. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "6"
human_gate: true
gates: [HG-BUDGET]
---

# Skill 07: Orchestrate Transformation Roadmap

## Purpose

Sequence transformation through operable states, bounded WIP, dependencies, evidence gates, and pre-registered pilots.

## Required inputs

The Required inputs of `methodology/06-roadmap.md` (approved Target Operating Architecture or, in Compact, Capability Target States; selected Initiatives and their System Effect Assessments; Authority Ceilings where AI authority changes).

## Normative sources

- `methodology/06-roadmap.md` and the modules in its Method

## Produces

Only what the active profile requires (`APPLICATION_PROFILES.md`):

- `artifacts/transformation-roadmap.md` — execution-ready Initiative records (`INI-###`)
- Transformation Slices (`SLC-###`, record contract `execution/DELIVERY_SLICE.md`), referenced from the Initiative `slice_ids`
- Experiments (`EXP-###`, record contract `execution/EXPERIMENT_MODEL.md`), where used
- `artifacts/transition-state.md` — where the profile requires it (skill 21)
- `artifacts/pilot-plan.md` — where a pilot is required (skill 25)
- `artifacts/evaluation-plan.md` — where a pilot is required: pre-registered plan (skill 26) and datasets for AI components (skill 27)
- `artifacts/execution-gate.md` — the Execution Gate records each Initiative needs, including Gate C (skill 25); Governed (optional otherwise)
- `artifacts/transformation-portfolio.md` — Portfolio profile (skill 22)
- `artifacts/decision-assumption-log.md` — budget Decisions, Assumptions

## Specialist skills

- `skills/21-design-transition-states/SKILL.md` — where the profile requires Transition States
- `skills/22-build-transformation-portfolio/SKILL.md` — Portfolio profile
- `skills/25-design-pilot/SKILL.md` — where material uncertainty requires a pilot (INV-11)
- `skills/26-design-evaluation/SKILL.md` — for each pilot: pre-register its evaluation before it runs
- `skills/27-build-eval-dataset/SKILL.md` — for each AI component to be evaluated

## Procedure

1. Load the active profiles (`AGENT_CONTEXT_POLICY.md`) and `methodology/06-roadmap.md`.
2. Verify the phase's Required inputs; stop with `BLOCKED` while `HG-TOA` is open.
3. Execute the phase Activities, invoking the specialists where their conditions hold; 26 runs after 25 and before the pilot starts.
4. Place every planned AI authority increase behind an `HG-AUTHORITY` entry in the Initiative `decision_gates`.
5. Merge specialist outputs into the phase instances; keep stable IDs and the `TRACEABILITY.md` §4 trace.
6. Validate the phase Exit condition (`EXECUTION_MODEL.md` §2) and the Validation of each produced contract.
7. Stop with `INSUFFICIENT_EVIDENCE` when a plan would rest on invented facts; record Evidence Debt.
8. Submit material budget for approval.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-BUDGET`; the approval is recorded as a DEC with `gate:` set, listing the budgeted `INI-###`, `PLT-###`, or `PTF-###` in `subject_ids`. Gates reached by specialists (e.g. `HG-RISK`, `HG-AUTHORITY` for a pilot) are carried into the handoff. Any other `STANDARD.md` §8 gate applies whenever its trigger occurs.

## MUST NOT

- plan a big-bang migration, scale before proof, or autonomy before observability;
- define or change success criteria after results are known;
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
