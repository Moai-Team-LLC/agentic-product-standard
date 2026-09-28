# AITM-SMB Standard

**Version:** 1.1.0  
**Status:** Stable

AITM-SMB is an open, domain-neutral, agent-readable methodology for AI transformation of small and medium-sized businesses.

Its purpose is to redesign a business system so that people, processes, decisions, information, software, automation, and AI jointly produce a measurable business result.

---

## 1. Core thesis

> The unit of AI transformation is the Business Capability, not the AI use case.

AITM-SMB begins with business Outcomes and organizational Capabilities.

AI is one possible intervention family.

---

## 2. Canonical transformation chain

```text
Outcome
→ Capability
→ Current State
→ Gap
→ Cause
→ Intervention
→ Initiative
→ Capability Target State
→ Target Operating Architecture
→ Transition State
→ Pilot / Transformation Slice
→ Rollout
→ Operating Model
→ Metric
→ Evidence
→ Value Realization
→ Evolution
```

The chain MAY be traversed iteratively, but material decisions MUST remain traceable.

---

## 3. Core invariants

AITM-SMB applications MUST preserve these invariants:

### INV-01 — Outcome before technology

A transformation begins with a measurable business Outcome, not a tool or vendor.

### INV-02 — Capability over use case

The primary transformation object is a Business Capability.

### INV-03 — Diagnosis before solution

A Symptom MUST NOT be converted directly into a solution.

Preferred chain:

```text
Observation
→ Symptom
→ Capability Gap
→ Cause Hypothesis
→ Evidence
→ Validated Cause
→ Intervention
```

### INV-04 — Evidence over assumption

Facts, Evidence, Assumptions, Hypotheses, Decisions, and Open Questions MUST remain distinguishable.

### INV-05 — AI is optional

An intervention may be process, role, decision, data, knowledge, software, deterministic automation, AI, control, or feedback redesign.

Intervention families: `PUBLIC_API.md` §6, defined in `design/INTERVENTION_PATTERNS.md`.

### INV-06 — AI usefulness is separate from AI authority

A strong AI fit does not imply that AI should act autonomously.

### INV-07 — Authority is explicit and revocable

AI authority MUST be granted explicitly, bounded, observable, and reducible.

### INV-08 — Architecture before vendors

Target behavior and system boundaries SHOULD be defined before vendor selection unless a vendor is already a fixed constraint.

### INV-09 — Optimize the system

Local capability improvement MUST be checked for upstream, downstream, shared-resource, incentive, and Constraint Migration effects.

### INV-10 — Transition states are operable

Material transformation SHOULD move through independently operable intermediate states when direct transition creates excessive uncertainty or risk.

### INV-11 — Evidence before scale

Material uncertainty SHOULD be reduced through experiments, shadow execution, or bounded pilots before wider rollout.

### INV-12 — Deployment is not transformation

A deployed system is not considered transformed until operating behavior changes and effect can be measured.

### INV-13 — AI quality is not business value

AI evaluation metrics do not substitute for business Outcome metrics.

### INV-14 — Every material decision is traceable

Selected Initiatives MUST link to Outcomes, Capabilities, Gaps, Interventions, Metrics, and Evidence.

### INV-15 — Proportionality over bureaucracy

Only artifacts and modules that improve a decision, control a risk, preserve traceability, or produce necessary Evidence SHOULD be activated.

---

## 4. System model

A relevant Capability SHOULD be examined across:

```text
People
Decision Rights
Process
Data
Knowledge
Applications
Automation
AI
Controls
Metrics
Economics
Feedback
```

The methodology models only what is necessary for the transformation boundary.

---

## 5. Intervention logic

The challenge order over the intervention families (`PUBLIC_API.md` §6; definitions: `design/INTERVENTION_PATTERNS.md`).

Before recommending AI, consider:

```text
ELIMINATE
→ SIMPLIFY
→ STANDARDIZE
→ INSTRUMENT
→ INTEGRATE
→ AUTOMATION (deterministic)
→ AI_ASSIST
→ AI_AUTOMATE
→ AI_AUGMENT
→ AI_AUTONOMIZE
```

This is a challenge sequence, not a mandatory implementation sequence.

PROCESS, ROLE, DECISION, DATA, KNOWLEDGE, SOFTWARE, CONTROL, and FEEDBACK have no position in this order; consider them wherever the diagnosed Cause points to them (INV-05).

Challenge questions: `DECISION_MODEL.md` §1.

---

## 6. AI autonomy ladder

```text
L0 — No AI
L1 — Suggest
L2 — Draft
L3 — Execute with explicit approval
L4 — Execute within bounded policy
L5 — Pursue bounded objective and escalate exceptions
```

Authority definitions per level: `diagnostics/AUTONOMY_SUITABILITY.md` §2.

The level is assessed per action class of a Capability, not per system.

These are authority levels. They are not maturity levels (`maturity/MATURITY_MODEL.md` uses M0–M5) and not software-architecture levels. Where another ladder is in use, write `AITM-L<n>` (crosswalk: `docs/crosswalk-agentic-product-standard.md`).

