```yaml
artifact:
  type: decision-assumption-log
  id: scenario-b/decision-assumption-log
  framework_version: 1.1.0
  status: reviewed
  owner: Operations Director
  upstream: []
  downstream: [01-intent.md, 03-diagnosis.md, 04-interventions.md, 05-target-and-roadmap.md, 06-scorecard.md]
  evidence: [EVD-001, EVD-002, EVD-003, EVD-004, EVD-005, EVD-006, EVD-007, EVD-008, EVD-009]
  assumptions: [ASM-001, ASM-002, HYP-001, HYP-002, HYP-003, HYP-004]
  decisions: [DEC-001, DEC-002, DEC-003, DEC-004, DEC-005, DEC-006, DEC-007, DEC-008, DEC-009, DEC-010]
  open_questions: [DEC-010 awaits the Operations Director (HG-PROMOTION)]
```

# Decision & Assumption Log

Fictional, informative example (see `examples/compact-scenario-b/README.md`). Contract: `artifacts/decision-assumption-log.md`. Semantics: Decision `DECISION_MODEL.md`; gates `STANDARD.md` §8; Hypothesis and Cause `diagnostics/ROOT_CAUSE_ANALYSIS.md`.

Every gate approval below was given by the named person in a review meeting and recorded afterwards; no agent approved anything. The names are fictional role titles.

| Decision | Gate | Subject | Approved by | Date |
|---|---|---|---|---|
| DEC-001 | — | Compact profile | confirmed by DEC-003 | 2026-03-04 |
| DEC-002 | — | materiality thresholds | Operations Director | 2026-03-05 |
| DEC-003 | `HG-OUTCOME` | OUT-001, DEC-001 | Operations Director | 2026-03-06 |
| DEC-004 | `HG-AUTHORITY` | AUT-001 ceiling L2, AUT-002 ceiling L0 | Operations Director | 2026-04-07 |
| DEC-005 | `HG-INITIATIVE` | INI-001 | Operations Director | 2026-04-10 |
| DEC-006 | — | INT-001 deferred; INT-005, INT-007 rejected | Operations Director | 2026-04-10 |
| DEC-007 | `HG-BUDGET` | INI-001 | Managing Director | 2026-04-10 |
| DEC-008 | `HG-TOA` | STA-002 | Operations Director | 2026-04-17 |
| DEC-009 | `HG-AUTHORITY` | AUT-001 level in operation L0 to L2 | Operations Director | 2026-05-22 |
| DEC-010 | `HG-PROMOTION` | PLT-001 | open (proposed) | — |

## Decisions

```yaml
decision:
  id: DEC-001
  statement: Run the engagement under the Compact profile, with no add-on.
  owner: Operations Director
  gate:
  subject_ids: [ATI-001]
  alternatives:
    - Standard + Measured, the default when uncertain
    - Compact + Governed
  rationale: >-
    Base profile (PROFILE_SELECTION.md section 2) - every Compact use-when
    condition holds. One Capability (order exception resolution); limited system
    change (fields and rules in the existing order system); low AI authority (the
    Outcome owner intends no AI action above Draft; the review trigger covers any
    proposal beyond it); high reversibility (rules can switch to
    warn-only, AI can be switched off); five order-desk roles affected; moderate
    risk. Governed - not added: no regulated process, no sensitive data beyond
    names and delivery addresses, no irreversible action delegated to AI.
    Portfolio - not added: one Initiative. Measured - not added: the owner needs
    the effect on exception cost and delay, not a formally attributed value claim.
  evidence_ids: [EVD-001, EVD-005]
  assumption_ids: []
  consequences:
    - minimum content per APPLICATION_PROFILES.md section 3; no Business System Map, Prioritization Matrix or Value Realization Report
  review_trigger: >-
    Re-check at the Phase 1 exit, and whenever a second interdependent
    Capability, another system, sensitive data, or any proposal for AI above L2
    or for AI committing or releasing orders comes into scope.
  status: approved
  approved_by: Operations Director (Outcome owner), confirmed through DEC-003
  date: 2026-03-04
```

