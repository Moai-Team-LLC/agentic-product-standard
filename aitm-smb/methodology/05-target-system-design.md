# Phase 5 — Design Target System (Target System Design)

## Objective

Design the future behavior of each selected Capability and, where the profile requires it, the integrated future operating system across Capabilities, not only isolated solutions.

## Required inputs

- approved Outcomes;
- selected Initiatives (`INI-###`, Phase 4) and their Interventions;
- Capability Map with CURRENT States, and Capability Diagnosis;
- AI Suitability and Autonomy Assessments with approved Authority Ceilings, for selected `AI_*` Interventions;
- design constraints (Transformation Intent);
- Business System Map, where the profile requires it.

## Method

Use:

1. `design/TARGET_STATE_DESIGN.md`
2. `design/LOCAL_OPTIMIZATION_GUARD.md`
3. `design/CAPABILITY_NETWORK.md`
4. `design/CONSTRAINT_ANALYSIS.md`
5. `design/DECISION_RIGHTS_ARCHITECTURE.md`
6. `design/TARGET_OPERATING_ARCHITECTURE.md`
7. `design/SYSTEM_TRANSFORMATION_MODEL.md`
8. `design/INFORMATION_KNOWLEDGE_ARCHITECTURE.md`
9. `design/APPLICATION_BOUNDARIES.md`

Items 1–2 apply in every profile. Items 3–9 apply where the profile requires their outputs (Standard and above), or where they change a decision (INV-15).

## Activities

1. create a Capability Target State (`STA-###`, `type: TARGET`) for each selected Capability, with its Outcomes, the Gaps it closes, and, where AI is present, AI authority per action class within the approved Authority Ceiling (skill 15);
2. Standard and above: map inter-capability dependencies (Capability Network, skill 17);
3. Standard and above: identify the current System Constraint and its likely Constraint Migration (skill 18);
4. answer the system-effect questions for each selected Initiative (skill 19; audit with skill 24); in Compact a short record suffices;
5. Standard and above: define roles and Decision Rights (skill 23);
6. Standard and above: integrate the Capability Target States into one Target Operating Architecture: information and knowledge ownership, application and integration boundaries, automation and AI responsibilities, governance, metrics, and economic boundaries (skill 20);
7. Standard and above: run the pre-approval system checks (`design/SYSTEM_TRANSFORMATION_MODEL.md` §6);
8. if the System Constraint or a System Effect Assessment changes a Phase 4 priority, return the affected selection to the Phase 4 gate (`EXECUTION_MODEL.md` §3);
9. submit the Target Operating Architecture (Compact: the Capability Target States) and material Decision Rights changes for approval.

## Outputs

Produce only the outputs the active profile requires (`APPLICATION_PROFILES.md`, `EXECUTION_MODEL.md` §2); other outputs are optional under INV-15.

- every profile: Capability Target States (`artifacts/capability-target-state.md`), referenced by each Capability's `target_state_id`;
- every profile: system-effect check per selected Initiative (`artifacts/system-effect-assessment.md`);
- Standard adds: Capability Network (`artifacts/capability-network.md`), System Constraint (`artifacts/system-constraint.md`), full System Effect Assessments, Decision Rights Map (`artifacts/decision-rights-map.md`), Target Operating Architecture (`artifacts/target-operating-architecture.md`);
- Portfolio adds: cross-capability dependency analysis (Capability Network `DEP-###` records);
- Decision & Assumption Log updates.

## Human gates

- `HG-TOA` — stop with `HUMAN_DECISION_REQUIRED` until a Decision closing it lists the `TOA-###` (Compact: the Capability Target State `STA-###` IDs) in `subject_ids`.
- `HG-DECISION-RIGHTS` — for each material Decision Rights change (`BDS-###` in `subject_ids`).
- `HG-INITIATIVE` again for a selection returned to Phase 4.

A target AI level above the approved Authority Ceiling requires re-assessing the ceiling first (`HG-AUTHORITY`, `diagnostics/AUTONOMY_SUITABILITY.md` §6). Any other gate applies whenever its trigger occurs. Governed profile: Execution Gate B (`execution/EXECUTION_GATE_MODEL.md`).

## Exit condition

Matches `EXECUTION_MODEL.md` §2:

```text
Capability Target States (STA, type TARGET) for the selected Capabilities
AND the design outputs the profile requires (from Standard: a coherent Target Operating Architecture)
AND dependencies, material authority, and system effects (INV-09) explicit
AND system-level metrics exist
AND Target Operating Architecture approved (HG-TOA; Compact: Capability Target States)
```

Refinements: Standard and above: the current System Constraint is identified, or recorded as Evidence Debt; every selection affected by the System Constraint or a System Effect Assessment has been re-confirmed at the Phase 4 gate.

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` (`AGENTS.md` §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

Merging Capability Target State and Target Operating Architecture (`STANDARD.md` §7), or designing from vendor capabilities before target behavior and system boundaries (INV-08).
