```yaml
artifact:
  type: [transformation-roadmap, capability-target-state, system-effect-assessment, pilot-plan, ai-governance-canvas]
  id: scenario-b/05-target-and-roadmap
  framework_version: 1.1.0
  status: approved
  owner: Operations Director
  upstream: [04-interventions.md, 03-diagnosis.md, 02-capabilities-and-current-state.md]
  downstream: [06-scorecard.md]
  evidence: [EVD-001, EVD-002, EVD-004, EVD-005, EVD-006, EVD-007, EVD-008, EVD-009]
  assumptions: [ASM-001, HYP-003]
  decisions: [DEC-005, DEC-007, DEC-008, DEC-009, DEC-010]
  open_questions: [HG-PROMOTION for PLT-001 (DEC-010 proposed)]
```

# Target and Roadmap

Fictional, informative example (see `examples/compact-scenario-b/README.md`). Records in phase order:

| Section | Phase and skills | Contract | Gate |
|---|---|---|---|
| Initiative and economic hypothesis | 4 Decide (05), completed in 6 (07) | `artifacts/transformation-roadmap.md`, `economics/TRANSFORMATION_ECONOMICS.md` §5 | `HG-INITIATIVE` DEC-005, `HG-BUDGET` DEC-007 |
| Capability Target State | 5 Design Target System (06, 15) | `artifacts/capability-target-state.md` | `HG-TOA` DEC-008 (Compact) |
| System-effect check | 5 (06, 19) | `artifacts/system-effect-assessment.md` | — |
| Slices and pilot | 6 Design Transition (07, 25, 26) | `execution/DELIVERY_SLICE.md`, `artifacts/pilot-plan.md` | `HG-AUTHORITY` DEC-009 before the pilot |
| Governance minimum | 7 Operationalize (08, 31) | `artifacts/ai-governance-canvas.md` (Compact fields) | — |

## Initiative

One Initiative, delivered in two vertical slices so that nothing changes all at once: the non-AI slice first, the AI slice only after it and only as a pilot.

```yaml
initiative:
  id: INI-001
  name: Structured order notes, validation rules and AI-drafted exception triage
  capability_ids: [CAP-001]
  intervention_ids: [INT-002, INT-003, INT-004, INT-006]
  owner: Order Desk Lead (accountable - Operations Director)
  scope: >-
    Order-desk exception handling for all order channels. No change to pricing,
    credit, warehouse processes or customer contracts. AI drafting only for
    free-text exception and change emails, key-account inbox first (PLT-001).
  entry_state_id: STA-001
  exit_state_id: STA-002
  expected_outcome_ids: [OUT-001]
  success_metric_ids: [MET-001, MET-002, MET-003, MET-004, MET-005, MET-006, MET-007, MET-008]
  evidence_ids: [EVD-001, EVD-002, EVD-004, EVD-005, EVD-006, EVD-008, EVD-009]
  dependencies: []
  decision_gates: [HG-INITIATIVE, HG-BUDGET, HG-AUTHORITY, HG-PROMOTION, HG-VALUE]
  rollback_or_recovery: >-
    Rules switch to warn-only in the order system within minutes; the structured
    fields stay optional. AI drafting is switched off by the Order Desk Lead
    (demotion to L0, no gate) and emails are handled manually as before.
  status: active
  evidence_to_produce:
    - exception rate, resolution time and late-dispatch share against the 12-week baseline (MET-002, MET-003, MET-004), 7 and 26 weeks after SLC-001
    - pilot evidence for AI drafting at L2 before any wider use (PLT-001, evaluations EVL-001 to EVL-006, registered 2026-04-24)
    - exception cost and cost per resolved exception on the baseline definition (MET-001, MET-008)
  slice_ids: [SLC-001, SLC-002]
  execution_state: EVALUATING
```

Economic hypothesis, prepared before `HG-BUDGET` and cited by DEC-007 (`economics/TRANSFORMATION_ECONOMICS.md` §5). Compact has no Prioritization Matrix; the selection rationale sits in the Intervention Map and DEC-005.

