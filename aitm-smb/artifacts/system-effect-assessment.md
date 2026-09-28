---
artifact_type: system-effect-assessment
framework_version: 1.1.0
status: canonical
entity: System Effect Assessment
id_prefix: SFX
owner_module: design/LOCAL_OPTIMIZATION_GUARD.md
produced_by: [06-design-target-system, 19-assess-system-effects, 24-audit-local-optimization]
---

# System Effect Assessment

## Purpose

Prevent local optimization from degrading the wider operating system: record the INV-09 effects of a selected Initiative and how they are mitigated.

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

In the Compact profile, a short record answering the `design/LOCAL_OPTIMIZATION_GUARD.md` §2 questions suffices.

## Rules

One assessment per selected Initiative. A skill that finds an existing SFX for the same `initiative_id` (or `toa_id`) updates it instead of creating a second one.

A `local_only` or `degrades_outcome` verdict is reported in the handoff `risks`; where it changes a Phase 4 priority, the selection returns to the Phase 4 gate (`design/LOCAL_OPTIMIZATION_GUARD.md` §5).

## Validation

- [ ] one SFX per selected Initiative, linked by `initiative_id`
- [ ] upstream, downstream, shared-resource, incentive, and Constraint Migration effects answered (`design/LOCAL_OPTIMIZATION_GUARD.md` §2)
- [ ] `system_verdict` states whether the change improves the target Outcome or only a local metric
- [ ] material negative effects have a mitigation or sequencing change
