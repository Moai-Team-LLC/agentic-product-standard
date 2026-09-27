---
name: 19-assess-system-effects
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: system-design
---

# Skill: Assess System Effects

## Required inputs

- candidate Initiative
- Capability Network
- System Constraint

## Produces

- `artifacts/system-effect-assessment.md`

## Procedure

1. Identify new upstream requirements.
2. Identify new downstream demand.
3. Identify shared-resource effects.
4. Identify metric or incentive distortion.
5. Predict likely Constraint Migration.
6. Define mitigations or sequencing changes.

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