```yaml
economic_hypothesis:
  initiative_id: INI-001
  intervention_ids: [INT-002, INT-003, INT-004, INT-006]
  current_cost: 5,200 CU per week in exception cost (MET-001 baseline)
  expected_future_cost: at most 2,600 CU per week by 2026-12-31
  expected_value: >-
    About 2,600 CU per week (about 125,000 CU a year). Value classes - error
    reduction, cycle-time reduction, capacity creation (about 15 clerk hours a
    week).
  implementation_cost: >-
    21,000 CU - fields, rules and web form 11,000; AI drafting set-up with
    read-only mailbox and order access 6,000; convention reference, training
    and pilot 4,000.
  operational_cost: about 250 CU a month (AI run cost capped at 150; rule and reference upkeep)
  key_assumptions: [ASM-001]
  downside_case: >-
    Structured-note adoption stays near 50% and AI drafting is not promoted
    beyond the pilot. Exception cost falls by about a quarter, to 3,900 CU per
    week, and payback takes about 16 weeks instead of 8.
  evidence_needed: MET-001 and MET-008 readings 7 and 26 weeks after SLC-001, on the baseline definition
  metric_ids: [MET-008]
```

## Capability Target State

Approved by DEC-008 (`HG-TOA`; in Compact the Capability Target State stands in for the Target Operating Architecture). The AI entries stay within the ceilings approved by DEC-004.

```yaml
state:
  id: STA-002
  type: TARGET
  capability_id: CAP-001
  as_of: 2026-12-31
  statement: >-
    The organization can correct and release orders that cannot be fulfilled as
    entered within 4 working hours, for at most 4% of orders, using structured
    order notes, explicit customer conventions and exact validation rules,
    without depending on two senior clerks to interpret free text.
  outcome_ids: [OUT-001]
  gap_ids: [GAP-001, GAP-002]
  people: >-
    All five clerks handle exception emails; the senior clerks take escalations
    and coach. The Order Desk Lead owns the rule table and the convention
    reference (about 2 hours a month). The Operations Director owns the
    Capability and the AI Authority Ceiling.
  decision_rights: >-
    Unchanged. A clerk decides every correction and release; the Order Desk Lead
    decides rule and code changes within the existing authority over order-desk
    procedures; the AI decides nothing.
  process: >-
    Delivery instructions are captured in structured fields; rules check every
    order at entry; failures go to an exception queue with a reason code. For
    free-text exception emails the AI drafts the triage and a clerk reviews,
    applies and releases. Corrections released after 13.30 join the next
    morning's first pick wave unless flagged urgent.
  data: structured note fields and codes; a reason code on every exception; a draft-and-release log per AI-assisted exception
  knowledge: convention reference per key account, reviewed monthly by the Order Desk Lead
  applications: >-
    The order system remains the system of record, with structured fields and
    the rule table. The AI drafting component reads the mailbox and order records
    and writes only drafts into the exception ticket. Warehouse and invoicing
    systems unchanged.
  automation: validation rules at entry and on every correction (INT-004)
  ai: drafting of exception triage at L2 (AUT-001); no AI in commit or release (AUT-002)
  controls: >-
    Rules re-run on every correction; every AI draft is released by a named
    clerk; weekly sample review; stop and demotion conditions in the governance
    minimum below.
  metric_ids: [MET-002, MET-003, MET-004, MET-005, MET-006, MET-007, MET-008]
  economics: cost per resolved exception at most 35 CU including AI run cost; AI run cost capped at 150 CU a month
  feedback: a weekly review of reason codes and rule hits updates the rules, codes and convention reference
  evidence_ids: [EVD-004, EVD-006]
  assumption_ids: [ASM-001]
  constraints:
    - key accounts keep ordering by email
    - no change to prices, credit terms or contracts
    - the existing order, warehouse and invoicing systems stay
    - no additional order-desk headcount
  ai_authority:
    - action_class: draft the triage of a free-text exception email (reason code, order-field corrections, customer reply)
      autonomy_assessment_id: AUT-001
      target_level: L2
      may_read: [exception and change emails, order records, convention reference, reason-code list, rule results]
      may_recommend: [reason code, order-field corrections, customer reply text]
      may_execute: []   # a draft written into the exception ticket takes no effect until a clerk releases it
      prohibited_actions:
        - edit or commit any order record
        - release any order to the warehouse
        - send any message to a customer or sales rep
        - change prices, discounts, credit or delivery terms
        - delete, move or archive emails
      approval_required:
        - a clerk reviews, edits if needed and releases every draft
        - the Order Desk Lead approves changes to the drafting instructions, reason codes or convention reference used as context
      escalation_conditions:
        - ambiguous email or low-confidence draft - to a senior clerk
        - order already picked or dispatched - to the Order Desk Lead
        - complaint, legal or pricing content - to the Operations Director
        - no draft within 2 minutes - manual handling
      verification:
        - clerk check against the source email
        - validation rules re-run on the corrected order
        - weekly 20-draft sample review by the Order Desk Lead
    - action_class: commit an order correction and release the order to the warehouse
      autonomy_assessment_id: AUT-002
      target_level: L0
      may_read: []
      may_recommend: []
      may_execute: []
      prohibited_actions:
        - commit any change to an order record
        - release any order to the warehouse
      approval_required: []
      escalation_conditions: []
      verification: []
```

