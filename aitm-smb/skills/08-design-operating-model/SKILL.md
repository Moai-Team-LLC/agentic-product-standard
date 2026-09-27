---
name: 08-design-operating-model
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "7"
human_gate: true
---

# Skill: Orchestrate Operating Model & Governance

## Purpose

Make the transformed system ownable, observable, governable, supportable, and adoptable.

## Specialist skills

- `skills/28-design-observability/SKILL.md`
- `skills/30-design-adoption/SKILL.md`
- `skills/31-operationalize-governance/SKILL.md`
- `skills/35-audit-operational-readiness/SKILL.md`

## Produces

- `artifacts/operating-model.md`
- `artifacts/ai-governance-canvas.md`
- `artifacts/observability-plan.md`
- `artifacts/adoption-plan.md`

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
