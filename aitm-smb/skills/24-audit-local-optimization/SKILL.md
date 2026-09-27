---
name: 24-audit-local-optimization
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: system-design
---

# Skill: Audit Local Optimization Risk

## Required inputs

- Initiative or Target Operating Architecture
- Capability Network

## Produces

- `artifacts/system-effect-assessment.md`

## Procedure

1. Identify throughput increases created by the change.
2. Identify downstream capacity risks.
3. Identify exception-load shifts.
4. Identify shared-resource contention.
5. Identify KPI gaming or incentive risks.
6. Determine whether the initiative improves system Outcome or only a local metric.

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
