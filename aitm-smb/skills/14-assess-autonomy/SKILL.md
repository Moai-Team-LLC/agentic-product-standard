---
name: 14-assess-autonomy
description: "Assesses how much authority AI may hold for each action class of an AI-type Intervention, separately from AI fit: rates the autonomy dimensions, recommends an autonomy level on the L0-L5 authority ladder, and proposes the Authority Ceiling with prohibited actions, approval requirements, escalation conditions and an accountable owner; stops for authority approval (HG-AUTHORITY). Use in Phase 3, invoked by skill 04 for each AI_* candidate proposed for selection, or when a ceiling must be re-assessed. Produces Autonomy Assessments. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: diagnostic-specialist
phase: "3"
human_gate: true
gates: [HG-AUTHORITY]
---

# Skill 14: Assess Agentic Autonomy

## Purpose

Separate AI usefulness from AI authority: propose the highest safe authority per action class, for a human to approve. Invoked by [`skills/04-design-interventions/SKILL.md`](../04-design-interventions/SKILL.md).

## Required inputs

- one candidate Intervention whose `type` is `AI_*` and that is proposed for selection, with its AI Suitability Assessment (classes A–C, or D with a recorded justification, [`diagnostics/AI_SUITABILITY.md`](../../diagnostics/AI_SUITABILITY.md) §5; never E);
- its Capability, action classes, and governance context (policies, permissions, risk owner).

## Normative sources

- [`diagnostics/AUTONOMY_SUITABILITY.md`](../../diagnostics/AUTONOMY_SUITABILITY.md) (levels §2; Authority Ceiling §6)
- [`DECISION_MODEL.md`](../../DECISION_MODEL.md) §3 (autonomy challenge)

## Produces

- [`artifacts/autonomy-assessment.md`](../../artifacts/autonomy-assessment.md) — one Autonomy Assessment (`AUT-###`) per `AI_*` Intervention and action class

## Procedure

1. Apply the autonomy challenge ([`DECISION_MODEL.md`](../../DECISION_MODEL.md) §3); name the action classes of the Intervention. Record one `AUT-###` per action class with `capability_id`, `intervention_id`, and `action_class`.
2. Per action class, rate every dimension in [`diagnostics/AUTONOMY_SUITABILITY.md`](../../diagnostics/AUTONOMY_SUITABILITY.md) §3 against the conditions in §4–§5, or mark it `not_relevant` with the reason in its note.
3. Recommend a level from the §2 ladder (`recommended_level`), with `rationale`.
4. Propose the Authority Ceiling (§6): `maximum_allowed_level`, `prohibited_actions`, `approval_required`, `escalation_conditions`, `owner`. It takes effect only after `HG-AUTHORITY`.
5. Set `current_level: L0` unless an approved Decision already grants a level; validate against the contract's Validation.
6. Stop with `INSUFFICIENT_EVIDENCE` when a rating would require invented business facts; record Evidence Debt.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-AUTHORITY` for each proposed Authority Ceiling above L0 (an L0 ceiling grants nothing and needs no gate); record the gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing the `AUT-###` in `subject_ids` and stating the ceiling's level and scope in `statement`; the named human's approval updates it to `approved`. Raising `current_level` is a grant by skill 34. Lowering a level or ceiling (demotion) needs no gate.

## MUST NOT

- derive authority from AI fit or technical capability (INV-06);
- recommend a level above the proposed ceiling;
- record an approval the named human did not give;
- invent business facts, present inference as Evidence, or hide uncertainty;
- widen scope silently, or renumber or reuse stable IDs;
- recommend AI before simpler intervention families are considered.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
