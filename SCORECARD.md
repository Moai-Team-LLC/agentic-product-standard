# Agentic Product Self-Assessment Scorecard

*A factor-by-factor maturity check for any agentic product, scored against [`STANDARD.md`](STANDARD.md) and [`AGENT_STANDARD.md`](AGENT_STANDARD.md).*

Most standards ship principles but no way to ask *"where do we actually stand?"* This scorecard does. Answer every item **Yes / No / N-A**, then read your maturity off the gates below. It is deliberately binary — a half-met control is a No. Since v4.0 it is also machine-checkable: answer it in an `aps-conformance.yaml` with evidence for every Yes, and [`aps-conformance`](docs/conformance.md) scores it in CI and emits SARIF.

> **How to use it.** Run it on one agentic product, with the team in the room, against a real deployment (not the slide). Disagreements are the point — they surface the controls nobody owns. Re-run each release; the score should only ratchet up.

> **The paved road.** Many of these controls come satisfied out of the box if you run the recommended reference stack — the **[AgenticProduct family](ECOSYSTEM.md)**: AgenticMind (memory), AgenticOps (runtime & fleet ops), AgenticPerformance (evals & observability), AgenticGateway (model & cost plane), and AgenticAssurance (red-team the Security & Identity items). It's the fastest way to green, not a requirement — you can satisfy any item your own way (Principle 2). See the [`reference-stack`](skills/agentic-product-architect/reference-stack/SKILL.md) skill.

---

## Maturity levels (mapped to the operating envelope)

<!-- canon:begin:scorecard.bands -->
| Level | Operating envelope | Meaning |
|---|---|---|
| **M0 — Prototype** | any autonomy at O0 — no production claim | Works on a demo. No production claim. |
| **M1 — Shippable** | L0–L2 at O0 | Contracts, schemas, guardrails, an eval set, permissions in code, a declared operating point. Every consequential action is human-approved. Safe to put in front of users behind a workflow. |
| **M2 — Production** | up to L3; O1/O2 only with a Loop License | Durable, observable, tenant-isolated, security-checked, identity-scoped, cost-bounded, CI-gated on evals, on the current protocol baselines. |
| **M3 — Autonomous-ready** | L4 at any oversight mode | Online evals, `pass^k` reliability, red-team kit run, full OTel trajectory observability. Earns the right to an open-ended loop. |

**Your level is the highest band whose every applicable gate item is satisfied.** One unmet gate item caps you at the level below — there is no partial credit, and no skipping a band. The operating point you run at sets the band you must reach: L4 at any oversight mode → **M3**; L3, or any system at O1/O2 → **M2**; everything else in production → **M1**.

<!-- canon:end:scorecard.bands -->

---

## The scorecard

Each item lists the **gate level** at which it becomes mandatory and, where it applies only to some products, the condition (e.g. *if MCP*, *O1+*). The small print carries the item's stable **id** — what an [`aps-conformance.yaml`](docs/conformance.md) answers — and the Definition of Done items it evidences (`STANDARD.md` Part III). Every DoD item is evidenced by at least one scorecard item; CI checks it.

*This section is generated from [`canon/scorecard.yaml`](canon/scorecard.yaml). Edit the canon, then run `python3 tools/aps.py render`.*

<!-- canon:begin:scorecard.items -->
### Architecture & contracts
- [ ] **(M1)** The operating point is declared — autonomy level (L0–L4) and oversight mode (O0–O2) — and matches what runs in production. <sub>`arch.operating-point`</sub>
- [ ] **(M1)** The system uses the least autonomous architecture sufficient for the task. <sub>`arch.least-autonomy`</sub>
- [ ] **(M1)** Every agent has an Agent Contract; every tool a Tool Contract. <sub>`arch.contracts`</sub>
- [ ] **(M1)** Acceptance criteria are *hard-to-vary*: each names the single probe that falsifies it. <sub>`arch.hard-to-vary`</sub>
- [ ] **(M2)** Each climb in autonomy was earned by pass@1 ≥ 90% at the level below; each relaxation of oversight by the Loop License's pass^5 threshold. <sub>`arch.earned-autonomy`</sub>
- [ ] **(M2, if multi-agent)** Multi-agent is an orchestrator with isolated subagents — not a peer-to-peer bus. <sub>`arch.orchestrator`</sub>

