---
name: 23-design-decision-rights
description: "Designs the Decision Rights Map: for each material operational business decision, the accountable human decision owner and the current and target authority models, decomposed where authority differs between parts, with the information, knowledge, policy and escalation it needs, and AI authority that does not exceed the approved Authority Ceiling. Use in Phase 5 when a design changes who or what decides. Produces BDS records per artifacts/decision-rights-map.md and stops for decision-rights approval. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: design-specialist
phase: "5"
human_gate: true
gates: [HG-DECISION-RIGHTS]
---

# Skill 23: Design Decision Rights

## Purpose

Make explicit who, or what, may make each material business decision today and in the target state. Invoked by [`skills/06-design-target-system/SKILL.md`](../06-design-target-system/SKILL.md).

## Required inputs

- Capability Target States ([`artifacts/capability-target-state.md`](../../artifacts/capability-target-state.md)) and, where one is being designed, the Target Operating Architecture;
- Autonomy Assessments with approved Authority Ceilings ([`artifacts/autonomy-assessment.md`](../../artifacts/autonomy-assessment.md)), where AI takes part;
- the current authority model (who decides today), with Evidence.

## Normative sources

- [`design/DECISION_RIGHTS_ARCHITECTURE.md`](../../design/DECISION_RIGHTS_ARCHITECTURE.md)
- [`diagnostics/AUTONOMY_SUITABILITY.md`](../../diagnostics/AUTONOMY_SUITABILITY.md) (§2 levels, §6 Authority Ceiling)

## Produces

- [`artifacts/decision-rights-map.md`](../../artifacts/decision-rights-map.md) — BDS records (`business_decision`), created or updated.

## Procedure

1. Identify the material business decisions of the Capabilities in scope (materiality: [`STANDARD.md`](../../STANDARD.md) §16).
2. Decompose compound decisions where authority differs between parts ([`design/DECISION_RIGHTS_ARCHITECTURE.md`](../../design/DECISION_RIGHTS_ARCHITECTURE.md) §4); link parts with `part_of`.
3. Record `current_authority` as an authority model (§3), with Evidence.
4. Define `target_authority` as an authority model and name the human `decision_owner`, also at L4 and L5 (§3).
5. Attach information, knowledge, policy, and escalation requirements.
6. Where AI takes part, set `autonomy_assessment_id` and verify the level of `target_authority` does not exceed that assessment's `maximum_allowed_level`; if it would, keep the approved level and return the item to [`skills/14-assess-autonomy/SKILL.md`](../14-assess-autonomy/SKILL.md) to re-assess the ceiling.
7. Validate against the Validation of [`artifacts/decision-rights-map.md`](../../artifacts/decision-rights-map.md).
8. Stop with `INSUFFICIENT_EVIDENCE` when current authority cannot be established without invented facts (record Evidence Debt), `HUMAN_DECISION_REQUIRED` while a required upstream gate is still open (gate in `open_gates`), or `BLOCKED` when a required input is missing.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-DECISION-RIGHTS` for each material change from `current_authority` to `target_authority`; record the gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing the BDS-### in `subject_ids`; the named human's approval updates it to `approved`. A target authority above the currently approved AI level (AUT `current_level`) takes effect only when the increase is due, through [`skills/34-manage-authority-promotion/SKILL.md`](../34-manage-authority-promotion/SKILL.md) and `HG-AUTHORITY`. Lowering AI authority needs no gate.

## MUST NOT

- automate the label of a decision instead of its actual authority structure ([`design/DECISION_RIGHTS_ARCHITECTURE.md`](../../design/DECISION_RIGHTS_ARCHITECTURE.md) §5);
- leave a decision without a human decision owner;
- set a target authority above the approved Authority Ceiling;
- record an approval the named human has not explicitly given; renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
