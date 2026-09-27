---
name: 10-audit-aitm-engagement
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "cross-phase"
human_gate: false
---

# Skill: Orchestrate Conformance Audit

## Purpose

Audit semantic traceability, selected-profile conformance, evidence discipline, human gates, and authority boundaries.

## Specialist skills

- `skills/38-audit-conformance/SKILL.md`

## Produces

- conformance findings and decisions

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