### Context & state
- [ ] **(M1)** Context stays within a measured budget in a typical cycle (40% of the window until you have measured it). <sub>`ctx.budget` · DoD 1</sub>
- [ ] **(M1)** State is externalized — not held only in the context window or in a protocol session. <sub>`ctx.state` · DoD 2</sub>
- [ ] **(M2)** Compaction is tested on long-running scenarios; sub-agent outputs are condensed. <sub>`ctx.compaction` · DoD 3</sub>

### Tools & permissions
- [ ] **(M1)** Tools are allow-listed; active count < 20 per agent (or RAG-over-tools). <sub>`tools.allowlist`</sub>
- [ ] **(M1)** Tool inputs are schema-validated; permissions enforced in **code**, not prompt. <sub>`tools.permissions` · DoD 5</sub>
- [ ] **(M1)** Consequential (P3+) actions require human approval — or, at O1+, stay inside the Loop License's declared blast radius; destructive (P6) actions require approval at every oversight mode. <sub>`tools.approval` · DoD 4</sub>
- [ ] **(M2)** Tool execution is sandboxed (containers / OAuth scopes / least privilege). <sub>`tools.sandbox` · DoD 6</sub>

### Security & identity
- [ ] **(M2)** Lethal-trifecta check performed and documented; if all three legs present, one is broken. <sub>`sec.trifecta` · DoD 13</sub>
- [ ] **(M2, if MCP)** MCP tool definitions pinned by hash with change alerts, re-verified whenever a cached tool list expires; servers from an allow-listed registry, version-pinned + signature-checked. <sub>`sec.mcp-pinning` · DoD 14</sub>
- [ ] **(M2, if MCP)** Every MCP connection speaks revision 2026-07-28 (or carries a dated sunset); no state rides on a protocol session; no new use of Roots / Sampling / Logging; `requestState` is treated as untrusted input. <sub>`sec.mcp-baseline` · DoD 26</sub>
- [ ] **(M2, if MCP)** MCP clients register with Client ID Metadata Documents (not Dynamic Client Registration alone), validate `iss` (RFC 9207), and key stored credentials by issuer; servers never pass tokens through. <sub>`sec.mcp-auth` · DoD 26</sub>
- [ ] **(M2, if MCP)** The official MCP conformance suite runs in CI, at a pinned version, against every MCP server and client you own. <sub>`sec.mcp-conformance` · DoD 26</sub>
- [ ] **(M2)** OAuth 2.1 scoped, short-lived, audience-bound tokens; no token passthrough; no over-scoping. <sub>`sec.tokens` · DoD 27</sub>
- [ ] **(M2)** Each agent acts under its own least-privilege non-human identity — no shared service account; identity & tenant derived from auth, never the model. <sub>`sec.identity` · DoD 27</sub>
- [ ] **(M2)** Every action is attributable in traces to the agent identity that took it and to the human or system that delegated it. <sub>`sec.attribution` · DoD 27</sub>
- [ ] **(M3)** Indirect prompt injection (poisoned docs / tool output) is in the threat model and red-team tested. <sub>`sec.indirect-injection`</sub>

### Tenant isolation *(if multi-tenant)*
- [ ] **(M2)** `tenant_id` derived from auth only; no-tenant requests fail closed. <sub>`tenant.auth-derived` · DoD 32</sub>
- [ ] **(M2)** Isolation enforced below the LLM (RLS / repository layer); survives prompt injection. <sub>`tenant.below-llm` · DoD 32</sub>
- [ ] **(M2)** Retrieval, memory, cache keys (including MCP `private`-scoped results), traces, sub-agent messages, and jobs are all tenant-scoped. <sub>`tenant.scoped-paths` · DoD 32</sub>
- [ ] **(M2)** A code-asserted cross-tenant leakage eval runs in CI. <sub>`tenant.leakage-eval` · DoD 32</sub>

