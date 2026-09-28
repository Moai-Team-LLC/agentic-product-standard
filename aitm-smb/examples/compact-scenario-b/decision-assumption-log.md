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
  assumptions: [ASM-001, ASM-002, ASM-003, HYP-001, HYP-002, HYP-003, HYP-004]
  decisions: [DEC-001, DEC-002, DEC-003, DEC-004, DEC-005, DEC-006, DEC-007, DEC-008, DEC-009, DEC-010, DEC-011]
  open_questions: [DEC-011 awaits the Operations Director (HG-PROMOTION)]
```

# Decision & Assumption Log

Fictional, informative example (see [`examples/compact-scenario-b/README.md`](README.md)). Contract: [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md). Semantics: Decision [`DECISION_MODEL.md`](../../DECISION_MODEL.md); gates [`STANDARD.md`](../../STANDARD.md) §8; Hypothesis and Cause [`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../../diagnostics/ROOT_CAUSE_ANALYSIS.md).

Every Decision below was first recorded by the skill that reached it, with `status: proposed`, `approved_by` empty and `date` the date proposed ([`AGENTS.md`](../../AGENTS.md) §4). The named person decided in a review meeting, and the approval updated the same record to `approved`, with `approved_by` and the approval `date`; no agent approved anything. Records show their current state; the proposal dates are in the table. The names are fictional role titles.

| Decision | Gate | Subject | Proposed (skill, date) | Approved by | Approved |
|---|---|---|---|---|---|
| DEC-001 | — | profile: Compact, no add-on | 36, 2026-03-04 | Operations Director, with `HG-OUTCOME` (DEC-003) | 2026-03-06 |
| DEC-002 | — | materiality thresholds | 01, 2026-03-05 | Operations Director | 2026-03-05 |
| DEC-003 | `HG-OUTCOME` | OUT-001, DEC-001 | 01, 2026-03-05 | Operations Director | 2026-03-06 |
| DEC-004 | — | HYP-003 accepted as testable (GAP-002) | 16 for 03, 2026-03-26 | Operations Director | 2026-03-27 |
| DEC-005 | `HG-AUTHORITY` | AUT-001 ceiling L2 | 14 for 04, 2026-04-02 | Operations Director | 2026-04-07 |
| DEC-006 | `HG-INITIATIVE` | INI-001 | 05, 2026-04-08 | Operations Director | 2026-04-10 |
| DEC-007 | — | INT-001 deferred; INT-005, INT-007 rejected | 05, 2026-04-08 | Operations Director | 2026-04-10 |
| DEC-008 | `HG-BUDGET` | INI-001 | 05, 2026-04-08 | Managing Director | 2026-04-10 |
| DEC-009 | `HG-TOA` | STA-002 | 06, 2026-04-15 | Operations Director | 2026-04-17 |
| DEC-010 | `HG-AUTHORITY` | AUT-001 current_level L0 to L2, PLT-001 scope | 34 for 08, 2026-05-20 | Operations Director | 2026-05-22 |
| DEC-011 | `HG-PROMOTION` | PLT-001 | 32 for 08, 2026-06-24 | open (proposed) | — |

