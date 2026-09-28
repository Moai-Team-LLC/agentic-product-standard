```yaml
artifact:
  type: [intervention-map, ai-suitability-assessment, autonomy-assessment]
  id: scenario-b/04-interventions
  framework_version: 1.1.0
  status: approved
  owner: Operations Director
  upstream: [03-diagnosis.md]
  downstream: [05-target-and-roadmap.md]
  evidence: [EVD-002, EVD-004, EVD-005, EVD-007, EVD-008]
  assumptions: [ASM-001, ASM-002, HYP-001, HYP-002, HYP-003]
  decisions: [DEC-004, DEC-005, DEC-006, DEC-007, DEC-010]
  open_questions: []
```

# Intervention Map

Fictional, informative example (see [`examples/compact-scenario-b/README.md`](README.md)). Phase 3 (Design Interventions): skills 04, 13 and 14, 2026-03-30 to 2026-04-03. INT-007 was recorded as rejected in Phase 3 (class E); the other statuses and their rationale were set in Phase 4 by skill 05 after the Decisions of 2026-04-10. GAP-002 entered this phase through DEC-004 (HYP-003 accepted as testable). Contracts: [`artifacts/intervention-map.md`](../../artifacts/intervention-map.md) (record [`CORE_MODEL.md`](../../CORE_MODEL.md) §6), [`artifacts/ai-suitability-assessment.md`](../../artifacts/ai-suitability-assessment.md), [`artifacts/autonomy-assessment.md`](../../artifacts/autonomy-assessment.md). Families: [`design/INTERVENTION_PATTERNS.md`](../../design/INTERVENTION_PATTERNS.md).

Challenge order applied to both Gaps ([`STANDARD.md`](../../STANDARD.md) §5, [`DECISION_MODEL.md`](../../DECISION_MODEL.md) §1):

| Family | Question | Result |
|---|---|---|
| ELIMINATE | Can free-text notes be refused altogether? | INT-001, deferred: key accounts keep ordering by email (ATI-001 constraint) |
| SIMPLIFY | Fewer kinds of note? | folded into the code list of INT-002 |
| STANDARDIZE | Can notes become structured fields? | INT-002, selected |
| INSTRUMENT | Is missing measurement the problem? | partly: reason codes on every exception, delivered with INT-004 |
| INTEGRATE | Can the mailbox and order system be joined? | not now: emailed orders stay free text whatever the link; revisit with INT-001 |
| KNOWLEDGE | Can the senior clerks' conventions be made available to all? | INT-003, selected |
| AUTOMATION | Can deterministic rules catch the errors? | INT-004, selected, for form errors (pack sizes, dates, flags) |
| CONTROL | Would a second check help? | INT-005, rejected: addresses the rejected HYP-002 |
| AI_ASSIST | Does AI add value beyond the above? | INT-006, selected at L2: interpreting free-text emails is what rules cannot do |
| AI_AUTOMATE | Can AI complete a bounded step on its own inside the workflow? | not proposed separately: the reason code and field changes matter only as part of a correction a clerk checks, so they stay drafts in INT-006 |
| AI_AUGMENT | Would continuous AI prediction or recommendation help, e.g. flagging orders likely to fail? | not proposed: INT-004 already holds every order that fails an exact check at entry; what remains is interpreting free text (INT-006) |
| AI_AUTONOMIZE | Does autonomy add value beyond assistance? | INT-007, rejected: class E (AIS-002), so not carried into Phase 4 |

