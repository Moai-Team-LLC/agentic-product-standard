---
name: 21-design-transition-states
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: system-design
---

# Skill: Design Transition States

## Required inputs

- Current State
- Target Operating Architecture
- risk/uncertainty model

## Produces

- `artifacts/transition-state.md`

## Procedure

1. Identify changes that cannot safely occur together.
2. Create independently operable intermediate states.
3. Use shadow or parallel states where uncertainty warrants them.
4. Define entry/exit conditions.
5. Define evidence to collect.
6. Define rollback or recovery.
7. Sequence authority increases explicitly.

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
