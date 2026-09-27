---
name: 18-identify-system-constraint
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: system-design
---

# Skill: Identify System Constraint

## Required inputs

- Capability Network
- metrics
- diagnostic evidence

## Produces

- `artifacts/system-constraint.md`

## Procedure

1. List material bottlenecks and limiting conditions.
2. Test which condition most limits the target Outcome.
3. Distinguish local bottlenecks from the system constraint.
4. Record evidence and uncertainty.
5. Estimate likely Constraint Migration after improvement.

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
