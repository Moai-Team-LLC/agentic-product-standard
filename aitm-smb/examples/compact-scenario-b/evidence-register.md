```yaml
artifact:
  type: evidence-register
  id: scenario-b/evidence-register
  framework_version: 1.1.0
  status: reviewed
  owner: Order Desk Lead
  upstream: []
  downstream: [01-intent.md, 02-capabilities-and-current-state.md, 03-diagnosis.md, 04-interventions.md, 05-target-and-roadmap.md, 06-scorecard.md]
  evidence: [EVD-001, EVD-002, EVD-003, EVD-004, EVD-005, EVD-006, EVD-007, EVD-008, EVD-009]
  assumptions: [ASM-001, ASM-002]
  decisions: []
  open_questions: [MET-001 reading after the June finance close]
```

# Evidence Register

Fictional, informative example (see `examples/compact-scenario-b/README.md`). Contract: `artifacts/evidence-register.md`; records: Evidence and Evidence Debt, `evidence/EVIDENCE_STANDARD.md` §3 and §5. Sources are referenced, not copied; interview content stays with the Order Desk Lead (`evidence/EVIDENCE_STANDARD.md` §8).

The diagnosis is triangulated (`evidence/EVIDENCE_STANDARD.md` §4): system data (EVD-001, EVD-004, EVD-005), observed work (EVD-002) and interviews (EVD-003). The interviews alone pointed at the wrong cause.

## Evidence

```yaml
evidence:
  id: EVD-001
  source_type: system records
  source: order-system exception log export, 2025-12-01 to 2026-02-20, kept by the Order Desk Lead
  date: 2026-03-03
  scope: all 14,300 orders and 1,373 exceptions of the 12 weeks
  claim_supported: >-
    Exception rate 9.6% (MET-003), median resolution 22 working hours (MET-004),
    31% of exceptions late for dispatch, 3.0% of all orders (MET-002); GAP-001,
    GAP-002, OUT-001 baseline.
  limitations: free-text reason blank on 40% of entries; resolution time converted from calendar to working hours; winter season only
  confidence: high
```

```yaml
evidence:
  id: EVD-002
  source_type: observed workflow
  source: two-week timed observation of the order desk and warehouse re-picks by the engagement analyst, notes kept by the Order Desk Lead
  date: 2026-03-20
  scope: 212 exception handlings, 2026-03-09 to 2026-03-20
  claim_supported: >-
    124 of 212 handlings involved a free-text email; such emails waited a median
    5.5 working hours before first touch and took a median 14 minutes (MET-005);
    83% were handled by the two senior clerks; 8 of 124 emails (about one in
    fifteen) were ambiguous even to the senior clerks; 36 of 212 exceptions waited
    for an outside answer; 9 ambiguous notes were re-keyed differently by
    different clerks; handling and re-pick time for MET-001. HYP-001, HYP-003,
    against HYP-002 and HYP-004.
  limitations: two weeks in one season; clerks knew they were observed
  confidence: medium
```

```yaml
evidence:
  id: EVD-003
  source_type: stakeholder interview
  source: nine interviews (five clerks, Order Desk Lead, Warehouse Lead, one sales rep, Finance Lead), notes kept by the Order Desk Lead
  date: 2026-03-13
  scope: views on why exceptions happen and why they take long
  claim_supported: >-
    Notes are ambiguous and re-typed (HYP-001); only the senior clerks know
    customers' conventions (HYP-003); two interviewees blamed rushing clerks
    (HYP-002); clerks said customers are slow to answer (HYP-004).
  limitations: stakeholder interpretation; the two blame statements came from outside the order desk
  confidence: low
```

```yaml
evidence:
  id: EVD-004
  source_type: transaction data
  source: cause-coded random sample of 200 exceptions from EVD-001, coded independently by the analyst and the Order Desk Lead
  date: 2026-03-26
  scope: 200 of 1,373 exceptions, 2025-12-01 to 2026-02-20
  claim_supported: >-
    142 of 200 (71%) trace to a misread or unapplied free-text note, while notes
    appear on 18% of orders (about 38% exception rate with a note, 3.4% without);
    per-clerk rates 8.9% to 10.4% with no tenure effect; of 96 corrections made
    from an email, 2 were wrong (2.1 per 100, MET-007 baseline). HYP-001 for,
    HYP-002 against.
  limitations: coding is a judgment (the two coders agreed on 176 of 200 before resolving the rest together); winter sample
  confidence: high
```

