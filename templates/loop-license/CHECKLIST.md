# The Loop License — one-page checklist

*From [The Agentic Product Standard](../../STANDARD.md), Part IV. Run this against a real deployment, with the team in the room, before an agent runs **unattended** (Autonomy Ladder L3+). Every box is binary — a half-met control is a No. One unchecked box means the system stays at L2 (human-in-the-loop), no matter how good the model is.*

## The six gates — all six, or no license

- [ ] **1. Eval pass-rate threshold.** A named minimum pass rate on a representative eval set, measured *before* promotion. State the number and the set.
- [ ] **2. Regression gate.** CI blocks promotion when the pass rate drops against the recorded baseline. A loop that can silently regress has no license.
- [ ] **3. Declared blast radius.** The maximum scope one unattended run can affect — files, records, spend, external calls, tenants — written down and enforced *below the model*, never asserted by it.
- [ ] **4. Cost cap.** A per-run and per-window token/spend ceiling, enforced in code, that halts the loop.
- [ ] **5. Kill switch.** An out-of-band control that stops the loop mid-flight without a redeploy, reachable by a human who is not the agent.
- [ ] **6. Escalation path.** A named human (or higher-authority system) the loop hands to on repeated failure, on a stop condition, or on any action outside the declared blast radius.

## The teeth — what makes the six real

- [ ] **Stop conditions declared** in the Agent Contract and enforced by the runner: max iterations · token/time/spend budgets · timeout · escalation after N consecutive failures.
- [ ] **Independent verification.** The producing model does **not** grade its own work. Deterministic checks first; any LLM judge is calibrated (TPR/TNR tracked) and decorrelated from the writer (different model or materially different prompt/context; sees the artifact, not the writer's reasoning).
- [ ] **Ingestion boundary.** "Find work" is treated as untrusted input: indirect-injection cases in the eval suite; instructions and data on separate channels; triggers scoped and allow-listed (OWASP LLM01).
- [ ] **Instruction supply chain.** Skills / prompts / instructions are versioned, have recorded provenance, are eval-gated before deploy, are regression-tested on update, and are audited for trigger collisions (OWASP LLM03).
- [ ] **Loop economics.** Cost per run *and* cost per **verified** outcome are tracked in traces; per-run and per-window caps are declared.
- [ ] **Architecture-phase declarations.** The memory model (what is persisted, retention, provenance, replayability) and the determinism map (which steps are deterministic vs. model-driven) were declared at design time, not reconstructed after an incident.

---

**Scoring.** All boxes Yes → the loop is licensed for unattended L3+ operation, this release. The first No is your next piece of work. Re-run every release; the score should only ratchet up.

*Definition of Done items 16–19 map to this checklist. The reference implementations of enforcement and measurement are the [AgenticProduct family](../../ECOSYSTEM.md) (AgenticGateway for cost/model, AgenticPerformance for evals/observability, AgenticAssurance for the ingestion-boundary red-team) — paved road, not a mandate (Principle 2).*
