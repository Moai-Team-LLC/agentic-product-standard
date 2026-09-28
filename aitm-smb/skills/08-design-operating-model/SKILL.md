---
name: 08-design-operating-model
description: "Phase 7 orchestrator. Makes the transformed system operable and governed and moves it from pilot to rollout: ownership, observability (skill 28), adoption and role transitions (skill 30), AI governance (skill 31), pilot evaluation (skill 32), rollout planning after promotion (skill 29), new evaluations (skill 26) and readiness checks (skill 35) before each rollout stage, and authority grants and changes (skill 34); stops at Decision Rights, AI authority, risk and pilot-promotion gates. Use once the roadmap is approved and while pilots and rollouts run. Produces the Operating Model, Observability, Adoption and Rollout Plans, the AI Governance Canvas, pilot results and Execution Gate records. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "7"
human_gate: true
gates: [HG-DECISION-RIGHTS, HG-AUTHORITY, HG-RISK, HG-PROMOTION]
---

# Skill 08: Orchestrate Operating Model & Governance

## Purpose

Make the transformed system ownable, observable, governable, supportable, and adoptable; evaluate pilots, and expand scope only through a promotion decision, verified rollout gates, and approved AI authority.

## Required inputs

The Required inputs of [`methodology/07-operating-model-governance.md`](../../methodology/07-operating-model-governance.md) (approved target and Transformation Roadmap, Authority Ceilings where AI is used, Pilot Plans with pre-registered Evaluation Plans where piloting).

## Normative sources

- [`methodology/07-operating-model-governance.md`](../../methodology/07-operating-model-governance.md) and the modules in its Method

## Produces

Only what the active profile requires ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md)).

- [`artifacts/transformation-roadmap.md`](../../artifacts/transformation-roadmap.md) — Compact: the Initiative `operation` extension (the Phase 7 minimum, `adoption` included), which MAY stand in for the Operating Model, Observability Plan, and Adoption Plan ([`methodology/07-operating-model-governance.md`](../../methodology/07-operating-model-governance.md))
- [`artifacts/operating-model.md`](../../artifacts/operating-model.md)
- [`artifacts/observability-plan.md`](../../artifacts/observability-plan.md) (skill 28)
- [`artifacts/adoption-plan.md`](../../artifacts/adoption-plan.md) — with `role_transitions` (skill 30)
- [`artifacts/ai-governance-canvas.md`](../../artifacts/ai-governance-canvas.md) — where AI is used (skills 31, 34)
- [`artifacts/evaluation-plan.md`](../../artifacts/evaluation-plan.md) — pilot `results` and `pilot_result` (skill 32); new pre-registered EVL plans for rollout stages (skill 26)
- [`artifacts/rollout-plan.md`](../../artifacts/rollout-plan.md) — where rolling out (skill 29)
- [`artifacts/autonomy-assessment.md`](../../artifacts/autonomy-assessment.md) — updates after promotion or demotion (skill 34)
- [`artifacts/execution-gate.md`](../../artifacts/execution-gate.md) — Gates D (skill 32), E (skill 35), F (this skill); Governed
- [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md) — gate Decisions, Risk records (`RSK-###`), Assumptions

## Specialist skills

- [`skills/28-design-observability/SKILL.md`](../28-design-observability/SKILL.md) — before any AI or automated work runs; an Observability Plan where the profile requires it
- [`skills/30-design-adoption/SKILL.md`](../30-design-adoption/SKILL.md) — role changes and adoption; an Adoption Plan where the profile requires it
- [`skills/31-operationalize-governance/SKILL.md`](../31-operationalize-governance/SKILL.md) — where AI is used
- [`skills/32-evaluate-pilot/SKILL.md`](../32-evaluate-pilot/SKILL.md) — after each pilot runs
- [`skills/29-plan-rollout/SKILL.md`](../29-plan-rollout/SKILL.md) — only after `HG-PROMOTION` is approved for the pilot
- [`skills/26-design-evaluation/SKILL.md`](../26-design-evaluation/SKILL.md) — before a rollout stage whose scope the pilot's evaluations do not cover: pre-registers new EVL plans
- [`skills/35-audit-operational-readiness/SKILL.md`](../35-audit-operational-readiness/SKILL.md) — before each rollout stage
- [`skills/34-manage-authority-promotion/SKILL.md`](../34-manage-authority-promotion/SKILL.md) — whenever AI authority is to change, including before a pilot or rollout stage runs above the currently approved level (AUT `current_level`)

## Procedure

1. Load the active profiles ([`AGENT_CONTEXT_POLICY.md`](../../AGENT_CONTEXT_POLICY.md)) and [`methodology/07-operating-model-governance.md`](../../methodology/07-operating-model-governance.md).
2. Verify the phase's Required inputs; while an upstream gate they depend on (`HG-TOA` or `HG-BUDGET`) is open, stop with `HUMAN_DECISION_REQUIRED` (gate in `open_gates`); stop with `BLOCKED` only when an input is missing.
3. Make the system operable: assign ownership and invoke 28, 30, and 31 (phase Activities 1–8). In Compact, the result MAY be recorded as the Initiative `operation`, `adoption` included ([`artifacts/transformation-roadmap.md`](../../artifacts/transformation-roadmap.md)).
4. For each pilot: before it starts, grant any level above the currently approved one through 34 ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../../governance/AUTHORITY_ESCALATION_MODEL.md) §3 (a)); after it runs, evaluate it with 32; for a material pilot stop at `HG-PROMOTION`.
5. After promotion: plan the rollout with 29; before each stage, pre-register new evaluations with 26 where its scope is not covered, raise a level only through 34, and verify readiness with 35.
6. Change AI authority only through 34 (an increase needs `HG-AUTHORITY`; demotion needs no gate); incidents go to [`skills/40-handle-incident/SKILL.md`](../40-handle-incident/SKILL.md).
7. Governed: when the target scope runs under the approved operating model, update Gate F `evidence_provided` and propose its status to the approver ([`artifacts/execution-gate.md`](../../artifacts/execution-gate.md)).
8. Merge specialist outputs into the phase instances; keep stable IDs and the [`TRACEABILITY.md`](../../TRACEABILITY.md) §4 trace.
9. Validate the phase Exit condition ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §2) and the Validation of each produced contract.
10. Stop with `INSUFFICIENT_EVIDENCE` when a promotion or readiness claim would rest on invented facts; record Evidence Debt.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-PROMOTION` (material pilot to rollout), `HG-AUTHORITY` (any level above the approved one, AUT `current_level`, and any restoration after a demotion), `HG-RISK` (accepting a material Risk `RSK-###`, e.g. for a pilot or rollout stage), and `HG-DECISION-RIGHTS` (material Decision Rights changed through role transitions); record each gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing the gated IDs in `subject_ids`; the named human's approval updates it to `approved`. Any other [`STANDARD.md`](../../STANDARD.md) §8 gate applies whenever its trigger occurs.

## MUST NOT

- widen scope or raise AI authority because a pilot or demo looks promising;
- rewrite success criteria after results are known;
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
