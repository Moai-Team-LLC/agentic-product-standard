# Crosswalk: AITM-SMB and the Agentic Product Standard

**Status:** Informative. This crosswalk is not an Extension ([`EXTENSION_MODEL.md`](../EXTENSION_MODEL.md) §5) and adds no requirement to either standard. Where it summarizes a rule, the source text governs: for AITM-SMB, the files linked here; for the Agentic Product Standard (APS), its [STANDARD.md](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/main/STANDARD.md) and [CONTEXT.md](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/main/CONTEXT.md). APS names and Definition of Done (DoD) numbers below follow APS 4.0.0; §7 explains how to read this against APS 3.x.

## 1. Two standards, two questions

| | AITM-SMB | Agentic Product Standard |
|---|---|---|
| Question | Which business Capability should change, whether AI belongs in that change, how much authority AI may hold, and whether the business improved | How to build, evaluate, secure, and operate the AI component once it is wanted |
| Unit | Business Capability; authority per action class | the agentic product and its agents |
| Decides | Intervention type, authority level, Authority Ceiling, pilot evidence, value | operating point (autonomy level × oversight mode), composition pattern, harness, eval gates, Loop License |
| Human role | human decision gates (`HG-*`, [`STANDARD.md`](../STANDARD.md) §8) | per-action approval at oversight O0; live supervision at O1; approval of destructive actions at every mode |

## 2. One authority ladder, two APS axes

AITM-SMB and APS both number levels from L0. They answer different questions, and a level on one implies nothing about a level of the same number on the other.

