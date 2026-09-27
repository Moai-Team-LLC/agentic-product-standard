---
name: 02-map-current-system
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "1"
human_gate: false
---

# Skill: Orchestrate Current-System Mapping

## Purpose

Build the outcome-scoped current system and capability model.

## Specialist skills

- `skills/11-discover-capabilities/SKILL.md`

## Produces

- `artifacts/business-system-map.md`
- `artifacts/capability-map.md`

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
