---
artifact_type: capability-network
framework_version: 1.1.0
status: canonical
entity: Capability Network
id_prefix: CPN
owner_module: design/CAPABILITY_NETWORK.md
produced_by: [06-design-target-system, 17-map-capability-network]
---

# Capability Network

## Purpose

Show how the Capabilities relevant to the target Outcomes depend on one another, so that critical and shared dependencies are visible before the target system is designed.

## Record

Capability Network with its Capability Dependency (`DEP-###`) records:

```yaml
capability_network:
  id: CPN-###
  outcome_ids: []
  capability_ids: []          # CAP-### inside the transformation boundary
  dependencies:
    - id: DEP-###
      source_capability_id:   # CAP-###
      relation:               # one relation of design/CAPABILITY_NETWORK.md §2, read source RELATION target
      target_capability_id:   # CAP-###
      criticality: low | medium | high
      evidence_ids: []
      failure_effect:
      capacity_effect:
      notes:
```

## Validation

- [ ] every dependency uses one [`design/CAPABILITY_NETWORK.md`](../design/CAPABILITY_NETWORK.md) §2 relation, in the stated direction, recorded once
- [ ] critical dependencies ([`design/CAPABILITY_NETWORK.md`](../design/CAPABILITY_NETWORK.md) §4) are marked `criticality: high` with failure and capacity effects
- [ ] shared capabilities are visible ([`design/CAPABILITY_NETWORK.md`](../design/CAPABILITY_NETWORK.md) §6)
- [ ] transformation boundary is limited to Capabilities relevant to the target Outcomes ([`design/CAPABILITY_NETWORK.md`](../design/CAPABILITY_NETWORK.md) §7)
