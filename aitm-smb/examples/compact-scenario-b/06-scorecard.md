```yaml
artifact:
  type: [transformation-scorecard, evaluation-plan]
  id: scenario-b/06-scorecard
  framework_version: 1.1.0
  status: draft
  owner: Operations Director
  upstream: [01-intent.md, 05-target-and-roadmap.md, evidence-register.md]
  downstream: []
  evidence: [EVD-001, EVD-002, EVD-004, EVD-005, EVD-008, EVD-009]
  assumptions: [ASM-001]
  decisions: [DEC-003, DEC-007, DEC-010]
  open_questions:
    - HG-PROMOTION for PLT-001 (DEC-010 proposed)
    - MET-001 and MET-008 readings after the June finance close (Evidence Debt)
```

# Transformation Scorecard

Fictional, informative example (see `examples/compact-scenario-b/README.md`). Contracts: `artifacts/transformation-scorecard.md` (Metric record `METRICS.md` §6) and `artifacts/evaluation-plan.md` (Evaluation record `evaluation/EVALUATION_SYSTEM.md` §4). The baselines MET-001 and MET-002 were recorded in Phase 0 (skill 01); the other Metrics were appended when defined; the observations and the effect conclusion were written by skill 09 on 2026-07-01; the pilot results by skill 32 on 2026-06-24.

## Metrics

```yaml
metric:
  id: MET-001
  name: Weekly cost of order exceptions
  class: outcome
  owner: Operations Director
  definition: >-
    Credit notes and re-delivery freight coded "order error", plus order-desk
    handling time and warehouse re-pick time for exceptions valued at a loaded
    rate of 35 CU an hour; CU per week.
  source: finance credit-note and freight records (EVD-005); exception log (EVD-001); handling and re-pick times (EVD-002)
  baseline: 5,200 CU per week, 12 weeks to 2026-02-20 (3,100 measured; 2,100 of time components estimated)
  target: at most 2,600 CU per week by 2026-12-31
  cadence: monthly, after the finance close
  outcome_ids: [OUT-001]
  capability_ids: [CAP-001]
  initiative_ids: [INI-001]
```

```yaml
metric:
  id: MET-002
  name: Orders dispatched late because of an exception
  class: outcome
  owner: Operations Director
  definition: orders dispatched after the promised day that had an exception, divided by all orders, per week
  source: exception log joined with the warehouse dispatch log
  baseline: 3.0% of orders, 12 weeks to 2026-02-20 (EVD-001)
  target: at most 1.0% by 2026-12-31
  cadence: weekly
  outcome_ids: [OUT-001]
  capability_ids: [CAP-001]
  initiative_ids: [INI-001]
```

```yaml
metric:
  id: MET-003
  name: Exception rate
  class: capability
  owner: Order Desk Lead
  definition: orders needing manual correction before pick, divided by all orders, per week
  source: exception log (reason codes from SLC-001 onward)
  baseline: 9.6%, 12 weeks to 2026-02-20 (EVD-001)
  target: at most 4.0% by 2026-12-31
  cadence: weekly
  outcome_ids: [OUT-001]
  capability_ids: [CAP-001]
  initiative_ids: [INI-001]
```

```yaml
metric:
  id: MET-004
  name: Exception resolution time
  class: capability
  owner: Order Desk Lead
  definition: median working hours from detection (rule hold, email receipt or warehouse report) to release, per week
  source: exception log time stamps; mailbox receipt times
  baseline: 22 working hours, 12 weeks to 2026-02-20 (EVD-001)
  target: at most 4 working hours by 2026-12-31
  cadence: weekly
  outcome_ids: [OUT-001]
  capability_ids: [CAP-001]
  initiative_ids: [INI-001]
```

```yaml
metric:
  id: MET-005
  name: Clerk minutes per free-text exception email
  class: operating
  owner: Order Desk Lead
  definition: median active minutes from opening the email to releasing the corrected order and the reply
  source: observation for the baseline (EVD-002); ticket and order-system time stamps from SLC-002 onward
  baseline: 14 minutes (EVD-002)
  target: at most 8 minutes by 2026-12-31
  cadence: weekly during the pilot, then monthly
  outcome_ids: []
  capability_ids: [CAP-001]
  initiative_ids: [INI-001]
```

```yaml
metric:
  id: MET-006
  name: AI draft acceptance
  class: ai_evaluation
  owner: Order Desk Lead
  definition: share of AI drafts released with the same reason code and no changed order field, read from the draft-and-release log
  source: draft-and-release log
  baseline: none - no AI component before the pilot (explicit baseline gap)
  target: at least 80%
  cadence: weekly
  outcome_ids: []
  capability_ids: [CAP-001]
  initiative_ids: [INI-001]
```

