# Agentic Product Self-Assessment Scorecard

*A factor-by-factor maturity check for any agentic product, scored against [`STANDARD.md`](STANDARD.md) and [`AGENT_STANDARD.md`](AGENT_STANDARD.md).*

Most standards ship principles but no way to ask *"where do we actually stand?"* This scorecard does. Answer every item **Yes / No / N-A**, then read your maturity off the gates below. It is deliberately binary — a half-met control is a No.

> **How to use it.** Run it on one agentic product, with the team in the room, against a real deployment (not the slide). Disagreements are the point — they surface the controls nobody owns. Re-run each release; the score should only ratchet up.

> **The paved road.** Many of these controls come satisfied out of the box if you run the recommended reference stack — the **[AgenticProduct family](ECOSYSTEM.md)**: AgenticMind (memory), AgenticOps (runtime & fleet ops), AgenticPerformance (evals & observability), AgenticSelfHealingCode (self-healing), AgenticGateway (model & cost plane), and AgenticAssurance (red-team the Security & Identity items). It's the fastest way to green, not a requirement — you can satisfy any item your own way (Principle 2). See the [`reference-stack`](skills/agentic-product-architect/reference-stack/SKILL.md) skill.

---

## Maturity levels (mapped to the Autonomy Ladder)

| Level | Autonomy Ladder | Meaning |
|---|---|---|
| **M0 — Prototype** | L0–L1 (single call / augmented) | Works on a demo. No production claim. |
| **M1 — Shippable** | L2 (workflow) | Contracts, schemas, guardrails, an eval set, permissions in code. Safe to put in front of users behind a workflow. |
| **M2 — Production** | L3 (orchestrator-worker) | Durable, observable, tenant-isolated, security-checked, cost-bounded, CI-gated on evals. |
| **M3 — Autonomous-ready** | L4 (autonomous loop) | Online evals, `pass^k` reliability, red-team kit run, full OTel trajectory observability. Earns the right to an open-ended loop. |

**Your level is the highest band whose every gate item is satisfied.** One unmet gate item caps you at the level below — there is no partial credit, and no skipping a band.

---

## The scorecard

Each item lists the **gate level** at which it becomes mandatory. Items map to the Definition of Done in `STANDARD.md` (Part III) and `AGENT_STANDARD.md`.

### Architecture & contracts
- [ ] **(M1)** The system uses the least autonomous architecture sufficient for the task.
- [ ] **(M1)** Every agent has an Agent Contract; every tool a Tool Contract.
- [ ] **(M1)** Acceptance criteria are *hard-to-vary*: each names the single probe that falsifies it.
- [ ] **(M2)** Each escalation in autonomy was earned by ≥90% eval pass rate at the level below.
- [ ] **(M2)** Multi-agent (if any) is an orchestrator with isolated subagents — not a peer-to-peer bus.

### Context & state
- [ ] **(M1)** Context-window utilization stays below ~40% in a typical cycle.
- [ ] **(M1)** State is externalized (does not live only in the context window).
- [ ] **(M2)** Compaction is tested on long-running scenarios; sub-agent outputs are condensed.

### Tools & permissions
- [ ] **(M1)** Tools are allow-listed; active count < 20 per agent (or RAG-over-tools).
- [ ] **(M1)** Tool inputs are schema-validated; permissions enforced in **code**, not prompt.
- [ ] **(M1)** Destructive / financial / external-comms actions require human approval.
- [ ] **(M2)** Tool execution is sandboxed (containers / OAuth scopes / least privilege).

### Security & identity
- [ ] **(M2)** Lethal-trifecta check performed and documented; if all three legs present, one is broken.
- [ ] **(M2)** MCP tool definitions pinned by hash with change alerts; servers from an allow-listed registry, version-pinned + signature-checked.
- [ ] **(M2)** OAuth 2.1 scoped, short-lived, audience-bound tokens; no token passthrough; no over-scoping.
- [ ] **(M2)** Each agent has a distinct least-privilege identity; identity & tenant derived from auth, never the model.
- [ ] **(M3)** Indirect prompt injection (poisoned docs / tool output) is in the threat model and red-team tested.

### Tenant isolation *(if multi-tenant)*
- [ ] **(M2)** `tenant_id` derived from auth only; no-tenant requests fail closed.
- [ ] **(M2)** Isolation enforced below the LLM (RLS / repository layer); survives prompt injection.
- [ ] **(M2)** Retrieval, memory, cache keys, traces, sub-agent messages, jobs are all tenant-scoped.
- [ ] **(M2)** A code-asserted cross-tenant leakage eval runs in CI.

