---
artifact_type: system-effect-assessment
framework_version: 1.1.0
status: canonical
entity: System Effect Assessment
id_prefix: SFX
owner_module: design/LOCAL_OPTIMIZATION_GUARD.md
produced_by: [05-prioritize-initiatives, 06-design-target-system, 19-assess-system-effects, 24-audit-local-optimization]
---

# System Effect Assessment

## Purpose

Prevent local optimization from degrading the wider operating system: record the INV-09 effects of an Initiative before its selection is decided, and how they are mitigated.

## Record

```yaml
system_effect:
  id: SFX-###
  initiative_id:              # INI-###
  toa_id:                     # TOA-###, instead of initiative_id, when a whole Target Operating Architecture is assessed
  upstream_effects: []
  downstream_effects: []
  shared_resource_effects: []
  incentive_risks: []
  likely_constraint_migration:
  operational_risks: []       # including which role absorbs new exceptions
  system_verdict: improves_outcome | local_only | degrades_outcome | unknown
  mitigation: []              # mitigations or sequencing changes
```

In the Compact profile, a short record answering the [`design/LOCAL_OPTIMIZATION_GUARD.md`](../design/LOCAL_OPTIMIZATION_GUARD.md) §2 questions suffices.

## Rules

One assessment per Initiative proposed for selection: drafted in Phase 4 before `HG-INITIATIVE` (skill 05 via skill 19), refined at system level in Phase 5 (skill 06 via skills 19, 24; [`design/LOCAL_OPTIMIZATION_GUARD.md`](../design/LOCAL_OPTIMIZATION_GUARD.md) §4). A skill that finds an existing SFX for the same `initiative_id` (or `toa_id`) updates it instead of creating a second one.

A `local_only` or `degrades_outcome` verdict is reported in the handoff `risks`; where a refined effect changes a Phase 4 priority, the selection returns to `HG-INITIATIVE` ([`design/LOCAL_OPTIMIZATION_GUARD.md`](../design/LOCAL_OPTIMIZATION_GUARD.md) §5).

## Validation

- [ ] one SFX per Initiative proposed for selection, linked by `initiative_id`, recorded before the selection is decided (`HG-INITIATIVE` when material)
- [ ] upstream, downstream, shared-resource, incentive, and Constraint Migration effects answered ([`design/LOCAL_OPTIMIZATION_GUARD.md`](../design/LOCAL_OPTIMIZATION_GUARD.md) §2)
- [ ] `system_verdict` states whether the change improves the target Outcome or only a local metric
- [ ] material negative effects have a mitigation or sequencing change
