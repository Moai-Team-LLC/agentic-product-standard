---
name: 05-prioritize-initiatives
description: "Phase 4 orchestrator. Decides which candidate Interventions to select, defer, reject or investigate, with written trade-offs, economic hypotheses, System Constraint relevance and, under the Portfolio profile, portfolio criteria; creates an Initiative record for each selection and stops for Initiative and budget approval (HG-INITIATIVE, HG-BUDGET). Use after intervention design, before target-system design. Produces Initiative records in the Transformation Roadmap, the Prioritization Matrix, Intervention status updates and selection Decisions. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "4"
human_gate: true
gates: [HG-INITIATIVE, HG-BUDGET]
---

# Skill 05: Orchestrate Prioritization

## Purpose

Select, defer, reject, or investigate intervention candidates using explicit trade-offs and human approval, and record each selection as an Initiative.

## Required inputs

The Required inputs of `methodology/04-prioritization.md` (candidate Interventions ready for prioritization, their AI Suitability and Autonomy Assessments, approved Outcomes and Metrics, economic assumptions, System Constraint and Transformation Portfolio where they exist).

## Normative sources

- `methodology/04-prioritization.md` and the modules in its Method, in particular:
  - `artifacts/prioritization-matrix.md` — assessment dimensions
  - `economics/TRANSFORMATION_ECONOMICS.md` §5 — economic hypothesis, required for each material candidate before `HG-BUDGET`
  - `design/CONSTRAINT_ANALYSIS.md` §6 — when a System Constraint exists
  - `portfolio/PORTFOLIO_PRIORITIZATION.md` — Portfolio profile: criteria (§2) and stop condition (§5)

## Produces

- `artifacts/transformation-roadmap.md` — Initiative records (`INI-###`, `status: proposed`) created at selection (`CORE_MODEL.md` §7)
- `artifacts/prioritization-matrix.md` — where the profile requires it (Standard, Portfolio)
- `artifacts/intervention-map.md` — `status` and `status_rationale` of each candidate only
- `artifacts/decision-assumption-log.md` — selection and budget Decisions, provisional-selection review triggers, Assumptions

## Specialist skills

None. The modules in Normative sources apply directly.

## Procedure

1. Load the active profiles (`AGENT_CONTEXT_POLICY.md`) and `methodology/04-prioritization.md`.
2. Verify the phase's Required inputs; stop with `BLOCKED` when no candidate is ready for prioritization.
3. Execute the phase Activities in order; where the profile requires a System Constraint and none is identified yet, record the selection as provisional with a `review_trigger`.
4. Before `HG-BUDGET`, prepare an economic hypothesis (`economics/TRANSFORMATION_ECONOMICS.md` §5) for each material candidate.
5. Portfolio profile: select no Initiative while a `portfolio/PORTFOLIO_PRIORITIZATION.md` §5 stop condition holds, unless a DEC records the override.
6. Create an `INI-###` (`status: proposed`) for each selected candidate; keep stable IDs and the `TRACEABILITY.md` §4 trace.
7. Validate the phase Exit condition (`EXECUTION_MODEL.md` §2) and the Validation of each produced contract.
8. Stop with `INSUFFICIENT_EVIDENCE` when a decision would rest on invented economics or facts; record Evidence Debt.
9. Submit material selections and material budget for approval.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-INITIATIVE` (material selections) and `HG-BUDGET` (material budget); the approval is recorded as a DEC with `gate:` set, listing the `INI-###` in `subject_ids`. Only then set Initiative `status: approved` and Intervention `status: selected`. The `HG-BUDGET` Decision cites each material candidate's economic hypothesis as `economics/TRANSFORMATION_ECONOMICS.md` §5 specifies. Any other `STANDARD.md` §8 gate applies whenever its trigger occurs.

## MUST NOT

- let a numeric score replace written judgment;
- select an Initiative only because it is easy, visible, or uses AI;
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