Profile re-check (DEC-001 review trigger, [`PROFILE_SELECTION.md`](../../PROFILE_SELECTION.md) §6), at the Phase 3 exit on 2026-04-03 and again before the Phase 4 gates: INT-007 proposed AI committing and releasing orders, an irreversible action, and INT-006 adds an AI drafting component. INT-007 is class E, so it was rejected and never proposed for selection (confirmed by DEC-007). The highest autonomy level proposed for any action class is L2 (AUT-001), which [`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md) §2 classes as low AI authority, and INT-006 is one bounded component with read access and a single writable draft field inside the existing systems. Every Compact use-when condition still holds and no Governed condition does, so DEC-001 stands and no new profile Decision was needed.

## Interventions

```yaml
intervention:
  id: INT-001
  gap_ids: [GAP-001, GAP-002]
  hypothesis_ids: [HYP-001]
  type: ELIMINATE
  description: >-
    Stop accepting free-text delivery notes; all orders and changes only through
    the web form with structured fields.
  expected_effect: removes most note-driven exceptions and most exception emails
  simpler_alternatives_considered: []
  risks:
    - key accounts refuse the channel change
    - some order volume moves to competitors
  assumption_ids: []
  status: deferred
  required_context: n/a
  required_actions: customer communication and contract changes with key accounts
  required_permissions: n/a
  verification: n/a
  status_rationale: >-
    Conflicts with the ATI-001 constraint that key accounts keep ordering by
    email this year. Revisit at the key-account contract renewals (DEC-007).
```

```yaml
intervention:
  id: INT-002
  gap_ids: [GAP-001, GAP-002]
  hypothesis_ids: [HYP-001]
  type: STANDARDIZE
  description: >-
    Replace the free-text note with structured fields in the order system, the
    web form and the emailed order template (delivery window, split delivery
    allowed, substitution allowed, pack-size exception), plus a short code list
    for the remaining cases. Clerks fill the same fields from emailed orders.
  expected_effect: most note-driven misreadings disappear; exception rate moves from 9.6% toward 4%
  simpler_alternatives_considered: [INT-001]
  risks:
    - customers and sales reps keep writing free text (ASM-001)
  assumption_ids: [ASM-001]
  status: selected
  required_context: the note types found in the cause-coded sample (EVD-004)
  required_actions: configure fields and codes; update web form and order template; brief clerks and sales reps
  required_permissions: order-system configuration by the IT support contractor
  verification: share of orders with delivery instructions that use the fields (ASM-001); exception rate MET-003
  status_rationale: addresses the validated cause HYP-001 directly; cheap and reversible (DEC-006)
```

```yaml
intervention:
  id: INT-003
  gap_ids: [GAP-002, GAP-001]
  hypothesis_ids: [HYP-003, HYP-001]
  type: KNOWLEDGE
  description: >-
    Write down the customer conventions the two senior clerks hold
    (substitutions, pack sizes, split deliveries, recurring phrasings) as a
    one-page reference per key account, owned and reviewed monthly by the Order
    Desk Lead.
  expected_effect: all five clerks can handle exception emails; recurring phrasings are read the same way by everyone
  simpler_alternatives_considered: []
  risks:
    - the reference goes stale without an owner
  assumption_ids: []
  status: selected
  required_context: interviews and shadowing of the two senior clerks
  required_actions: capture, review with sales reps, publish to the order desk
  required_permissions: none beyond the order desk's current access
  verification: share of exception emails handled by clerks other than the two senior clerks
  status_rationale: needed on its own to spread the email work, and as the context INT-006 drafts from (DEC-006)
```

```yaml
intervention:
  id: INT-004
  gap_ids: [GAP-001]
  hypothesis_ids: [HYP-001]
  type: AUTOMATION
  description: >-
    Deterministic validation rules at order entry and on every correction -
    pack-size multiples per product, delivery-date feasibility per delivery
    zone, split and substitution flags against the customer's contract terms.
    An order that fails is held in an exception queue with a reason code.
  expected_effect: form errors are caught at entry instead of at pick; every exception carries a reason code
  simpler_alternatives_considered: [INT-002, INT-005]
  risks:
    - false holds on contracts that allow exceptions
    - rule-table upkeep load
  assumption_ids: []
  status: selected
  required_context: product pack sizes, delivery zones and contract flags from the order system
  required_actions: build the rule table; test on 150 historical exceptions; one warn-only week
  required_permissions: order-system rule configuration by the IT support contractor; rule changes approved by the Order Desk Lead
  verification: weekly review of rule hits and false holds by the Order Desk Lead
  status_rationale: these checks are exact rules, so deterministic logic suffices and AI is not needed (INV-05) (DEC-006)
```

```yaml
intervention:
  id: INT-005
  gap_ids: [GAP-001]
  hypothesis_ids: [HYP-002]
  type: CONTROL
  description: A second clerk checks every order that carries a note before release, plus refresher training for all clerks.
  expected_effect: fewer misreadings reach the warehouse
  simpler_alternatives_considered: []
  risks:
    - roughly doubles handling time for 18% of orders
    - adds to the queue in front of the senior clerks
  assumption_ids: []
  status: rejected
  required_context: n/a
  required_actions: n/a
  required_permissions: n/a
  verification: n/a
  status_rationale: >-
    Addresses HYP-002, which the evidence rejected (EVD-004); a second reader of
    the same ambiguous note does not remove the ambiguity (EVD-002) (DEC-007).
```

```yaml
intervention:
  id: INT-006
  gap_ids: [GAP-002]
  hypothesis_ids: [HYP-003]
  type: AI_ASSIST
  description: >-
    For each free-text exception or change email, an AI component drafts a
    reason code, the proposed order-field corrections and a reply to the
    customer, using the email, the order record (read only) and the convention
    reference (INT-003). An order-desk clerk reviews, edits if needed, applies
    the correction and releases; the validation rules (INT-004) re-run on the
    corrected order.
  expected_effect: >-
    Handling time per email from 14 to at most 8 minutes; email work no longer
    queues for the two senior clerks; resolution time moves toward 4 hours.
  simpler_alternatives_considered: [INT-001, INT-002, INT-003, INT-004]
  risks: [RSK-001]
  assumption_ids: [ASM-002]
  status: selected
  required_context: email text and attachments, order record, convention reference, reason-code list
  required_actions: draft reason code, field corrections and customer reply into the exception ticket
  required_permissions: read the order mailbox and order records; write only to the draft field of the exception ticket
  verification: >-
    A clerk reviews every draft before release; the validation rules re-run;
    weekly sample review; pre-registered evaluations EVL-001 to EVL-006.
  status_rationale: >-
    AIS-001 class B. After INT-002 to INT-004, free-text emails still need
    interpretation, which deterministic rules cannot provide. Its Authority
    Ceiling, AUT-001 at L2, was approved by DEC-005 on 2026-04-07, before the
    selection; selected with INI-001 (DEC-006).
```

```yaml
intervention:
  id: INT-007
  gap_ids: [GAP-002]
  hypothesis_ids: [HYP-003]
  type: AI_AUTONOMIZE
  description: >-
    An AI agent reads exception emails, corrects the order record and releases
    the order to the warehouse on its own, escalating only the cases it judges
    uncertain.
  expected_effect: near-zero clerk time for email exceptions; release within minutes
  simpler_alternatives_considered: [INT-006]
  risks:
    - a wrong release is irreversible once the order is picked or dispatched
    - a systematic misreading repeats across many orders before anyone sees it
    - needs write access to order records that the order system cannot limit to note fields
  assumption_ids: []
  status: rejected
  required_context: as INT-006
  required_actions: commit order changes; release orders to the warehouse
  required_permissions: write access to order records and the release function
  verification: none before pick except the validation rules, which check form, not customer intent
  status_rationale: >-
    AIS-002 class E (verification limits and execution risk), so AI must not be
    selected for it (diagnostics/AI_SUITABILITY.md section 5). It was not carried
    into Phase 4 and has no Autonomy Assessment; committing and releasing orders
    stay prohibited AI actions in the AUT-001 ceiling. Its gain over INT-006 is
    at most the clerk time INT-006 is expected to leave, about 8 minutes per
    email or 280 CU a week, which is of the same order as the cost of wrong
    releases at the manual escape rate alone (DEC-007).
```

## AI Suitability Assessments

One per `AI_*` candidate ([`diagnostics/AI_SUITABILITY.md`](../../diagnostics/AI_SUITABILITY.md)), by skill 13. A class is a finding about fit, not a selection and not authority. A dimension that does not apply is `not_relevant`, with the reason in its note.

```yaml
ai_suitability:
  id: AIS-001
  intervention_id: INT-006
  gap_ids: [GAP-002]
  simpler_alternatives_considered: [INT-001, INT-002, INT-003, INT-004]
  non_ai_alternative: >-
    INT-003 with INT-004 lets all five clerks handle emails and catches form
    errors, but every free-text email must still be read, interpreted and
    re-keyed by hand. [ASSUMPTION] ASM-002, the Order Desk Lead's estimate from
    the handling steps observed in EVD-002 - about 11 to 13 minutes per email,
    short of the 8-minute target and of the resolution-time target.
  semantic_load: high - customers describe changes in their own words ("same as last time but no pallets")
  input_variability: high - dozens of writing styles, forwarded threads, attachments
  judgment_requirement: medium - mapping wording to a reason code and field changes; the final judgment stays with the clerk
  knowledge_intensity: medium - needs the convention reference (INT-003) and the order record
  interaction_requirement: low - no dialogue; the reply is a draft the clerk sends
  prediction_requirement: not_relevant - nothing is forecast; the task interprets the email in hand
  generation_requirement: medium - draft field changes and a short customer reply
  probabilistic_tolerance: medium - tolerable because every draft is reviewed and the rules re-run; not tolerable without review
  verification_feasibility: high - a clerk compares draft and email in about a minute; rules re-check the corrected order
  recoverability: high - nothing takes effect before a clerk releases it; a wrong draft is discarded
  context_readiness: medium - order records and the reference exist for key accounts; conventions of smaller customers are incomplete
  data_sensitivity: medium - customer names, delivery addresses and order contents; no payment data
  execution_risk: low - the AI executes nothing
  economic_frequency: high - about 60 free-text exception emails a week, every working day (EVD-002)
  classification: B
  rationale: >-
    Hybrid fit. Interpreting unstructured, variable customer wording is an
    AI-positive signal (diagnostics/AI_SUITABILITY.md section 3); the exact
    checks stay deterministic (INT-004) and the fields structured (INT-002). The
    AI part is selectable for the interpretation step only; authority is
    assessed separately in AUT-001. Economic value - at a median 14 minutes the
    emails take about 14 clerk hours a week and queue for two people (EVD-002);
    cutting handling to 8 minutes frees about 6 hours a week, and spreading the
    work removes the queue.
  evidence_ids: [EVD-002, EVD-004]
  assumption_ids: [ASM-002]
```

```yaml
ai_suitability:
  id: AIS-002
  intervention_id: INT-007
  gap_ids: [GAP-002]
  simpler_alternatives_considered: [INT-006]
  non_ai_alternative: INT-002 to INT-004 without AI, or INT-006 with a clerk releasing every correction
  semantic_load: high - same input as AIS-001
  input_variability: high - same input as AIS-001
  judgment_requirement: high - the agent would also decide whether its reading of an ambiguous email is good enough to act on
  knowledge_intensity: medium - as AIS-001
  interaction_requirement: low - as AIS-001
  prediction_requirement: not_relevant - as AIS-001
  generation_requirement: medium - as AIS-001
  probabilistic_tolerance: low - a released wrong order is not an acceptable probabilistic outcome at this volume
  verification_feasibility: low - without a human, nothing checks customer intent before pick; the rules check form only
  recoverability: low - after pick or dispatch, recovery needs recall, re-delivery and a credit note (EVD-005)
  context_readiness: medium - as AIS-001
  data_sensitivity: medium - as AIS-001, plus write access to order records
  execution_risk: high - commits order changes and releases goods
  economic_frequency: high - the same about 60 emails a week as AIS-001
  classification: E
  rationale: >-
    AI contraindicated for this candidate as defined: verification limits and
    execution risk make autonomous correction and release unsuitable. Economic
    value - the saving over INT-006 is at most the 8 clerk minutes per email
    INT-006 is expected to leave, about 280 CU a week at the Finance Lead's
    loaded rate of 35 CU an hour. That is of the same order as the cost of wrong
    releases at the manual escape rate alone - about 1.3 a week at 60 to 400 CU
    each (EVD-004, EVD-005) - before any rise from removing the human check.
    Recorded as rejected with this class as rationale
    (diagnostics/AI_SUITABILITY.md section 5); no Autonomy Assessment follows.
  evidence_ids: [EVD-002, EVD-004, EVD-005]
  assumption_ids: []
```

## Autonomy Assessments and Authority Ceilings

One per action class of each `AI_*` candidate proposed for selection (skill 14; [`methodology/03-intervention-design.md`](../../methodology/03-intervention-design.md), activity 4). INT-006 is the only one, with one action class; INT-007, class E, gets none. Skill 14, invoked by skill 04, recorded the `HG-AUTHORITY` Decision for the proposed ceiling as `proposed` on 2026-04-02, and Phase 3 exited with that gate open; INT-006 was selected only after DEC-005 approved the ceiling on 2026-04-07. DEC-010 (`HG-AUTHORITY`, via skill 34) later raised the level in operation from L0 to L2 for the pilot scope only. Commit and release stay human actions.

```yaml
autonomy:
  id: AUT-001
  capability_id: CAP-001
  intervention_id: INT-006
  action_class: draft the triage of a free-text exception email (reason code, order-field corrections, customer reply)
  recommended_level: L2
  current_level: L2
  reversibility: high - a draft has no effect until a clerk releases it
  financial_impact: low - none directly; indirect only through a released wrong draft (RSK-001)
  customer_impact: medium - a released wrong correction or reply reaches the customer
  legal_impact: low - prices, credit and contract terms are excluded
  security_impact: low - read-only access to mailbox and orders; no send permission; the only write is the draft field of the exception ticket
  safety_impact: not_relevant - no safety-relevant goods or actions in scope
  decision_ambiguity: medium - about one email in fifteen is ambiguous even to the senior clerks (EVD-002)
  policy_clarity: medium - reason codes and conventions are explicit for key accounts, incomplete for smaller customers
  observability: high - every draft, edit and release is logged with the clerk's name
  verification: high - the clerk checks the draft against the email; the rules re-run
  exception_detectability: medium - rules catch form errors; intent errors show at pick or through the customer
  recovery: high - discard the draft, or amend the order before pick
  permission_precision: high - read access plus one writable draft field
  maximum_allowed_level: L2
  prohibited_actions:
    - edit or commit any order record
    - release any order to the warehouse
    - send any message to a customer or sales rep
    - change prices, discounts, credit or delivery terms
    - delete, move or archive emails
  approval_required:
    - an order-desk clerk reviews, edits if needed and releases every draft
    - the Order Desk Lead approves changes to the drafting instructions, reason codes or convention reference used as context
  escalation_conditions:
    - the email is ambiguous or the draft is marked low confidence - to a senior clerk
    - the order is already picked or dispatched - to the Order Desk Lead
    - complaint, legal or pricing content - to the Operations Director
    - no draft within 2 minutes - manual handling
  owner: Operations Director
  promotion_recommendation: retain
  rationale: >-
    Assistance is sufficient to remove the interpretation queue. L3 would add
    little because the clerk applies the correction in the same screen, and it
    would need write access to order records, which the order system cannot
    limit to note fields; L2 is the approved ceiling (DEC-005). current_level
    L2 since DEC-010 (2026-05-22), set by skill 34 for the PLT-001 scope - the
    key-account inbox; wider use at L2 waits for HG-PROMOTION (DEC-011). Pilot
    evidence (EVD-008) supports keeping L2; skill 34 (for skill 09, 2026-07-01)
    recommends retain, and no increase is proposed.
  evidence_ids: [EVD-002, EVD-007, EVD-008]
  assumption_ids: []
```
