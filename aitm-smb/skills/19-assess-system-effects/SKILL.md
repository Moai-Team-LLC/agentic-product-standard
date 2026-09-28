---
name: 19-assess-system-effects
description: "Checks a selected Initiative for effects beyond its own Capability: upstream support, downstream demand, shared-resource and incentive effects, likely Constraint Migration and who absorbs new exceptions, with a verdict on whether it improves the target Outcome or only a local metric, and mitigations. Use in Phase 5 for every selected Initiative in every profile (in Compact a short record), invoked by skill 06. Produces one System Effect Assessment per Initiative. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: design-specialist
phase: "5"
human_gate: false
---

# Skill 19: Assess System Effects

## Purpose

Make INV-09 checkable for each selected Initiative: local improvement must not degrade the wider system. Invoked by `skills/06-design-target-system/SKILL.md`.

## Required inputs

- a selected Initiative (`INI-###`) and its Interventions;
- Capability Network and System Constraint, where the profile requires them.

## Normative sources

- `design/LOCAL_OPTIMIZATION_GUARD.md`
- `design/CONSTRAINT_ANALYSIS.md` §5 (Constraint Migration)

## Produces

- `artifacts/system-effect-assessment.md` — one System Effect Assessment (`SFX-###`) per selected Initiative

## Procedure

1. Answer every question in `design/LOCAL_OPTIMIZATION_GUARD.md` §2, using the Capability Network and System Constraint where present.
2. Check the common failures (§3) and predict the likely Constraint Migration.
3. Set `system_verdict`; add mitigations or sequencing changes for material negative effects.
4. Record one SFX per Initiative; if one exists for the same `initiative_id`, update it (§4). In Compact, a short record suffices.
5. When an effect changes a Phase 4 priority (§5), report it in `risks` and `decisions_needed` (`HG-INITIATIVE`).
6. Validate against the `artifacts/system-effect-assessment.md` Validation.
7. Stop with `INSUFFICIENT_EVIDENCE` when an effect cannot be judged without invented facts (record Evidence Debt); with `HUMAN_DECISION_REQUIRED` when any `STANDARD.md` §8 gate is reached.

## MUST NOT

- optimize an isolated metric instead of the target Outcomes;
- hide dependency effects or likely Constraint Migration;
- leave ownership of new exceptions implicit;
- increase AI authority implicitly;
- invent business facts, present inference as Evidence, or hide uncertainty;
- widen scope silently, or renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