```yaml
decision:
  id: DEC-002
  statement: >-
    Materiality thresholds for this engagement (STANDARD.md section 16). An item
    is material when it involves a budget commitment above 5,000 CU, any AI
    authority above L0, a change that lets an order be committed or released or
    a message reach a customer without a person's release, or a change to
    prices, credit or contract terms. When unclear, treat the item as material.
  owner: Operations Director
  gate:
  subject_ids: [ATI-001]
  alternatives: []
  rationale: gives the agent and the order desk a shared test for which decisions go to the Operations Director
  evidence_ids: []
  assumption_ids: []
  consequences:
    - INI-001 is material (budget and AI authority), so HG-INITIATIVE and HG-BUDGET apply
    - wider use of AI drafting is material, so HG-PROMOTION applies to PLT-001
  review_trigger: any change of the Outcome owner or a budget above 50,000 CU
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-03-05
```

```yaml
decision:
  id: DEC-003
  statement: Approve OUT-001 with its baseline, target and horizon, and confirm the Compact profile (DEC-001).
  owner: Operations Director
  gate: HG-OUTCOME
  subject_ids: [OUT-001, DEC-001]
  alternatives:
    - a revenue Outcome for key accounts, rejected as too indirect for this engagement
  rationale: exception cost and delay are measurable from existing records (EVD-001, EVD-005) and matter independently of any tool
  evidence_ids: [EVD-001, EVD-005]
  assumption_ids: []
  consequences:
    - Phase 1 may start
    - the Compact profile is binding until a new profile Decision supersedes DEC-001
  review_trigger: order volume changes by more than 25%, or a key-account contract changes order channels
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-03-06
```

```yaml
decision:
  id: DEC-004
  statement: >-
    Approve the Authority Ceilings for AI in CAP-001. AUT-001 (drafting the
    triage of exception emails) at L2, Draft. AUT-002 (committing corrections and
    releasing orders) at L0, so no AI in commit or release. No AI action in
    CAP-001 may exceed L2. The level in operation stays L0 until a separate
    HG-AUTHORITY decision.
  owner: Operations Director
  gate: HG-AUTHORITY
  subject_ids: [AUT-001, AUT-002]
  alternatives:
    - ceiling L3 for AUT-002, where the AI prepares the commit and a clerk approves it
    - no AI at all, ceiling L0 for both action classes
  rationale: >-
    AUT-001 - drafts are reversible, observable and checked by a clerk in about a
    minute. AUT-002 - release is irreversible after pick, verification of intent
    is weak without a person, and write permissions cannot be scoped; L3 has no
    evidence behind it yet.
  evidence_ids: [EVD-002, EVD-004, EVD-005]
  assumption_ids: []
  consequences:
    - INT-007 cannot be selected as proposed (it needs L4)
    - INT-006 may be selected at L2 at most
  review_trigger: three months of L2 operating evidence, or any repeated escape pattern
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-04-07
```

```yaml
decision:
  id: DEC-005
  statement: Select INI-001 for CAP-001, implementing INT-002, INT-003, INT-004 and INT-006.
  owner: Operations Director
  gate: HG-INITIATIVE
  subject_ids: [INI-001, INT-002, INT-003, INT-004, INT-006]
  alternatives:
    - non-AI slices only (INT-002, INT-003, INT-004), kept as the fallback if PLT-001 fails
    - two separate Initiatives for rules and AI drafting, rejected because the AI slice depends on the reason codes and the convention reference
  rationale: >-
    The selected Interventions address the validated cause HYP-001 and the
    testable cause HYP-003 in challenge order - structure and rules first, AI
    only for the interpretation that rules cannot do, and only at L2. The AI
    slice follows the non-AI slice and runs as a pilot first.
  evidence_ids: [EVD-002, EVD-004]
  assumption_ids: [ASM-001, ASM-002]
  consequences:
    - INI-001 approved; the four Interventions set to selected
    - AI drafting runs only after the governance minimum and an HG-AUTHORITY decision on the level in operation
  review_trigger: the PLT-001 result; ASM-001 below 50% at week 8
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-04-10
```

