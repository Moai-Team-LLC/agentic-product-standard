```yaml
artifact:
  type: [transformation-roadmap, system-effect-assessment, capability-target-state, pilot-plan, ai-governance-canvas]
  id: scenario-b/05-target-and-roadmap
  framework_version: 1.1.0
  status: approved
  owner: Operations Director
  upstream: [04-interventions.md, 03-diagnosis.md, 02-capabilities-and-current-state.md]
  downstream: [06-scorecard.md]
  evidence: [EVD-001, EVD-002, EVD-004, EVD-005, EVD-006, EVD-007, EVD-008, EVD-009]
  assumptions: [ASM-001, HYP-003]
  decisions: [DEC-005, DEC-006, DEC-008, DEC-009, DEC-010, DEC-011]
  open_questions: [HG-PROMOTION for PLT-001 (DEC-011 proposed)]
```

# Target and Roadmap

Fictional, informative example (see [`examples/compact-scenario-b/README.md`](README.md)). Records in phase order:

| Section | Phase and skills | Contract | Gate |
|---|---|---|---|
| Initiative, with its economic hypothesis and operation minimum | 4 Decide (05), completed in 6 (07), `operation` in 7 (08) | [`artifacts/transformation-roadmap.md`](../../artifacts/transformation-roadmap.md), [`economics/TRANSFORMATION_ECONOMICS.md`](../../economics/TRANSFORMATION_ECONOMICS.md) §5 | `HG-INITIATIVE` DEC-006, `HG-BUDGET` DEC-008 |
| System-effect check | 4 (05 invoking 19), refined in 5 (06 invoking 19 and 24) | [`artifacts/system-effect-assessment.md`](../../artifacts/system-effect-assessment.md) | drafted before DEC-006, refined before DEC-009 |
| Capability Target State | 5 Design Target System (06, 15) | [`artifacts/capability-target-state.md`](../../artifacts/capability-target-state.md) | `HG-TOA` DEC-009 (Compact) |
| Transformation Slices | 6 Design Transition (07) | roadmap `slices`, record [`execution/DELIVERY_SLICE.md`](../../execution/DELIVERY_SLICE.md) §2 | — |
| Pilot | 6 (07, 25, 26); run in 7 (08, 34, 32) | [`artifacts/pilot-plan.md`](../../artifacts/pilot-plan.md) | `HG-AUTHORITY` DEC-010 before it, `HG-PROMOTION` DEC-011 after it |
| Governance minimum | 7 Operationalize (08, 31) | [`artifacts/ai-governance-canvas.md`](../../artifacts/ai-governance-canvas.md) (Compact fields) | — |

## Initiative

One Initiative, delivered in two vertical slices so that nothing changes all at once: the non-AI slice first, the AI slice only after it and only as a pilot.

