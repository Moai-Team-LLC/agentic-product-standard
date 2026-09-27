---
name: 23-design-decision-rights
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: system-design
---

# Skill: Design Decision Rights

## Required inputs

- Target Capability States
- Autonomy Assessments
- current authority model

## Produces

- `artifacts/decision-rights-map.md`

## Procedure

1. Identify material business decisions.
2. Decompose compound decisions where useful.
3. Define current authority.
4. Define target authority.
5. Attach information, knowledge, policy, and escalation requirements.
6. Verify AI authority stays below approved ceiling.

## System-level controls

- Optimize target Outcomes, not isolated metrics.
- Surface dependency effects.
- Surface likely Constraint Migration.
- Keep ownership and decision rights explicit.
- Do not increase AI authority implicitly.
- Prefer bounded, operable transition states.

## Validation

- [ ] Outcome linkage preserved
- [ ] capability dependencies considered
- [ ] local optimization risk checked
- [ ] system constraint considered
- [ ] ownership explicit
- [ ] evidence/assumptions separated

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
