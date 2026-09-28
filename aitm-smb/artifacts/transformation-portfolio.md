---
artifact_type: transformation-portfolio
framework_version: 1.1.0
status: canonical
entity: Transformation Portfolio
id_prefix: PTF
owner_module: portfolio/TRANSFORMATION_PORTFOLIO.md
produced_by: [07-build-roadmap, 22-build-transformation-portfolio]
---

# Transformation Portfolio

## Purpose

Coordinate several Initiatives toward system-level Outcomes: their categories, shared enablers, dependencies, risks, and the amount of change the organization can absorb. Required by the Portfolio profile.

## Record

```yaml
portfolio:
  id: PTF-###
  outcome_ids: []
  current_constraint:         # CST-###
  initiatives: []             # INI-###
  initiative_categories: {}   # INI-### → CONSTRAINT | ENABLER | CAPABILITY | RISK | LEARNING (portfolio/TRANSFORMATION_PORTFOLIO.md §3)
  dependencies: []            # material dependencies between Initiatives and on shared enablers
  shared_enablers: []
  shared_risks: []            # material ones also as Risk records (RSK-###, artifacts/decision-assumption-log.md)
  resource_constraints: []
  change_capacity:            # change saturation: portfolio/PORTFOLIO_PRIORITIZATION.md §4
  wip_limit:                  # maximum concurrently active Initiatives (portfolio/TRANSFORMATION_PORTFOLIO.md §5)
  governance_gates: []        # HG-* and GAT-### ids that govern the portfolio
  metric_ids: []
```

## Rules

No Initiative is added while a stop condition in `portfolio/PORTFOLIO_PRIORITIZATION.md` §5 holds, unless a Decision records the override.

## Validation

- [ ] every Initiative is listed and categorized (`initiative_categories`)
- [ ] every enabler Initiative links a business Outcome (`portfolio/TRANSFORMATION_PORTFOLIO.md` §4)
- [ ] transformation WIP is explicit (`wip_limit`), and active Initiatives do not exceed it
- [ ] change saturation, resource contention, and shared risks are visible
- [ ] no Initiative added while a stop condition holds, unless a Decision records the override
