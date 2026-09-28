# Worked example: a Compact engagement on Scenario B

> **Fictional and non-normative.** This example is informative guidance (`NORMATIVE_INDEX.md`, tier 13). The business, the people and every number are invented and illustrative; no real company, brand, product, vendor, cloud or AI provider is described or implied. "CU" means currency units. On any conflict, the methodology files govern.

It shows what the instance files of one Compact engagement look like: the records, their IDs, the trace between them, the human-gate Decisions, and an honest stopping point. It sits inside the AITM-SMB folder only as informative material (`SCOPE.md`); a real engagement writes its instances into a workspace outside the folder (`artifacts/_ARTIFACT_CONTRACT.md` §6).

## The scenario in five lines

1. A 45-person wholesale distributor handles about 1,200 customer orders a week through a web form, emailed orders and sales reps, on several legacy systems (Abstract Scenario B, `validation/ABSTRACT_SCENARIOS.md`).
2. About one order in ten needs manual correction before it can be picked; every exception costs clerk time, re-picks, credit notes and re-delivery freight, and a third of them delay dispatch.
3. The Operations Director wants the weekly cost of these exceptions halved and the share of orders they make late cut from 3% to 1% by the end of the year (OUT-001).
4. Diagnosis found that free-text order notes are re-keyed by hand and misread (validated), not that staff are careless (rejected).
5. The business standardized the notes, added deterministic validation rules, and piloted AI drafting of exception emails at L2 (Draft); a proposal to let AI correct and release orders on its own was rejected.

## How to read it

Read the files in order. Each starts with the `artifact:` metadata block (`artifacts/_ARTIFACT_CONTRACT.md` §4); merged files list every contract they hold (`CONFORMANCE.md` §4). Records are fenced YAML, one mapping per record, keyed by record type (`intent:`, `gap:`, `decision:` ...).

| File | Contracts | Phase | Skills |
|---|---|---|---|
| `01-intent.md` | transformation-intent (with OUT-001 and the conformance declaration) | 0 Frame | 36, 37, 01; 38 at the end |
| `02-capabilities-and-current-state.md` | capability-map (CAP-001, CURRENT STA-001) | 1 Observe | 02, 11 |
| `03-diagnosis.md` | capability-diagnosis (GAP-001, GAP-002), diagnostic-record (DIA-001, DIA-002) | 2 Diagnose | 03, 12, 16 |
| `04-interventions.md` | intervention-map (INT-001 to INT-007), ai-suitability-assessment (AIS-001, AIS-002), autonomy-assessment (AUT-001, AUT-002) | 3 Design Interventions | 04, 13, 14 |
| `05-target-and-roadmap.md` | transformation-roadmap (INI-001 with its economic hypothesis), capability-target-state (TARGET STA-002), system-effect-assessment (SFX-001), pilot-plan (PLT-001), ai-governance-canvas (Governance minimum); also the Transformation Slices SLC-001 and SLC-002, whose record contract is `execution/DELIVERY_SLICE.md` | 4 to 7 | 05, 06, 15, 19, 07, 25, 31 |
| `06-scorecard.md` | transformation-scorecard (MET-001 to MET-008, effect conclusion), evaluation-plan (EVL-001 to EVL-006, pilot results) | 0 to 8 (results in 7 and 8) | 01, 26, 32, 09; any skill that defines a Metric |
| `evidence-register.md` | evidence-register (EVD-001 to EVD-009, Evidence Debt) | any | any |
| `decision-assumption-log.md` | decision-assumption-log (DEC-001 to DEC-010, HYP-001 to HYP-004, ASM-001, ASM-002, RSK-001) | any | any |

The profile is Compact (DEC-001, confirmed by DEC-003). Everything Compact requires is present (`APPLICATION_PROFILES.md` §3, `MINIMUM_ARTIFACT_SET.md` §2.1). The Diagnostic Records and the pilot are optional in Compact; they are included because they keep symptoms apart from causes and because the AI slice carried material uncertainty (INV-11). Nothing from Standard or Governed was produced "just in case".

What the example avoids, following Scenario B's warnings: automating waste (notes are structured before anything is automated), a big-bang change (two slices; the AI slice only after the non-AI one, and first as a pilot), and AI where deterministic automation suffices (rules handle the exact checks; AI only interprets free text).

## Trace

The minimum valid path (`EXECUTION_MODEL.md` §6) and the semantic trace (`TRACEABILITY.md` §1) with the actual IDs:

