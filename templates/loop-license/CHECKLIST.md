# The Loop License — one-page checklist

*From [The Agentic Product Standard](../../STANDARD.md), Part IV. Run this against a real deployment, with the team in the room, before a system's consequential actions run **without a human approving each one** — oversight **O1** (human on the loop) or **O2** (unattended), at any autonomy level. Every box is binary — a half-met control is a No. One unchecked box means the system stays at **O0** (a human approves each consequential action), no matter how good the model is.*

**Operating point being licensed:** `L_ · O_` — the system's autonomy level and the oversight mode requested.

## The six gates — all six, or no license

- [ ] **1. Eval threshold.** Named minimums on a representative eval set, measured *before* promotion: **pass@1** and **pass^5** (all five of five attempts succeed). At **O2**, also the **legitimacy-rate** floor from the audit below. State the numbers and the set.
- [ ] **2. Regression gate.** CI blocks promotion when the pass rate drops against the recorded baseline. A loop that can silently regress has no license.
- [ ] **3. Declared blast radius.** The maximum scope one run can affect — files, records, spend, external calls, tenants — written down and enforced *below the model*, never asserted by it. Strongest form: the agent runs read-only and emits typed action requests that a deterministic applier validates and executes ([`safe-outputs`](../safe-outputs/README.md)). Destructive (P6) actions still require explicit human approval.
- [ ] **4. Cost cap.** A per-run and per-window token/spend ceiling, enforced in code, that halts the loop.
- [ ] **5. Kill switch.** An out-of-band control that stops the loop mid-flight without a redeploy, reachable by a human who is not the agent.
- [ ] **6. Escalation path.** A named human (or higher-authority system) the loop hands to on repeated failure, on a stop condition, or on any action outside the declared blast radius.

## The teeth — what makes the six real

- [ ] **Stop conditions declared** in the Agent Contract and enforced by the runner: max iterations · token/time/spend budgets · timeout · escalation after N consecutive failures.
- [ ] **Independent verification.** The producing model does **not** grade its own work. Deterministic checks first; any LLM judge is calibrated (TPR/TNR tracked) and decorrelated from the writer (different model or materially different prompt/context; sees the artifact, not the writer's reasoning). **The checks are out of the agent's reach** — it cannot modify its tests, graders, eval sets, or thresholds.
- [ ] **Success-legitimacy audit (O2).** Each release, a stratified sample of *successful* runs is reviewed for illegitimate success (edited or skipped tests, special-cased graders, hard-coded outputs); the legitimacy rate is published next to pass@1 and pass^5 and gates promotion (Part IV · DoD 30).
- [ ] **Ingestion boundary.** "Find work" is treated as untrusted input: indirect-injection cases in the eval suite; instructions and data on separate channels; triggers scoped and allow-listed (OWASP LLM01).
- [ ] **Instruction supply chain.** Skills / prompts / instructions are versioned, have recorded provenance, are eval-gated before deploy, are regression-tested on update, and are audited for trigger collisions (OWASP LLM03). Skills are valid against the Agent Skills specification, scanned for hidden content, and hash-locked.
- [ ] **Loop economics.** Cost per run *and* cost per **verified** outcome are tracked in traces; per-run and per-window caps are declared.
- [ ] **Architecture-phase declarations.** The operating point, the memory model (what is persisted, retention, provenance, replayability) and the determinism map (which steps are deterministic vs. model-driven) were declared at design time, not reconstructed after an incident.
- [ ] **Human-oversight plan.** A sampling schedule per oversight mode, a reviewer SLA, and automatic re-escalation triggers (a regression-gate failure or override-rate spike drops the loop to the previous mode); human reviews are captured as stratified labeled data — escalations *plus* a random routine sample; override rate and approval latency are tracked, with a rubber-stamp alarm (Part V, *Human oversight as a program*).

---

**Scoring.** All boxes Yes → the system is licensed to run at the requested oversight mode, this release (the legitimacy-audit box is N/A at O1). The first No is your next piece of work. Re-run every release; the score should only ratchet up.

*Definition of Done items 16–19 and 30 (at O2) map to this checklist — in an `aps-conformance.yaml` they are the `loop.*` scorecard items — and so does the O1+ part of item 33, the human-oversight plan (`meas.oversight-plan`; its automation-bias half, `meas.automation-bias`, binds at every mode). The reference implementations of enforcement and measurement are the [AgenticProduct family](../../ECOSYSTEM.md) (AgenticGateway for cost/model, AgenticPerformance for evals/observability, AgenticAssurance for the ingestion-boundary red-team) — paved road, not a mandate (Principle 2).*
