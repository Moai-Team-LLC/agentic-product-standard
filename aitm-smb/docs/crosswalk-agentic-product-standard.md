# Crosswalk: AITM-SMB and the Agentic Product Standard

**Status:** Informative. This crosswalk is not an Extension ([`EXTENSION_MODEL.md`](../EXTENSION_MODEL.md) §5) and adds no requirement to either standard. Where it summarizes a rule, the source text governs: for AITM-SMB, the files linked here; for the Agentic Product Standard (APS), its [STANDARD.md](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/main/STANDARD.md) and [CONTEXT.md](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/main/CONTEXT.md). APS section names below follow APS STANDARD.md v3.3.

## 1. Two standards, two questions

| | AITM-SMB | Agentic Product Standard |
|---|---|---|
| Question | Which business Capability should change, whether AI belongs in that change, how much authority AI may hold, and whether the business improved | How to build, evaluate, secure, and operate the AI component once it is wanted |
| Unit | Business Capability; authority per action class | the agentic product and its agents |
| Decides | Intervention type, autonomy level, Authority Ceiling, pilot evidence, value | architecture level, composition pattern, harness, eval gates, Loop License |
| Human role | human decision gates (`HG-*`, [`STANDARD.md`](../STANDARD.md) §8) | the Human-in-the-Loop harness layer; approval of destructive actions |

## 2. Two ladders, different questions

Both standards number a ladder from L0. The ladders are independent: a level on one implies nothing about the other.

- **AITM-SMB L0–L5: business authority.** What the AI may do in the business, for one action class of a Capability. Defined in [`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §2; granted only through `HG-AUTHORITY`.
- **APS L0–L4: software architecture.** How the AI component is built. Defined in APS STANDARD.md, Canon 1 (The Autonomy Ladder).

| Level | AITM-SMB (authority) | APS (architecture) |
|---|---|---|
| L0 | No AI | Single LLM call |
| L1 | Suggest | Augmented LLM |
| L2 | Draft | Workflow |
| L3 | Execute with explicit approval | Orchestrator-Worker |
| L4 | Execute within bounded policy | Autonomous Agent Loop |
| L5 | Pursue bounded objective and escalate exceptions | — |

Write **AITM-L*n*** and **APS-L*n*** whenever both appear in one text, record, or conversation, e.g. "an APS-L2 workflow operating at AITM-L3".

Two illustrations of independence:

- An APS-L0 classifier whose output a deterministic router applies within a written policy can hold AITM-L4 authority for that action class.
- An APS-L4 research loop whose only output is a report that a human reviews and releases holds AITM-L2.

Neither ladder is a maturity scale. AITM-SMB's informative [`maturity/MATURITY_MODEL.md`](../maturity/MATURITY_MODEL.md) (M0–M5) and the APS [SCORECARD.md](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/main/SCORECARD.md) (M0–M3) share letters, not meanings.

## 3. Which APS obligations bind at which AITM level

The pairings are typical, not required. Both sets of obligations apply at once: AITM-SMB's to the business authority, APS's to the build.

| AITM authority | Human in the action path | Typical APS architecture | APS obligations that carry it |
|---|---|---|---|
| AITM-L0 — No AI | no AI in the path | none | none |
| AITM-L1 — Suggest | a human decides and acts | APS-L0–L1 | those of the component's own APS level; the AI takes no action |
| AITM-L2 — Draft | a human reviews and releases every work product | APS-L0–L2 | release is a human-in-the-loop step: harness layer 5 (Canon 4); where the build waits for it, Part II Layer 5: "Human-in-the-loop is a durable pause, not a side channel" |
| AITM-L3 — Execute with explicit approval | a human approves each specific action before it executes | APS-L1–L2 | as for AITM-L2, plus "Permissions are enforced by code, not by prompt" (Canon 5; Definition of Done item 5), so an unapproved action cannot execute |
| AITM-L4 — Execute within bounded policy | none per action; out-of-policy cases escalate | APS-L2, or APS-L3+ | at APS-L3+ (unattended): the Loop License (Part IV) and Definition of Done items 16–19; at APS-L0–L2: Part IV is "recommended, not required" |
| AITM-L5 — Pursue bounded objective and escalate exceptions | humans supervise outcomes, not steps; exceptions escalate | usually APS-L3–L4 | the Loop License, stop conditions, independent verification, ingestion boundary, and loop economics (Part IV); License Composition when agents form a graph; the human-oversight plan (Part V) |

Three consequences:

1. **AITM-L0 to L3 keep a human in every consequential action**, performing, releasing, or approving it. In APS terms that human sits in harness layer 5; it is not a Loop License matter.
2. **AITM-L4 and L5 act without per-action approval.** APS binds its Loop License only at APS-L3+ (Part IV: "Everything in this Part binds at L3+"). An AITM-L4 or L5 grant built as an APS-L0–L2 system therefore carries no Loop License obligation from APS. AITM-SMB's own requirements still apply: the authority definition of the level (L4: written policy, escalation of out-of-policy cases, observable and reversible or recoverable actions; L5: an approved, bounded objective within bounded permissions, budget, and time, with exceptions escalated; [`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §2), the observability, verification, exception-detectability, and recovery dimensions of the assessment (§3), and the AI Governance Canvas ([`artifacts/ai-governance-canvas.md`](../artifacts/ai-governance-canvas.md)).
3. **APS limits hold whatever AITM-SMB grants.** APS Definition of Done item 4 ("All destructive actions require explicit human approval") applies at every APS level, so in a build that meets the APS Definition of Done a destructive action class operates at AITM-L3 at most, which an Authority Ceiling expresses in `approval_required`. And APS caps a system that misses any Loop License gate at APS-L2, "human-in-the-loop": an AITM-L4 or L5 grant built at APS-L3+ cannot run unattended until the license holds; built at APS-L0–L2, it falls under consequence 2.

