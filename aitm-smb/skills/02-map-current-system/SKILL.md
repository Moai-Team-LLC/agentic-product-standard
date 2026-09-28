---
name: 02-map-current-system
description: "Phase 1 orchestrator. Builds an evidence-based model of how the business produces value today for the approved Outcomes: discovers Capabilities and their CURRENT States (skill 11) and, where the profile requires it, maps value streams, roles, decisions, processes, data, knowledge and applications. Use after Outcomes are approved (HG-OUTCOME) and before diagnosis. Produces the Capability Map, the Business System Map and Evidence Register entries. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "1"
human_gate: false
---

# Skill 02: Orchestrate Current-System Mapping

## Purpose

Build the outcome-scoped current system and capability model that diagnosis compares against.

## Required inputs

The Required inputs of `methodology/01-current-system.md` (approved Transformation Intent and profile Decision).

## Normative sources

- `methodology/01-current-system.md` and the modules in its Method

## Produces

- `artifacts/capability-map.md` — Capabilities (`CAP-###`) and their CURRENT States (`STA-###`)
- `artifacts/business-system-map.md` — where the profile requires it
- `artifacts/evidence-register.md` — Evidence and Evidence Debt

## Specialist skills

- `skills/11-discover-capabilities/SKILL.md` — always: Capabilities and CURRENT States for the approved Outcomes

## Procedure

1. Load the active profiles (`AGENT_CONTEXT_POLICY.md`) and `methodology/01-current-system.md`.
2. Verify the phase's Required inputs; stop with `BLOCKED` while `HG-OUTCOME` is open.
3. Execute the phase Activities, invoking skill 11 for Capabilities and CURRENT States.
4. Merge specialist outputs into the phase instances; keep stable IDs and the `TRACEABILITY.md` §4 trace.
5. Validate the phase Exit condition (`EXECUTION_MODEL.md` §2) and the Validation of each produced contract.
6. Re-check the profiles at the phase exit (`PROFILE_SELECTION.md` §6); a change is a new profile Decision (skill 36).
7. Stop with `INSUFFICIENT_EVIDENCE` when meeting the exit would require invented business facts (record Evidence Debt); with `HUMAN_DECISION_REQUIRED` at any `STANDARD.md` §8 gate whose trigger occurs.

## MUST NOT

- put target-state solutions into the current-state model;
- map the whole enterprise instead of the Outcome-relevant boundary;
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
