---
name: 17-map-capability-network
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: system-design
---

# Skill: Map Capability Network

## Required inputs

- Capability Map
- Outcome scope
- current-state evidence

## Produces

- `artifacts/capability-network.md`

## Procedure

1. Identify inputs and outputs of each relevant Capability.
2. Map information, work, knowledge, decision, control, resource, and system dependencies.
3. Mark criticality and failure effects.
4. Identify shared capabilities.
5. Limit the graph to dependencies relevant to target Outcomes.

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
