---
artifact_type: capability-map
framework_version: 1.1.0
status: canonical
entity: Capability
id_prefix: CAP
produced_by: [02-map-current-system, 11-discover-capabilities]
---

# Capability Map

## Purpose

Represent what the organization must be capable of doing, independently of the current org chart or software, and how each relevant Capability operates today (its CURRENT State).

## Record

Record contracts: Capability `CORE_MODEL.md` §2; State `CORE_MODEL.md` §3, `type: CURRENT` (one per Capability in scope, referenced by `current_state_id`).

Extends `capability` with:

```yaml
capability:
  dependencies: []    # CAP-### this Capability depends on; with a Capability Network: DEP-### (artifacts/capability-network.md)
  confidence: low | medium | high   # evidence strength for the Capability and its boundary
  boundary_notes:
```

Discovery method and granularity test: `diagnostics/CAPABILITY_DISCOVERY.md`. `target_state_id` stays empty until Phase 5.

## Rules

A capability SHOULD:

- be phrased as an organizational ability;
- remain meaningful if people or software change;
- connect to at least one Outcome.

A capability SHOULD NOT be named after a tool or department unless the organizational ability is genuinely identical.

A CURRENT State describes the present only; it MUST NOT contain target-state solutions.

## Validation

- [ ] every Capability links at least one approved Outcome (`outcome_ids`)
- [ ] every Capability passes the granularity test and is not named after a tool or department
- [ ] every Capability has an owner
- [ ] every Capability in scope has a CURRENT State backed by Evidence (`evidence_ids`) or labeled Assumptions (`assumption_ids`)
- [ ] no CURRENT State contains a target-state solution
