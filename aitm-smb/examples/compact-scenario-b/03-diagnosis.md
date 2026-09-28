```yaml
artifact:
  type: capability-diagnosis
  id: scenario-b/03-diagnosis
  framework_version: 1.1.0
  status: reviewed
  owner: Operations Director
  upstream: [02-capabilities-and-current-state.md, evidence-register.md]
  downstream: [04-interventions.md]
  evidence: [EVD-001, EVD-002, EVD-003, EVD-004, EVD-005, EVD-008]
  assumptions: [HYP-001, HYP-002, HYP-003, HYP-004]
  decisions: [DEC-004]
  open_questions: []
```

# Capability Diagnosis

Fictional, informative example (see [`examples/compact-scenario-b/README.md`](README.md)). Phase 2 (Diagnose): skills 03, 12 and 16. Contract: [`artifacts/capability-diagnosis.md`](../../artifacts/capability-diagnosis.md). In Compact the Observations and Symptoms MAY sit on the Gap instead of in a Diagnostic Record ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md) §3); they are kept in their own fields, apart from the Gap's conditions and from its causes (INV-03, [`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../../diagnostics/ROOT_CAUSE_ANALYSIS.md) §1). The cause Hypotheses are Hypothesis records in [`decision-assumption-log.md`](decision-assumption-log.md), as [`MINIMUM_ARTIFACT_SET.md`](../../MINIMUM_ARTIFACT_SET.md) §2.1 maps them.

| Hypothesis | Gap | Cause class | Status | Confidence |
|---|---|---|---|---|
| HYP-001 free-text notes are re-keyed by hand and misread | GAP-001 | INFORMATION | validated | high |
| HYP-002 staff are careless or insufficiently trained | GAP-001 | SKILL | rejected | high |
| HYP-003 free-text emails wait for the two senior clerks who alone can interpret them | GAP-002 | KNOWLEDGE | validated | medium |
| HYP-004 resolution waits on answers from customers or sales reps | GAP-002 | FLOW | rejected | medium |

The first explanation offered in the interviews was "the clerks rush" (HYP-002). It was kept as a competing Hypothesis and tested, not accepted: error rates do not differ by clerk or tenure, and they concentrate on orders with free-text notes (EVD-004). "Lack of AI" was not considered a cause ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../../diagnostics/ROOT_CAUSE_ANALYSIS.md) §3).

Intervention readiness at the Phase 2 exit, 2026-03-27 ([`diagnostics/DIAGNOSTIC_MODEL.md`](../../diagnostics/DIAGNOSTIC_MODEL.md) §6):

- GAP-001: HYP-001 validated, HYP-002 rejected. Intervention-ready.
- GAP-002: the Evidence pointed at HYP-003 and against HYP-004, but the claim that the interpretation queue sets most of the resolution time could only be confirmed by changing who interprets, which is itself an intervention. Skill 16 proposed accepting HYP-003 as testable in `decisions_needed`; the Operations Director, owner of CAP-001 and OUT-001, approved it in DEC-004 on 2026-03-27. GAP-002 was intervention-ready on that basis, with PLT-001 later designed as the test.

After the pilot, skill 32 named the diagnosis update its results require. Skill 03 re-entered Phase 2 on 2026-06-26 ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §3) and invoked skill 16, which validated HYP-003 from the pilot comparison (EVD-008); skill 03 then set GAP-002 `cause_status: validated`. The records below show that state.

## Gaps

```yaml
gap:
  id: GAP-001
  capability_id: CAP-001
  current_state_id: STA-001
  current_condition: 9.6% of orders (about 114 a week) need manual correction before pick.
  required_condition: at most 4% of orders need manual correction before pick.
  business_impact: >-
    Most of the 5,200 CU weekly exception cost (credit notes, re-delivery
    freight, re-picks, order-desk time) scales with the number of exceptions.
  cause_status: validated
  hypothesis_ids: [HYP-001, HYP-002]
  evidence_ids: [EVD-001, EVD-002, EVD-004, EVD-005]
  assumption_ids: []
  confidence: high
  observations:
    - evidence_id: EVD-001
      statement: 1,373 of 14,300 orders (9.6%) needed manual correction before pick in the 12 weeks to 2026-02-20.
    - evidence_id: EVD-004
      statement: 142 of 200 sampled exceptions (71%) trace to a free-text note that was misread or not applied; notes appear on 18% of orders.
    - evidence_id: EVD-004
      statement: The five clerks' exception rates range from 8.9% to 10.4%, with no difference by tenure.
    - evidence_id: EVD-002
      statement: In two weeks, 9 ambiguous notes were re-keyed differently by different clerks.
  symptoms: [frequent rework before pick, re-picks in the warehouse, wrong deliveries reported by customers]
```

```yaml
gap:
  id: GAP-002
  capability_id: CAP-001
  current_state_id: STA-001
  current_condition: median 22 working hours from detection to release; 31% of exceptions miss the planned dispatch day.
  required_condition: median at most 4 working hours; at most 10% of exceptions miss the planned dispatch day.
  business_impact: >-
    3.0% of all orders are dispatched late because of an exception; two key
    accounts complained formally in the first quarter.
  cause_status: validated
  hypothesis_ids: [HYP-003, HYP-004]
  evidence_ids: [EVD-001, EVD-002, EVD-008]
  assumption_ids: []
  confidence: medium
  observations:
    - evidence_id: EVD-001
      statement: Median time from detection to release was 22 working hours; 31% of exceptions missed the planned dispatch day.
    - evidence_id: EVD-002
      statement: 124 of 212 observed exception handlings involved a free-text email; such emails waited a median 5.5 working hours before first touch and took a median 14 minutes to handle.
    - evidence_id: EVD-002
      statement: The two senior clerks handled 83% of the exception emails.
    - evidence_id: EVD-002
      statement: 36 of 212 observed exceptions (17%) waited for an answer from the customer or a sales rep.
  symptoms: [slow exception resolution, missed dispatch days, a queue in front of two people]
```

Root-cause ladder for GAP-001 ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../../diagnostics/ROOT_CAUSE_ANALYSIS.md) §2): the direct cause is misread notes; the system condition is that nothing checks note-driven fields at entry; the architectural condition is that the order system treats delivery instructions as free text. The Interventions in [`04-interventions.md`](04-interventions.md) target the lowest two layers, not the symptom.
