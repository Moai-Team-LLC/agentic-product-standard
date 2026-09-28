---
name: 19-assess-system-effects
description: "Checks an Initiative for effects beyond its own Capability: upstream support, downstream demand, shared-resource and incentive effects, likely Constraint Migration and who absorbs new exceptions, with a verdict on whether it improves the target Outcome or only a local metric, and mitigations. Use in every profile (in Compact a short record): in Phase 4 for each Initiative proposed for selection, before HG-INITIATIVE (invoked by skill 05), and in Phase 5 to refine it at system level (invoked by skill 06). Produces one System Effect Assessment per Initiative. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: design-specialist
phase: "4-5"
human_gate: false
---

# Skill 19: Assess System Effects

## Purpose

Make INV-09 checkable for each Initiative before its selection is decided: local improvement must not degrade the wider system. Invoked by [`skills/05-prioritize-initiatives/SKILL.md`](../05-prioritize-initiatives/SKILL.md) (Phase 4) and [`skills/06-design-target-system/SKILL.md`](../06-design-target-system/SKILL.md) (Phase 5, system level).

## Required inputs

- an Initiative (`INI-###`) proposed for selection (Phase 4) or a selected one (Phase 5), and its Interventions;
- Capability Network and System Constraint, where they exist (Phase 5, where the profile requires them).

## Normative sources

- [`design/LOCAL_OPTIMIZATION_GUARD.md`](../../design/LOCAL_OPTIMIZATION_GUARD.md)
- [`design/CONSTRAINT_ANALYSIS.md`](../../design/CONSTRAINT_ANALYSIS.md) §5 (Constraint Migration)

## Produces

- [`artifacts/system-effect-assessment.md`](../../artifacts/system-effect-assessment.md) — one System Effect Assessment (`SFX-###`) per Initiative proposed for selection

## Procedure

1. Answer every question in [`design/LOCAL_OPTIMIZATION_GUARD.md`](../../design/LOCAL_OPTIMIZATION_GUARD.md) §2, using the Capability Network and System Constraint where present.
2. Check the common failures (§3) and predict the likely Constraint Migration.
3. Set `system_verdict`; add mitigations or sequencing changes for material negative effects.
4. Record one SFX per Initiative; if one exists for the same `initiative_id`, update it (§4). Phase 4: at least a draft, with an effect that cannot yet be judged marked `unknown` and its Evidence Debt recorded; Phase 5: refine it at system level. In Compact, a short record suffices.
5. When a refined effect (Phase 5) changes a Phase 4 priority (§5), report it in `risks` and `decisions_needed` (`HG-INITIATIVE`).
6. Validate against the [`artifacts/system-effect-assessment.md`](../../artifacts/system-effect-assessment.md) Validation.
7. Stop with `INSUFFICIENT_EVIDENCE` when, at system level (Phase 5), a material effect still cannot be judged without invented facts (record Evidence Debt); with `HUMAN_DECISION_REQUIRED` when any [`STANDARD.md`](../../STANDARD.md) §8 gate is reached.

## MUST NOT

- optimize an isolated metric instead of the target Outcomes;
- hide dependency effects or likely Constraint Migration;
- leave ownership of new exceptions implicit;
- increase AI authority implicitly;
- invent business facts, present inference as Evidence, or hide uncertainty;
- widen scope silently, or renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
