---
name: 36-select-application-profile
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: framework-operations
---

# Skill: Select Application Profile

## Required inputs

- transformation scope
- risk/impact context
- known system complexity

## Produces

- no persistent artifact required; return findings through `AGENT_OUTPUT_STANDARD.md`

## Procedure

1. Assess number of capabilities and systems affected.
2. Assess reversibility and AI authority.
3. Assess customer, financial, legal, security, and data impact.
4. Assess portfolio complexity and change load.
5. Select Compact, Standard, Governed, Portfolio, and/or Measured.
6. Record rationale and escalation triggers.

## Controls

- Follow `NORMATIVE_INDEX.md`.
- Preserve Core semantics.
- Do not activate modules without profile justification.
- Record deviations explicitly.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
