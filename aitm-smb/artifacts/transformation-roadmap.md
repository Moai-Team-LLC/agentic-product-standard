---
artifact_type: transformation-roadmap
framework_version: 1.1.0
status: canonical
entity: Initiative
id_prefix: INI
produced_by: [05-prioritize-initiatives, 07-build-roadmap]
---

# Transformation Roadmap

## Purpose

Hold the selected Initiatives and their sequence from the Current State, through Transition States, to the Capability Target States (integrated in the Target Operating Architecture, where one exists).

## Record

Record contract: Initiative `CORE_MODEL.md` §7.

Extends `initiative` with:

```yaml
initiative:
  evidence_to_produce: []     # evidence plan: what the Initiative and its slices must demonstrate, and how
  slice_ids: []               # SLC-### (execution/DELIVERY_SLICE.md); each slice's initiative_id points back
  dependency_types: {}        # optional: INI-### from dependencies → HARD | INFORMATION | GOVERNANCE | LEARNING | CAPACITY
  execution_state:            # optional, once active: one state of execution/EXECUTION_PRINCIPLES.md §4
```

`decision_gates` hold `HG-*` ids and, under the Governed profile, `GAT-###` Execution Gate records (`execution/EXECUTION_GATE_MODEL.md`); other profiles MAY use GAT records (`EXECUTION_MODEL.md` §2).

## Rules

The Initiative record is created at selection (Phase 4, `methodology/04-prioritization.md`) and completed in Phase 6 (`methodology/06-roadmap.md`).

`status: approved` for a material Initiative requires a Decision closing `HG-INITIATIVE`; committing material budget requires `HG-BUDGET` (`STANDARD.md` §8).

Sequencing: `transition/TRANSFORMATION_SEQUENCING.md`. A planned AI authority increase sits behind an `HG-AUTHORITY` entry in `decision_gates`.

## Validation

- [ ] every Initiative links Interventions, Capabilities, expected Outcomes, success Metrics, and Evidence or a visible `MISSING:` entry (INV-14, `TRACEABILITY.md` §4)
- [ ] every material Initiative is approved through `HG-INITIATIVE` before `status: approved`
- [ ] execution-ready (Phase 6): owner, bounded `scope`, entry and exit States, dependencies, `decision_gates`, `evidence_to_produce`, rollback or recovery
- [ ] where material uncertainty remains, the evidence plan includes an Experiment or Pilot before wider rollout (INV-11)
- [ ] sequence follows constraint relevance and dependency order (`transition/TRANSFORMATION_SEQUENCING.md`), or records why not