### Cost
- [ ] **(M2)** Per-run token/cost ceiling enforced in code (circuit breaker on runaway sessions). <sub>`cost.ceiling` · DoD 15</sub>
- [ ] **(M2)** Prompt/KV caching enabled on stable prefixes; cost-per-task tracked in traces. <sub>`cost.caching` · DoD 15</sub>
- [ ] **(M2)** Ceilings and routing are re-derived from measured cost per task whenever the model or provider changes. <sub>`cost.model-swap` · DoD 15</sub>
- [ ] **(M2, if multi-agent)** For multi-agent, the task value justifies the ~15× token cost. <sub>`cost.multi-agent`</sub>

### Reliability
- [ ] **(M2)** Durable execution: pause / resume / retry survives a killed process. <sub>`rel.durable` · DoD 7</sub>
- [ ] **(M1)** Structured outputs validated by schema; assertions on the critical path. <sub>`rel.schema` · DoD 8</sub>
- [ ] **(M1)** Guardrails (schema, PII, jailbreak, indirect-injection, egress) on input and output. <sub>`rel.guardrails` · DoD 9</sub>

### Evals & observability
- [ ] **(M1)** Eval set ≥ 50 examples per top-priority failure mode; built from real traces. <sub>`eval.set` · DoD 10</sub>
- [ ] **(M2, if LLM judges)** LLM judges are binary and calibrated against human labels (TPR/TNR tracked). <sub>`eval.judges` · DoD 11</sub>
- [ ] **(M2)** CI blocks deploy on eval regression; 100% of production runs traced. <sub>`eval.ci-gate` · DoD 12</sub>
- [ ] **(M2)** Telemetry follows the OTel GenAI semantic conventions at a pinned revision, with `invoke_agent` / `chat` / `execute_tool` spans; a schema test runs on exported traces, and a migration test precedes any pin bump. <sub>`obs.telemetry-pinned` · DoD 29</sub>
- [ ] **(M2)** Prompt and completion content is not captured in traces by default; capture is enabled by a written policy with retention and access limits. <sub>`obs.no-content` · DoD 29</sub>
- [ ] **(M3)** Traces capture the **trajectory**, not just the final answer. <sub>`obs.trajectory` · DoD 29</sub>
- [ ] **(M3)** Online evals run on completed production threads; failing traces feed the offline set. <sub>`eval.online`</sub>
- [ ] **(M3)** Reliability tracked with `pass^k`, not only `pass@1`. <sub>`eval.pass-k`</sub>

### Operating without per-action approval — the Loop License *(if the system runs at O1 or O2)*
- [ ] **(M2)** **Loop License** held: eval threshold (pass@1 **and** pass^5), regression gate, declared blast radius, cost cap, kill switch, and escalation path — all six declared, enforced in code, tested ([`templates/loop-license/CHECKLIST.md`](templates/loop-license/CHECKLIST.md)). <sub>`loop.license` · DoD 16</sub>
- [ ] **(M2, L3+ or O1+)** Stop conditions declared in the Agent Contract and enforced by the runner: max iterations, token/time/spend budgets, timeout, escalation after N consecutive failures (also binds at L3+ under O0). <sub>`loop.stop-conditions` · DoD 17</sub>
- [ ] **(M2)** Independent verification: the producing model does not grade its own work; deterministic checks first; the LLM judge is calibrated and decorrelated from the writer. <sub>`loop.verification` · DoD 18</sub>
- [ ] **(M2)** The agent cannot modify its own tests, graders, eval sets, or thresholds — they sit outside its write scope. <sub>`loop.checks-out-of-reach` · DoD 18, 30</sub>
- [ ] **(M2)** "Find work" treated as untrusted input — indirect-injection cases in the eval suite, instruction/data channel separation, least-privilege triggers (OWASP LLM01). <sub>`loop.ingestion` · DoD 16</sub>
- [ ] **(M2)** Instruction supply chain governed: skills/prompts/instructions versioned, provenanced, eval-gated before deploy, regression-tested on update, trigger-collisions audited; skills validated against the Agent Skills specification and hash-locked (OWASP LLM03). <sub>`loop.supply-chain` · DoD 16</sub>
- [ ] **(M2)** Loop economics: cost per run **and** cost per *verified* outcome tracked in traces; per-run/per-window caps declared. <sub>`loop.economics` · DoD 19</sub>
- [ ] **(M2)** Memory model and determinism map were declared at architecture time (what is persisted, retention, provenance, replayability; which steps are deterministic vs. model-driven). <sub>`loop.declarations` · DoD 16</sub>
- [ ] **(M2, O2)** At O2, a sample of successful runs is reviewed each release for illegitimate success; the legitimacy rate is published and gates promotion. <sub>`loop.legitimacy` · DoD 30</sub>

