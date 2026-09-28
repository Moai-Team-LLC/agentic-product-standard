---
name: 06-design-target-system
description: "Phase 5 orchestrator. Designs the target system for the selected Initiatives: a Capability Target State per selected Capability (skill 15), system-level refinement of the System Effect Assessments (skills 19, 24) and, from the Standard profile, the Capability Network, System Constraint, Decision Rights and an integrated Target Operating Architecture (skills 17, 18, 23, 20); stops for architecture and decision-rights approval (HG-TOA, HG-DECISION-RIGHTS); under Governed, records Execution Gate B. Use after Initiatives are selected, before roadmap design. Produces only the design artifacts the active profile requires. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: orchestrator
  phase: "5"
  human_gate: "true"
  gates: "HG-TOA, HG-DECISION-RIGHTS"
---

# Skill 06: Orchestrate Target System Design

## Purpose

Design the future behavior of each selected Capability and, where the profile requires it, compose the Capability Target States into one system-level Target Operating Architecture.

## Required inputs

The Required inputs of [`methodology/05-target-system-design.md`](../../methodology/05-target-system-design.md) (approved Outcomes, selected Initiatives and their System Effect Assessments, Capability Map and Diagnosis, approved Authority Ceilings for selected `AI_*` Interventions, design constraints).

## Normative sources

- [`methodology/05-target-system-design.md`](../../methodology/05-target-system-design.md) and the modules in its Method

## Produces

Only what the active profile requires ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md)); Compact: the Capability Target States and the short System Effect Assessment of each selected Initiative.

- [`artifacts/capability-target-state.md`](../../artifacts/capability-target-state.md) — every profile (skill 15)
- [`artifacts/system-effect-assessment.md`](../../artifacts/system-effect-assessment.md) — every profile: each selected Initiative's Phase 4 assessment, refined at system level (skills 19, 24)
- [`artifacts/capability-network.md`](../../artifacts/capability-network.md) — Standard and above (skill 17)
- [`artifacts/system-constraint.md`](../../artifacts/system-constraint.md) — Standard and above (skill 18)
- [`artifacts/decision-rights-map.md`](../../artifacts/decision-rights-map.md) — Standard and above (skill 23)
- [`artifacts/target-operating-architecture.md`](../../artifacts/target-operating-architecture.md) — Standard and above (skill 20)
- [`artifacts/execution-gate.md`](../../artifacts/execution-gate.md) — Gate B per selected Initiative after `HG-TOA`; Governed
- [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md) — gate Decisions, Assumptions

## Specialist skills

- [`skills/15-design-target-state/SKILL.md`](../15-design-target-state/SKILL.md) — every profile: each selected Capability
- [`skills/17-map-capability-network/SKILL.md`](../17-map-capability-network/SKILL.md) — Standard and above
- [`skills/18-identify-system-constraint/SKILL.md`](../18-identify-system-constraint/SKILL.md) — Standard and above
- [`skills/19-assess-system-effects/SKILL.md`](../19-assess-system-effects/SKILL.md) — every selected Initiative: refines its Phase 4 assessment at system level (Compact: a short record)
- [`skills/24-audit-local-optimization/SKILL.md`](../24-audit-local-optimization/SKILL.md) — after 19, to audit each System Effect Assessment; Standard and above, again after 20 for the Target Operating Architecture; updates, never duplicates, an assessment
- [`skills/23-design-decision-rights/SKILL.md`](../23-design-decision-rights/SKILL.md) — Standard and above, where material decisions or authority change
- [`skills/20-design-target-operating-architecture/SKILL.md`](../20-design-target-operating-architecture/SKILL.md) — Standard and above, after 15, 17, 18, 19, 23

## Procedure

1. Load the active profiles ([`AGENT_CONTEXT_POLICY.md`](../../AGENT_CONTEXT_POLICY.md)) and [`methodology/05-target-system-design.md`](../../methodology/05-target-system-design.md).
2. Verify the phase's Required inputs; while `HG-INITIATIVE` for a selected Initiative, or `HG-AUTHORITY` for a ceiling it relies on, is open, stop with `HUMAN_DECISION_REQUIRED` (gate in `open_gates`); stop with `BLOCKED` only when a required input is missing.
3. Execute the phase Activities, invoking the specialists in the order above where their conditions hold.
4. Merge specialist outputs into the phase instances; keep stable IDs and the [`TRACEABILITY.md`](../../TRACEABILITY.md) §4 trace.
5. If the System Constraint or a refined System Effect Assessment changes a Phase 4 priority, return that selection to `HG-INITIATIVE` ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §3).
6. Validate the phase Exit condition ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §2) and the Validation of each produced contract; review aid: [`rubrics/SYSTEM_DESIGN_RUBRIC.md`](../../rubrics/SYSTEM_DESIGN_RUBRIC.md).
7. Stop with `INSUFFICIENT_EVIDENCE` when the design would rest on invented facts; record Evidence Debt.
8. Submit the Target Operating Architecture (Compact: the Capability Target States) and material Decision Rights changes for approval.
9. Governed: once `HG-TOA` is approved, record Execution Gate B for each selected Initiative.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-TOA` and, for material Decision Rights changes, `HG-DECISION-RIGHTS`; record each gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing the `TOA-###` (Compact: the Capability Target State `STA-###`) or `BDS-###` in `subject_ids`; the named human's approval updates it to `approved`. Any other [`STANDARD.md`](../../STANDARD.md) §8 gate applies whenever its trigger occurs.

## MUST NOT

- merge Capability Target State and Target Operating Architecture ([`STANDARD.md`](../../STANDARD.md) §7);
- design from vendor capabilities before target behavior and system boundaries;
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
