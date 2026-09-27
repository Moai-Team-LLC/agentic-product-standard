---
artifact_type: business-system-map
framework_version: 1.0.0
status: canonical
---

# Business System Map

## Purpose

Describe how value is currently produced as a system.

## Scope

The map is outcome-scoped.

It is not a complete enterprise inventory.

## Structure

```yaml
system_map:
  outcome_ids: []
  value_streams: []
  capabilities: []
  roles: []
  decisions: []
  processes: []
  data_assets: []
  knowledge_assets: []
  applications: []
  automations: []
  controls: []
  dependencies: []
```

## Required relations

At minimum:

```text
Value Stream → uses → Capability
Capability → realized by → Process
Process → performed by → Role
Role → makes → Decision
Decision → uses → Data / Knowledge
Capability → supported by → Application
```

## Rule

Only model elements relevant to the transformation boundary.