- **AITM-SMB L0–L5: business authority.** What the AI may do in the business, for one action class of a Capability. Defined in [`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §2; granted only through `HG-AUTHORITY`.
- **APS autonomy L0–L4: who chooses the next step** in the AI component (single call, augmented LLM, workflow, bounded decomposition, autonomous agent loop). APS STANDARD.md, Canon 1.
- **APS oversight O0–O2: whether a human approves each consequential action** (APS permission tier P3 and above: external write, financial, communication, destructive). O0 is human in the loop, O1 human on the loop, O2 unattended. APS STANDARD.md, Canon 1; [APS ADR-0004](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/main/docs/adr/0004-autonomy-and-oversight-axes.md).

APS calls the pair a system runs at its **operating point**, written `L3 · O0`.

AITM authority corresponds to the APS **oversight** axis, not to APS autonomy. Up to AITM-L3 a human performs, releases or approves every consequential action, which is APS O0. AITM-L4 and L5 act without per-action approval, which is APS O1 or O2. The APS autonomy level is a build choice that AITM-SMB does not constrain.

Write **AITM-L*n*** and **APS-L*n*** / **APS-O*n*** whenever both appear in one text, record or conversation, for example "AITM-L3 authority built at APS `L2 · O0`".

Two illustrations of independence:

- An APS-L0 classifier whose output a deterministic router applies within a written policy runs at APS O1 or O2 and holds AITM-L4 authority for that action class.
- An APS-L4 research loop whose only output is a report that a human reviews and releases runs at APS O0 and holds AITM-L2.

None of these is a maturity scale. AITM-SMB's informative [`maturity/MATURITY_MODEL.md`](../maturity/MATURITY_MODEL.md) (M0–M5) and the APS [SCORECARD.md](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/main/SCORECARD.md) (M0–M3) share letters, not meanings.

## 3. Which APS obligations bind at which AITM level

Both sets of obligations apply at once: AITM-SMB's to the business authority, APS's to the build.

| AITM authority | Human in the action path | APS oversight | Typical APS autonomy | APS obligations that carry it |
|---|---|---|---|---|
| AITM-L0 — No AI | no AI in the path | — | — | none |
| AITM-L1 — Suggest | a human decides and acts | O0; the AI holds no consequential permission | L0–L1 | those of the component's autonomy level |
| AITM-L2 — Draft | a human reviews and releases every work product | O0 | L0–L2 | release is a per-action approval: the Human-in-the-Loop layer (Canon 4), as a durable pause (Stack 5, "Human-in-the-loop is a durable pause, not a side channel"); approval run as a program (DoD 33) |
| AITM-L3 — Execute with explicit approval | a human approves each specific action before it executes | O0 | any | as for AITM-L2; per-action approval is the control (DoD 4); "Permissions enforced by code, not by prompt" (DoD 5); stop conditions (DoD 17) when the build is at APS-L3 or above |
| AITM-L4 — Execute within bounded policy | none per action; out-of-policy cases escalate | O1 or O2 | any, including an APS-L2 pipeline that auto-applies its output | the Loop License at any autonomy level (Part IV; DoD 16–19); at O2 also the success-legitimacy audit (DoD 30); the oversight plan (DoD 33) |
| AITM-L5 — Pursue bounded objective and escalate exceptions | humans supervise outcomes, not steps; exceptions escalate | O1 or O2 | usually L3–L4 | as for AITM-L4, with stop conditions, independent verification and loop economics (Part IV; DoD 17–19); the Graph License when agents form a graph (DoD 25) |

Four consequences:

1. **AITM-L0 to L3 keep a human in every consequential action**, performing, releasing or approving it. That is APS O0: the Loop License is recommended, not required, and the human approval is itself the control, which APS asks to be run as a program with override rates, approval latency and a rubber-stamp alarm (DoD 33).
2. **AITM-L4 and L5 act without per-action approval.** That is APS O1 or O2, and APS binds its Loop License there at any autonomy level (Part IV: "Everything in this Part binds at O1+"). An AITM-L4 grant built as a simple workflow still owes the license.
3. **APS limits hold whatever AITM-SMB grants.** "All destructive actions require explicit human approval — at every oversight mode, O2 included" (DoD 4), so in an APS-conformant build a destructive action class operates at AITM-L3 at most, which an Authority Ceiling expresses in `approval_required`. A system that misses any Loop License gate is capped at O0, so an AITM-L4 or L5 grant cannot run without per-action approval until the license holds.
4. **No APS operating point grants business authority.** Running at O1 or O2 needs an approved `HG-AUTHORITY` Decision for AITM-L4 or L5 on that action class.

## 4. Artifact and field map

The AITM-SMB record states what is allowed; the APS declaration enforces it in the build, "below the model".

| AITM-SMB record and field | APS counterpart | Note |
|---|---|---|
| Authority level of an action class (`current_level`, [`artifacts/autonomy-assessment.md`](../artifacts/autonomy-assessment.md)) | the oversight mode of the operating point (Canon 1; Part IV, Architecture-phase declarations) | AITM-L1–L3 → O0; AITM-L4–L5 → O1 or O2 |
| Authority Ceiling: `maximum_allowed_level`, `prohibited_actions`, `approval_required` ([`artifacts/autonomy-assessment.md`](../artifacts/autonomy-assessment.md)) | Loop License gate 3, declared blast radius; permissions enforced by code (DoD 5); least privilege (Stack 8) | "No technical implementation, pilot, rollout stage, or promotion may exceed the approved ceiling" ([`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §6) |
| `escalation_conditions` and the accountable `owner` (Autonomy Assessment, AI Governance Canvas) | Loop License gate 6, escalation path; escalation after N consecutive failures (Part IV, Stop conditions & fail paths) | APS asks for a named human; AITM-SMB names the accountable owner |
| AI Governance Canvas `cost_limit` | Loop License gate 4, cost cap; Stack 9 (Cost & FinOps); DoD 15 and 19 | |
| AI Governance Canvas `stop_conditions`; revocability (INV-07, a core invariant in [`STANDARD.md`](../STANDARD.md) §3) | Loop License gate 5, kill switch; stop conditions (Part IV; DoD 17) | stop controls |
| AI Governance Canvas `recovery_path` | fail paths (Part IV); durable execution (Stack 5; DoD 7) | rollback and recovery, not a stop control |
| AI Governance Canvas `permissions`, `data_access`, `tool_access` | Stack 8 (Security & Identity): agent identity, least privilege (DoD 27); lethal-trifecta check (DoD 13) | |
| AI evaluations in [`artifacts/evaluation-plan.md`](../artifacts/evaluation-plan.md) (layers `ai_task`, `human_ai`, `technical`) and its `datasets` ([`evaluation/EVALUATION_DATASET.md`](../evaluation/EVALUATION_DATASET.md)) | golden set with labeling provenance (Part V, Ground-truth discipline; DoD 22); Loop License gates 1–2, eval threshold (pass@1 and pass^5) and regression gate; DoD 10–12 | AITM-SMB pre-registers business-relevant thresholds; the APS golden set and eval gate implement them |
| [`artifacts/observability-plan.md`](../artifacts/observability-plan.md): `ai_signals`, `traces`, `cost_signals` | harness Layers 6–7 (Evaluation; Observability & Tracing); Stack 6 (Observability & Evals); DoD 12 and 29 | |
| [`artifacts/incident-record.md`](../artifacts/incident-record.md) and demotion ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §4) | kill switch; re-escalation triggers of the oversight plan (Part V, Human oversight as a program); "Every new failure mode becomes a permanent regression test" (Part V, Eval rules), matching the incident's `eval_case_added` | AITM-SMB demotion needs no gate |
| AI Change records ([`governance/AI_CHANGE_CONTROL.md`](../governance/AI_CHANGE_CONTROL.md)) | the instruction supply chain (Part IV): versioned, with provenance, evaluated before deploy | |

## 5. The hand-off

AITM-SMB decides **whether and how much** AI; APS decides **how to build and license** it.

Before APS design starts, AITM-SMB has typically settled:

