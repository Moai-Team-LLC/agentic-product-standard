# Worked example: a Compact engagement on Scenario B

> **Fictional and non-normative.** This example is informative guidance ([`NORMATIVE_INDEX.md`](../../NORMATIVE_INDEX.md), tier 13). The business, the people and every number are invented and illustrative; no real company, brand, product, vendor, cloud or AI provider is described or implied. "CU" means currency units. On any conflict, the methodology files govern.

It shows what the instance files of one Compact engagement look like: the records, their IDs, the trace between them, the human-gate Decisions, and an honest stopping point. It sits inside the AITM-SMB folder only as informative material ([`SCOPE.md`](../../SCOPE.md)); a real engagement writes its instances into a workspace outside the folder ([`artifacts/_ARTIFACT_CONTRACT.md`](../../artifacts/_ARTIFACT_CONTRACT.md) §6).

## The scenario in five lines

1. A 45-person wholesale distributor handles about 1,200 customer orders a week through a web form, emailed orders and sales reps, on several legacy systems (Abstract Scenario B, [`validation/ABSTRACT_SCENARIOS.md`](../../validation/ABSTRACT_SCENARIOS.md)).
2. About one order in ten needs manual correction before it can be picked; every exception costs clerk time, re-picks, credit notes and re-delivery freight, and a third of them delay dispatch.
3. The Operations Director wants the weekly cost of these exceptions halved and the share of orders they make late cut from 3% to 1% by the end of the year (OUT-001).
4. Diagnosis found that free-text order notes are re-keyed by hand and misread (validated), not that staff are careless (rejected).
5. The business standardized the notes, added deterministic validation rules, and piloted AI drafting of exception emails at L2 (Draft); a proposal to let AI correct and release orders on its own was rejected.

## How to read it

Read the files in order. Each starts with the `artifact:` metadata block ([`artifacts/_ARTIFACT_CONTRACT.md`](../../artifacts/_ARTIFACT_CONTRACT.md) §4); merged files list every contract they hold ([`CONFORMANCE.md`](../../CONFORMANCE.md) §4). Records are fenced YAML, keyed by record type: one mapping per record (`intent:`, `gap:`, `decision:` ...), or a list under the plural key (`slices:`), as [`artifacts/_ARTIFACT_CONTRACT.md`](../../artifacts/_ARTIFACT_CONTRACT.md) §7 allows. Every record shows its current state; the Decisions and Evidence that cite it carry its history.

| File | Contracts | Phase | Skills |
|---|---|---|---|
| [`01-intent.md`](01-intent.md) | transformation-intent (ATI-001 with OUT-001 and the conformance declaration) | 0 Frame | 36, 37, 01; 38 at the end |
| [`02-capabilities-and-current-state.md`](02-capabilities-and-current-state.md) | capability-map (CAP-001, CURRENT STA-001) | 1 Observe | 02, 11 |
| [`03-diagnosis.md`](03-diagnosis.md) | capability-diagnosis (GAP-001, GAP-002, each with its Observations and Symptoms) | 2 Diagnose; re-entered after the pilot | 03, 12, 16 |
| [`04-interventions.md`](04-interventions.md) | intervention-map (INT-001 to INT-007), ai-suitability-assessment (AIS-001, AIS-002), autonomy-assessment (AUT-001) | 3 Design Interventions; statuses in 4 | 04, 13, 14; 05; 34 |
| [`05-target-and-roadmap.md`](05-target-and-roadmap.md) | transformation-roadmap (INI-001 with its economic hypothesis and operation minimum; slices SLC-001, SLC-002), system-effect-assessment (SFX-001), capability-target-state (TARGET STA-002), pilot-plan (PLT-001), ai-governance-canvas (Governance minimum) | 4 to 7 | 05, 19, 06, 15, 24, 07, 25, 08, 34, 31 |
| [`06-scorecard.md`](06-scorecard.md) | transformation-scorecard (MET-001 to MET-009, effect conclusion), evaluation-plan (EVL-001 to EVL-006, pilot results) | 0 to 8 (results in 7 and 8) | 01, 26, 32, 09; any skill that defines a Metric |
| [`evidence-register.md`](evidence-register.md) | evidence-register (EVD-001 to EVD-009; Evidence Debt, two items resolved and one open) | any | any |
| [`decision-assumption-log.md`](decision-assumption-log.md) | decision-assumption-log (DEC-001 to DEC-011, HYP-001 to HYP-004, ASM-001 to ASM-003, RSK-001) | any | any |