```yaml
evidence:
  id: EVD-005
  source_type: financial data
  source: finance records of credit notes and re-delivery freight coded "order error", 2025-12-01 to 2026-02-20, from the Finance Lead
  date: 2026-03-03
  scope: 12 weeks, 37,200 CU in total
  claim_supported: 3,100 CU per week of the MET-001 baseline; 60 to 400 CU per wrong delivery (AUT-002, RSK-001)
  limitations: 8% of credit notes carry no reason code; freight attributed by reason code
  confidence: medium
```

```yaml
evidence:
  id: EVD-006
  source_type: system records
  source: warehouse pick-wave and dispatch logs, 12 weeks to 2026-04-10, from the Warehouse Lead
  date: 2026-04-14
  scope: afternoon pick wave and releases after the 14.00 cut-off
  claim_supported: afternoon wave at 84% of capacity on average and 95% on Mondays; about 22 orders a week released after the cut-off (SFX-001)
  limitations: capacity measured in order lines, not labour hours
  confidence: medium
```

```yaml
evidence:
  id: EVD-007
  source_type: offline evaluation
  source: AI drafts for 60 historical key-account exception emails compared with the clerks' actual corrections, run by the IT support contractor
  date: 2026-05-20
  scope: 60 emails from February 2026
  claim_supported: reason code matched in 50 of 60; 44 of 60 drafts needed no material edit; input to DEC-009 and AUT-001
  limitations: small, historical, key accounts only; no clerk behaviour observed
  confidence: low
```

```yaml
evidence:
  id: EVD-008
  source_type: pilot records
  source: PLT-001 draft-and-release log, ticket and mailbox time stamps, sample reviews, escape log and access log
  date: 2026-06-24
  scope: 163 emails in the key-account inbox, 2026-05-25 to 2026-06-19, with the general inbox as comparison
  claim_supported: >-
    Results of EVL-001 to EVL-006; email exceptions resolved in a median 5.2
    working hours in the pilot inbox against 11.4 in the general inbox (HYP-003);
    a median 13.1 clerk minutes per email in the manually handled general inbox,
    with fields and rules live, against 8.6 in the pilot inbox (ASM-002).
  limitations: four weeks; key-account customers differ from the rest; clerks knew the pilot was reviewed; only 2 escapes observed
  confidence: medium
```

```yaml
evidence:
  id: EVD-009
  source_type: system records
  source: order-system exception log export, 2026-05-11 to 2026-06-26, kept by the Order Desk Lead
  date: 2026-06-29
  scope: 8,420 orders and 488 exceptions in 7 weeks
  claim_supported: >-
    MET-002 1.9%, MET-003 5.8%, MET-004 median 10.5 working hours; structured
    fields used on 58% of orders with delivery instructions in week 7 (ASM-001);
    14 wrong rule holds in weeks 1 and 2; releases after the pick cut-off 31 a week.
  limitations: seven early-summer weeks against a winter baseline; overlaps with PLT-001
  confidence: medium
```

## Evidence Debt

Visible, as `evidence/EVIDENCE_STANDARD.md` §5 requires. It is also listed in the last handoff (`examples/compact-scenario-b/README.md`).

```yaml
evidence_debt:
  - claim: MET-001 (weekly exception cost) and MET-008 (cost per resolved exception) for evidence period 1
    decision_affected: effect conclusion for OUT-001 in 06-scorecard.md; any future HG-VALUE request; context for DEC-010
    missing_evidence: June credit notes and re-delivery freight by reason code (finance month-end close)
    risk_if_wrong: the cost Outcome may move less than exception rate and time did, for example if the remaining exceptions are the costly ones
    validation_plan: the Finance Lead exports June credit notes and freight by reason code after the close; MET-001 and MET-008 are recomputed on the baseline definition (EVD-005)
    deadline_or_gate: 2026-07-17, and before any HG-VALUE request
```