## 4. Artifact and field map

The AITM-SMB record states what is allowed; the APS declaration enforces it in the build, "below the model".

| AITM-SMB record and field | APS counterpart | Note |
|---|---|---|
| Authority Ceiling: `maximum_allowed_level`, `prohibited_actions`, `approval_required` ([`artifacts/autonomy-assessment.md`](../artifacts/autonomy-assessment.md)) | Loop License gate 3, declared blast radius; permissions enforced by code (Definition of Done item 5); least privilege (Part II Layer 8) | "No technical implementation, pilot, rollout stage, or promotion may exceed the approved ceiling" ([`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §6) |
| `escalation_conditions` and the accountable `owner` (Autonomy Assessment, AI Governance Canvas) | Loop License gate 6, escalation path; escalation after N failures (Part IV, Stop conditions & fail paths) | APS asks for a named human; AITM-SMB names the accountable owner |
| AI Governance Canvas `cost_limit` (cost boundary) | Loop License gate 4, cost cap; Part II Layer 9 (Cost & FinOps); Definition of Done items 15, 19 | |
| AI Governance Canvas `stop_conditions`; revocability (INV-07, a core invariant in [`STANDARD.md`](../STANDARD.md) §3) | Loop License gate 5, kill switch; stop conditions (Part IV) | stop controls |
| AI Governance Canvas `recovery_path` | fail paths (Part IV); durable execution (Part II Layer 5) | rollback and recovery, not a stop control |
| AI Governance Canvas `permissions`, `data_access`, `tool_access` | Part II Layer 8 (Security & Identity): agent identity, least privilege; lethal-trifecta check (Definition of Done item 13) | |
| AI evaluations in [`artifacts/evaluation-plan.md`](../artifacts/evaluation-plan.md) (layers `ai_task`, `human_ai`, `technical`) and its `datasets` ([`evaluation/EVALUATION_DATASET.md`](../evaluation/EVALUATION_DATASET.md)) | golden set with labeling provenance (Part V, Ground-truth discipline); Loop License gates 1–2, eval pass-rate threshold and regression gate; Definition of Done items 10–12 | AITM-SMB pre-registers business-relevant thresholds; the APS golden set and eval gate implement them |
| [`artifacts/observability-plan.md`](../artifacts/observability-plan.md): `ai_signals`, `traces`, `cost_signals` | harness layers 6–7 (Evaluation; Observability & Tracing); Part II Layer 6 (Observability & Evals) | |
| [`artifacts/incident-record.md`](../artifacts/incident-record.md) and demotion ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §4) | kill switch; re-escalation triggers of the human-oversight plan (Part V); "Every new failure mode becomes a permanent regression test" (Part V, Eval rules), matching the incident's `eval_case_added` | AITM-SMB demotion needs no gate |
| AI Change records ([`governance/AI_CHANGE_CONTROL.md`](../governance/AI_CHANGE_CONTROL.md)) | the instruction supply chain (Part IV): versioned, with provenance, evaluated before deploy | |

## 5. The hand-off

AITM-SMB decides **whether and how much** AI; APS decides **how to build and license** it.

Before APS design starts, AITM-SMB has typically settled:

- a selected Intervention of an `AI_*` type ([`artifacts/intervention-map.md`](../artifacts/intervention-map.md)) inside an approved Initiative (`HG-INITIATIVE`);
- its AI Suitability Assessment ([`artifacts/ai-suitability-assessment.md`](../artifacts/ai-suitability-assessment.md)) and Autonomy Assessment, with an Authority Ceiling approved through `HG-AUTHORITY`;
- the Capability Target State that describes what the AI does in the target behavior ([`artifacts/capability-target-state.md`](../artifacts/capability-target-state.md));
- the pilot and its pre-registered evaluation, where a pilot is planned;
- the AI Governance Canvas fields the active profile requires, at least the Governance minimum ([`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md) §3).