The profile is Compact (DEC-001, approved with `HG-OUTCOME` in DEC-003). Everything Compact requires is present ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md) §3, [`MINIMUM_ARTIFACT_SET.md`](../../MINIMUM_ARTIFACT_SET.md) §2.1), including the Governance minimum for the one `AI_*` candidate proposed for selection: AIS-001, AUT-001 with its approved Authority Ceiling, and the six canvas fields. Compact options are used where they save work: Observations and Symptoms sit on the Gaps instead of in Diagnostic Records, and the Phase 7 minimum sits on INI-001 as `operation`. The pilot and its evaluation plan are optional in Compact; they are included because the AI slice carried material uncertainty (INV-11). Nothing from Standard or Governed was produced "just in case".

What the example avoids, following Scenario B's warnings: automating waste (notes are structured before anything is automated), a big-bang change (two slices; the AI slice only after the non-AI one, and first as a pilot), and AI where deterministic automation suffices (rules handle the exact checks; AI only interprets free text).

Rules the records show, with the binding text in the files they cite:

- Every gate reached is first recorded as a proposed Decision, then updated on approval; the one still open stays proposed ([`decision-assumption-log.md`](decision-assumption-log.md)).
- The profile Decision marks its unknown answer `[OPEN]` and is approved with `HG-OUTCOME`.
- Every Outcome has a Metric. The owners' Phase 0 cost estimate is an Assumption with a named owner (ASM-003), and its Evidence Debt was resolved; no baseline rests on agent inference.
- A cause is accepted as testable only by the owner's Decision (DEC-004).
- Every `AI_*` candidate has an AI Suitability Assessment; only the one proposed for selection has an Autonomy Assessment, and it was selected only after its ceiling was approved.
- The system-effect check was drafted before `HG-INITIATIVE`, with one effect `unknown` and Evidence Debt, then refined in Phase 5.
- The economic hypothesis sits on the Initiative and is cited by `HG-BUDGET`.
- The pilot's authority grant was planned as a `decision_gates` entry naming AUT-001 and granted by skill 34 before the pilot ran; widening the scope at the same level is rollout (`HG-PROMOTION`), not `HG-AUTHORITY`.

## Trace

The minimum valid path ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §6) and the semantic trace ([`TRACEABILITY.md`](../../TRACEABILITY.md) §1) with the actual IDs:

```text
OUT-001  Cut the cost and the delay caused by order exceptions
 └─ CAP-001  Order exception resolution
     ├─ STA-001  CURRENT, as of 2026-03-20
     ├─ GAP-001  9.6% of orders need correction before pick (required: at most 4%)
     │   ├─ HYP-001  free-text notes re-keyed by hand and misread ........ validated
     │   └─ HYP-002  staff careless or undertrained ....................... rejected
     └─ GAP-002  median 22 working hours to resolve (required: at most 4)
         ├─ HYP-003  emails wait for two senior clerks who alone interpret them ... validated
         │           (accepted as testable by DEC-004, validated from PLT-001)
         └─ HYP-004  waiting for customer answers ......................... rejected
              │
              ├─ INT-002 STANDARDIZE · INT-003 KNOWLEDGE · INT-004 AUTOMATION ... selected
              ├─ INT-006 AI_ASSIST, L2 Draft (AIS-001 class B, AUT-001 ceiling L2) ... selected
              ├─ INT-001 ELIMINATE ............................................... deferred
              ├─ INT-005 CONTROL (four-eyes check, answers HYP-002) .............. rejected
              └─ INT-007 AI_AUTONOMIZE (AIS-002 class E, no autonomy assessment) .. rejected
                   │
                   └─ INI-001  with economic hypothesis and operation minimum
                        ├─ SFX-001  system-effect check, before selection: improves_outcome
                        ├─ entry STA-001 → exit STA-002 TARGET, as of 2026-12-31
                        ├─ slices SLC-001 (non-AI) and SLC-002 (AI, pilot PLT-001)
                        ├─ MET-001 MET-002 (outcome) · MET-003 MET-004 (capability)
                        │  MET-005 MET-009 (operating) · MET-006 (ai_evaluation)
                        │  MET-007 (risk_governance) · MET-008 (economic)
                        └─ EVD-001 … EVD-009, EVL-001 … EVL-006
```