An `AI_*` intervention family names the kind of AI contribution; authority is set only by the autonomy level.

Granting or increasing authority requires HG-AUTHORITY (§8).

Higher autonomy requires stronger:

```text
policy clarity
permission precision
observability
evaluation
recoverability
exception detection
business justification
```

---

## 7. Architecture abstraction levels

AITM-SMB distinguishes two target design levels.

### Capability Target State

Future behavior of one Business Capability.

### Target Operating Architecture

Integrated future operating system across relevant Capabilities.

These concepts MUST NOT be merged.

---

## 8. Human decision gates

Explicit human approval is required at each gate:

| Gate ID | Human approval is required before |
|---|---|
| `HG-OUTCOME` | approving transformation Outcomes |
| `HG-INITIATIVE` | selecting material Initiatives |
| `HG-TOA` | approving the Target Operating Architecture (in Compact: the Capability Target States) |
| `HG-DECISION-RIGHTS` | changing material Decision Rights |
| `HG-AUTHORITY` | granting or increasing AI authority (any autonomy level above L0, including an Authority Ceiling) |
| `HG-RISK` | accepting material customer, financial, security, legal, or operational risk |
| `HG-BUDGET` | committing material budget |
| `HG-PROMOTION` | promoting a material pilot to rollout |
| `HG-VALUE` | declaring value realized (value state REALIZED or SUSTAINED) |

Rules:

- A gate applies whenever its trigger occurs, in any phase.
- Approval is recorded as a Decision (`DEC-###`, `artifacts/decision-assumption-log.md`) with `gate:` set and `approved_by:` naming the human.
- An agent that reaches an open gate stops with status `HUMAN_DECISION_REQUIRED` (`PUBLIC_API.md` §8) and lists the gate in `open_gates`.
- Reducing AI authority (demotion) never requires a gate and MAY be done immediately by the operating owner.
- Materiality: §16.

Other files reference gates by ID and MUST NOT restate this list.

---

## 9. Measurement

Every material Initiative MUST define at least one business or capability metric.

AITM-SMB distinguishes these metric classes (defined in `METRICS.md`):

```text
Business Outcome Metrics
Capability Metrics
Operating Metrics
AI Evaluation Metrics
Economic Metrics
Risk / Governance Metrics
```

Lower-level metrics explain performance but do not replace business Outcomes.

---

## 10. Execution

The preferred implementation unit is a vertical **Transformation Slice** (`SLC-###`; `execution/DELIVERY_SLICE.md`):

```text
bounded behavior change
+ required process / role change
+ required data / application change
+ automation / AI where justified
+ controls
+ metrics
+ evaluation
```

Technical components MAY be delivered separately when they are explicit prerequisites.

---

## 11. Value realization

AITM-SMB distinguishes value states (defined in `measurement/VALUE_REALIZATION.md` §2):

```text
HYPOTHESIZED
→ OBSERVED
→ ATTRIBUTED
→ REALIZED
→ SUSTAINED
```

Declaring REALIZED or SUSTAINED requires HG-VALUE (§8).

A transformation is not complete merely because a system is deployed or adopted.

---

## 12. Application profiles

AITM-SMB uses composable profiles:

```text
Compact
Standard
Governed
Portfolio
Measured
```

Profile depth is determined by complexity, risk, authority, and change load—not by employee count alone.

See `APPLICATION_PROFILES.md`.

---

## 13. Domain neutrality

AITM-SMB Core MUST NOT depend on:

```text
a specific company
a specific industry
a specific product
a specific cloud
a specific AI provider
a specific software stack
a specific consulting engagement
```

Specialization belongs in Extensions (`EXTENSION_MODEL.md`).

---

## 14. Conformance

An application conforms to AITM-SMB only when it preserves the core semantic chain (§2), the MUST invariants (§3), and the selected profile requirements (`CONFORMANCE.md` §3).

Template completion alone is not conformance.

Waiving a §3 MUST makes the application non-conforming for that invariant; the waiver is recorded as an exception (`CONFORMANCE.md` §6).

See `CONFORMANCE.md`.

---

## 15. Agent execution

AI agents MUST follow:

```text
NORMATIVE_INDEX.md
AGENT_CONTEXT_POLICY.md
AGENTS.md
AGENT_OUTPUT_STANDARD.md
```

Agents MUST NOT silently convert inference into business fact or cross a human decision gate (§8).

---

## 16. Materiality

An item is **material** when being wrong about it could change an approved Outcome, or could create customer, financial, legal, security, or AI-authority exposure that the accountable Outcome owner would expect to decide personally.

The Outcome owner MAY record explicit materiality thresholds as a Decision in Phase 0.

When materiality is unclear, treat the item as material.

Agents MUST NOT classify an item as immaterial to avoid a gate.

---

## 17. Normative language

```text
MUST      mandatory
MUST NOT  prohibited
SHOULD    recommended unless explicitly justified otherwise
MAY       optional
```
