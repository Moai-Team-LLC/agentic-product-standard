---
name: 09-measure-evolution
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "8"
human_gate: false
---

# Skill: Orchestrate Measurement & Evolution

## Purpose

Evaluate business effect, capability effect, economics, AI quality, and update the architecture from evidence.

## Specialist skills

- `skills/26-design-evaluation/SKILL.md`
- `skills/33-assess-value-realization/SKILL.md`

## Produces

- `artifacts/transformation-scorecard.md`
- `artifacts/value-realization-report.md`

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
