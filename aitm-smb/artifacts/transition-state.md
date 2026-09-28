---
artifact_type: transition-state
framework_version: 1.1.0
status: canonical
entity: State
id_prefix: STA
owner_module: transition/TRANSITION_STATE_MODEL.md
produced_by: [07-build-roadmap, 21-design-transition-states]
---

# Transition State

## Purpose

Describe an independently operable intermediate state between the Current State and the Capability Target States, and what changes to reach it.

## Record

Record contract: State [`CORE_MODEL.md`](../CORE_MODEL.md) §3, with `type: TRANSITION` and `as_of` set to the intended horizon. The State dimensions describe how the Capabilities operate in this state; the `*_changes` fields list what changes from the predecessor.

Extends `state` with:

```yaml
state:
  name:
  capability_ids: []          # every Capability this state changes; capability_id names the primary one
  predecessor:                # STA-###: previous TRANSITION State, or the CURRENT State(s) for the first
  successor:                  # STA-###: next TRANSITION State, or the TARGET State(s) for the last
  owner:                      # role accountable for operating in this state
  mode: CUTOVER | SHADOW | PARALLEL    # transition/TRANSITION_STATE_MODEL.md §3
  time_bound:                 # end date or volume; expected when mode is PARALLEL
  capability_changes: []
  role_changes: []
  decision_right_changes: []  # BDS-### changed
  process_changes: []
  data_changes: []
  application_changes: []
  ai_changes: []              # authority changes: AUT-###, action class, level before and after (L0–L5)
  governance_changes: []
  evidence_to_collect: []
  entry_conditions: []
  exit_conditions: []
  rollback_or_recovery:
```

## Rules

Every Transition State MUST be independently operable ([`transition/TRANSITION_STATE_MODEL.md`](../transition/TRANSITION_STATE_MODEL.md) §2).

An authority increase in `ai_changes` stays within the approved Authority Ceiling and takes effect only through a Decision closing `HG-AUTHORITY` that lists its `AUT-###` ([`transition/TRANSITION_STATE_MODEL.md`](../transition/TRANSITION_STATE_MODEL.md) §7).

## Validation

- [ ] `type: TRANSITION`; `capability_id` and, when several, `capability_ids` name the Capabilities it changes
- [ ] valid per [`transition/TRANSITION_STATE_MODEL.md`](../transition/TRANSITION_STATE_MODEL.md) §8: operable, `owner` named, critical Metrics observable (`metric_ids`), failure containable, exit conditions defined
- [ ] `predecessor` and `successor` link the sequence from the CURRENT to the TARGET States
- [ ] a SHADOW or PARALLEL `mode` is justified; a PARALLEL state has a `time_bound`
- [ ] every authority increase names its Autonomy Assessment and levels, within the approved Authority Ceiling
- [ ] rollback or recovery defined
