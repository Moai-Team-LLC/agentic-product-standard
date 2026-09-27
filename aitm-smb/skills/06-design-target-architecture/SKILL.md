---
name: 06-design-target-architecture
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "5"
human_gate: true
---

# Skill: Orchestrate Target Operating Architecture

## Purpose

Compose capability target states into a system-level Target Operating Architecture.

## Specialist skills

- `skills/15-design-target-state/SKILL.md`
- `skills/17-map-capability-network/SKILL.md`
- `skills/18-identify-system-constraint/SKILL.md`
- `skills/19-assess-system-effects/SKILL.md`
- `skills/20-design-target-operating-architecture/SKILL.md`
- `skills/23-design-decision-rights/SKILL.md`
- `skills/24-audit-local-optimization/SKILL.md`

## Produces

- `artifacts/capability-target-state.md`
- `artifacts/capability-network.md`
- `artifacts/system-constraint.md`
- `artifacts/target-operating-architecture.md`
- `artifacts/decision-rights-map.md`
- `artifacts/system-effect-assessment.md`

## Orchestration procedure

1. load the selected Application Profile;
2. load the relevant methodology phase;
3. verify required upstream artifacts;
4. invoke the listed specialist skills only where their conditions apply;
5. preserve stable identifiers and traceability;
6. merge specialist outputs into phase artifacts;
7. validate phase exit conditions;
8. stop at any human decision gate.

## Rule

This orchestrator MUST NOT create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