```text
OUT-001  Cut the cost and the delay caused by order exceptions
 └─ CAP-001  Order exception resolution
     ├─ STA-001  CURRENT, as of 2026-03-20
     ├─ GAP-001  9.6% of orders need correction before pick (required: at most 4%)
     │   ├─ HYP-001  free-text notes re-keyed by hand and misread ........ validated
     │   └─ HYP-002  staff careless or undertrained ....................... rejected
     └─ GAP-002  median 22 working hours to resolve (required: at most 4)
         ├─ HYP-003  emails wait for two senior clerks who alone interpret them ... validated
         └─ HYP-004  waiting for customer answers ......................... rejected
              │
              ├─ INT-002 STANDARDIZE · INT-003 KNOWLEDGE · INT-004 AUTOMATION ... selected
              ├─ INT-006 AI_ASSIST, L2 Draft (AIS-001 class B, AUT-001 ceiling L2) ... selected
              ├─ INT-001 ELIMINATE ............................................... deferred
              ├─ INT-005 CONTROL (four-eyes check, answers HYP-002) .............. rejected
              └─ INT-007 AI_AUTONOMIZE (AIS-002 class E, AUT-002 ceiling L0) ..... rejected
                   │
                   └─ INI-001  slices SLC-001 (non-AI) and SLC-002 (AI, pilot PLT-001)
                        ├─ entry STA-001 → exit STA-002 TARGET, as of 2026-12-31
                        ├─ SFX-001  system-effect check: improves_outcome
                        ├─ MET-001 MET-002 (outcome) · MET-003 MET-004 (capability)
                        │  MET-005 (operating) · MET-006 (ai_evaluation)
                        │  MET-007 (risk_governance) · MET-008 (economic)
                        └─ EVD-001 … EVD-009, EVL-001 … EVL-006
```

## Human gates

Closed, each by an approved Decision naming the human (`STANDARD.md` §8):

| Gate | Decision | Subject | Approved by | Date |
|---|---|---|---|---|
| `HG-OUTCOME` | DEC-003 | OUT-001 and the profile Decision DEC-001 | Operations Director (Outcome owner) | 2026-03-06 |
| `HG-AUTHORITY` | DEC-004 | Authority Ceilings: AUT-001 at L2, AUT-002 at L0 | Operations Director (Outcome owner) | 2026-04-07 |
| `HG-INITIATIVE` | DEC-005 | INI-001 | Operations Director (Outcome owner) | 2026-04-10 |
| `HG-BUDGET` | DEC-007 | INI-001, 21,000 CU | Managing Director (budget holder) | 2026-04-10 |
| `HG-TOA` | DEC-008 | STA-002 (Compact: the Capability Target State) | Operations Director (Outcome owner) | 2026-04-17 |
| `HG-AUTHORITY` | DEC-009 | AUT-001 level in operation from L0 to L2, for PLT-001 | Operations Director (Outcome owner) | 2026-05-22 |

Open:

- `HG-PROMOTION` for PLT-001: the pilot recommends `PROMOTE`; DEC-010 is recorded as proposed and waits for the Operations Director.

Not reached, and why:

- `HG-VALUE`: nobody claims realized value. The scorecard shows a partial effect, the cost reading is Evidence Debt, and Compact without Measured keeps no Value Realization Report.
- `HG-RISK`: no material risk has been accepted; RSK-001 is open and controlled.
- `HG-DECISION-RIGHTS`: no material Decision Right changes. Clerks still decide every correction and release, the Order Desk Lead's ownership of the rule table sits within the existing authority over order-desk procedures (STA-002), and the AI decides nothing.

## Where the engagement stopped

On 2026-07-01, seven weeks after the non-AI slice went live and two weeks after the pilot ended. The last handoff, from the Phase 8 orchestrator, is below (`AGENT_OUTPUT_STANDARD.md`). It stops at the open gate instead of proceeding to rollout.

