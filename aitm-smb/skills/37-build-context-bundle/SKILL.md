---
name: 37-build-context-bundle
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: framework-operations
---

# Skill: Build Agent Context Bundle

## Required inputs

- selected profile
- requested skill
- upstream artifacts

## Produces

- no persistent artifact required; return findings through `AGENT_OUTPUT_STANDARD.md`

## Procedure

1. Load canonical Core files.
2. Load selected profile.
3. Load only the relevant methodology/module documents.
4. Load relevant artifact contract and skill.
5. Load upstream approved artifacts and evidence.
6. Verify normative dependencies are present.

## Controls

- Follow `NORMATIVE_INDEX.md`.
- Preserve Core semantics.
- Do not activate modules without profile justification.
- Record deviations explicitly.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
