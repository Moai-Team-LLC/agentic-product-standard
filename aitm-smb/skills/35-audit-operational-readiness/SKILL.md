---
name: 35-audit-operational-readiness
description: "Verifies before each rollout stage that the rollout gates hold: pilot success criteria and promotion, failure modes, active monitoring without dark automation, ownership, support path and incident path, explicit role changes, rollback or recovery, operating governance controls, autonomy level approved and within the Authority Ceiling, eval coverage, and cost envelope. Use in Phase 7 before a rollout stage starts. Records the result on the stage's Execution Gate E per artifacts/execution-gate.md (Governed) and returns blocking gaps as findings. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: execution-governance
phase: "7"
human_gate: false
---

# Skill 35: Audit Operational Readiness

## Purpose

Check with evidence, before scope expands, that the next rollout stage can be operated, observed, supported, governed, and recovered. Invoked by `skills/08-design-operating-model/SKILL.md` before each rollout stage.

## Required inputs

- Rollout Plan (ROL) and the stage to be entered;
- Observability Plan, AI Governance Canvas, Operating Model, and Adoption Plan;
- Evaluation Plan results, Incident records (INC-###, `artifacts/incident-record.md`), and Autonomy Assessment, where AI is used.

## Normative sources

- `execution/ROLLOUT_MODEL.md` (§3 rollout gates)
- `execution/EXECUTION_GATE_MODEL.md` (Gate E)
- `operations/OBSERVABILITY_MODEL.md`
- `operations/INCIDENT_MODEL.md`

## Produces

- `artifacts/execution-gate.md` — the stage's Gate E record (`gate_id` in the Rollout Plan; created here if none exists): `evidence_provided` and a proposed status (Governed);
- `findings`: every unmet gate as a blocking gap, in every profile.

## Procedure

1. Verify each rollout gate of `execution/ROLLOUT_MODEL.md` §3 for the stage, citing Evidence.
2. Verify monitoring is active and no dark-automation pattern remains (`operations/OBSERVABILITY_MODEL.md` §6).
3. Verify the incident path: who records INC-### records (`skills/40-handle-incident/SKILL.md`), who responds, and which alerts open an incident.
4. Verify eval coverage for AI components (Evaluation Plan and datasets) and cost controls within the cost envelope.
5. Verify support and adoption readiness: role changes explicit (`change/ROLE_TRANSITION_MODEL.md` §5), training and support defined.
6. Verify the stage's autonomy level is approved and within the Authority Ceiling.
7. Report each unmet gate as a blocking gap; Governed: update Gate E with the evidence provided and a proposed status. Review aid: `rubrics/EXECUTION_READINESS_RUBRIC.md`.
8. Stop with `INSUFFICIENT_EVIDENCE` when a gate cannot be verified from Evidence, `BLOCKED` when a required input is missing, or `HUMAN_DECISION_REQUIRED` when the stage needs an open `HG-AUTHORITY` or `HG-RISK` Decision.

## MUST NOT

- pass or waive Gate E; its human approver decides;
- present a readiness result as approval of any gated decision;
- accept a gate as verified without Evidence.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