DEC-004 is a Decision of the Capability and Outcome owner, not a gate ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../../diagnostics/ROOT_CAUSE_ANALYSIS.md) §7).

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
    Recorded by skill 36 from the Outcome owner's answers. Selection dimensions
    (APPLICATION_PROFILES.md section 2) - business criticality moderate (order
    errors cost money and two key accounts complained; no safety or regulatory
    consequence); one Capability expected (order exception resolution); systems -
    fields and rules in the existing order system, no replacement; AI authority
    low (no autonomy level proposed for any action class); financial impact
    moderate (about 5,200 CU a week); customer impact moderate (wrong or late
    deliveries, recoverable by re-delivery and credit notes); data sensitivity
    low (names, delivery addresses, order contents); regulatory exposure none
    known for wholesale order handling; irreversibility low (configuration and
    rules can be switched back); organizational change load low (five order-desk
    roles). Base (PROFILE_SELECTION.md section 2) - Compact, every Compact
    use-when condition holds. Governed - not added. No sensitive data, regulated
    process, high AI authority, material security exposure or irreversible action
    is in scope. Legal exposure is [OPEN] - whether the key-account contracts
    carry penalties for wrong or late delivery is not known yet. An unknown
    Governed condition counts as holding (section 4), but the Outcome owner
    records otherwise here - no contract term, price, credit or delivery
    commitment is in scope (ATI-001 constraints), and a change to what the
    business owes a customer triggers a new profile Decision; the contracts are
    checked by the Phase 1 exit. Portfolio - not added, one Capability and one
    expected Initiative, no shared enabler in contention. Measured - not added,
    the owner needs the effect on exception cost and delay, not a formally
    attributed value claim.
  evidence_ids: [EVD-001, EVD-005]
  assumption_ids: []
  consequences:
    - minimum content per APPLICATION_PROFILES.md section 3; no Business System Map, Diagnostic Record, Prioritization Matrix or Value Realization Report required
    - the selection is provisional until approved with HG-OUTCOME
  review_trigger: >-
    Re-check at the Phase 1 exit, including the [OPEN] legal-exposure answer,
    and whenever a second interdependent Capability, another system, sensitive
    data, a change to customer contract terms, or any proposal for AI above L2
    or for AI committing or releasing orders comes into scope.
  status: approved
  approved_by: Operations Director (Outcome owner), with HG-OUTCOME in DEC-003
  date: 2026-03-06
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
  alternatives:
    - no engagement thresholds; apply STANDARD.md section 16 case by case
    - a budget threshold of 10,000 CU
  rationale: >-
    Gives the agent and the order desk a shared test for which decisions go to
    the Operations Director. 5,000 CU is about one week of the current exception
    cost; a higher threshold would let a single slice pass without HG-BUDGET.
  evidence_ids: [EVD-005]
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
  statement: Approve OUT-001 with its baseline, target and horizon, and approve the profile Decision DEC-001 (Compact, no add-on).
  owner: Operations Director
  gate: HG-OUTCOME
  subject_ids: [OUT-001, DEC-001]
  alternatives:
    - a revenue Outcome for key accounts, rejected as too indirect for this engagement
    - an Outcome on the exception rate alone, rejected because it would not show the cost or the delay
  rationale: >-
    Exception cost and delay are measurable from existing records and matter
    independently of any tool. The credit-note and freight part of the cost
    baseline and the late-dispatch share are measured (EVD-001, EVD-005); the
    handling and re-pick part rests on ASM-003, the Order Desk Lead's estimate
    with the Warehouse Lead, with Evidence Debt due at the Phase 1 exit.
  evidence_ids: [EVD-001, EVD-005]
  assumption_ids: [ASM-003]
  consequences:
    - Phase 1 may start
    - the Compact profile is binding until a new profile Decision supersedes DEC-001
    - if the Phase 1 observation contradicts ASM-003, the baseline and target return to HG-OUTCOME
  review_trigger: order volume changes by more than 25%, or a key-account contract changes order channels
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-03-06
```

```yaml
decision:
  id: DEC-004
  statement: >-
    Accept HYP-003 as a testable cause of GAP-002 for intervention design. Its
    test is a same-period comparison of resolution time for email exceptions once
    interpretation no longer depends on the two senior clerks.
  owner: Operations Director
  gate:
  subject_ids: [HYP-003, GAP-002]
  alternatives:
    - continue diagnosis first, e.g. a two-week trial routing exception emails to all clerks without support
    - treat HYP-004 (waiting for customers) as the working cause
  rationale: >-
    Proposed by skill 16 in decisions_needed at the Phase 2 exit. The Evidence
    points at the interpretation queue - 83% of exception emails handled by two
    people, a median 5.5 working hours before first touch - and against waiting
    for customers, which held up 17% of exceptions (EVD-002, EVD-003). Whether the
    queue sets most of the resolution time can be confirmed only by changing who
    interprets, which is itself an intervention; an unsupported routing trial
    would mostly measure the clerks' missing conventions.
  evidence_ids: [EVD-002, EVD-003]
  assumption_ids: []
  consequences:
    - HYP-003 and the cause_status of GAP-002 become accepted_as_testable; GAP-002 is intervention-ready
    - every Intervention addressing HYP-003 comes with a test that could reject it
  review_trigger: the test result; evidence that most of the wait lies outside the order desk
  status: approved
  approved_by: Operations Director (Capability and Outcome owner)
  date: 2026-03-27