```yaml
decision:
  id: DEC-006
  statement: Defer INT-001 until the key-account contract renewals; reject INT-005 and INT-007.
  owner: Operations Director
  gate:
  subject_ids: [INT-001, INT-005, INT-007]
  alternatives: []
  rationale: >-
    INT-001 conflicts with the ATI-001 constraint that key accounts keep ordering
    by email. INT-005 addresses HYP-002, which the evidence rejected. INT-007 is
    AI suitability class E (AIS-002) and needs L4 against a ceiling of L0
    (AUT-002, DEC-004); its gain over INT-006, at most about 280 CU a week of
    clerk time, is of the same order as the cost of wrong releases at the
    manual escape rate alone.
  evidence_ids: [EVD-002, EVD-004, EVD-005]
  assumption_ids: []
  consequences:
    - no second-person check and no autonomous correction or release
    - DEC-001 re-checked against its review trigger - with INT-007 rejected, no AI above L2 and no AI commit or release is in scope, so the Compact profile stands
  review_trigger: key-account contract renewals (INT-001); a re-assessment of AUT-002 (INT-007)
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-04-10
```

```yaml
decision:
  id: DEC-007
  statement: Commit 21,000 CU of implementation budget and up to 250 CU a month of operating cost for INI-001.
  owner: Managing Director
  gate: HG-BUDGET
  subject_ids: [INI-001]
  alternatives:
    - fund the non-AI slices only (15,000 CU)
  rationale: >-
    Economic hypothesis of INI-001 (05-target-and-roadmap.md) - exception cost
    5,200 CU a week now, at most 2,600 expected, payback about 8 weeks. Downside
    case - structured-note adoption stays near 50% and AI drafting is not
    promoted; cost falls about a quarter, to 3,900 CU a week, and payback takes
    about 16 weeks, still within the year.
  evidence_ids: [EVD-001, EVD-002, EVD-005]
  assumption_ids: [ASM-001]
  consequences:
    - AI run cost capped at 150 CU a month
    - spending beyond 21,000 CU needs a new HG-BUDGET decision
  review_trigger: spend reaches 80% of the budget; the MET-008 readings at 7 and 26 weeks
  status: approved
  approved_by: Managing Director (budget holder)
  date: 2026-04-10
```

```yaml
decision:
  id: DEC-008
  statement: Approve STA-002 as the Capability Target State of CAP-001 (Compact, in place of a Target Operating Architecture).
  owner: Operations Director
  gate: HG-TOA
  subject_ids: [STA-002]
  alternatives: []
  rationale: >-
    STA-002 closes GAP-001 and GAP-002, keeps decision rights unchanged, keeps AI
    within the ceilings of DEC-004, and SFX-001 shows no material negative
    system effect after mitigation.
  evidence_ids: [EVD-004, EVD-006]
  assumption_ids: [ASM-001]
  consequences:
    - Phase 6 may cut the slices and design the pilot
  review_trigger: system effects outside the range predicted in SFX-001; ASM-001 invalidated
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-04-17
```

```yaml
decision:
  id: DEC-009
  statement: >-
    Raise the level in operation of AUT-001 from L0 to L2 (Draft), within the
    DEC-004 ceiling, so that PLT-001 can run. Use stays limited to the PLT-001
    scope until HG-PROMOTION.
  owner: Operations Director
  gate: HG-AUTHORITY
  subject_ids: [AUT-001, PLT-001]
  alternatives:
    - a shadow run at L0 first, with drafts hidden from clerks
  rationale: >-
    The governance minimum is in place (05-target-and-roadmap.md), the pilot
    evaluations were registered on 2026-04-24, and the offline check found the
    right reason code in 50 of 60 historical emails (EVD-007). The AI cannot
    write to orders or send messages. A shadow run was not chosen because the
    open question is how clerks work with drafts, which a shadow run cannot show.
  evidence_ids: [EVD-007]
  assumption_ids: []
  consequences:
    - AUT-001 current_level L2 in the PLT-001 scope
    - the Order Desk Lead may switch drafting off at any time without a gate
  review_trigger: any PLT-001 stop criterion
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-05-22
```

