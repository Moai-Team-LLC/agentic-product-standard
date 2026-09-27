---
name: 22-build-transformation-portfolio
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: system-design
---

# Skill: Build Transformation Portfolio

## Required inputs

- selected Initiatives
- Capability Network
- System Constraint
- Transition States

## Produces

- `artifacts/transformation-portfolio.md`

## Procedure

1. Classify initiatives as constraint, enabler, capability, risk, or learning.
2. Map dependencies.
3. Identify shared enablers.
4. Identify resource contention.
5. Estimate change saturation.
6. Sequence portfolio around Outcome leverage, constraint, learning, and risk.

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
