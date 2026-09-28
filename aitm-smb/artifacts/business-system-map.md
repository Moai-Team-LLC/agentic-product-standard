---
artifact_type: business-system-map
framework_version: 1.1.0
status: canonical
owner_module: ontology/ONTOLOGY.md
produced_by: [02-map-current-system]
---

# Business System Map

## Purpose

Describe how value is currently produced as a system: the business-system entities around the Capabilities in scope and their relations. Required from the Standard profile ([`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md)).

## Record

Entity semantics: [`ontology/ONTOLOGY.md`](../ontology/ONTOLOGY.md).

```yaml
system_map:
  outcome_ids: []
  value_streams: []        # Value Stream names; these are the values of value_stream_ids
  capabilities: []         # CAP-### (records in artifacts/capability-map.md)
  roles: []
  decisions: []
  processes: []
  data_assets: []
  knowledge_assets: []
  applications: []
  automations: []
  controls: []
  dependencies: []
  relations: []            # {from, relation, to}: from/to name elements above; relation as named in Rules (e.g. performed by)
```

How each Capability operates today is its CURRENT State in the Capability Map; this map shows how the Capabilities connect.

## Rules

The map is outcome-scoped. It is not a complete enterprise inventory. Only model elements relevant to the transformation boundary.

Relations are recorded in `relations`. Required relations, at minimum:

```text
Value Stream → uses → Capability
Capability → realized by → Process
Process → performed by → Role
Role → makes → Decision
Decision → uses → Data / Knowledge
Capability → supported by → Application
```

## Validation

- [ ] every element relates to an in-scope Outcome
- [ ] the required relations are present in `relations`
- [ ] Capabilities are referenced by `CAP-###`, not redefined
- [ ] the map describes the current system only, with no target-state solutions
