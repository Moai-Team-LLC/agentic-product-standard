---
name: 34-manage-authority-promotion
description: "Reviews AI authority for one action class of a Capability from evidence and recommends promote, retain, or demote: reads the current level and Authority Ceiling from the Autonomy Assessment, checks the demotion triggers and promotion criteria of the Authority Escalation Model against evaluation results, incident history and operating signals, never proposes a level above the ceiling, follows the promotion path, and proposes a High-class AI Change. Use in Phase 7 or 8 before a pilot or rollout stage runs above the approved level, when operation would use more authority, when restoring authority after a demotion, or when evidence suggests reducing it; it performs every grant. Demotion takes effect at once; promotion stops for HG-AUTHORITY. Updates artifacts/autonomy-assessment.md and the changes in artifacts/ai-governance-canvas.md. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: execution-governance
  phase: "7-8"
  human_gate: "true"
  gates: "HG-AUTHORITY"
---

# Skill 34: Manage AI Authority Promotion

## Purpose

Change AI authority only on evidence: promote through an approved human decision, demote as soon as evidence requires (INV-07). Invoked by [`skills/08-design-operating-model/SKILL.md`](../08-design-operating-model/SKILL.md) (before a pilot starts and before each rollout stage that raises a level) and [`skills/09-measure-evolution/SKILL.md`](../09-measure-evolution/SKILL.md), and after a demotion by [`skills/40-handle-incident/SKILL.md`](../40-handle-incident/SKILL.md). It performs every authority grant; widening scope at the approved level is rollout, not a grant.

## Required inputs

- Autonomy Assessment (AUT) with `current_level` and approved Authority Ceiling ([`artifacts/autonomy-assessment.md`](../../artifacts/autonomy-assessment.md));
- Evaluation results (EVL, [`artifacts/evaluation-plan.md`](../../artifacts/evaluation-plan.md)), or, for a pilot grant, the Pilot Plan (PLT) and its pre-registered evaluation;
- Incident history (INC-### records, [`artifacts/incident-record.md`](../../artifacts/incident-record.md));
- AI Governance Canvas and Observability Plan (controls and operating signals).

## Normative sources

- [`governance/AUTHORITY_ESCALATION_MODEL.md`](../../governance/AUTHORITY_ESCALATION_MODEL.md)
- [`diagnostics/AUTONOMY_SUITABILITY.md`](../../diagnostics/AUTONOMY_SUITABILITY.md) (§2 levels, §6 Authority Ceiling)
- [`governance/AI_CHANGE_CONTROL.md`](../../governance/AI_CHANGE_CONTROL.md)

## Produces

- [`artifacts/autonomy-assessment.md`](../../artifacts/autonomy-assessment.md) — `promotion_recommendation`, `rationale`, `evidence_ids`; `current_level` changes only on demotion or after an approved promotion;
- [`artifacts/ai-governance-canvas.md`](../../artifacts/ai-governance-canvas.md) — an AI Change (CHG-###) in `changes`, where AI Change Control applies.

## Procedure

1. Read `current_level` and the Authority Ceiling (`maximum_allowed_level` and its boundaries) from the Autonomy Assessment.
2. Check every demotion trigger ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../../governance/AUTHORITY_ESCALATION_MODEL.md) §4) against incidents, evaluations, and operating signals. If one fires, recommend demote: no gate; the operating owner may reduce authority at once, down to L0. Record the new `current_level` and the reason in `rationale`, and the demotion Decision afterwards in [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md) ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../../governance/AUTHORITY_ESCALATION_MODEL.md) §6).
3. For a proposed increase, compare the target level with `maximum_allowed_level`; if it would exceed the ceiling, stop the promotion and return it to [`skills/14-assess-autonomy/SKILL.md`](../14-assess-autonomy/SKILL.md) to re-assess the ceiling first ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../../governance/AUTHORITY_ESCALATION_MODEL.md) §2).
4. Verify every promotion criterion from Evidence: §3 (a) for a bounded pilot within the ceiling (from the Pilot Plan and its pre-registered evaluation); §3 (b) for any other increase, including restoring authority (EVL results, incident rate from INC-### records, operating signals). Any unmet criterion means retain.
5. Follow the promotion path (§2); authority SHOULD NOT jump directly to the maximum technically possible level ([`transition/TRANSITION_STATE_MODEL.md`](../../transition/TRANSITION_STATE_MODEL.md) §7).
6. Record `promotion_recommendation` and `rationale` with Evidence. Once the `HG-AUTHORITY` Decision is approved, set `current_level` to the level it states and note the scope in `rationale`.
7. Where AI Change Control applies, record the authority change as an AI Change (CHG-###, [`governance/AI_CHANGE_CONTROL.md`](../../governance/AI_CHANGE_CONTROL.md) §3) of class High (§2): proposed before a promotion; recorded after a demotion, which never waits for it.
8. Validate against the Validation of [`artifacts/autonomy-assessment.md`](../../artifacts/autonomy-assessment.md).
9. Stop with `INSUFFICIENT_EVIDENCE` when a criterion cannot be verified from Evidence (recommend retain; record Evidence Debt), `HUMAN_DECISION_REQUIRED` while the Authority Ceiling's `HG-AUTHORITY` is still open (gate in `open_gates`), or `BLOCKED` when a required input is missing.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-AUTHORITY` before any promotion, including a pilot's or rollout stage's grant and restoring authority after a demotion; record the gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4) that lists the AUT-### in `subject_ids` (the PLT-### or ROL-### as context) and states the new level and scope in `statement`; the named human's approval updates it to `approved`. Until then the level in operation does not change. An L0 ceiling grants nothing and needs no gate.

## MUST NOT

- propose or apply a level above the approved Authority Ceiling;
- raise `current_level` before the `HG-AUTHORITY` Decision is approved;
- delay a demotion to wait for a gate or a Decision;
- grant authority from technical capability or AI quality alone, or record an approval the named human has not explicitly given.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
