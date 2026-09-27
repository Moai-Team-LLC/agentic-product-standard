---
name: 05-prioritize-initiatives
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "4"
human_gate: true
---

# Skill: Orchestrate Prioritization

## Purpose

Select, defer, reject, or investigate intervention candidates using explicit trade-offs and human approval.

## Specialist skills

- none required; execute the phase contract directly

## Produces

- `artifacts/prioritization-matrix.md`

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
