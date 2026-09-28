---
name: 05-prioritize-initiatives
description: "Phase 4 orchestrator. Decides which candidate Interventions to select, defer, reject or investigate, with written trade-offs, economic hypotheses, System Constraint relevance and, under the Portfolio profile, portfolio criteria; creates an Initiative record for each candidate proposed for selection, records its system effects (skill 19) before the selection is decided, and stops for Initiative and budget approval (HG-INITIATIVE, HG-BUDGET). Use after intervention design, before target-system design. Produces Initiative records with their economic hypotheses in the Transformation Roadmap, draft System Effect Assessments, the Prioritization Matrix, Intervention status updates, Execution Gate A (Governed) and selection Decisions. Part of AITM-SMB; paths are relative to the AITM-SMB root."
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

The Required inputs of [`methodology/04-prioritization.md`](../../methodology/04-prioritization.md) (candidate Interventions ready for prioritization, their AI Suitability and Autonomy Assessments, approved Outcomes and Metrics, economic assumptions, System Constraint and Transformation Portfolio where they exist).

## Normative sources

- [`methodology/04-prioritization.md`](../../methodology/04-prioritization.md) and the modules in its Method, in particular:
  - [`artifacts/prioritization-matrix.md`](../../artifacts/prioritization-matrix.md) — assessment dimensions
  - [`economics/TRANSFORMATION_ECONOMICS.md`](../../economics/TRANSFORMATION_ECONOMICS.md) §5 — economic hypothesis, held on each material Initiative before `HG-BUDGET`
  - [`design/LOCAL_OPTIMIZATION_GUARD.md`](../../design/LOCAL_OPTIMIZATION_GUARD.md) §2, §4–§5 — system-effect check before the selection is decided
  - [`design/CONSTRAINT_ANALYSIS.md`](../../design/CONSTRAINT_ANALYSIS.md) §6 — when a System Constraint exists
  - [`portfolio/PORTFOLIO_PRIORITIZATION.md`](../../portfolio/PORTFOLIO_PRIORITIZATION.md) — Portfolio profile: criteria (§2) and stop condition (§5)

## Produces

- [`artifacts/transformation-roadmap.md`](../../artifacts/transformation-roadmap.md) — Initiative records (`INI-###`, `status: proposed`, [`CORE_MODEL.md`](../../CORE_MODEL.md) §7) for each candidate proposed for selection; each material one with its `economic_hypothesis`
- [`artifacts/system-effect-assessment.md`](../../artifacts/system-effect-assessment.md) — a draft System Effect Assessment (`SFX-###`) per Initiative, before its selection is decided (skill 19)
- [`artifacts/prioritization-matrix.md`](../../artifacts/prioritization-matrix.md) — where the profile requires it (Standard, Portfolio)
- [`artifacts/intervention-map.md`](../../artifacts/intervention-map.md) — `status` and `status_rationale` of each candidate only
- [`artifacts/execution-gate.md`](../../artifacts/execution-gate.md) — Gate A per Initiative; Governed
- [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md) — selection and budget Decisions, provisional-selection review triggers, Assumptions

## Specialist skills

- [`skills/19-assess-system-effects/SKILL.md`](../19-assess-system-effects/SKILL.md) — every candidate proposed for selection, once its `INI-###` exists and before `HG-INITIATIVE`: at least a draft SFX ([`design/LOCAL_OPTIMIZATION_GUARD.md`](../../design/LOCAL_OPTIMIZATION_GUARD.md) §4)

Otherwise the modules in Normative sources apply directly.

## Procedure

1. Load the active profiles ([`AGENT_CONTEXT_POLICY.md`](../../AGENT_CONTEXT_POLICY.md)) and [`methodology/04-prioritization.md`](../../methodology/04-prioritization.md).
2. Verify the phase's Required inputs; stop with `BLOCKED` when no candidate is ready for prioritization.
3. Execute the phase Activities in order; where the profile requires a System Constraint and none is identified yet, record the selection as provisional with a `review_trigger`. `investigate` keeps the Interventions at `status: candidate` and records an Evidence Debt item naming what must be learned.
4. Portfolio profile: select no Initiative while a [`portfolio/PORTFOLIO_PRIORITIZATION.md`](../../portfolio/PORTFOLIO_PRIORITIZATION.md) §5 stop condition holds, unless an approved Decision of the portfolio owner records the override and its reason.
5. Create an `INI-###` (`status: proposed`) for each candidate proposed for selection; keep stable IDs and the [`TRACEABILITY.md`](../../TRACEABILITY.md) §4 trace.
6. For each material Initiative, once its record exists, record its economic hypothesis on it (`economic_hypothesis`, [`economics/TRANSFORMATION_ECONOMICS.md`](../../economics/TRANSFORMATION_ECONOMICS.md) §5) before `HG-BUDGET`.
7. For each Initiative proposed for selection, invoke skill 19 to record at least a draft System Effect Assessment before `HG-INITIATIVE`.
8. Governed: record Execution Gate A per Initiative, with evidence that its Gaps meet the Phase 2 readiness condition.
9. Validate the phase Exit condition ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §2) and the Validation of each produced contract.
10. Stop with `INSUFFICIENT_EVIDENCE` when a decision would rest on invented economics or facts; record Evidence Debt.
11. Submit material selections, with their System Effect Assessments, and material budget for approval.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-INITIATIVE` (material selections) and `HG-BUDGET` (material budget); record each gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing the `INI-###` in `subject_ids`; the named human decides `HG-INITIATIVE` with each System Effect Assessment in hand, and the approval updates the DEC to `approved`. Only then set Initiative `status: approved` and Intervention `status: selected` (an `AI_*` Intervention only once its Authority Ceiling is approved). The `HG-BUDGET` Decision cites each material Initiative's `economic_hypothesis` as [`economics/TRANSFORMATION_ECONOMICS.md`](../../economics/TRANSFORMATION_ECONOMICS.md) §5 specifies. Any other [`STANDARD.md`](../../STANDARD.md) §8 gate applies whenever its trigger occurs.

## MUST NOT

- let a numeric score replace written judgment;
- select an Initiative only because it is easy, visible, or uses AI;
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
