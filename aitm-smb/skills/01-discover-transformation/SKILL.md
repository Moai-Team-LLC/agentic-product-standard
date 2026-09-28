---
name: 01-discover-transformation
description: "Phase 0 orchestrator. Frames an AI transformation of a small or medium-sized business: defines measurable business Outcomes with an accountable owner, baseline or known baseline gap, target, horizon, constraints and non-goals, selects the Application Profiles (skill 36), and stops for Outcome approval (HG-OUTCOME). Use at the start of an engagement or when the Outcomes change. Produces the Transformation Intent with Outcome records, baseline Metric records, and the profile and gate Decisions in the Decision and Assumption Log. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "0"
human_gate: true
gates: [HG-OUTCOME]
---

# Skill 01: Orchestrate Transformation Intent

## Purpose

Frame measurable business Outcomes, ownership, horizon, constraints, and evidence gaps, and obtain their approval before any diagnosis starts.

## Required inputs

The Required inputs of `methodology/00-intent.md`: owner-supplied business context, access to stakeholders, available Evidence. No upstream artifact is required.

## Normative sources

- `methodology/00-intent.md` and the modules in its Method

## Produces

- `artifacts/transformation-intent.md` — Transformation Intent (`ATI-###`) with Outcome records (`OUT-###`), constraints, non-goals
- `artifacts/decision-assumption-log.md` — profile Decision, `HG-OUTCOME` Decision, Assumptions
- `artifacts/transformation-scorecard.md` — baseline Metric records (`MET-###`, `METRICS.md` §6) in `metrics`, where a baseline is measured

Evidence and Evidence Debt, including unmeasured baselines, are appended as any skill may (`skills/INDEX.md` §4).

## Specialist skills

- `skills/36-select-application-profile/SKILL.md` — when no profile Decision exists; the selection stays provisional until `HG-OUTCOME`
- `skills/37-build-context-bundle/SKILL.md` — to bound the context for this phase and for the next orchestrator

## Procedure

1. Load `methodology/00-intent.md`. If no profile Decision exists, select a provisional profile with skill 36 and record it as a DEC; `HG-OUTCOME` confirms it. Then run skill 37.
2. Verify the phase's Required inputs. Without an accountable owner or a meaningful business Outcome, stop with `BLOCKED` (phase Prohibited shortcut).
3. Execute the phase Activities in order.
4. Keep stable IDs and the `TRACEABILITY.md` §4 trace.
5. Validate the phase Exit condition (`EXECUTION_MODEL.md` §2) and the Validation of each produced contract.
6. Stop with `INSUFFICIENT_EVIDENCE` when meeting the exit would require invented business facts; record Evidence Debt.
7. Submit the Outcomes and the profile Decision for approval.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-OUTCOME`; the approval is recorded as a DEC with `gate:` set, listing the `OUT-###` IDs and the profile Decision in `subject_ids`. No later phase may use unapproved Outcomes. Any other `STANDARD.md` §8 gate applies whenever its trigger occurs.

## MUST NOT

- accept a means (adopt AI, deploy agents, automate, use a vendor) as an Outcome;
- invent baselines, owners, or targets;
- create a second definition of any concept owned by a specialist skill or normative module;
- record an approval the named human did not give.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
