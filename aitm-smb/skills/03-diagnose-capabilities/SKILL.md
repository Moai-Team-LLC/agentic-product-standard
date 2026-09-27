---
name: 03-diagnose-capabilities
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "2"
human_gate: false
---

# Skill: Orchestrate Capability Diagnosis

## Purpose

Move from observations and symptoms to evidence-backed Gaps and causes.

## Specialist skills

- `skills/12-separate-symptoms-gaps-causes/SKILL.md`
- `skills/16-validate-root-cause/SKILL.md`

## Produces

- `artifacts/capability-diagnosis.md`
- `artifacts/diagnostic-record.md`

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