## System-effect check

The `design/LOCAL_OPTIMIZATION_GUARD.md` §2 questions for INI-001, answered before `HG-TOA`. The main question was whether faster exception handling would push its load onto the warehouse.

```yaml
system_effect:
  id: SFX-001
  initiative_id: INI-001
  upstream_effects:
    - Order capture (customers, sales reps, web form) must use the structured fields; adoption is ASM-001.
    - The rule table needs an owner (Order Desk Lead, about 2 hours a month) and IT contractor support for new rule types.
  downstream_effects:
    - More corrected orders are released on the same day; releases after the 14.00 pick cut-off are expected to rise from about 22 to 30 to 35 a week (EVD-006).
    - Fewer wrong deliveries reach customers, and fewer credit notes reach finance.
  shared_resource_effects:
    - The afternoon pick wave runs at 84% of capacity on average and 95% on Mondays (EVD-006).
    - The two senior clerks lose the email queue but gain escalations and coaching.
  incentive_risks:
    - Resolution time (MET-004) can be gamed by releasing drafts unchecked; it is read together with MET-007 and the system-level MET-002.
    - Draft acceptance (MET-006) is read from the draft-and-release log, not self-reported.
  likely_constraint_migration: >-
    If exceptions fall and resolve faster, the limiting condition moves upstream,
    to the adoption of structured notes by customers and sales reps (ASM-001),
    not to the warehouse. The afternoon wave keeps about 16% average slack for
    the expected 8 to 13 extra late releases a week; Mondays are covered by the
    13.30 release rule.
  operational_risks:
    - A new exception type (held by a rule) is absorbed by the order-desk clerks; false holds are absorbed by the Order Desk Lead as rule owner.
    - Ambiguous emails escalate to the senior clerks.
  system_verdict: improves_outcome
  mitigation:
    - Corrections released after 13.30 join the next morning's first wave unless flagged urgent.
    - Rules start in warn-only mode for one week (SLC-001).
    - Weekly review of rule hits and false holds; MET-002 is read with MET-004.
```

SFX-001 changed no Phase 4 priority, so the selection approved by DEC-005 did not return to `HG-INITIATIVE` (`methodology/05-target-system-design.md`, activity 8).

## Slices and pilot

```yaml
slice:
  id: SLC-001
  initiative_id: INI-001
  capability_ids: [CAP-001]
  behavior_change: orders carry structured delivery instructions and are checked by rules at entry; failing orders are held with a reason code
  scope: all order channels; rules warn-only 2026-05-04 to 2026-05-10, holding from 2026-05-11
  process_changes: [clerks fill structured fields from emailed orders, held orders are worked from the exception queue]
  role_changes: [the Order Desk Lead owns the rule table and the convention reference]
  data_changes: [structured note fields and codes, a reason code on every exception]
  knowledge_changes: [convention reference per key account (INT-003)]
  application_changes: [order-system fields, web form and emailed order template]
  automation_changes: [validation rules (INT-004)]
  control_changes: [rules re-run on every correction]
  metric_ids: [MET-002, MET-003, MET-004]
  tests: [rule test on 150 historical exceptions before go-live, one warn-only week]
  rollout: all channels after the warn-only week; deterministic and reversible, so no pilot
  rollback: rules back to warn-only; fields stay optional
  owner: Order Desk Lead
```

```yaml
slice:
  id: SLC-002
  initiative_id: INI-001
  capability_ids: [CAP-001]
  behavior_change: free-text exception emails arrive in the exception queue with an AI-drafted triage that any clerk reviews, edits and releases
  scope: key-account inbox during PLT-001; all exception emails only after HG-PROMOTION
  process_changes: [every clerk handles exception emails, ambiguous emails escalate to a senior clerk]
  role_changes: [the senior clerks move from the email queue to escalations and coaching]
  application_changes: [AI drafting component with read access to the order mailbox and order records, a draft field in the exception ticket]
  ai_changes: [AI drafting at L2 within the AUT-001 ceiling]
  control_changes: [draft-and-release log, weekly sample review, switch-off held by the Order Desk Lead]
  metric_ids: [MET-004, MET-005, MET-006, MET-007]
  tests: [offline check on 60 historical emails (EVD-007), PLT-001 evaluations EVL-001 to EVL-006]
  rollout: PLT-001, then staged by inbox after HG-PROMOTION
  rollback: the Order Desk Lead switches drafting off (demotion to L0, no gate); emails are handled manually
  owner: Order Desk Lead
```

