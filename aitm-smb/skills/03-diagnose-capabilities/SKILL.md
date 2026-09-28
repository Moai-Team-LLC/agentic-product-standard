---
name: 03-diagnose-capabilities
description: "Phase 2 orchestrator. Diagnoses why current Capabilities do not produce the required Outcomes: separates observations and symptoms from Gaps (skill 12), generates competing cause Hypotheses and tests them against evidence (skill 16), and decides which Gaps are intervention-ready. Use after the current system is mapped and before any intervention is designed. Produces the Capability Diagnosis, Diagnostic Records and cause Hypotheses in the Decision and Assumption Log. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "2"
human_gate: false
---

# Skill 03: Orchestrate Capability Diagnosis

## Purpose

Move from observations and symptoms to evidence-backed Gaps and causes, so that interventions address causes rather than pain points.

## Required inputs

The Required inputs of `methodology/02-capability-diagnosis.md` (approved Transformation Intent, Capability Map with CURRENT States).

## Normative sources

- `methodology/02-capability-diagnosis.md` and the modules in its Method
- `AGENT_DIAGNOSTIC_PROTOCOL.md` — agents follow it in this phase

## Produces

- `artifacts/capability-diagnosis.md` — Gaps (`GAP-###`) with `cause_status`
- `artifacts/diagnostic-record.md` — Diagnostic Records (`DIA-###`)
- `artifacts/decision-assumption-log.md` — cause Hypotheses (`HYP-###`, `kind: cause`), Assumptions

Evidence and Evidence Debt are appended as any skill may (`skills/INDEX.md` §4).

## Specialist skills

- `skills/12-separate-symptoms-gaps-causes/SKILL.md` — always: observations, symptoms, Gaps, competing cause Hypotheses
- `skills/16-validate-root-cause/SKILL.md` — for the cause Hypotheses of each material Gap, before the Gap is declared intervention-ready

## Procedure

1. Load the active profiles (`AGENT_CONTEXT_POLICY.md`), `methodology/02-capability-diagnosis.md`, and `AGENT_DIAGNOSTIC_PROTOCOL.md`.
2. Verify the phase's Required inputs; stop with `BLOCKED` when one is missing.
3. Execute the phase Activities: skill 12, then skill 16.
4. Merge specialist outputs into the phase instances; set each Gap's `cause_status` from its Hypotheses (skill 16 findings); keep stable IDs and the `TRACEABILITY.md` §4 trace.
5. Validate the phase Exit condition (`EXECUTION_MODEL.md` §2) and the Validation of each produced contract; review aid: `rubrics/DIAGNOSTIC_QUALITY_RUBRIC.md`.
6. Pass only intervention-ready Gaps to Phase 3; for the others, record Evidence Debt. Stop with `INSUFFICIENT_EVIDENCE` when no material Gap is ready without invented facts; with `HUMAN_DECISION_REQUIRED` at any `STANDARD.md` §8 gate whose trigger occurs.

## MUST NOT

- jump from a symptom to a solution;
- treat a cause Hypothesis as validated without Evidence;
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