### Measurement science & oversight *(deepens Evals & observability)*
- [ ] **(M2, if LLM judges)** Any judge that gates O1+ operation / auto-apply / release has a current **Judge Card**: calibration (ECE/Brier) + anchored accuracy vs. a ground-truth sample within a recency window; an `uncalibrated`/`stale` judge gates nothing. <sub>`meas.judge-card` · DoD 20</sub>
- [ ] **(M2, if LLM judges)** Gating confidence uses validated self-consistency or swap-consistency — **not** raw verbalized confidence; pairwise judging randomizes order or applies a swap-consistency check. <sub>`meas.confidence` · DoD 20</sub>
- [ ] **(M2, if memory/retrieval)** Retrieval / memory evaluated with **Recall@k + MRR** on a labeled set, separately from end-to-end evals; embedding/chunking/index changes pass a retrieval regression gate. <sub>`meas.retrieval` · DoD 21</sub>
- [ ] **(M2)** Golden sets declare **labeling provenance** (rubric version, labeler, date, agreement); unanchored sets back no license or gate; rubrics are versioned with judge re-baselining on change. <sub>`meas.provenance` · DoD 22</sub>
- [ ] **(M2, if LLM judges)** Inter-judge agreement monitored; sustained near-perfect agreement triggers a decorrelation review, sustained low agreement a rubric review. <sub>`meas.inter-judge` · DoD 22</sub>
- [ ] **(M2)** Input and behavior **drift** monitored vs. the eval distribution with a declared refresh policy (behavior drift at autonomy ≥ L2). <sub>`meas.drift` · DoD 23</sub>
- [ ] **(M3)** Provider-hosted models are canaried on a cadence; a detected silent change triggers the eval regression gate before continued reliance. <sub>`meas.canary` · DoD 23</sub>
- [ ] **(M2)** Wherever a human approval counts as a control, override rate and approval latency (p50/p95) are tracked per queue, and a rubber-stamp alarm triggers a review. <sub>`meas.automation-bias` · DoD 33</sub>
- [ ] **(M2, O1+)** Human-oversight program: sampling schedule per oversight mode with automatic re-escalation on regression; reviews captured as stratified labeled data. <sub>`meas.oversight-plan` · DoD 33</sub>

### Composition (multi-agent) *(if more than one agent is composed)*
- [ ] **(M2, multi-agent, O1+)** **Graph License** held: the six gates at graph scope, the weakest-link bound on every action path, shared-state provenance, fan-in verification points, and every edge class marked enforced or declared ([`templates/graph-license/CHECKLIST.md`](templates/graph-license/CHECKLIST.md)). <sub>`graph.license` · DoD 25</sub>
- [ ] **(M2, multi-agent, O1+)** The graph eval suite includes poisoned-state scenarios — a hijacked or hallucinating node writing to shared state — and downstream nodes do not act on it. <sub>`graph.poisoned-state` · DoD 25</sub>
- [ ] **(M2, if delegating across a trust boundary)** Before delegating across a trust boundary, the peer's signed Agent Card is verified (JWS over the JCS-canonicalized card; keys from a trusted keystore or an allow-listed `jku`); a forged or unsigned card fails closed; delegated scope never exceeds the delegator's. <sub>`graph.inter-agent-trust` · DoD 28</sub>

