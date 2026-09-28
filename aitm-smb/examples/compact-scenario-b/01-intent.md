```yaml
artifact:
  type: transformation-intent
  id: scenario-b/01-intent
  framework_version: 1.1.0
  status: approved
  owner: Operations Director
  upstream: []
  downstream: [02-capabilities-and-current-state.md, 06-scorecard.md]
  evidence: [EVD-001, EVD-002, EVD-005]
  assumptions: [ASM-003]
  decisions: [DEC-001, DEC-002, DEC-003]
  open_questions: []
```

# Transformation Intent

Fictional, informative example (see [`examples/compact-scenario-b/README.md`](README.md)). Phase 0 (Frame): skills 36, 37 and 01. Contract: [`artifacts/transformation-intent.md`](../../artifacts/transformation-intent.md); Outcome record: [`CORE_MODEL.md`](../../CORE_MODEL.md) §1. "CU" means currency units; all numbers are illustrative.

Skill 36 recorded the profile Decision DEC-001 as `proposed` on 2026-03-04; skill 01 recorded the `HG-OUTCOME` Decision DEC-003 as `proposed` on 2026-03-05, listing OUT-001 and DEC-001 in its `subject_ids`. The Operations Director approved both on 2026-03-06. Skill 01 recorded a Metric for the Outcome's cost and one for its delay (MET-001, MET-002, in [`06-scorecard.md`](06-scorecard.md)). The `conformance` section was written by skill 38 at the end of the recorded run.

Baseline history: at `HG-OUTCOME` only the credit-note and freight part of the cost baseline, 3,100 CU a week, was measured (EVD-005). The handling and re-pick part, about 2,100 CU a week, was the estimate the Order Desk Lead stated with the Warehouse Lead at the kickoff: `[ASSUMPTION]` ASM-003, owned by the Order Desk Lead, with Evidence Debt due at the Phase 1 exit. The Phase 1 timed observation (EVD-002, 2026-03-20) validated ASM-003 and resolved that debt, so the approved baseline and target stand; the records below show the state after it.

```yaml
intent:
  id: ATI-001
  problem_statement: >-
    About one customer order in ten needs manual correction before it can be
    picked. Each order exception costs order-desk time, warehouse re-picks,
    credit notes and re-delivery freight, and about a third of them delay
    dispatch beyond the promised day.
  business_context: >-
    A 45-person wholesale distributor (fictional) handles about 1,200 customer
    orders a week in its order-to-delivery value stream, received through a web
    form (about 40%), by email or attachment (45%) and through sales reps (15%). Order entry, warehouse and
    invoicing run on three separate legacy systems, plus a shared order mailbox
    and a key-account spreadsheet. Why now: order volume grew about 20% in a
    year without more order-desk staff, and two key accounts complained
    formally about wrong deliveries in the first quarter.
  owner: Operations Director
  horizon: 2026-12-31
  outcomes:
    - id: OUT-001
      name: Cut the cost and the delay caused by order exceptions
      owner: Operations Director
      baseline: >-
        5,200 CU per week in exception cost (MET-001; credit notes and freight
        from finance records, handling and re-pick time from the Phase 1 timed
        observation) and 3.0% of all orders dispatched late because of an
        exception (MET-002), 12 weeks to 2026-02-20
      target: at most 2,600 CU per week and at most 1.0% of orders dispatched late because of an exception
      horizon: 2026-12-31
      metric_ids: [MET-001, MET-002]
      evidence_ids: [EVD-001, EVD-002, EVD-005]
      status: approved
  baseline_metric_ids: [MET-001, MET-002]
  constraints:
    - Key accounts keep ordering by email this year; no channel change is forced on them.
    - No change to prices, credit terms or customer contracts.
    - The order, warehouse and invoicing systems stay; changes are limited to configuration, fields and rules.
    - No additional order-desk headcount.
    - Customer data stays within the order desk's existing access; only names, delivery addresses and order contents are processed.
  non_goals:
    - replacing the order, warehouse or invoicing systems
    - redesigning warehouse picking and dispatch
    - pricing or credit decisions
    - reducing order-desk headcount
  known_risks:
    - Customers and sales reps may not adopt structured order notes.
    - Faster release of corrected orders may overload the afternoon pick wave.
  profile_decision_id: DEC-001
  evidence_ids: [EVD-001, EVD-005]
  assumption_ids: [ASM-003]
  conformance:
    framework_version: 1.1.0
    profiles: [Compact]
    validated_at: 2026-07-01
    validated_by: 38-audit-conformance, run by the agent for the Operations Director
    unresolved_exceptions: []
```

Why this is an Outcome and not a means: it names a business result (cost and delay) that matters whether or not any tool or AI is used ([`CORE_MODEL.md`](../../CORE_MODEL.md) §1). "Automate the order desk" or "use AI for emails" were raised in the kickoff and recorded as possible means, not as Outcomes.

Conformance notes (skill 38, 2026-07-01): the minimum valid path ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §6) and every [`CONFORMANCE.md`](../../CONFORMANCE.md) §1 item are traceable in this workspace; the trace check `python3 tools/validate.py --engagement examples/compact-scenario-b` passes. Every gated item used downstream is listed in an approved gate Decision naming the human; the one proposed gate Decision, DEC-011 (`HG-PROMOTION`), is reported in `open_gates`, and nothing downstream uses its subject. Every Assumption has a named business role as owner; no State, Gap or Outcome baseline rests on agent inference alone. The declaration is not approval of any gated decision ([`examples/compact-scenario-b/README.md`](README.md)).