```yaml
aitm_output:
  framework_version: 1.1.0
  profiles: [Compact]
  skill: 09-measure-evolution
  status: HUMAN_DECISION_REQUIRED
  status_reason: >-
    Evidence period 1 of INI-001 read; effect conclusion PARTIAL_EFFECT.
    HG-PROMOTION for PLT-001 is open (reached by skill 32 on 2026-06-24; DEC-010
    proposed). PARTIAL also applies - MET-001 and MET-008 wait for the June
    finance close. HG-VALUE is not reached; no value state is claimed.
  artifacts_changed:
    - 06-scorecard.md MET-001 MET-002 MET-003 MET-004 MET-005 MET-006 MET-007 MET-008 (observations, conclusion)
    - evidence-register.md EVD-009 (and the Evidence Debt for MET-001) EVD-008 (claim_supported, for ASM-002)
    - decision-assumption-log.md HYP-003 ASM-002 (validated)
    - 03-diagnosis.md GAP-002 (cause_status validated) DIA-002 (next_action)
    - 04-interventions.md AUT-001 (promotion_recommendation, rationale, evidence_ids; skill 34)
  trace:
    outcome_ids: [OUT-001]
    capability_ids: [CAP-001]
    state_ids: [STA-001, STA-002]
    gap_ids: [GAP-001, GAP-002]
    hypothesis_ids: [HYP-001, HYP-003]
    intervention_ids: [INT-002, INT-003, INT-004, INT-006]
    initiative_ids: [INI-001]
    metric_ids: [MET-001, MET-002, MET-003, MET-004, MET-005, MET-006, MET-007, MET-008]
    evidence_ids: [EVD-008, EVD-009]
    other_ids: [PLT-001, SLC-001, SLC-002, EVL-001, EVL-002, EVL-003, EVL-004, EVL-005, EVL-006, AUT-001, SFX-001, DIA-002, DEC-010, ASM-001, ASM-002, RSK-001]
  findings:
    - MET-003 fell from 9.6% to 5.8% and MET-004 from 22 to 10.5 working hours; both are short of their targets (4.0%, 4 hours).
    - Outcome metric MET-002 fell from 3.0% to 1.9% of orders; the cost Outcome metric MET-001 cannot be read yet.
    - The baseline is winter and evidence period 1 early summer (EVD-009); seasonality is a competing explanation that period 2 must check.
    - PLT-001 met all six pre-registered thresholds, two with limitations; pilot_result PROMOTE.
    - HYP-003 validated with medium confidence from the same-period inbox comparison; GAP-002 cause_status updated.
    - ASM-002 validated - without AI, the general inbox took a median 13.1 clerk minutes per email with fields and rules live (EVD-008), well above the 8-minute target; the customer mix differs from the pilot inbox.
    - ASM-001 reads 58% at week 7 against the 70% assumed; decision point at week 8.
    - SFX-001 held; releases after the pick cut-off rose from 22 to 31 a week, inside the predicted range.
    - AUT-001 promotion_recommendation retain; L2 is the approved ceiling and no increase is proposed.
  assumptions: [ASM-001]
  decisions_needed:
    - gate: HG-PROMOTION
      subject_ids: [PLT-001, SLC-002, EVL-001, EVL-002, EVL-003, EVL-004, EVL-005, EVL-006, DEC-010]
      question: Promote AI drafting at L2 (SLC-002) from the key-account inbox to all free-text exception emails, staged by inbox?
  open_gates: [HG-PROMOTION]
  evidence_debt:
    - claim: MET-001 (weekly exception cost) and MET-008 (cost per resolved exception) for evidence period 1
      decision_affected: effect conclusion for OUT-001; any future HG-VALUE request; context for DEC-010
      missing_evidence: June credit notes and re-delivery freight by reason code (finance month-end close)
      risk_if_wrong: the cost Outcome may move less than exception rate and time did
      validation_plan: the Finance Lead exports June credit notes and freight by reason code; MET-001 and MET-008 are recomputed on the baseline definition
      deadline_or_gate: 2026-07-17, and before any HG-VALUE request
  risks: [RSK-001]
  next_skill: 08-design-operating-model
```

What happens next is the Operations Director's call, not the agent's: approve, revise or stop the promotion (DEC-010). If approved, skill 08 plans the staged rollout within the L2 ceiling; either way, skill 09 reads evidence period 2, including MET-001, before anyone asks for `HG-VALUE`.

## Check it

From the AITM-SMB folder:

```bash
python3 tools/validate.py --engagement examples/compact-scenario-b
```

The check confirms that every referenced ID is defined exactly once with a registered prefix, that the minimum valid path and the core trace links exist, and that every approved Outcome and active Initiative is backed by an approved gate Decision naming the human. It does not judge whether the diagnosis is right; that is what the review aids in `rubrics/` and skill 38 are for.