## Human gates

Gate IDs with the subjects decided here; the binding text is [`STANDARD.md`](../../STANDARD.md) §8. Each gate Decision was recorded as `proposed` when the gate was reached; the proposal dates are in [`decision-assumption-log.md`](decision-assumption-log.md).

Closed, each by an approved Decision naming the human:

| Gate | Decision | Subject | Approved by | Date |
|---|---|---|---|---|
| `HG-OUTCOME` | DEC-003 | OUT-001 and the profile Decision DEC-001 | Operations Director (Outcome owner) | 2026-03-06 |
| `HG-AUTHORITY` | DEC-005 | Authority Ceiling of AUT-001: L2, drafting exception-email triage in CAP-001 | Operations Director (Outcome owner) | 2026-04-07 |
| `HG-INITIATIVE` | DEC-006 | INI-001, decided with SFX-001 in hand | Operations Director (Outcome owner) | 2026-04-10 |
| `HG-BUDGET` | DEC-008 | INI-001, 21,000 CU, citing its economic hypothesis | Managing Director (budget holder) | 2026-04-10 |
| `HG-TOA` | DEC-009 | STA-002 (Compact: the Capability Target State) | Operations Director (Outcome owner) | 2026-04-17 |
| `HG-AUTHORITY` | DEC-010 | AUT-001 current_level from L0 to L2, PLT-001 scope only | Operations Director (Outcome owner) | 2026-05-22 |

Owner Decisions without a gate: DEC-001 (profile, approved with `HG-OUTCOME`), DEC-002 (materiality thresholds), DEC-004 (HYP-003 accepted as testable), DEC-007 (deferred and rejected candidates).

Open:

- `HG-PROMOTION` for PLT-001: the pilot recommends `PROMOTE`; skill 32 recorded DEC-011 as `proposed` on 2026-06-24, and it waits for the Operations Director. The level would stay L2, so widening the scope is rollout and needs no `HG-AUTHORITY` Decision.

Not reached, and why:

- `HG-VALUE`: nobody claims realized value. The scorecard shows a partial effect, the cost reading is Evidence Debt, and Compact without Measured keeps no Value Realization Report; a later `HG-VALUE` Decision would list INI-001 and the Outcome Metrics MET-001 and MET-002 ([`measurement/VALUE_REALIZATION.md`](../../measurement/VALUE_REALIZATION.md) §2).
- `HG-RISK`: no material risk has been accepted; RSK-001 is open and controlled.
- `HG-DECISION-RIGHTS`: no material Decision Right changes. Clerks still decide every correction and release, the Order Desk Lead's ownership of the rule table sits within the existing authority over order-desk procedures (STA-002), and the AI decides nothing.

## Where the engagement stopped

