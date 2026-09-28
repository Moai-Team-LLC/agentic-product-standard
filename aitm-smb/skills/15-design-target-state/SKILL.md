---
name: 15-design-target-state
description: "Designs the Capability Target State of one selected Capability: its target capability statement, people and decision rights, process, data and knowledge, application and automation boundaries, AI only where a selected Intervention justifies it and within the approved Authority Ceiling, controls, metrics, and the Gaps it closes. Use in Phase 5, invoked by skill 06 for each selected Capability, in every profile. Produces a Capability Target State (a State of type TARGET). Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: design-specialist
phase: "5"
human_gate: false
---

# Skill 15: Design Capability Target State

## Purpose

Define how one transformed Capability should behave, capability-scoped and separate from the system-level Target Operating Architecture (`STANDARD.md` §7). Invoked by `skills/06-design-target-system/SKILL.md`.

## Required inputs

- selected Initiatives and their Interventions for the Capability;
- the Capability with its CURRENT State, and its Gaps (Capability Map, Capability Diagnosis);
- approved Authority Ceilings for selected `AI_*` Interventions;
- design constraints (Transformation Intent).

## Normative sources

- `design/TARGET_STATE_DESIGN.md`
- `CORE_MODEL.md` §3 (State)
- `diagnostics/AUTONOMY_SUITABILITY.md` §6 (Authority Ceiling)

## Produces

- `artifacts/capability-target-state.md` — one State (`STA-###`, `type: TARGET`) per selected Capability

## Procedure

1. Create the State with `as_of` set to the intended horizon; set the Capability's `target_state_id` to it.
2. Write the target capability statement in `statement` (`design/TARGET_STATE_DESIGN.md` §2).
3. Design the dimensions (§3) in the design order of §1, applying the design rule (§5); add AI only where a selected Intervention justifies it.
4. Link `outcome_ids`, the Gaps it closes (`gap_ids`), `metric_ids`, and `constraints`; make ownership and system boundaries explicit.
5. Where AI is present, add one `ai_authority` entry per action class, with its `autonomy_assessment_id` and a `target_level` within that assessment's approved Authority Ceiling; a level above it needs a re-assessed ceiling first (skill 14, `HG-AUTHORITY`).
6. Check completeness (`design/TARGET_STATE_DESIGN.md` §6); every element addresses a diagnosed Gap. Validate against the contract's Validation.
7. Stop with `BLOCKED` when a selected `AI_*` Intervention has no approved ceiling; with `INSUFFICIENT_EVIDENCE` when the design would require invented business facts; with `HUMAN_DECISION_REQUIRED` when any `STANDARD.md` §8 gate is reached.

## MUST NOT

- use this State as a substitute for the Target Operating Architecture;
- design from vendor capabilities before target behavior (INV-08);
- set a target level above the approved Authority Ceiling;
- invent business facts, present inference as Evidence, or hide uncertainty;
- widen scope silently, or renumber or reuse stable IDs;
- recommend AI before simpler intervention families are considered.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