Skill 05 created INI-001 on 2026-04-08 with `status: proposed` and its economic hypothesis, and invoked skill 19 for SFX-001 before the selection was decided. DEC-006 (`HG-INITIATIVE`) and DEC-008 (`HG-BUDGET`) approved it on 2026-04-10. DEC-008 cites the economic hypothesis as [`economics/TRANSFORMATION_ECONOMICS.md`](../../economics/TRANSFORMATION_ECONOMICS.md) §5 specifies: INI-001 in `subject_ids`, its key assumption ASM-001 in `assumption_ids`, its downside case in `rationale`. Compact has no Prioritization Matrix; the selection rationale sits in the Intervention Map and DEC-006. Skill 07 completed the record in Phase 6 (slices, decision gates, evidence plan, rollback); skill 25 placed the pilot's authority grant in `decision_gates` as a planned `HG-AUTHORITY` entry naming AUT-001. Skill 08 added `operation` in Phase 7, on 2026-04-30, before SLC-001's warn-only week, and extended it for SLC-002 on 2026-05-15. The Initiative has been `active` since SLC-001 went live.

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
  decision_gates:
    - gate: HG-INITIATIVE      # DEC-006, approved
      subject_ids: [INI-001]
    - gate: HG-BUDGET          # DEC-008, approved
      subject_ids: [INI-001]
    - gate: HG-AUTHORITY       # planned pilot grant, AUT-001 from L0 to L2 for PLT-001; closed by DEC-010
      subject_ids: [AUT-001]
    - gate: HG-PROMOTION       # DEC-011, proposed
      subject_ids: [PLT-001]
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
  operation:
    operating_owner: Order Desk Lead, for the fields, the rules, the convention reference and AI drafting (accountable - Operations Director)
    observability_signal: >-
      Weekly review by the Order Desk Lead of the exception log - exception rate
      (MET-003), resolution time (MET-004), rule hits, false holds and reason
      codes - and, while AI drafting runs, of the draft-and-release log (MET-006),
      the escapes and the access log of the AI component (MET-007). Adoption
      signals - structured-field use (MET-009), and the share of exception emails
      handled by clerks other than the two senior clerks (INT-003).
    support_path: >-
      A clerk asks a senior clerk (ambiguous emails, coaching), then the Order
      Desk Lead (false holds, rule and code changes, switching drafting off), who
      calls the IT support contractor for the order-system fields and rules and
      the AI drafting component.
    role_changes:
      - the Order Desk Lead owns the rule table and the convention reference (about 2 hours a month)
      - every clerk handles exception emails; the senior clerks move from the email queue to escalations and coaching
    failure_or_rollback_path: >-
      Rules switch to warn-only within minutes and the fields stay optional. The
      Order Desk Lead or the Operations Director switches AI drafting off at once
      (demotion to L0, no gate) and emails return to manual handling. A wrong
      correction found before pick is amended in the order system; after dispatch
      it is recovered by recall or re-delivery and a credit note, and logged as an
      escape for MET-007.
    adoption:
      training: >-
        A one-hour briefing for all clerks before each slice goes live; a note and
        a call for sales reps and key accounts on the fields and the order template.
      support: >-
        The senior clerks coach the other clerks on exception emails; questions on
        the fields and the rules go along the support path.
      feedback: >-
        Clerks flag wrong holds and wrong drafts in the exception ticket, and the
        weekly review updates the rules, the codes and the convention reference.
      adoption_metric_ids: [MET-009]
```

`operation` is the Compact Phase 7 minimum ([`artifacts/transformation-roadmap.md`](../../artifacts/transformation-roadmap.md)), recorded here instead of an Operating Model, Observability Plan and Adoption Plan. Adoption is defined in `adoption`, as the Phase 7 exit requires, with MET-009 as its adoption metric ([`06-scorecard.md`](06-scorecard.md)).

## System-effect check

Skill 05 invoked skill 19 on 2026-04-08, once INI-001 existed, to answer the [`design/LOCAL_OPTIMIZATION_GUARD.md`](../../design/LOCAL_OPTIMIZATION_GUARD.md) §2 questions before `HG-INITIATIVE`. The draft answered every question from the Evidence then available and marked one effect `unknown`: whether faster releases would overload the afternoon pick wave, with Evidence Debt due before `HG-TOA` ([`evidence-register.md`](evidence-register.md)). The Operations Director decided DEC-006 with that draft in hand. In Phase 5, skill 06 invoked skill 19 to refine the same record with the Warehouse Lead's pick-wave logs (EVD-006) and skill 24 to audit it, on 2026-04-15: the debt was resolved and the 13.30 release rule became a mitigation. The record below is the refined one.

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
  evidence_ids: [EVD-002, EVD-006]
  assumption_ids: [ASM-001]
```

The refinement changed no Phase 4 priority, so the selection approved by DEC-006 did not return to `HG-INITIATIVE` ([`methodology/05-target-system-design.md`](../../methodology/05-target-system-design.md), activity 8).

## Capability Target State

