---
name: 39-audit-framework-integrity
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: framework-operations
---

# Skill: Audit Framework Integrity

## Required inputs

- AITM-SMB repository

## Produces

- no persistent artifact required; return findings through `AGENT_OUTPUT_STANDARD.md`

## Procedure

1. Check normative links.
2. Check duplicate canonical definitions.
3. Check skill dependencies.
4. Check artifact references.
5. Check MANIFEST/version consistency.
6. Check deprecated content.
7. Report semantic drift.

## Controls

- Follow `NORMATIVE_INDEX.md`.
- Preserve Core semantics.
- Do not activate modules without profile justification.
- Record deviations explicitly.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
