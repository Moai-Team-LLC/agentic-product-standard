---
name: 21-design-transition-states
description: "Designs independently operable Transition States (State records of type TRANSITION) between the CURRENT and TARGET States: sequence, mode (cutover, shadow, parallel), owner, changes by dimension, evidence to collect, entry and exit conditions, rollback or recovery, and explicitly sequenced authority steps within the Authority Ceiling. Use in Phase 6 when the profile requires Transition States (Standard and above) or when changes cannot safely happen at once. Produces STA records per artifacts/transition-state.md. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: design-specialist
  phase: "6"
  human_gate: "false"
---

# Skill 21: Design Transition States

## Purpose

Break the move from the Current State to the Capability Target States into bounded states the business can operate, observe, and recover in. Invoked by [`skills/07-build-roadmap/SKILL.md`](../07-build-roadmap/SKILL.md).

## Required inputs

- CURRENT States ([`artifacts/capability-map.md`](../../artifacts/capability-map.md)) and approved Capability Target States ([`artifacts/capability-target-state.md`](../../artifacts/capability-target-state.md));
- approved Target Operating Architecture, where the profile requires one;
- selected Initiatives ([`artifacts/transformation-roadmap.md`](../../artifacts/transformation-roadmap.md)) and their System Effect Assessments;
- material Uncertainties ([`artifacts/evidence-register.md`](../../artifacts/evidence-register.md));
- Autonomy Assessments with approved Authority Ceilings, where AI authority changes.

## Normative sources

- [`transition/TRANSITION_STATE_MODEL.md`](../../transition/TRANSITION_STATE_MODEL.md)
- [`transition/TRANSFORMATION_SEQUENCING.md`](../../transition/TRANSFORMATION_SEQUENCING.md)
- [`evidence/UNCERTAINTY_MODEL.md`](../../evidence/UNCERTAINTY_MODEL.md)

## Produces

- [`artifacts/transition-state.md`](../../artifacts/transition-state.md) — STA records (`type: TRANSITION`), created or updated.

## Procedure

1. Identify changes that cannot safely occur together (dependency types: [`transition/TRANSFORMATION_SEQUENCING.md`](../../transition/TRANSFORMATION_SEQUENCING.md) §4) and order them with its default sequencing logic (§3).
2. For each material Uncertainty, apply its resolution method ([`evidence/UNCERTAINTY_MODEL.md`](../../evidence/UNCERTAINTY_MODEL.md) §3); use a SHADOW or PARALLEL mode where uncertainty warrants it ([`transition/TRANSITION_STATE_MODEL.md`](../../transition/TRANSITION_STATE_MODEL.md) §5, §6), with a `time_bound` for PARALLEL.
3. Define each state: `name`, the Capabilities changed (`capability_ids`), predecessor and successor, `owner`, changes by dimension, evidence to collect, entry and exit conditions, rollback or recovery.
4. Sequence authority increases per [`transition/TRANSITION_STATE_MODEL.md`](../../transition/TRANSITION_STATE_MODEL.md) §7: each in `ai_changes` with its AUT-### and levels, within the approved Authority Ceiling, behind a `{gate: HG-AUTHORITY, subject_ids: [AUT-###]}` entry in the Initiative's `decision_gates` that closes when the increase is due (skill 34).
5. Check every state is independently operable ([`transition/TRANSITION_STATE_MODEL.md`](../../transition/TRANSITION_STATE_MODEL.md) §2) and none is invalid under its §8.
6. Validate against the Validation of [`artifacts/transition-state.md`](../../artifacts/transition-state.md); review aid: [`rubrics/SYSTEM_DESIGN_RUBRIC.md`](../../rubrics/SYSTEM_DESIGN_RUBRIC.md) (Transition).
7. Stop with `INSUFFICIENT_EVIDENCE` when a state would rest on invented business facts (record Evidence Debt), `BLOCKED` when a required input is missing, or `HUMAN_DECISION_REQUIRED` when a [`STANDARD.md`](../../STANDARD.md) §8 gate trigger occurs or a required upstream gate is still open (gate in `open_gates`).

## MUST NOT

- design a state the business cannot operate in or whose ownership is ambiguous;
- increase AI authority implicitly or above the Authority Ceiling;
- plan big-bang migration, scale before proof, or autonomy before observability;
- invent business facts; renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
