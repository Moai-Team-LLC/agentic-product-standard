---
name: 39-audit-framework-integrity
description: "Audits the AITM-SMB repository itself before a release: runs python3 tools/validate.py and its engagement check on the worked example, resolves orphan warnings, and performs the MAINTENANCE release audits that need judgment: duplicate definitions and artifact-versus-module record parity, semantic consistency, registry-versus-directory parity, skill and contract shape, profile and artifact completeness, skill dependencies, versions, CHANGELOG and migration table, and the abstract-scenario walk-through. Use before every release and after structural changes; it is a maintainer skill, not an engagement skill. Produces findings only. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: framework-operations
phase: "maintenance"
human_gate: false
---

# Skill 39: Audit Framework Integrity

## Purpose

Catch documentation drift before release: in an agent-readable methodology, drift is a methodology defect. Covers every release check in `MAINTENANCE.md` §2 and §5.

## Required inputs

- the AITM root at the release candidate;
- the target version and its `CHANGELOG.md` section.

## Normative sources

- `MAINTENANCE.md` (§2 release checks, §5 release audit)
- `VERSIONING.md`
- `NORMATIVE_INDEX.md`, `CANONICAL_CONCEPTS.md`
- `tools/validate.py`

## Produces

- no persistent artifact; `findings`: one per defect, with file, check, and evidence. The maintainer records the release result in `releases/`.

## Procedure

1. Run `python3 tools/validate.py`; every error is a finding (`MAINTENANCE.md` §2 step 1).
2. Run `python3 tools/validate.py --engagement examples/compact-scenario-b`; every error is a finding (step 2).
3. Orphan check: for each orphan warning, name where the file should be referenced, or propose its removal (step 4).
4. Duplicate-definition audit (`MAINTENANCE.md` §3, §4): each record shape is defined once, where `CANONICAL_CONCEPTS.md` names it; compare every artifact contract's fields with its owning module and every "extends" list with its base record (artifact-versus-module parity); report dangerous duplication, including gate lists restated outside `STANDARD.md` §8.
5. Semantic consistency: Core, modules, contracts, and skills agree under `NORMATIVE_INDEX.md` precedence.
6. Registry parity: `skills/INDEX.md`, `artifacts/INDEX.md`, `MODULE_CATALOG.md`, and `MANIFEST.md` match the directories and files 1:1 (numbers, names, classes, phases, gates, producers); each SKILL.md follows `skills/_SKILL_TEMPLATE.md` and each contract `artifacts/_ARTIFACT_CONTRACT.md`.
7. Profile completeness: every `APPLICATION_PROFILES.md` item resolves to an artifact contract (`MINIMUM_ARTIFACT_SET.md`), module, or skill.
8. Skill dependency and artifact completeness (`MAINTENANCE.md` §5): every skill input is produced upstream, every orchestrator's specialists exist, no skill is unreachable, and every contract has a producing skill.
9. Versions and changelog: versions align (`VERSIONING.md` §8), and the `CHANGELOG.md` section exists and the release notes in `releases/` carry a migration table for every field rename (`VERSIONING.md` §9; `MAINTENANCE.md` §2 step 5).
10. Scenario walk-through: walk changed components through `validation/ABSTRACT_SCENARIOS.md` and the worked example; report any that needs a core-definition change or produces a listed anti-pattern.
11. Review `rubrics/RELEASE_READINESS.md` (informative; step 6).

## MUST NOT

- fix defects silently while auditing; report them, and change files only through `CONTRIBUTING.md`;
- treat informative rubrics as normative;
- load engagement data; this skill audits the framework, not an engagement.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