```yaml
metric:
  id: MET-007
  name: Wrong-correction escapes and out-of-ceiling actions
  class: risk_governance
  owner: Order Desk Lead
  definition: >-
    Corrections made from an email that are later found wrong (at pick, at
    dispatch or by the customer) per 100 corrected emails; plus the count of AI
    actions outside the AUT-001 ceiling, from the access log.
  source: exception log, customer complaints, access log of the AI component
  baseline: 2.1 per 100 manual email corrections (EVD-004); out-of-ceiling actions not applicable before AI
  target: not above the manual baseline; zero out-of-ceiling actions
  cadence: weekly
  outcome_ids: [OUT-001]
  capability_ids: [CAP-001]
  initiative_ids: [INI-001]
```

```yaml
metric:
  id: MET-008
  name: Cost per resolved exception
  class: economic
  owner: Operations Director
  definition: MET-001 weekly cost plus AI run cost, divided by the exceptions resolved in the week
  source: MET-001 sources; AI run-cost statement
  baseline: 46 CU (5,200 CU for about 114 exceptions a week)
  target: at most 35 CU by 2026-12-31
  cadence: monthly, after the finance close
  outcome_ids: [OUT-001]
  capability_ids: [CAP-001]
  initiative_ids: [INI-001]
```

## Pilot evaluation plan and results

Registered on 2026-04-24, before PLT-001 started; the plan fields were not changed afterwards. Layers not evaluated in the pilot: business outcome and economics, because 163 emails over four weeks are too few for a cost or late-dispatch reading; both are read at Initiative level in the scorecard below (MET-001, MET-002, MET-008).

```yaml
evaluation_plan:
  initiative_id: INI-001
  pilot_id: PLT-001
  owner: Order Desk Lead
  registered_on: 2026-04-24
  evaluations:
    - id: EVL-001
      initiative_id: INI-001
      layer: ai_task
      metric_ids: [MET-006]
      method: compare each AI draft with the released version (reason code and order fields)
      sample: all pilot emails, at least 150
      threshold: at least 80% released without material edit
      owner: Order Desk Lead
    - id: EVL-002
      initiative_id: INI-001
      layer: human_ai
      metric_ids: [MET-006]
      method: weekly sample of 20 released drafts - source email opened before release (log), wrong drafts edited, escalation conditions honoured
      sample: 80 released drafts over four weeks
      threshold: at least 95% of sampled releases show the source email opened; every sampled email meeting an escalation condition escalated
      owner: Order Desk Lead
    - id: EVL-003
      initiative_id: INI-001
      layer: operating
      metric_ids: [MET-005]
      method: median active minutes per email from ticket and order time stamps, pilot inbox against the general inbox in the same weeks
      sample: all pilot emails and all general-inbox exception emails in the pilot weeks
      threshold: at most 9 minutes in the pilot inbox
      owner: Order Desk Lead
    - id: EVL-004
      initiative_id: INI-001
      layer: capability
      metric_ids: [MET-004]
      method: median resolution time of email-originated exceptions, pilot inbox against the general inbox in the same weeks
      sample: all email-originated exceptions in the pilot weeks
      threshold: at most 6 working hours in the pilot inbox
      owner: Operations Director
    - id: EVL-005
      initiative_id: INI-001
      layer: risk_governance
      metric_ids: [MET-007]
      method: trace every escape found at pick, at dispatch or by customers to its draft; review the access log weekly for any write or send by the AI component
      sample: all pilot emails
      threshold: at most 2.1 escapes per 100 and zero actions outside the ceiling
      owner: Order Desk Lead
    - id: EVL-006
      initiative_id: INI-001
      layer: technical
      metric_ids: []
      method: time from mailbox receipt to draft in the ticket; fallbacks to manual handling logged
      sample: all pilot emails
      threshold: draft within 2 minutes for at least 98% of emails
      owner: Order Desk Lead
  datasets: []   # Compact: no evaluation dataset required; the 60 emails of the offline check (EVD-007) are not a registered dataset
```