### Governance & regulation
- [ ] **(M1, if regulated)** A regulatory classification record exists — jurisdictions, role and risk class under each regime (EU AI Act — provider/deployer, Annex I/III, Art. 50), application dates — with an owner and a re-review trigger on any change of purpose, users, or model. <sub>`gov.classification` · DoD 31</sub>

### Fleet operations *(if running a persistent fleet)*
- [ ] **(M2)** Each deployed agent is a versioned **runtime manifest** (resources, schedule, runtime + model, env interpolation), distinct from its Agent Contract; the same manifest runs in dev and prod, with agent-logic split from the platform prompt injected at run time. <sub>`fleet.manifest`</sub>
- [ ] **(M2)** Scheduled / triggered runs are coordinated by a lock (fire-once across replicas); missed runs (misfires) are detected and handled, not silently dropped. <sub>`fleet.scheduling`</sub>
- [ ] **(M2)** Overflow work queues in a durable backlog that survives a restart — no in-memory-only work queue. <sub>`fleet.backlog`</sub>
- [ ] **(M2)** Per-agent isolation + resource limits; runs terminate gracefully (drain, then SIGINT→SIGKILL); deploy / start / stop / restart are operations, not full redeploys. <sub>`fleet.lifecycle`</sub>
- [ ] **(M3)** Fleet observability: per-agent health/heartbeat + topology, plus an append-only operational audit (lifecycle / auth / tool-call events), on top of the per-run traces above. <sub>`fleet.observability`</sub>
- [ ] **(M3)** Inter-agent calls follow an explicit "who-may-call-whom" matrix (default deny); coordination prefers an event bus over hard-wired calls. <sub>`fleet.call-matrix`</sub>

### Model & provider *(if calls fan out over multiple models/providers)*
- [ ] **(M2)** All model calls go through one provider-abstraction point; adding a provider is config, not code. <sub>`model.abstraction`</sub>
- [ ] **(M2)** Model selection per task class is sourced from measured eval results, and the source eval run is recorded. <sub>`model.eval-sourced`</sub>
- [ ] **(M2)** Clients hold exactly one credential; upstream provider keys are vaulted and never reach clients or logs. <sub>`model.one-credential`</sub>
- [ ] **(M3, multi-provider, multi-tenant)** Tenant-scoped budgets, cache, and routing with a cross-tenant leakage test in CI. <sub>`model.tenant-scoped`</sub>

### Maintenance discipline
- [ ] **(M1)** No safety-class gate is disabled repo-wide to pass CI (correctness test, type-safety / `no-unsafe-*` / `no-explicit-any`, security lint, coverage/mutation floor); false positives are scoped to a file/glob with a named reason, and the gate is re-proven to still fire (Canon 5, *gate-integrity invariant*). <sub>`maint.gate-integrity` · DoD 24</sub>
- [ ] **(M2)** Every forbidden action has a code-asserted anti-criterion (not prose alone). <sub>`maint.anti-criteria`</sub>
- [ ] **(M3)** Rules are tagged anti-fragile vs. fragile; fragile scaffolding is re-tested each model upgrade (bitter-pill). <sub>`maint.bitter-pill`</sub>

<!-- canon:end:scorecard.items -->
---

## Scoring

1. Declare your operating point (autonomy L0–L4, oversight O0–O2) and what the product contains (multi-tenant, MCP, multi-agent, …). Items whose condition does not hold for you are N/A.
2. Mark every remaining item Yes / No / N-A. An N-A needs a reason; a Yes needs evidence you could hand to a reviewer.
3. For each band M1 → M2 → M3, check that **all** applicable items at or below that gate are Yes (or N-A). Your maturity is the highest band that fully passes.
4. Your operating point must not need a higher band than you reached (see the table above). The first No you hit is your next piece of work.

In CI, [`aps-conformance`](docs/conformance.md) does all four from an `aps-conformance.yaml` — start from [the generated template](templates/conformance/aps-conformance.template.yaml) — and reports failing controls as SARIF against the Definition of Done items and regulatory obligations they support.

> A score is a snapshot, not a trophy. The standard's one durable rule still holds: *the model is the variable, the harness is the constant — invest proportionally.*
