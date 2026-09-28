---
artifact_type: transformation-roadmap
framework_version: 1.1.0
status: canonical
entity: Initiative
id_prefix: INI
produced_by: [05-prioritize-initiatives, 07-build-roadmap, 08-design-operating-model]
---

# Transformation Roadmap

## Purpose

Hold the selected Initiatives and their sequence from the Current State, through Transition States, to the Capability Target States (integrated in the Target Operating Architecture, where one exists).

## Record

Record contract: Initiative [`CORE_MODEL.md`](../CORE_MODEL.md) §7.

Extends `initiative` with:

```yaml
initiative:
  evidence_to_produce: []     # evidence plan: what the Initiative and its slices must demonstrate, and how
  slice_ids: []               # SLC-### (execution/DELIVERY_SLICE.md); each slice's initiative_id points back
  dependency_types: {}        # optional: INI-### from dependencies → HARD | INFORMATION | GOVERNANCE | LEARNING | CAPACITY
  economic_hypothesis:        # material Initiatives, before HG-BUDGET: record economics/TRANSFORMATION_ECONOMICS.md §5; initiative_id is this INI
  operation:                  # optional, Compact only: the Phase 7 minimum instead of separate plans (EXECUTION_MODEL.md §2)
    operating_owner:          # role accountable for the change in operation
    observability_signal:     # what shows it is working or failing
    support_path:
    role_changes: []
    failure_or_rollback_path:
    adoption:                 # short form of the Adoption Plan (artifacts/adoption-plan.md; change/CHANGE_ADOPTION_MODEL.md §3, §4)
      training:
      support:                # support for affected roles while they adopt the change
      feedback:               # how users report problems and how the feedback is acted on
      adoption_metric_ids: [] # MET-### (artifacts/transformation-scorecard.md)
```

Also holds, unless a Pilot Plan ([`artifacts/pilot-plan.md`](pilot-plan.md)) holds them:

```yaml
slices: []                    # Transformation Slice records (SLC-###), record contract execution/DELIVERY_SLICE.md
experiments: []               # Experiment records (EXP-###), record contract execution/EXPERIMENT_MODEL.md
```

`decision_gates` items ([`CORE_MODEL.md`](../CORE_MODEL.md) §7) are `GAT-###` Execution Gate records ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md); required under the Governed profile, optional otherwise, [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2) and/or mappings `{gate: HG-*, subject_ids: []}` naming what the gate will decide.

## Rules

The Initiative record is created at selection (Phase 4, [`methodology/04-prioritization.md`](../methodology/04-prioritization.md)) and completed in Phase 6 ([`methodology/06-roadmap.md`](../methodology/06-roadmap.md)). In Compact, skill 08 MAY add `operation` in Phase 7; every `operation` field is then filled, `adoption` included, so the Phase 7 exit holds ([`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2).

`status: approved` for a material Initiative requires a Decision closing `HG-INITIATIVE`; committing material budget requires `HG-BUDGET` ([`STANDARD.md`](../STANDARD.md) §8), whose Decision cites the `economic_hypothesis` as [`economics/TRANSFORMATION_ECONOMICS.md`](../economics/TRANSFORMATION_ECONOMICS.md) §5 specifies.

Sequencing: [`transition/TRANSFORMATION_SEQUENCING.md`](../transition/TRANSFORMATION_SEQUENCING.md). A planned AI authority increase sits behind a `{gate: HG-AUTHORITY, subject_ids: [AUT-###]}` entry in `decision_gates`; the Decision that closes it lists that `AUT-###` and states the new level and scope ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3).

## Validation

- [ ] every Initiative links Interventions, Capabilities, expected Outcomes, success Metrics, and Evidence or a visible `MISSING:` entry (INV-14, [`TRACEABILITY.md`](../TRACEABILITY.md) §4)
- [ ] every material Initiative is approved through `HG-INITIATIVE` before `status: approved`, and carries its `economic_hypothesis` before `HG-BUDGET`
- [ ] execution-ready (Phase 6): owner, bounded `scope`, entry and exit States, dependencies, `decision_gates`, `evidence_to_produce`, rollback or recovery
- [ ] where material uncertainty remains, the evidence plan includes an Experiment or Pilot before wider rollout (INV-11)
- [ ] sequence follows constraint relevance and dependency order ([`transition/TRANSFORMATION_SEQUENCING.md`](../transition/TRANSFORMATION_SEQUENCING.md)), or records why not
- [ ] where `operation` is used (Compact): every field is filled, and `adoption` names at least one adoption Metric