### Cost
- [ ] **(M2)** Per-run token/cost ceiling enforced in code (circuit breaker on runaway sessions).
- [ ] **(M2)** Prompt/KV caching enabled on stable prefixes; cost-per-task tracked in traces.
- [ ] **(M2)** For multi-agent, the task value justifies the ~15× token cost.

### Reliability
- [ ] **(M2)** Durable execution: pause / resume / retry survives a killed process.
- [ ] **(M1)** Structured outputs validated by schema; assertions on the critical path.
- [ ] **(M1)** Guardrails (schema, PII, jailbreak, indirect-injection, egress) on input and output.

### Evals & observability
- [ ] **(M1)** Eval set ≥ 50 examples per top-priority failure mode; built from real traces.
- [ ] **(M2)** LLM judges are binary and calibrated against human labels (TPR/TNR tracked).
- [ ] **(M2)** CI blocks deploy on eval regression; 100% of production runs traced.
- [ ] **(M3)** Traces follow OTel GenAI conventions and capture the **trajectory**, not just the final answer.
- [ ] **(M3)** Online evals run on completed production threads; failing traces feed the offline set.
- [ ] **(M3)** Reliability tracked with `pass^k`, not only `pass@1`.

### Unattended operation *(the Loop License — if the agent runs at L3+ without a human in each turn)*
- [ ] **(M2)** **Loop License** held: eval pass-rate threshold, regression gate, declared blast radius, cost cap, kill switch, and escalation path — all six declared, enforced in code, tested ([`templates/loop-license/CHECKLIST.md`](templates/loop-license/CHECKLIST.md)).
- [ ] **(M2)** Stop conditions declared in the Agent Contract and enforced by the runner: max iterations, token/time/spend budgets, timeout, escalation after N consecutive failures.
- [ ] **(M2)** Independent verification: the producing model does not grade its own work; deterministic checks first; the LLM judge is calibrated and decorrelated from the writer.
- [ ] **(M2)** "Find work" treated as untrusted input — indirect-injection cases in the eval suite, instruction/data channel separation, least-privilege triggers (OWASP LLM01).
- [ ] **(M2)** Instruction supply chain governed: skills/prompts/instructions versioned, provenanced, eval-gated before deploy, regression-tested on update, trigger-collisions audited (OWASP LLM03).
- [ ] **(M2)** Loop economics: cost per run **and** cost per *verified* outcome tracked in traces; per-run/per-window caps declared.
- [ ] **(M2)** Memory model and determinism map were declared at architecture time (what is persisted, retention, provenance, replayability; which steps are deterministic vs. model-driven).

### Fleet operations *(if running a persistent fleet)*
- [ ] **(M2)** Each deployed agent is a versioned **runtime manifest** (resources, schedule, runtime + model, env interpolation), distinct from its Agent Contract; the same manifest runs in dev and prod, with agent-logic split from the platform prompt injected at run time.
- [ ] **(M2)** Scheduled / triggered runs are coordinated by a lock (fire-once across replicas); missed runs (misfires) are detected and handled, not silently dropped.
- [ ] **(M2)** Overflow work queues in a durable backlog that survives a restart — no in-memory-only work queue.
- [ ] **(M2)** Per-agent isolation + resource limits; runs terminate gracefully (drain, then SIGINT→SIGKILL); deploy / start / stop / restart are operations, not full redeploys.
- [ ] **(M3)** Fleet observability: per-agent health/heartbeat + topology, plus an append-only operational audit (lifecycle / auth / tool-call events), on top of the per-run traces above.
- [ ] **(M3)** Inter-agent calls follow an explicit "who-may-call-whom" matrix (default deny); coordination prefers an event bus over hard-wired calls.

### Model & provider *(if calls fan out over multiple models/providers)*
- [ ] **(M2)** All model calls go through one provider-abstraction point; adding a provider is config, not code.
- [ ] **(M2)** Model selection per task class is sourced from measured eval results, and the source eval run is recorded.
- [ ] **(M2)** Clients hold exactly one credential; upstream provider keys are vaulted and never reach clients or logs.
- [ ] **(M3)** Tenant-scoped budgets, cache, and routing with a cross-tenant leakage test in CI.

### Maintenance discipline
- [ ] **(M2)** Every forbidden action has a code-asserted anti-criterion (not prose alone).
- [ ] **(M3)** Rules are tagged anti-fragile vs. fragile; fragile scaffolding is re-tested each model upgrade (bitter-pill).

---

## Scoring

1. Mark every item Yes / No / N-A.
2. For each band M1 → M2 → M3, check that **all** items at or below that gate are Yes (or N-A).
3. Your maturity is the highest band that fully passes. The first No you hit is your next piece of work.

> A score is a snapshot, not a trophy. The standard's one durable rule still holds: *the model is the variable, the harness is the constant — invest proportionally.*
