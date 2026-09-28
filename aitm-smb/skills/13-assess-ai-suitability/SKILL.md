---
name: 13-assess-ai-suitability
description: "Assesses whether probabilistic AI creates more value than process redesign, deterministic software or automation for one AI-type candidate Intervention: checks that simpler and non-AI alternatives were considered, rates every AI suitability dimension, and classifies AI fit A to E with its selection consequence. Use in Phase 3 (intervention design), invoked by skill 04 for each AI_* candidate. Produces an AI Suitability Assessment; it never sets authority. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: diagnostic-specialist
phase: "3"
human_gate: false
---

# Skill 13: Assess AI Suitability

## Purpose

Decide whether an `AI_*` candidate is justified against its simpler and non-AI alternatives. AI fit is not authority (INV-06). Invoked by [`skills/04-design-interventions/SKILL.md`](../04-design-interventions/SKILL.md).

## Required inputs

- one candidate Intervention whose `type` is `AI_*` (Intervention Map);
- its intervention-ready Gaps and cause Hypotheses;
- the other candidates for the same Gaps.

## Normative sources

- [`diagnostics/AI_SUITABILITY.md`](../../diagnostics/AI_SUITABILITY.md)
- [`DECISION_MODEL.md`](../../DECISION_MODEL.md) §1 (intervention challenge)

## Produces

- [`artifacts/ai-suitability-assessment.md`](../../artifacts/ai-suitability-assessment.md) — one AI Suitability Assessment (`AIS-###`) per `AI_*` candidate

## Procedure

1. Apply the intervention challenge ([`DECISION_MODEL.md`](../../DECISION_MODEL.md) §1) to the Gap; record the simpler candidates in `simpler_alternatives_considered` and the best non-AI option, with why it is or is not enough, in `non_ai_alternative`.
2. Rate every dimension in [`diagnostics/AI_SUITABILITY.md`](../../diagnostics/AI_SUITABILITY.md) §2 (one field each in [`artifacts/ai-suitability-assessment.md`](../../artifacts/ai-suitability-assessment.md)), or mark it `not_relevant` with the reason in its note.
3. Weigh the positive and negative signals (§3–§4) and classify fit A–E (§5) in `classification`, with `rationale`.
4. Apply the class consequence (§5): C and D need a recorded justification; for E, recommend rejecting the candidate.
5. Link the `AIS-###` to the Intervention and its Gaps, with `evidence_ids` and `assumption_ids`; validate against the contract's Validation.
6. Stop with `INSUFFICIENT_EVIDENCE` when a rating would require invented business facts (record Evidence Debt); with `HUMAN_DECISION_REQUIRED` when any [`STANDARD.md`](../../STANDARD.md) §8 gate is reached.

## MUST NOT

- recommend AI before simpler intervention families are considered;
- justify AI for a reason listed in [`diagnostics/AI_SUITABILITY.md`](../../diagnostics/AI_SUITABILITY.md) §7;
- treat a class as a selection or as authority;
- invent business facts, present inference as Evidence, or hide uncertainty;
- widen scope silently, or renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
