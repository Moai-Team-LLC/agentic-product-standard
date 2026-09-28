---
artifact_type: system-constraint
framework_version: 1.1.0
status: canonical
entity: System Constraint
id_prefix: CST
owner_module: design/CONSTRAINT_ANALYSIS.md
produced_by: [06-design-target-system, 18-identify-system-constraint]
---

# System Constraint

## Purpose

Record the condition that most limits improvement of a target Outcome, why it is system-limiting, and where it is likely to move once relaxed (Constraint Migration).

## Record

```yaml
system_constraint:
  id: CST-###
  outcome_ids: []
  capability_ids: []
  type:                       # common types: design/CONSTRAINT_ANALYSIS.md §2
  evidence_ids: []
  current_effect:
  why_system_limiting:        # result of the constraint test (design/CONSTRAINT_ANALYSIS.md §3)
  intervention_ids: []        # INT-### that relax it
  likely_next_constraint:     # predicted Constraint Migration (design/CONSTRAINT_ANALYSIS.md §5)
  monitoring_metric_ids: []
```

## Rules

Do not label every bottleneck a system constraint ([`design/CONSTRAINT_ANALYSIS.md`](../design/CONSTRAINT_ANALYSIS.md) §4).

A System Constraint is not a design Constraint; design Constraints go in `constraints` fields.

When the constraint has moved, record the new one as a new `CST-###` and mark the old one `status: superseded`.

## Validation

- [ ] linked to the target Outcomes and the Capabilities where the constraint sits
- [ ] passes the constraint test (`why_system_limiting`), backed by Evidence or labeled Assumptions
- [ ] distinguished from local bottlenecks
- [ ] likely next constraint predicted and monitored (`monitoring_metric_ids`)