Designed by skill 15 for skill 06 and approved by DEC-009 (`HG-TOA`; in Compact the Capability Target State stands in for the Target Operating Architecture). The AI entry stays within the ceiling approved by DEC-005. Committing corrections and releasing orders have no AI entry: they stay human actions, prohibited to AI in the AUT-001 ceiling.

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
  ai: drafting of exception triage at L2 (AUT-001); no AI in committing corrections or releasing orders
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
```

## Transformation Slices

Cut by skill 07 in Phase 6 and held here, in the roadmap's `slices` section ([`execution/DELIVERY_SLICE.md`](../../execution/DELIVERY_SLICE.md) §2); the Pilot Plan below does not repeat them. No Experiment records were needed.

```yaml
slices:
  - id: SLC-001
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
    rollout: all channels after the warn-only week, with the INI-001 operation minimum in place; deterministic and reversible, so no pilot
    rollback: rules back to warn-only; fields stay optional
    owner: Order Desk Lead
  - id: SLC-002
    initiative_id: INI-001
    capability_ids: [CAP-001]
    behavior_change: free-text exception emails arrive in the exception queue with an AI-drafted triage that any clerk reviews, edits and releases
    scope: key-account inbox during PLT-001; all exception emails only after HG-PROMOTION
    process_changes: [every clerk handles exception emails, ambiguous emails escalate to a senior clerk]
    role_changes: [the senior clerks move from the email queue to escalations and coaching]
    application_changes: [AI drafting component with read access to the order mailbox and order records, a draft field in the exception ticket]
    ai_changes: [AI drafting at L2 within the AUT-001 ceiling; the level in operation rises from L0 only through the HG-AUTHORITY entry in INI-001 decision_gates]
    control_changes: [draft-and-release log, weekly sample review, switch-off held by the Order Desk Lead]
    metric_ids: [MET-004, MET-005, MET-006, MET-007]
    tests: [offline check on 60 historical emails (EVD-007), PLT-001 evaluations EVL-001 to EVL-006]
    rollout: PLT-001, then staged by inbox after HG-PROMOTION, with evaluations for inboxes the pilot did not cover registered before each stage
    rollback: the Order Desk Lead switches drafting off (demotion to L0, no gate); emails are handled manually
    owner: Order Desk Lead
```

## Pilot

Compact does not require a pilot, but the AI slice carries material uncertainty (INV-11), so it runs as a pilot with evaluations registered before it started ([`execution/PILOT_MODEL.md`](../../execution/PILOT_MODEL.md)). Skill 25 designed PLT-001 for skill 07 on 2026-04-22, and skill 26 registered its evaluations on 2026-04-24 ([`06-scorecard.md`](06-scorecard.md)). The authority grant it needs, AUT-001 from L0 to L2, was only planned in Phase 6. In Phase 7 skill 08 invoked skill 34, which checked the pilot-grant criteria ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../../governance/AUTHORITY_ESCALATION_MODEL.md) §3 (a)) and recorded DEC-010 as `proposed` on 2026-05-20. The Operations Director approved it on 2026-05-22, and skill 34 set AUT-001 `current_level` to L2 for this scope before the pilot started on 2026-05-25.

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
    2.1 per 100 manual email corrections (EVD-004); MET-006 baseline none
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

Written by skill 31 for skill 08 on 2026-05-15, before any AI ran. Compact requires only the six Governance-minimum fields `owner`, `permissions`, `prohibited_actions`, `approval_required`, `escalation_conditions` and `recovery_path` ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md) §3); the link fields `capability_id`, `outcome_ids` and `authority_ceiling_ids` are always filled. Nothing here goes beyond the AUT-001 ceiling. No AI Change records are kept: AI Change Control is a Governed requirement.

```yaml
governance:
  capability_id: CAP-001
  outcome_ids: [OUT-001]
  authority_ceiling_ids: [AUT-001]
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
    - a wider scope at L2 goes to the Operations Director as rollout (HG-PROMOTION); any higher level needs HG-AUTHORITY
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