```yaml
results:
  - evaluation_id: EVL-001
    actual: 83% (136 of 163 drafts released without material edit)
    conclusion: PASS
    limitations: key-account emails only; material edit judged by the log diff
    evidence_ids: [EVD-008]
    recorded_on: 2026-06-24
  - evaluation_id: EVL-002
    actual: 78 of 80 sampled releases (97.5%) show the source email opened; 11 of 11 escalation cases escalated
    conclusion: PASS
    limitations: clerks knew the sample was reviewed
    evidence_ids: [EVD-008]
    recorded_on: 2026-06-24
  - evaluation_id: EVL-003
    actual: 8.6 minutes in the pilot inbox; 13.1 minutes in the general inbox
    conclusion: PASS
    limitations: four weeks; the general inbox has a different customer mix
    evidence_ids: [EVD-008]
    recorded_on: 2026-06-24
  - evaluation_id: EVL-004
    actual: 5.2 working hours in the pilot inbox; 11.4 in the general inbox
    conclusion: PASS_WITH_LIMITATIONS
    limitations: key accounts write more regular emails than other customers, so part of the difference may be customer mix
    evidence_ids: [EVD-008]
    recorded_on: 2026-06-24
  - evaluation_id: EVL-005
    actual: 2 escapes in 163 emails (1.2 per 100); zero writes or sends by the AI component
    conclusion: PASS_WITH_LIMITATIONS
    limitations: with 163 emails the uncertainty range still includes the manual baseline of 2.1
    evidence_ids: [EVD-008]
    recorded_on: 2026-06-24
  - evaluation_id: EVL-006
    actual: 161 of 163 drafts (98.8%) within 2 minutes; 2 manual fallbacks during a mailbox outage
    conclusion: PASS
    limitations: none material
    evidence_ids: [EVD-008]
    recorded_on: 2026-06-24
pilot_result: PROMOTE
```

`PROMOTE` is a recommendation. Promotion to all exception emails waits for `HG-PROMOTION` (DEC-010, proposed).

## Scorecard, evidence period 1

```yaml
scorecard:
  outcome_ids: [OUT-001]
  initiative_ids: [INI-001]
  owner: Operations Director
  evidence_period: 2026-05-11 to 2026-06-26 (7 weeks with SLC-001 holding orders; PLT-001 ran 2026-05-25 to 2026-06-19)
  outcome_metric_ids: [MET-001, MET-002]
  capability_metric_ids: [MET-003, MET-004]
  operating_metric_ids: [MET-005]
  ai_evaluation_metric_ids: [MET-006]
  economic_metric_ids: [MET-008]
  risk_governance_metric_ids: [MET-007]
  observations:
    - metric_id: MET-001
      observed: "MISSING:June credit notes and freight not yet closed by finance"
      as_of: 2026-06-26
      evidence_ids: ["MISSING:finance export after the June close (Evidence Debt in evidence-register.md)"]
    - metric_id: MET-002
      observed: 1.9% of orders (160 of 8,420); baseline 3.0%
      as_of: 2026-06-26
      evidence_ids: [EVD-009]
    - metric_id: MET-003
      observed: 5.8% (488 of 8,420); baseline 9.6%
      as_of: 2026-06-26
      evidence_ids: [EVD-009]
    - metric_id: MET-004
      observed: median 10.5 working hours; baseline 22
      as_of: 2026-06-26
      evidence_ids: [EVD-009]
    - metric_id: MET-005
      observed: 8.6 minutes in the pilot inbox, 13.1 in the manually handled general inbox; baseline 14
      as_of: 2026-06-19
      evidence_ids: [EVD-008]
    - metric_id: MET-006
      observed: 83% (pilot inbox only)
      as_of: 2026-06-19
      evidence_ids: [EVD-008]
    - metric_id: MET-007
      observed: 1.2 per 100 (2 of 163); zero out-of-ceiling actions; manual baseline 2.1
      as_of: 2026-06-19
      evidence_ids: [EVD-008]
    - metric_id: MET-008
      observed: "MISSING:depends on the MET-001 reading"
      as_of: 2026-06-26
      evidence_ids: ["MISSING:see MET-001"]
  unexpected_effects:
    - Pack-size rules wrongly held 14 orders from two customers whose contracts allow broken packs; the rule table was corrected in week 2. Rule upkeep took about 5 hours in the first month instead of the planned 2.
    - Releases after the 14.00 pick cut-off rose from 22 to 31 a week, inside the range SFX-001 predicted; Mondays are watched.
    - Structured fields were used on 58% of orders with delivery instructions in week 7, against the 70% ASM-001 assumes.
  evidence_ids: [EVD-008, EVD-009]
  conclusion: PARTIAL_EFFECT
```

Why `PARTIAL_EFFECT` and not more: the capability metrics and one outcome metric (MET-002) moved clearly against the baseline, but none has reached its target, the cost Outcome metric MET-001 cannot be read yet, and the AI slice ran only in one inbox. The two changes overlap in time; the pilot's same-period comparison (EVL-003, EVL-004) separates the AI slice's share only for email exceptions. The baseline is winter and the evidence period early summer (EVD-009), so seasonality is a competing explanation that evidence period 2 has to check. This is an effect conclusion, not a value conclusion: no value is declared, and declaring it REALIZED would need the cost reading, attribution and `HG-VALUE` (`measurement/VALUE_REALIZATION.md` §2).