- a selected Intervention of an `AI_*` type ([`artifacts/intervention-map.md`](../artifacts/intervention-map.md)) inside an approved Initiative (`HG-INITIATIVE`);
- its AI Suitability Assessment ([`artifacts/ai-suitability-assessment.md`](../artifacts/ai-suitability-assessment.md)) and Autonomy Assessment, with an Authority Ceiling approved through `HG-AUTHORITY`;
- the Capability Target State that describes what the AI does in the target behavior ([`artifacts/capability-target-state.md`](../artifacts/capability-target-state.md));
- the pilot and its pre-registered evaluation, where a pilot is planned;
- the AI Governance Canvas fields the active profile requires, at least the Governance minimum ([`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md) §3).

In phase terms ([`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §1), this is usually after the Target State is approved in phase 5 and while the pilot is designed in phase 6. APS then declares the operating point (Part IV, Architecture-phase declarations): the lowest autonomy level that does the job, climbing only on eval evidence, and the oversight mode that matches the approved AITM authority. It then chooses the composition patterns (Canon 2), the harness (Canon 4) and the eval program (Part V), and, at O1 or O2, the Loop License (Part IV).

What flows back into AITM-SMB:

- **Eval results and traces become Evidence.** APS eval results (pass@1, pass^5, the legitimacy rate at O2), judge calibration status and traces are recorded as Evidence ([`evidence/EVIDENCE_STANDARD.md`](../evidence/EVIDENCE_STANDARD.md) §3) and as results in the Evaluation Plan. They show AI quality, not business value (INV-13).
- **Approval-program metrics show whether human approval is real.** Override rates, approval latency and rubber-stamp alarms (DoD 33) are Evidence for AITM-L2 and L3 authority and for the promotion criteria ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3). An approval nobody reads is not a control.
- **Loop License status can be an input to Gates C and E.** Whether the six gates are declared, enforced and tested can inform Execution Gate C (Pilot Ready) and Gate E (Rollout Ready) ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md) §2), and a grant of AITM-L4 or L5 ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3).
- **Failures become Incidents.** Kill-switch events, regressions and failures in operation become Incident records; a matching demotion trigger lowers authority.
- **Loop economics feed economic Metrics.** Cost per run and cost per verified outcome (Part IV, Economics of the loop) feed the economic Metrics of the scorecard ([`METRICS.md`](../METRICS.md) §8), which test the economic hypothesis ([`economics/TRANSFORMATION_ECONOMICS.md`](../economics/TRANSFORMATION_ECONOMICS.md) §5).

Neither replaces the other:

- An APS Loop License grants no business authority; only a Decision closing `HG-AUTHORITY` does.
- An `HG-AUTHORITY` approval licenses no operation without per-action approval; only the Loop License does.
- A passing APS eval gate is not business value; `HG-VALUE` needs business Evidence.

## 6. Words that differ

| Word | AITM-SMB | APS |
|---|---|---|
| gate | a human decision gate (`HG-*`, [`STANDARD.md`](../STANDARD.md) §8), or an Execution Gate A–G, an evidence checkpoint on an Initiative ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md)) | usually a check in code or CI: eval gate, regression gate, the six Loop License gates |
| evaluation | an Evaluation record across eight layers, business Outcome first ([`evaluation/EVALUATION_SYSTEM.md`](../evaluation/EVALUATION_SYSTEM.md) §2) | the eval set and eval pyramid of the AI component (Part V) |
| escalation | a case handed to a human (`escalation_conditions`); also the promotion and demotion of authority ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md)) | the escalation path to a human (Loop License gate 6); the escalation rules for climbing autonomy and relaxing oversight (Canon 1) |
| L3 | Execute with explicit approval (authority) | Bounded decomposition (autonomy); formerly Orchestrator-Worker |
| oversight | not a ladder of its own: carried by the authority levels and human decision gates | the O0–O2 axis of the operating point |
| harness | not used | everything around the LLM loop (Canon 4) |

## 7. Reading this against APS 3.x

APS 3.0 to 3.3 had one ladder, L0–L4, and bound the Loop License to "L3+ unattended" ([APS 3.3.1 STANDARD.md](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/v3.3.1/STANDARD.md), Part IV). Under 3.x:

- AITM-L0 to L3 map as in §3: a human is in every consequential action.
- An AITM-L4 or L5 grant built at APS-L3 or L4 owes the Loop License.
- An AITM-L4 or L5 grant built at APS-L0 to L2 carries no Loop License obligation from APS 3.x ("recommended, not required"). AITM-SMB's own requirements still apply: the authority definition of the level, the observability, verification, exception-detectability and recovery dimensions of the assessment ([`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §2–§3), and the AI Governance Canvas.

APS 4.0 closes that gap by binding the Loop License on oversight (APS ADR-0004).
