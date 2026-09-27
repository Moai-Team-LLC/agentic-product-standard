---
name: 38-audit-conformance
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: framework-operations
---

# Skill: Audit AITM-SMB Conformance

## Required inputs

- engagement artifacts
- selected profiles

## Produces

- no persistent artifact required; return findings through `AGENT_OUTPUT_STANDARD.md`

## Procedure

1. Check minimal semantic chain.
2. Check profile-required modules/artifacts.
3. Check human decision gates.
4. Check evidence/assumption separation.
5. Check agent authority boundaries.
6. Check artifact proportionality and traceability.
7. List deviations and waivers.

## Controls

- Follow `NORMATIVE_INDEX.md`.
- Preserve Core semantics.
- Do not activate modules without profile justification.
- Record deviations explicitly.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