```

```yaml
decision:
  id: DEC-005
  statement: >-
    Set the Authority Ceiling of AUT-001 at L2 (Draft) - the AI may draft the
    triage of free-text exception and change emails in CAP-001 (reason code,
    order-field corrections, customer reply), for every inbox of the order
    mailbox, within the prohibited actions, approvals and escalation conditions
    recorded in AUT-001. This sets the ceiling only; the level in operation
    (current_level) stays L0 until a separate HG-AUTHORITY Decision grants it for
    a stated scope.
  owner: Operations Director
  gate: HG-AUTHORITY
  subject_ids: [AUT-001]
  alternatives:
    - ceiling L3, where the AI applies the correction and a clerk approves it with one click
    - no AI, ceiling L0
  rationale: >-
    Drafts are reversible, observable and checked by a clerk in about a minute
    (EVD-002). L3 would need write access to order records, which the order
    system cannot limit to note fields, and adds little because the clerk
    applies the correction in the same screen. Committing corrections and
    releasing orders stay prohibited AI actions; INT-007, which proposed them
    for AI, is class E (AIS-002) and was not proposed for selection, so no
    ceiling is set for that action class.
  evidence_ids: [EVD-002, EVD-004, EVD-005]
  assumption_ids: []
  consequences:
    - INT-006 may be selected in Phase 4, at L2 at most
    - any AI use first needs a grant of current_level through HG-AUTHORITY, for a stated scope
  review_trigger: three months of L2 operating evidence, or any repeated escape pattern
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-04-07
```

```yaml
decision:
  id: DEC-006
  statement: Select INI-001 for CAP-001, implementing INT-002, INT-003, INT-004 and INT-006.
  owner: Operations Director
  gate: HG-INITIATIVE
  subject_ids: [INI-001, INT-002, INT-003, INT-004, INT-006]
  alternatives:
    - non-AI slices only (INT-002, INT-003, INT-004), kept as the fallback if PLT-001 fails
    - two separate Initiatives for rules and AI drafting, rejected because the AI slice depends on the reason codes and the convention reference
  rationale: >-
    The selected Interventions address the validated cause HYP-001 and the cause
    HYP-003, accepted as testable in DEC-004, in challenge order - structure and
    rules first, AI only for the interpretation that rules cannot do, and only at
    L2, the ceiling DEC-005 approved. The AI slice follows the non-AI slice and
    runs as a pilot first. Decided with SFX-001 as skill 19 drafted it on
    2026-04-08 - upstream, the adoption of structured fields and an owner for the
    rules; downstream, more same-day releases and fewer wrong deliveries; the
    senior clerks' work shifting to escalations. No effect was found that
    degrades OUT-001; the load on the afternoon pick wave was unknown, with
    Evidence Debt due before HG-TOA.
  evidence_ids: [EVD-002, EVD-004]
  assumption_ids: [ASM-001, ASM-002]
  consequences:
    - INI-001 approved; the four Interventions set to selected
    - AI drafting runs only after the governance minimum and an HG-AUTHORITY Decision granting the level in operation for a stated scope
    - if the refined SFX-001 changes a priority, the selection returns to HG-INITIATIVE
  review_trigger: the refined SFX-001 (Phase 5); the PLT-001 result; ASM-001 below 50% at week 8
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-04-10
```

```yaml
decision:
  id: DEC-007
  statement: Defer INT-001 until the key-account contract renewals; reject INT-005 and INT-007.
  owner: Operations Director
  gate:
  subject_ids: [INT-001, INT-005, INT-007]
  alternatives:
    - keep the INT-005 second check for orders with notes as a stopgap until SLC-001 is live
    - redesign INT-007 at L3, with a clerk approving each AI commit and release
  rationale: >-
    INT-001 conflicts with the ATI-001 constraint that key accounts keep ordering
    by email. INT-005 addresses HYP-002, which the evidence rejected, and a
    second reader of the same ambiguous note does not remove the ambiguity.
    INT-007 is AI suitability class E (AIS-002), so AI must not be selected for
    it; it would need L4 for irreversible actions, and its gain over INT-006, at
    most about 280 CU a week of clerk time, is of the same order as the cost of
    wrong releases at the manual escape rate alone. An L3 redesign would need
    write permissions the order system cannot scope.
  evidence_ids: [EVD-002, EVD-004, EVD-005]
  assumption_ids: []
  consequences:
    - no second-person check and no autonomous correction or release
    - DEC-001 re-checked against its review trigger - with INT-007 rejected, no AI above L2 and no AI commit or release is in scope, so the Compact profile stands
  review_trigger: key-account contract renewals (INT-001); an order-system role that can limit write access to note fields (INT-007)
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-04-10
```

```yaml
decision:
  id: DEC-008
  statement: Commit 21,000 CU of implementation budget and up to 250 CU a month of operating cost for INI-001.
  owner: Managing Director
  gate: HG-BUDGET
  subject_ids: [INI-001]
  alternatives:
    - fund the non-AI slices only (15,000 CU)
  rationale: >-
    Cites the economic_hypothesis on INI-001 (05-target-and-roadmap.md,
    economics/TRANSFORMATION_ECONOMICS.md section 5) - exception cost 5,200 CU a
    week now, at most 2,600 expected, payback about 8 weeks. Downside case -
    structured-note adoption stays near 50% and AI drafting is not promoted;
    cost falls about a quarter, to 3,900 CU a week, and payback takes about 16
    weeks, still within the year.
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
  id: DEC-009
  statement: Approve STA-002 as the Capability Target State of CAP-001 (Compact, in place of a Target Operating Architecture).
  owner: Operations Director
  gate: HG-TOA
  subject_ids: [STA-002]
  alternatives:
    - a target without AI drafting (INT-002 to INT-004 only), kept as the fallback if PLT-001 fails
    - every correction released to the next morning's first pick wave, which protects the warehouse but gives up same-day dispatch
  rationale: >-
    STA-002 closes GAP-001 and GAP-002, keeps decision rights unchanged, and
    keeps AI within the DEC-005 ceiling. SFX-001, refined on 2026-04-15 with the
    pick-wave logs (EVD-006), shows no material negative system effect once the
    13.30 release rule applies, and changes no Phase 4 priority.
  evidence_ids: [EVD-004, EVD-006]
  assumption_ids: [ASM-001]
  consequences:
    - Phase 6 may cut the slices and design the pilot
    - no Decision Right changes, so HG-DECISION-RIGHTS is not triggered
  review_trigger: system effects outside the range predicted in SFX-001; ASM-001 invalidated
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-04-17
```

```yaml
decision:
  id: DEC-010
  statement: >-
    Raise AUT-001 current_level from L0 to L2 (Draft), within the DEC-005
    ceiling, for the PLT-001 scope only - free-text exception and change emails
    in the key-account inbox, from 2026-05-25 for four weeks or 150 emails,
    whichever comes later. A wider scope at L2 needs HG-PROMOTION; a higher
    level needs a new HG-AUTHORITY Decision.
  owner: Operations Director
  gate: HG-AUTHORITY
  subject_ids: [AUT-001, PLT-001]
  alternatives:
    - a shadow run at L0 first, with drafts hidden from clerks
  rationale: >-
    Pilot-grant criteria (governance/AUTHORITY_ESCALATION_MODEL.md section 3 (a)),
    checked by skill 34 - observability sufficient (every draft, edit and release
    is logged with the clerk's name, and the AI component has an access log);
    permissions bounded (read access and one writable draft field, no write to
    orders, no sending); recovery path defined (the governance minimum - the
    Order Desk Lead switches drafting off at once); stop criteria pre-registered
    (PLT-001, with its evaluations registered on 2026-04-24). The offline check
    found the right reason code in 50 of 60 historical emails (EVD-007). A shadow
    run was not chosen because the open question is how clerks work with drafts,
    which a shadow run cannot show.
  evidence_ids: [EVD-007]
  assumption_ids: []
  consequences:
    - skill 34 sets AUT-001 current_level to L2 and notes the PLT-001 scope in its rationale
    - closes the HG-AUTHORITY entry in the INI-001 decision_gates
    - the Order Desk Lead may switch drafting off at any time without a gate
  review_trigger: any PLT-001 stop criterion; the end of PLT-001
  status: approved
  approved_by: Operations Director (Outcome owner)
  date: 2026-05-22
```

The next Decision is proposed, not approved. Skill 32 recorded it when the pilot result was `PROMOTE`, so that the open gate is persisted; `approved_by` stays empty and `date` is the date proposed until the Operations Director decides.

```yaml
decision:
  id: DEC-011
  statement: >-
    Promote SLC-002 (AI-drafted exception triage at L2, AUT-001) from the PLT-001
    scope to all free-text exception emails, staged by inbox. The level stays L2
    within the DEC-005 ceiling; widening the scope at the same action class,
    level and ceiling is rollout (STANDARD.md section 8), so no HG-AUTHORITY
    Decision is needed.
  owner: Operations Director
  gate: HG-PROMOTION
  subject_ids: [PLT-001, EVL-001, EVL-002, EVL-003, EVL-004, EVL-005, EVL-006, SLC-002]
  alternatives:
    - revise and repeat the pilot on the general inbox
    - keep AI drafting in the key-account inbox only
    - stop AI drafting and keep the non-AI slice
  rationale: >-
    Pilot result PROMOTE - all six pre-registered thresholds met, two with
    limitations (EVL-004, EVL-005); no success criterion is unmet, so no waiver
    is recorded. The business-outcome and economics layers were not evaluated at
    pilot scale (not_evaluated in the plan), and the MET-001 reading is pending
    (Evidence Debt).
  evidence_ids: [EVD-008]
  assumption_ids: []
  consequences:
    - if approved, skill 08 plans the staged rollout with skill 29 and has skill 26 pre-register evaluations for the general inbox, whose customer mix the pilot did not cover (EVL-003, EVL-004 limitations)
    - the rollout gates of execution/ROLLOUT_MODEL.md section 3 are verified before each stage, including AUT-001 current_level L2 within its ceiling
  review_trigger: MET-007 above 3 per 100 in any rollout week, which leads to demotion to L0 by the Order Desk Lead
  status: proposed
  approved_by:
  date: 2026-06-24
```

## Hypotheses

Cause Hypotheses (`kind: cause`) for the Gaps in [`03-diagnosis.md`](03-diagnosis.md), each with its competing alternative; a rejected alternative cites the ruling Evidence in `evidence_against`. `confidence` is the strength of the Evidence behind the recorded status. A validated Cause keeps its ID.

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
    Same-period comparison once interpretation no longer depends on the two
    senior clerks (DEC-004). If the queue were not the cause, spreading
    interpretation - the convention reference plus AI drafts - would not shorten
    resolution. Run as PLT-001 against the manually handled general inbox; email
    exceptions resolved in a median 5.2 working hours against 11.4 (EVD-008).
  confidence: medium
  status: validated
```

HYP-003 was accepted as testable by DEC-004 on 2026-03-27 and validated on 2026-06-26 by skill 16, invoked by skill 03 after the pilot. Confidence stays medium because the two inboxes serve different customers.

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

Each Assumption is owned by the business role who stated it; agent inference would be a `[HYPOTHESIS]`, not an Assumption ([`AGENTS.md`](../../AGENTS.md) §3).

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
  evidence_ids: []
```

Stated by the Order Desk Lead in the Phase 4 review, after checking with the sales reps. Week 7 reading: 58% (EVD-009). The Assumption stays open until the week-8 decision point; if it is invalidated, DEC-006 and DEC-009 are reviewed (their review triggers).

```yaml
assumption:
  id: ASM-002
  statement: >-
    Without AI, the structured fields, the convention reference and the
    validation rules (INT-002 to INT-004) bring clerk time per free-text
    exception email down only to about 11 to 13 minutes, short of the 8-minute
    target, because every email must still be read, interpreted and re-keyed by
    hand.
  impact_if_wrong: >-
    If the non-AI Interventions alone reach about 8 minutes, AI drafting
    (INT-006) adds cost and risk without enough value (INV-05); SLC-002 is not
    promoted and the non-AI fallback of DEC-006 applies.
  validation_path: >-
    PLT-001 comparison - median clerk minutes per email in the manually handled
    general inbox, with the fields and rules live, against the pilot inbox in
    the same weeks (EVL-003).
  owner: Order Desk Lead
  status: validated
  evidence_ids: [EVD-008]
```

Stated by the Order Desk Lead in Phase 3, when skill 13 asked for the non-AI handling time for AIS-001; the estimate walks through the handling steps observed in EVD-002. Validated 2026-07-01 by skill 09: the manually handled general inbox took a median 13.1 minutes per email with the fields and rules in place (EVD-008). It serves smaller customers, for whom the convention reference is incomplete, so the reading may overstate the non-AI time for key-account emails; it still sits well above 8 minutes.

```yaml
assumption:
  id: ASM-003
  statement: >-
    Order-desk handling time and warehouse re-pick time for order exceptions cost
    about 2,100 CU a week at the Finance Lead's loaded rate of 35 CU an hour
    (about 1,060 handling, about 1,040 re-picks) in the 12 weeks to 2026-02-20.
  impact_if_wrong: >-
    The MET-001 baseline, and with it the OUT-001 target and the economic case,
    would be misstated.
  validation_path: two-week timed observation of exception handling and re-picks in Phase 1 (skills 02, 11)
  owner: Order Desk Lead
  status: validated
  evidence_ids: [EVD-002]
```

Stated by the Order Desk Lead with the Warehouse Lead at the Phase 0 kickoff and relied on by DEC-003, with Evidence Debt due at the Phase 1 exit. Validated on 2026-03-20 by the timed observation (EVD-002), which resolved that debt ([`evidence-register.md`](evidence-register.md)).

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

RSK-001 has not been accepted by anyone, so `HG-RISK` has not been triggered: the pilot ran with the controls above, not with an accepted residual risk. Running without one of these controls would be a risk acceptance and would need `HG-RISK`, whose Decision would list PLT-001 and RSK-001.