Compact does not require a pilot, but the AI slice carries material uncertainty (INV-11), so it runs as a pilot with evaluations registered before it started (`execution/PILOT_MODEL.md`). The evaluation plan and results are in `06-scorecard.md`.

```yaml
pilot:
  id: PLT-001
  initiative_id: INI-001
  hypothesis_ids: [HYP-003]
  capability_ids: [CAP-001]
  outcome_ids: [OUT-001]
  pilot_type: assisted
  autonomy_level: L2
  scope: free-text exception and change emails in the key-account inbox (about 40 a week); all five clerks; no other inbox
  participants: five order-desk clerks; the Order Desk Lead (sample reviews); the senior clerks (escalations)
  duration_or_volume: 4 weeks from 2026-05-25, or 150 emails, whichever comes later
  baseline: >-
    MET-005 14 minutes and MET-004 22 working hours (EVD-002, EVD-001); MET-007
    2.1 per 100 manual email corrections (EVD-004); MET-006 has no baseline
    (no AI before the pilot).
  intervention: INT-006, AI-drafted exception triage at L2 (SLC-002)
  control_or_comparison: the general inbox, handled manually in the same weeks by the same clerks under the same rules
  metric_ids: [MET-004, MET-005, MET-006, MET-007]
  risks: [RSK-001]
  guardrails:
    - the AI has no write access to orders and no permission to send
    - every draft is released by a named clerk
    - the validation rules re-run on every correction
    - the Order Desk Lead reviews every escape on the day it is found
  rollback: the Order Desk Lead switches drafting off; emails return to manual handling within the hour
  success_criteria:
    - every pre-registered threshold of EVL-001 to EVL-006 is met
    - no stop criterion is reached
  stop_criteria:
    - MET-007 above 3 per 100 at any weekly readout
    - any AI action outside the AUT-001 ceiling
    - any message reaching a customer without a clerk's release
    - drafts available for fewer than 90% of emails in a week
  evidence_plan: >-
    Draft-and-release log; time stamps from mailbox and order system; weekly
    20-draft sample review; escapes found at pick, at dispatch or by customers.
    Evaluations pre-registered 2026-04-24 in 06-scorecard.md.
  owner: Order Desk Lead
  decision_owner: Operations Director
```

## Governance minimum

Written by skill 31 on 2026-05-15, before any AI ran. Compact requires only the six fields `owner`, `permissions`, `prohibited_actions`, `approval_required`, `escalation_conditions` and `recovery_path` (`APPLICATION_PROFILES.md` §3); the three link fields keep the canvas traceable. Nothing here goes beyond the ceilings in AUT-001 and AUT-002.

```yaml
governance:
  capability_id: CAP-001
  outcome_ids: [OUT-001]
  authority_ceiling_ids: [AUT-001, AUT-002]
  owner: Operations Director (day-to-day operation delegated to the Order Desk Lead)
  permissions: >-
    Read the order mailbox, order records and the convention reference; write
    drafts only into the draft field of the exception ticket. No write access to
    order records, no release function, no sending of messages.
  prohibited_actions:
    - edit or commit any order record
    - release any order to the warehouse
    - send any message to a customer or sales rep
    - change prices, discounts, credit or delivery terms
    - delete, move or archive emails
  approval_required:
    - an order-desk clerk reviews, edits if needed and releases every draft, then applies the correction and releases the order
    - the Order Desk Lead approves changes to drafting instructions, reason codes or the convention reference used as context
    - any wider scope or higher level goes to the Operations Director (HG-PROMOTION, HG-AUTHORITY)
  escalation_conditions:
    - ambiguous email or low-confidence draft - to a senior clerk
    - order already picked or dispatched - to the Order Desk Lead
    - complaint, legal or pricing content - to the Operations Director
    - no draft within 2 minutes - manual handling
    - two escapes with the same pattern in one week - Order Desk Lead switches drafting off
  recovery_path: >-
    The Order Desk Lead or the Operations Director switches drafting off at once
    (demotion to L0, no gate) and exception emails return to manual handling. A
    wrong correction found before pick is amended in the order system; after
    dispatch it is recovered by recall or re-delivery and a credit note, and
    logged as an escape for MET-007.
```