In phase terms ([`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §1), this is usually after the Target State is approved in phase 5 and while the pilot is designed in phase 6. APS then chooses the lowest architecture level that does the job (Canon 1, climbing only on eval evidence), the composition patterns (Canon 2), the harness (Canon 4), the eval program (Part V), and, at APS-L3+, the Loop License (Part IV).

What flows back into AITM-SMB:

- **Eval results and traces become Evidence.** APS eval results, golden-set pass rates, judge calibration status, and traces are recorded as Evidence ([`evidence/EVIDENCE_STANDARD.md`](../evidence/EVIDENCE_STANDARD.md) §3) and as results in the Evaluation Plan. They show AI quality, not business value (INV-13).
- **Loop License status can be an input to Gates C and E.** Whether the six gates are declared, enforced, and tested can inform Execution Gate C (Pilot Ready) and Gate E (Rollout Ready) ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md) §2) and the promotion criteria ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3).
- **Failures become Incidents.** Kill-switch events, regressions, and failures in operation become Incident records; a matching demotion trigger lowers authority.
- **Loop economics feed economic Metrics.** Cost per run and cost per verified outcome (Part IV, Economics of the loop) feed the economic Metrics of the scorecard ([`METRICS.md`](../METRICS.md) §8), which test the economic hypothesis ([`economics/TRANSFORMATION_ECONOMICS.md`](../economics/TRANSFORMATION_ECONOMICS.md) §5).

Neither replaces the other:

- An APS Loop License grants no business authority; only a Decision closing `HG-AUTHORITY` does.
- An `HG-AUTHORITY` approval licenses no unattended loop; only the Loop License does.
- A passing APS eval gate is not business value; `HG-VALUE` needs business Evidence.

## 6. Words that differ

| Word | AITM-SMB | APS |
|---|---|---|
| gate | a human decision gate (`HG-*`, [`STANDARD.md`](../STANDARD.md) §8), or an Execution Gate A–G, an evidence checkpoint on an Initiative ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md)) | usually a check in code or CI: eval gate, regression gate, the six Loop License gates |
| evaluation | an Evaluation record across eight layers, business Outcome first ([`evaluation/EVALUATION_SYSTEM.md`](../evaluation/EVALUATION_SYSTEM.md) §2) | the eval set and eval pyramid of the AI component (Part V) |
| escalation | a case handed to a human (`escalation_conditions`); also the promotion and demotion of authority ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md)) | the escalation path to a human (Loop License gate 6); the escalation rule for climbing the architecture ladder (Canon 1) |
| L3 | Execute with explicit approval | Orchestrator-Worker |
| harness | not used | everything around the LLM loop (Canon 4) |
