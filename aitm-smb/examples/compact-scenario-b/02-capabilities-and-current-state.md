```yaml
artifact:
  type: capability-map
  id: scenario-b/02-capabilities-and-current-state
  framework_version: 1.1.0
  status: reviewed
  owner: Operations Director
  upstream: [01-intent.md]
  downstream: [03-diagnosis.md, 05-target-and-roadmap.md]
  evidence: [EVD-001, EVD-002, EVD-003, EVD-005]
  assumptions: [ASM-003]
  decisions: [DEC-001, DEC-003, DEC-009]
  open_questions: []
```

# Capability Map and CURRENT State

Fictional, informative example (see [`examples/compact-scenario-b/README.md`](README.md)). Phase 1 (Observe): skills 02 and 11. Contract: [`artifacts/capability-map.md`](../../artifacts/capability-map.md); records: Capability [`CORE_MODEL.md`](../../CORE_MODEL.md) §2, State [`CORE_MODEL.md`](../../CORE_MODEL.md) §3.

One Capability is in scope. It passes the granularity test ([`diagnostics/CAPABILITY_DISCOVERY.md`](../../diagnostics/CAPABILITY_DISCOVERY.md) §4): a clear purpose, one owner, it affects OUT-001, and it can be assessed, improved and measured (MET-003, MET-004) independently of order capture and of the warehouse. It is named as an organizational ability, not after the order desk (a department) or the order system (a tool).

Profile re-check at the Phase 1 exit ([`PROFILE_SELECTION.md`](../../PROFILE_SELECTION.md) §6), 2026-03-20: one Capability, no system replacement, no sensitive data beyond names and delivery addresses, no second transformation or shared enabler in view. The answer DEC-001 marked `[OPEN]`, legal exposure through key-account delivery terms, is now answered: the Operations Director and the Finance Lead read the key-account contracts, which provide re-delivery and credit notes for wrong or late deliveries and nothing beyond them. Every Compact use-when condition still holds and no Governed or Portfolio condition does, so DEC-001 stands and no new profile Decision was needed.

Phase 1 exit: STA-001 rests on Evidence (EVD-001, EVD-002, EVD-003, EVD-005). The one estimate carried from Phase 0, ASM-003, was validated by EVD-002; no part of the State rests on agent inference.

## Capability

```yaml
capability:
  id: CAP-001
  name: Order exception resolution
  purpose: >-
    Detect, correct and release customer orders that cannot be fulfilled as
    entered, quickly and correctly, and stop recurring exception causes at the
    point of order entry.
  owner: Operations Director
  outcome_ids: [OUT-001]
  value_stream_ids: [order-to-delivery]   # the value-stream name used in ATI-001; Compact keeps no Business System Map
  current_state_id: STA-001
  target_state_id: STA-002
  metric_ids: [MET-003, MET-004]
  evidence_ids: [EVD-001, EVD-002, EVD-003]
  dependencies: []
  confidence: high
  boundary_notes: >-
    Includes how delivery instructions are captured at order entry, because that
    is where most exceptions start, and the handling of exception and change
    emails. Excludes pricing and credit checks, warehouse picking and dispatch
    (downstream, a separate ability) and invoicing. target_state_id was set in
    Phase 5 (DEC-009).
```

## CURRENT State

Observed 2026-03-09 to 2026-03-20. It describes the present only; no solutions.

```yaml
state:
  id: STA-001
  type: CURRENT
  capability_id: CAP-001
  as_of: 2026-03-20
  people: >-
    Five order-desk clerks enter and correct orders; two of them, the senior
    clerks, handle 83% of free-text exception emails. The Order Desk Lead
    supervises. The Warehouse Lead reports exceptions found at pick.
  decision_rights: >-
    Formally any clerk may correct and release an order. In practice ambiguous
    customer wording is left for the two senior clerks. Nobody owns the rules for
    what makes an order valid.
  process: >-
    Delivery instructions arrive as free-text notes on 18% of orders and are
    re-keyed by hand into three order fields. Exceptions are found at entry, at
    pick, or when the customer writes. Change and exception emails are handled
    first in, first out from the shared order mailbox; an email waits a median
    5.5 working hours before anyone opens it.
  data: >-
    One free-text note field per order. The exception log has a free-text reason
    that is blank on 40% of entries.
  knowledge: >-
    Customer conventions (substitutions, pack sizes, split deliveries, recurring
    phrasings) are tacit and held by the two senior clerks; the key-account
    spreadsheet is two years out of date.
  applications: >-
    Legacy order system (system of record for orders), separate warehouse and
    invoicing systems, a shared order mailbox with a general inbox and a
    key-account inbox, and the key-account spreadsheet. The mailbox and the
    order system are not linked.
  automation: price-list check at entry only; no check of notes, pack sizes or delivery dates
  ai: none (L0)
  controls: no check of note-driven fields before pick; errors are caught by the warehouse or by the customer
  metric_ids: [MET-001, MET-002, MET-003, MET-004, MET-005]
  economics: >-
    About 5,200 CU per week in exception cost - credit notes and re-delivery
    freight 3,100 (finance records, EVD-005), order-desk handling time about
    1,060 and warehouse re-picks about 1,040 (timed observation, EVD-002, at the
    Finance Lead's loaded rate of 35 CU an hour).
  feedback: exception causes are not recorded consistently and are not fed back to order entry or to customers
  evidence_ids: [EVD-001, EVD-002, EVD-003, EVD-005]
  assumption_ids: []
```
