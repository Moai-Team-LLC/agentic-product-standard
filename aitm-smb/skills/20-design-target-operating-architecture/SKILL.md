---
name: 20-design-target-operating-architecture
description: "Integrates the Capability Target States of the Capabilities in scope into one Target Operating Architecture: value streams, roles and decision rights, coordination, information and knowledge ownership, application boundaries, automation and AI responsibilities within approved Authority Ceilings, governance, system-level metrics and economics; runs the consistency rules and pre-approval system checks and stops for approval (HG-TOA). Use in Phase 5 under the Standard profile or above, invoked by skill 06 after the Capability Target States, Capability Network, System Constraint and Decision Rights exist. Produces the Target Operating Architecture. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: design-specialist
phase: "5"
human_gate: true
gates: [HG-TOA]
---

# Skill 20: Design Target Operating Architecture

## Purpose

Describe how the transformed business system operates across Capabilities, without merging it with the Capability Target States it composes ([`STANDARD.md`](../../STANDARD.md) §7). Invoked by [`skills/06-design-target-system/SKILL.md`](../06-design-target-system/SKILL.md).

## Required inputs

- Capability Target States of the Capabilities in scope;
- Capability Network, System Constraint, and System Effect Assessments;
- Decision Rights Map, where it exists;
- selected Initiatives, approved Authority Ceilings, and design constraints.

## Normative sources

- [`design/TARGET_OPERATING_ARCHITECTURE.md`](../../design/TARGET_OPERATING_ARCHITECTURE.md)
- [`design/SYSTEM_TRANSFORMATION_MODEL.md`](../../design/SYSTEM_TRANSFORMATION_MODEL.md) §6 (pre-approval system checks)
- [`design/DECISION_RIGHTS_ARCHITECTURE.md`](../../design/DECISION_RIGHTS_ARCHITECTURE.md), [`design/INFORMATION_KNOWLEDGE_ARCHITECTURE.md`](../../design/INFORMATION_KNOWLEDGE_ARCHITECTURE.md), [`design/APPLICATION_BOUNDARIES.md`](../../design/APPLICATION_BOUNDARIES.md)

## Produces

- [`artifacts/target-operating-architecture.md`](../../artifacts/target-operating-architecture.md) — Target Operating Architecture (`TOA-###`)

## Procedure

1. Compose the Capability Target State of every Capability in `capability_ids` (`target_state_ids`); link the System Constraints addressed (`system_constraint_ids`).
2. Fill the model fields layer by layer ([`design/TARGET_OPERATING_ARCHITECTURE.md`](../../design/TARGET_OPERATING_ARCHITECTURE.md) §2); the decision model integrates the Decision Rights Map from skill 23 where it exists.
3. Keep automation and AI responsibilities within the approved Authority Ceilings; name system-level Metrics (`metric_ids`).
4. Apply the consistency rules (§4) and the design principle (§5).
5. Run the pre-approval system checks ([`design/SYSTEM_TRANSFORMATION_MODEL.md`](../../design/SYSTEM_TRANSFORMATION_MODEL.md) §6), including downstream capacity and likely Constraint Migration.
6. Record the TOA with `status: proposed`; validate against the contract's Validation.
7. Stop with `INSUFFICIENT_EVIDENCE` when the architecture would rest on invented facts; record Evidence Debt.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-TOA`; record the gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing the `TOA-###` in `subject_ids`; the named human's approval updates it to `approved`. Only then set the TOA `status: approved`. Any other [`STANDARD.md`](../../STANDARD.md) §8 gate applies whenever its trigger occurs.

## MUST NOT

- optimize local metrics at the expense of the target Outcomes;
- hide dependency effects or likely Constraint Migration;
- leave ownership or decision rights implicit;
- increase AI authority implicitly or beyond an approved ceiling;
- invent business facts, present inference as Evidence, or hide uncertainty;
- widen scope silently, or renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
