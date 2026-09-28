# Transition State Model

## 1. Purpose

AITM-SMB transforms an operating system through explicit intermediate states.

The target state is rarely reachable safely in one step.

A Transition State is a State of type TRANSITION ([`CORE_MODEL.md`](../CORE_MODEL.md) §3, §14): an intermediate state of the Capabilities it changes. The last state of a sequence reaches their Capability Target States; where a Target Operating Architecture exists, it is the system-level target.

---

## 2. State sequence

```text
Current State
→ Transition State 1
→ Transition State 2
→ ...
→ Capability Target States (integrated in the Target Operating Architecture, where one exists)
```

Each Transition State MUST be independently operable.

---

## 3. Transition State contract

Record contract: [`artifacts/transition-state.md`](../artifacts/transition-state.md) (extends the State record, [`CORE_MODEL.md`](../CORE_MODEL.md) §3).

Besides the State dimensions, a Transition State records its name, the Capabilities it changes, its predecessor and successor, an accountable owner, its mode, the changes it introduces, the evidence to collect, entry and exit conditions, and rollback or recovery.

Modes:

```text
CUTOVER   the new behavior replaces the old and controls production action (default)
SHADOW    the new behavior runs without controlling production action (§5)
PARALLEL  old and new systems coexist temporarily (§6)
```

---

## 4. Transition design principles

Prefer states that are:

```text
operable
observable
reversible where possible
bounded
measurable
safe under partial adoption
```

---

## 5. Shadow State

For high uncertainty, introduce a shadow state (`mode: SHADOW`):

```text
AI / new process runs
but does not control production action
```

Use it to evaluate:

```text
quality
latency
cost
policy compliance
exception rate
```

before authority increases.

---

## 6. Parallel State

Old and new systems may temporarily coexist (`mode: PARALLEL`).

This is justified when:

```text
migration risk is high
data conversion is uncertain
behavior requires comparison
rollback must remain possible
```

Parallel operation has cost and SHOULD be time-bounded (`time_bound`).

---

## 7. Authority transition

Authority MAY increase across states, for example:

```text
L1 — Suggest
→ L2 — Draft
→ L3 — Execute with explicit approval
→ L4 — Execute within bounded policy
```

Level labels and authority: [`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §2. The path is illustrative; every step follows the same rules:

- Authority SHOULD NOT jump directly to the maximum technically possible level.
- Each increase meets the criteria in [`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3 ((a) for a bounded pilot within the approved Authority Ceiling; (b) for an increase beyond pilot scope) and requires `HG-AUTHORITY` ([`STANDARD.md`](../STANDARD.md) §8), a Decision listing the `AUT-###` and stating the new level and scope.
- No state exceeds the approved Authority Ceiling ([`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §6).
- Record each authority change in `ai_changes` with the Autonomy Assessment and the levels before and after.

---

## 8. Transition-state failure

A Transition State is invalid if:

```text
the business cannot operate in it
ownership is ambiguous
critical metrics cannot be observed
failure cannot be contained
or exit conditions are undefined
```