On 2026-07-01, seven weeks after the non-AI slice went live and two weeks after the pilot ended. The last handoff, from the Phase 8 orchestrator, is below ([`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md)). It stops at the open gate instead of proceeding to rollout.

```yaml
aitm_output:
  framework_version: 1.1.0
  profiles: [Compact]
  skill: 09-measure-evolution
  status: HUMAN_DECISION_REQUIRED
  status_reason: >-
    Evidence period 1 of INI-001 read; effect conclusion PARTIAL_EFFECT.
    HG-PROMOTION for PLT-001 is open - skill 32 recorded DEC-011 as proposed on
    2026-06-24, and it waits for the Operations Director. PARTIAL also applies -
    MET-001 and MET-008 wait for the June finance close (open Evidence Debt).
    HG-VALUE is not reached; no value state is claimed.
  artifacts_changed:
    - 06-scorecard.md scorecard for OUT-001 and INI-001 (observations of MET-001 to MET-009, unexpected effects, conclusion)
    - evidence-register.md EVD-009; Evidence Debt for MET-001 and MET-008 (open)
    - decision-assumption-log.md ASM-002 (validated, evidence_ids)
    - 04-interventions.md AUT-001 (promotion_recommendation, rationale, evidence_ids; skill 34)
  trace:
    outcome_ids: [OUT-001]
    capability_ids: [CAP-001]
    state_ids: [STA-001, STA-002]
    gap_ids: [GAP-001, GAP-002]
    hypothesis_ids: [HYP-001, HYP-003]
    intervention_ids: [INT-002, INT-003, INT-004, INT-006]
    initiative_ids: [INI-001]
    metric_ids: [MET-001, MET-002, MET-003, MET-004, MET-005, MET-006, MET-007, MET-008, MET-009]
    evidence_ids: [EVD-008, EVD-009]
    other_ids: [PLT-001, SLC-001, SLC-002, EVL-001, EVL-002, EVL-003, EVL-004, EVL-005, EVL-006, AUT-001, SFX-001, DEC-011, ASM-001, ASM-002, RSK-001]
  findings:
    - MET-003 fell from 9.6% to 5.8% and MET-004 from 22 to 10.5 working hours; both are short of their targets (4.0%, 4 hours).
    - Outcome metric MET-002 fell from 3.0% to 1.9% of orders; the cost Outcome metric MET-001 cannot be read yet.
    - The baseline is winter and evidence period 1 early summer (EVD-009); seasonality is a competing explanation that period 2 must check.
    - PLT-001 met all six pre-registered thresholds, two with limitations; pilot_result PROMOTE, with no unmet criterion to waive.
    - ASM-002 validated - without AI, the general inbox took a median 13.1 clerk minutes per email with fields and rules live (EVD-008), well above the 8-minute target; the customer mix differs from the pilot inbox.
    - Structured-field use (MET-009) reads 58% at week 7 against the 70% ASM-001 assumes; decision point at week 8 (2026-07-06).
    - SFX-001 held; releases after the pick cut-off rose from 22 to 31 a week, inside the predicted range.
    - AUT-001 promotion_recommendation retain; current_level L2 in the PLT-001 scope equals the approved ceiling, and no increase is proposed.
    - No diagnosis, target or roadmap record is disproved by this period; HYP-003 was already validated from the pilot (skills 03 and 16, 2026-06-26), so nothing returns to skills 03, 06 or 07.
  assumptions: [ASM-001]
  decisions_needed:
    - gate: HG-PROMOTION
      subject_ids: [PLT-001, SLC-002, EVL-001, EVL-002, EVL-003, EVL-004, EVL-005, EVL-006, DEC-011]
      question: Promote AI drafting at L2 (SLC-002) from the key-account inbox to all free-text exception emails, staged by inbox?
  open_gates: [HG-PROMOTION]
  evidence_debt:
    - claim: MET-001 (weekly exception cost) and MET-008 (cost per resolved exception) for evidence period 1
      decision_affected: effect conclusion for OUT-001; any future HG-VALUE request; context for DEC-011
      missing_evidence: June credit notes and re-delivery freight by reason code (finance month-end close)
      risk_if_wrong: the cost Outcome may move less than exception rate and time did
      validation_plan: the Finance Lead exports June credit notes and freight by reason code; MET-001 and MET-008 are recomputed on the baseline definition
      deadline_or_gate: 2026-07-17, and before any HG-VALUE request
      status: open
      resolved_by: []
  risks: [RSK-001]
  next_skill: 08-design-operating-model
```

What happens next is the Operations Director's call, not the agent's: approve, revise or stop the promotion (DEC-011). An agent that resumes reads the proposed DEC-011, the approved profile Decision DEC-001 and the open Evidence Debt from the workspace, not this block. If DEC-011 is approved, skill 08 plans the staged rollout within the L2 ceiling (skill 29), has skill 26 pre-register evaluations for the general inbox, and verifies the rollout gates before each stage; either way, skill 09 reads evidence period 2, including MET-001, before anyone asks for `HG-VALUE`.

## Check it

From the AITM-SMB folder:

```bash
python3 tools/validate.py --engagement examples/compact-scenario-b
```

The check confirms that every referenced ID is defined exactly once with a registered prefix, that the minimum valid path and the core trace links exist, that every approved Outcome and active Initiative is backed by an approved gate Decision naming the human, and that AI authority above L0 has an `HG-AUTHORITY` Decision. It does not judge whether the diagnosis is right; that is what the review aids in [`rubrics/`](../../rubrics/) and skill 38 are for.