The next Decision is proposed, not approved. It was recorded by skill 32 when the pilot result was `PROMOTE`, so that the open gate is visible; `approved_by` stays empty until the Operations Director decides.

```yaml
decision:
  id: DEC-010
  statement: >-
    Promote SLC-002 (AI-drafted exception triage at L2) from the PLT-001 scope
    to all free-text exception emails, staged by inbox.
  owner: Operations Director
  gate: HG-PROMOTION
  subject_ids: [PLT-001, SLC-002, EVL-001, EVL-002, EVL-003, EVL-004, EVL-005, EVL-006]
  alternatives:
    - revise and repeat the pilot on the general inbox
    - keep AI drafting in the key-account inbox only
    - stop AI drafting and keep the non-AI slice
  rationale: >-
    Pilot result PROMOTE - all six pre-registered thresholds met, two with
    limitations (EVL-004, EVL-005). The business-outcome and economics layers are
    not readable at pilot scale, and the MET-001 reading is pending (Evidence
    Debt). The level stays L2; only the scope widens.
  evidence_ids: [EVD-008]
  assumption_ids: []
  consequences:
    - if approved, the rollout is staged by inbox, with the rollout gates of execution/ROLLOUT_MODEL.md section 3 checked before each stage
  review_trigger: MET-007 above 3 per 100 in any rollout week, which leads to demotion to L0 by the Order Desk Lead
  status: proposed
  approved_by:
  date:           # set when decided; proposed 2026-06-24
```

## Hypotheses

Cause Hypotheses (`kind: cause`) for the Gaps in `03-diagnosis.md`. A validated Cause keeps its ID.

```yaml
hypothesis:
  id: HYP-001
  kind: cause
  statement: >-
    Delivery instructions arrive as free-text notes and are re-keyed by hand into
    order fields; ambiguous notes are misread or not applied, and nothing checks
    them before pick.
  gap_ids: [GAP-001]
  cause_class: INFORMATION
  alternative_hypothesis_ids: [HYP-002]
  evidence_for: [EVD-002, EVD-003, EVD-004]
  evidence_against: []
  test: >-
    Evidence test (diagnostics/ROOT_CAUSE_ANALYSIS.md section 4). If notes were
    not the cause, orders with and without notes would have similar exception
    rates; the sample shows about 38% against 3.4% (EVD-004), and the same notes
    were read differently by different clerks (EVD-002).
  confidence: high
  status: validated
```

```yaml
hypothesis:
  id: HYP-002
  kind: cause
  statement: Order-desk staff are careless or insufficiently trained, so they make entry errors.
  gap_ids: [GAP-001]
  cause_class: SKILL
  alternative_hypothesis_ids: [HYP-001]
  evidence_for: [EVD-003]
  evidence_against: [EVD-002, EVD-004]
  test: >-
    If carelessness were the cause, error rates would differ by clerk and tenure
    and would not concentrate on orders with notes. Per-clerk rates range from
    8.9% to 10.4% with no tenure effect, 71% of exceptions trace to notes
    (EVD-004), and different clerks misread the same ambiguous notes (EVD-002).
  confidence: high
  status: rejected
```

```yaml
hypothesis:
  id: HYP-003
  kind: cause
  statement: >-
    Free-text exception emails wait for the two senior clerks, the only people
    who can interpret customers' wording because the conventions are tacit; this
    interpretation queue, not the customer, sets most of the resolution time.
  gap_ids: [GAP-002]
  cause_class: KNOWLEDGE
  alternative_hypothesis_ids: [HYP-004]
  evidence_for: [EVD-002, EVD-003, EVD-008]
  evidence_against: []
  test: >-
    Accepted as testable at the Phase 2 exit (2026-03-27), with PLT-001 as the
    test. If the queue were not the cause, spreading interpretation (convention
    reference plus AI drafts) would not shorten resolution. In the pilot, email
    exceptions resolved in a median 5.2 working hours against 11.4 in the
    manually handled inbox in the same weeks (EVD-008). Validated 2026-07-01;
    confidence stays medium because the two inboxes serve different customers.
  confidence: medium
  status: validated
```

```yaml
hypothesis:
  id: HYP-004
  kind: cause
  statement: Exceptions resolve slowly because the order desk waits for answers from customers or sales reps.
  gap_ids: [GAP-002]
  cause_class: FLOW
  alternative_hypothesis_ids: [HYP-003]
  evidence_for: [EVD-003]
  evidence_against: [EVD-002]
  test: >-
    If waiting for answers dominated, most exceptions would wait on an outside
    reply. Only 17% did, and emails waited a median 5.5 working hours before
    anyone opened them (EVD-002). It contributes, but it is not the main cause.
  confidence: medium
  status: rejected
```

## Assumptions

```yaml
assumption:
  id: ASM-001
  statement: At least 70% of orders that carry delivery instructions will use the structured note fields within 8 weeks after SLC-001 starts holding orders (2026-05-11).
  impact_if_wrong: >-
    Note-driven misreadings continue, the exception rate stays above the 4%
    target, and the savings shrink toward the downside case of the economic
    hypothesis.
  validation_path: weekly share of orders with delivery instructions that use the fields, from the order-system export; decision point at week 8 (2026-07-06)
  owner: Order Desk Lead
  status: open
```

Week 7 reading: 58% (EVD-009). The Assumption stays open until the week-8 decision point; if it is invalidated, DEC-005 and DEC-008 are reviewed (their review triggers).

```yaml
assumption:
  id: ASM-002
  statement: >-
    Without AI, the structured fields, the convention reference and the
    validation rules (INT-002 to INT-004) bring clerk time per free-text
    exception email down only to about 11 to 13 minutes, short of the 8-minute
    target, because every email must still be read, interpreted and re-keyed by
    hand. Estimated in Phase 3 from the handling steps observed in EVD-002.
  impact_if_wrong: >-
    If the non-AI Interventions alone reach about 8 minutes, AI drafting
    (INT-006) adds cost and risk without enough value (INV-05); SLC-002 is not
    promoted and the non-AI fallback of DEC-005 applies.
  validation_path: >-
    PLT-001 comparison - median clerk minutes per email in the manually handled
    general inbox, with the fields and rules live, against the pilot inbox in
    the same weeks (EVL-003).
  owner: Order Desk Lead
  status: validated
```

Recorded by skill 13 for AIS-001; validated 2026-07-01 by skill 09. The manually handled general inbox took a median 13.1 minutes per email with the fields and rules in place (EVD-008). It serves smaller customers, for whom the convention reference is incomplete, so the reading may overstate the non-AI time for key-account emails; it still sits well above 8 minutes.

## Risks

```yaml
risk:
  id: RSK-001
  statement: >-
    A clerk releases a misread AI draft unchanged (automation bias), so a wrongly
    corrected order reaches the warehouse or the customer. Concerns INT-006,
    AUT-001 and PLT-001.
  owner: Order Desk Lead
  impact: financial and customer - typically 60 to 400 CU per event in credit notes and re-delivery (EVD-005), plus customer trust
  likelihood: medium
  controls:
    - L2 only; every draft is released by a named clerk (AUT-001)
    - the validation rules re-run on every correction (INT-004)
    - weekly 20-draft sample review, and a same-day review of every escape by the Order Desk Lead
    - PLT-001 stop criterion (MET-007 above 3 per 100) and immediate demotion to L0
  acceptance_decision_id:
  status: open
```

RSK-001 has not been accepted by anyone, so `HG-RISK` has not been triggered: the pilot ran with the controls above, not with an accepted residual risk. Running without one of these controls would be a risk acceptance and would need `HG-RISK`.
