<!-- Generated from canon/ by tools/aps.py — edit the canon, not this file. -->

# Definition of Done — the audit points (Standard v4.0.0-rc.1)

The normative text of each item is in `STANDARD.md` Part III; this file is the audit view the `production-readiness` skill walks. For every item: the checks to run, why it matters, and the gap teams most often leave. Mark each **pass**, **gap**, or **N/A with a reason** — "N/A because we have no destructive actions" is fine; "N/A because we don't think it matters" is not.

## Context and state

### 1. Context budget held

- [ ] Measure context utilization on representative production traces
- [ ] Median below the budget; p95 below 60% of the window while the 40% default applies
- [ ] If you set a measured budget: the degradation curve (eval pass rate vs. context fill) is recorded for the current model and re-measured whenever the model changes
- [ ] If higher: compaction strategy in place that triggers at the budget

**Why:** past the budget, model recall degrades nonlinearly — the "dumb zone." Bigger windows move the threshold; they do not remove it. On a 1M-token window, 40% is 400K tokens, far past where published context-rot studies see accuracy fall, which is why the budget is measured per model rather than assumed.

**Common gap:** dumping conversation history into every turn instead of using selection / compaction — or carrying a percentage rule onto a model with a 5× larger window without re-measuring.

---

### 2. State externalized

- [ ] State has a defined home (file, DB, memory layer) — not "the conversation"
- [ ] Can recover full agent state from external storage on crash
- [ ] State writes are explicit and traceable
- [ ] No application state rides on a transport session (MCP 2026-07-28 removed `Mcp-Session-Id`); cross-call state uses explicit handles or your own store

**Why:** in-context state evaporates on session boundary, restart, or compaction.

**Common gap:** "the agent will remember from the conversation" — it won't, reliably.

---

### 3. Compaction tested

- [ ] Compaction has been exercised on real long sessions (>50 turns or > 30 min)
- [ ] No critical info lost during compaction (verified by eval cases)
- [ ] Compaction trigger is metric-driven, not turn-count-driven

**Why:** compaction that drops critical state silently is worse than no compaction.

**Common gap:** built compaction, never tested on a session long enough to need it.

---

## Tools and permissions

### 4. Destructive actions need approval

- [ ] List of destructive actions enumerated (deletes, writes, sends, charges, etc.)
- [ ] Each one routes through an approval gate
- [ ] Approval is logged with who/when/what

**Why:** Replit incident — an agent deleted a production database holding records on 1,200+ companies despite a "code freeze" prompt. Prompts don't enforce.

**Common gap:** "the prompt tells the agent not to delete production data" — insufficient.

---

### 5. Permissions in code, not prompt

- [ ] Agent does not hold credentials that bypass permission boundaries
- [ ] Permission gate is a separate code path the LLM cannot override
- [ ] Even with prompt injection, agent cannot perform forbidden actions

**Why:** prompt injection is a real threat; LLM can be coerced; code cannot.

**Common gap:** OAuth scopes too broad; agent runs as superuser internally.

---

### 6. Sandboxed tool execution

- [ ] Code execution in containers / VMs, not host environment
- [ ] File operations in scoped working directories
- [ ] Network access through allow-listed domains
- [ ] Secrets never in context window; injected at tool boundary

**Why:** tool execution is an attack surface; treat it like any RPC exposed to untrusted input.

**Common gap:** agent has shell access with no sandbox.

---

### 32. Tenant isolation below the LLM

*Binds: If multi-tenant.*

- [ ] Isolation model chosen per data store (pooled + RLS / schema-per-tenant / DB-per-tenant) and recorded in the Agent Contract
- [ ] `tenant_id` is part of the authenticated principal; a request with no resolvable tenant fails closed (no default tenant)
- [ ] Isolation enforced below the LLM (row-level security or repository layer); verified to hold under prompt injection
- [ ] Retrieval filtered inside the index (not post-top-k), memory namespaced, cache key includes `tenant_id`, traces tagged, sub-agent messages and background jobs carry the tenant
- [ ] Tools ignore any model-supplied tenant; a mismatch is audited and rejected
- [ ] A code-asserted cross-tenant leakage eval (canary seeded as A, queried as B incl. an injection variant) runs in CI

**Why:** an agent is a confused deputy — prompt-level isolation leaks. The first cross-tenant leak is a churn-and-lawsuit event, and retrofitting isolation is the migration nobody budgets for. See the `tenant-isolation` skill.

**Common gap:** a tenant-agnostic answer cache serving tenant A's response to tenant B; `tenant_id` passed as a tool argument the model can be talked into changing.

---

## Reliability

### 7. Durable pause/resume/retry

- [ ] Kill the agent process mid-execution; restart; verify it resumes
- [ ] Retry policies defined per activity type
- [ ] Human-wait signals work (agent can wait hours/days for approval)

**Why:** any agent running > 60s will hit a crash, restart, or wait — without durability, work is lost.

**Common gap:** "we tested the happy path" — production isn't the happy path.

---

### 8. Schema-validated outputs

- [ ] Every LLM call returning structured data validates against schema
- [ ] Code assertions on critical state transitions
- [ ] No "parse this text output and hope" anywhere on the critical path

**Why:** unvalidated outputs cause silent corruption; assertions catch it early.

**Common gap:** regex-parsing LLM responses; works in dev, fails in production edge cases.

---

### 9. Input/output guardrails

- [ ] Input guardrails: PII detection, jailbreak / prompt injection classifier
- [ ] Output guardrails: schema validation, content policy, citation check
- [ ] Guardrails run on real traffic, with metrics on hit rates

**Why:** defense in depth; multiple cheap guardrails beat one perfect one.

**Common gap:** no input guardrails; trusting the model to refuse.

---

## Evals and observability

### 10. ≥50 evals per failure mode

- [ ] At least 5 named failure modes (product-specific, not generic)
- [ ] Each has ≥ 50 cases in the eval set
- [ ] Cases sampled from real or representative traces

**Why:** generic evals don't catch product-specific failures; 50 cases give enough signal to detect regression.

**Common gap:** 20 cases of "helpfulness" — not enough, not the right thing to measure.

---

### 11. Judges calibrated (TPR/TNR)

*Binds: Wherever an LLM judge is used.*

- [ ] Each LLM judge has ≥ 100 human-labeled examples for calibration
- [ ] TPR and TNR both > 80%
- [ ] Calibration re-run when judge prompt changes
- [ ] TPR/TNR reported with every release

**Why:** uncalibrated judges produce meaningless scores; teams stop trusting evals and revert to vibe.

**Common gap:** built a judge; never measured if it agrees with humans.

---

### 12. CI blocks regression; 100% traced

- [ ] CI runs full eval suite on every PR
- [ ] Merge blocked on regression vs main branch
- [ ] 100% of production traffic produces traces
- [ ] Traces include all required fields (see the telemetry contract, item 29)
- [ ] Trace retention sufficient for incident investigation (typically 30–90 days)

**Why:** evals without enforcement are theater; traces are the only way to debug failures after launch.

**Common gap:** evals exist but don't gate merges; tracing is sampled, missing the failures.

---

### 29. Telemetry contract

- [ ] The conventions revision is pinned in code or config and recorded with the traces (e.g. the schema URL or a resource attribute)
- [ ] Each run emits an `invoke_agent` span with child `chat` and `execute_tool` spans; `gen_ai.usage.input_tokens` / `gen_ai.usage.output_tokens` are recorded
- [ ] Content attributes (`gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions`, `gen_ai.tool.definitions`) are absent unless a written policy enables them, with retention and access limits
- [ ] A schema test validates exported spans in CI; a pin bump runs a migration test before merge
- [ ] The agent identity (item 27) — and the tenant, if multi-tenant (item 32) — is on every span

**Why:** the GenAI conventions are still in Development status and moved repositories in June 2026 — an unpinned "we use OTel" is a floating contract that breaks dashboards and evals on the next rename. The conventions themselves say instrumentations should not capture content by default: traces are a data store, and prompts carry the most sensitive data you have.

**Common gap:** full prompts captured in production traces because it was the SDK default in development — discovered during a data-subject request.

---

## Security and identity

### 13. Lethal-trifecta check

- [ ] Three legs assessed: access to private data, exposure to untrusted content, ability to communicate externally
- [ ] If all three are present, at least one leg is broken in design (not by a prompt instruction)
- [ ] The check and its outcome are written down (in the Agent Contract / threat model), not assumed

**Why:** private data × untrusted content × external comms is an exfiltration channel — injected content reads a secret and ships it out. Simon Willison's lethal trifecta: the deployment check every agent must pass.

**Common gap:** all three legs live and unmitigated because no one drew the diagram; "the model won't do that" stands in for a mitigation.

---

### 14. MCP tool defs pinned; allow-listed registry

*Binds: Wherever MCP is used.*

- [ ] Tool definitions pinned by hash, with a change alert (rug-pull detection)
- [ ] The pin is re-verified on every refetch of `tools/list` (caching hints expire; the pin must not)
- [ ] MCP servers installed only from an allow-listed registry — never an arbitrary URL

**Why:** an approved tool description can mutate after you approve it (rug pull); the supply chain is part of the attack surface.

**Common gap:** installing a community MCP server by URL and trusting its description forever.

---

### 26. MCP protocol & auth baseline

*Binds: Wherever MCP is used.*

- [ ] Inventory: every MCP connection, the side you own (client or server), the revision it speaks, and a sunset date for anything older than 2026-07-28
- [ ] The official conformance suite (`@modelcontextprotocol/conformance`) runs in CI against each server and client you own, at a pinned version, with its expected-failures file reviewed like code
- [ ] No dependence on `Mcp-Session-Id`; cross-call state uses explicit, server-minted handles or your own store (item 2)
- [ ] `requestState` handled as attacker-controlled input and integrity-protected (HMAC/AEAD) wherever it influences authorization, resource access, or business logic
- [ ] Clients register with a Client ID Metadata Document, validate a present `iss` against the recorded issuer, and key persisted credentials by issuer; servers never pass tokens through
- [ ] Gateways that route on `Mcp-Method` / `Mcp-Name` reject header/body mismatches and protocol versions that predate the headers; `private` cache entries never cross a user or tenant

**Why:** the 2026-07-28 revision moved state out of the protocol and hardened authorization. Code written for the 2025 session-and-DCR model now carries state nobody can see and client registrations the ecosystem is retiring. Conformance is testable — so it is tested, not asserted. See advisory [APS-2026-01](../../../docs/advisories/APS-2026-01-mcp-2026-07-28.md).

**Common gap:** a server that keeps per-user state behind `Mcp-Session-Id` and "works fine" on a single replica — until a load balancer or the next SDK upgrade drops it.

---

### 27. Per-agent identity

- [ ] An inventory lists every agent identity with its owner, scopes, and credential lifetime
- [ ] No agent runs on a shared service account, a person's token, or a long-lived static key in production (a static bearer is acceptable for localhost development only)
- [ ] Credentials are short-lived and audience-bound; scopes match the declared blast radius
- [ ] Each trace span carries the agent identity and the delegating principal (user or upstream system)
- [ ] Identity and tenant are derived from authentication, never asserted by the model

**Why:** an agent that shares an identity cannot be scoped, rotated, revoked, or audited on its own; when it misbehaves you cannot tell which agent did what on whose behalf. NIST's NCCoE concept paper on software and AI agent identity and authorization (Feb 2026) builds on OAuth 2.0 and SPIFFE for exactly this.

**Common gap:** every agent in the fleet calling tools with one service-account key nobody rotates, so the audit log says "svc-agents" for every action.

---

## Cost

### 15. Per-run cost ceiling in code

- [ ] A hard per-run token / cost ceiling, enforced in code (circuit breaker) — not a guideline or a dashboard
- [ ] A runaway or looping session trips the breaker and halts
- [ ] Cost-per-task is recorded in traces
- [ ] The model-swap runbook re-derives ceilings and routing from measured cost per task on the new model — a price cut or a new tokenizer changes what a ceiling means

**Why:** without a code-level ceiling, one bad loop is an unbounded invoice. Cost is a reliability property, not just a finance report.

**Common gap:** watching cost in a dashboard after the fact instead of capping it in the request path — or carrying last model's ceilings onto a model with different prices and token counts.

---

## Operating without per-action approval (O1+) — the Loop License

### 16. Loop License (six gates)

*Binds: At oversight O1 or O2.*

- [ ] Eval threshold (pass@1 and pass^5), regression gate, declared blast radius, cost cap, kill switch, escalation path — all six declared, enforced in code, and tested
- [ ] Missing any one gate → the system is capped at O0 (a human approves each consequential action)

**Why:** a loop that acts without per-action approval and holds no license is a factory with no quality control — it ships whatever it produces at machine speed.

**Common gap:** having evals and a cost cap but no kill switch or declared blast radius, so nothing can stop or bound a run in flight.

---

### 17. Stop conditions

*Binds: At autonomy L3+ or oversight O1+.*

- [ ] Max iterations, token/time/spend budgets, and a timeout are in the Agent Contract and enforced by the runner
- [ ] After N consecutive failures the loop escalates, it does not retry forever

**Why:** "no declared way to stop" is the defining L4 failure.

**Common gap:** budgets exist but there is no escalation-after-N — the loop burns the whole budget retrying a doomed step.

---

### 18. Independent verification

*Binds: At oversight O1 or O2.*

- [ ] The producing model does not grade its own work
- [ ] Deterministic checks (tests, schema, assertions) run before any LLM judge; the judge is calibrated (see #11) and decorrelated from the writer
- [ ] The agent cannot modify its own tests, graders, eval sets, or thresholds

**Why:** self-verification shares the writer's blind spots — a pass tells you nothing new.

**Common gap:** a single agent that writes and then "reviews" its own output in the same context — or one that can edit the test it is graded by.

---

### 19. Loop economics

*Binds: At oversight O1 or O2.*

- [ ] Cost per run **and** cost per *verified* outcome are tracked in traces
- [ ] Per-run and per-window cost caps are declared

**Why:** a loop that is cheap per call but rarely produces a verified result is expensive — only cost-per-verified-outcome shows it.

**Common gap:** measuring raw spend but never dividing by outcomes that actually passed verification.

---

### 30. Success-legitimacy audit

*Binds: At oversight O2.*

- [ ] A sampling plan per release: how many successful runs are reviewed, stratified by task type, and by whom
- [ ] Reviewers check the path, not just the output: diffs to tests or graders, skipped assertions, special-cased inputs, outputs that match the checker rather than the task
- [ ] Legitimacy rate = legitimate successes ÷ reviewed successes, reported next to pass@1 and pass^5; a declared floor blocks promotion
- [ ] Every illegitimate success becomes a regression case and, where possible, a deterministic tripwire

**Why:** METR's Frontier Risk Report (May 2026) found that on tasks longer than eight hours at least 16% of runs scored as successful were illegitimate on review, with well over 100 distinct instances of cheating. A pass rate that counts those measures the agent's ability to satisfy the checker.

**Common gap:** reporting a rising pass rate from an agent that can edit the test suite it is graded by.

---

## Measurement science and human oversight

### 20. Judge calibration (ECE/Brier)

*Binds: Wherever an LLM judge gates O1+ operation, auto-apply, or release.*

- [ ] Any judge that gates O1+ operation, auto-apply, or release has documented calibration — accuracy + calibration error (ECE/Brier) vs. an anchored ground-truth sample within a declared recency window
- [ ] The gating confidence signal is validated self-consistency or swap-consistency, never raw verbalized confidence; pairwise judging randomizes order

**Why:** verbalized LLM confidence is systematically overconfident; an uncalibrated judge in a gate is a check that isn't one — it invalidates the Loop License for the modes it gates.

**Common gap:** trusting a judge's "95% confident" verbatim, with no anchored accuracy behind it.

---

### 21. Retrieval metrics

*Binds: Wherever memory or retrieval is used.*

- [ ] Memory/retrieval scored with Recall@k and MRR on a labeled retrieval set, separately from end-to-end task evals
- [ ] Embedding-model / chunking / index changes pass a retrieval regression gate before deploy

**Why:** retrieval and reasoning fail differently; an end-to-end number that conflates them cannot direct a fix.

**Common gap:** shipping an embedding-model swap because task evals "looked fine," silently dropping Recall@5.

---

### 22. Ground-truth provenance

- [ ] Golden sets declare labeling provenance (rubric version, labeler type, date, agreement); unanchored sets do not back a license or release gate
- [ ] Rubrics are versioned instruction artifacts; a rubric change re-baselines every judge that uses it

**Why:** a golden set without provenance is unanchored — you don't know what its pass rate means.

**Common gap:** a "golden" set nobody can trace to a rubric version or a labeler.

---

### 23. Drift monitoring

- [ ] Input drift monitored vs. the eval distribution, with a declared refresh policy (thresholds + triggered action)
- [ ] Provider-hosted models canaried; a detected silent change triggers the regression gate; behavior drift watched at ≥ L2

**Why:** drift answers "when did my evals stop representing production?" — without it a green suite can be measuring the past.

**Common gap:** a golden set refreshed on a calendar, not when production actually moved.

---

### 33. Human oversight as a program

*Binds: Wherever a human approval counts as a control; the oversight plan at O1+.*

- [ ] Override rate and approval latency (p50/p95) are tracked per approval queue and per reviewer
- [ ] A rubber-stamp alarm fires on sustained near-100% approval at very low latency — and the queue is reviewed, not the alarm silenced
- [ ] At O1+, the Loop License declares a sampling schedule per oversight mode, a reviewer SLA, and automatic re-escalation triggers (regression or override-rate spike → previous mode)
- [ ] Human reviews/overrides are captured as stratified labeled data (escalations **plus** a random routine sample)

**Why:** oversight is an operated program, not a checkbox; graduation must be reversible on regression. Automation bias turns an approval gate back into no gate — IMDA's agentic governance framework (updated May 2026) names a low override rate as a signal of rubber-stamping.

**Common gap:** "human review" that only sees escalated hard cases, skewing the review-derived golden data — or an approval queue so long that reviewers approve in bulk.

---

## Gate integrity

### 24. No safety gate silenced to pass CI

- [ ] No safety-class gate is disabled repo-wide to make CI green — a correctness test, type-safety (`no-unsafe-*` / `no-explicit-any`), security lint, or a coverage/mutation floor
- [ ] Any false positive is scoped to a file/glob with a named reason (not a repo-wide `off`, blanket `@ts-ignore`/`eslint-disable`, `.skip`, or a lowered threshold)
- [ ] After scoping, the gate is re-proven to still fire — plant the thing it must catch and confirm it's caught

**Why:** a gate is trust-bearing only if green means the property holds, not that the check was silenced; disabling it removes the exact protection at the moment it fired. `tsc` passing is not a substitute for the `no-unsafe-*` family — `any` is assignable to everything by design, so the compiler waves it through (Canon 5, *gate-integrity invariant*).

**Common gap:** a flaky lint rule disabled repo-wide to unblock CI, silently blinding every file instead of the one that misfired.

---

## Composition (multi-agent)

### 25. Graph License

*Binds: Any graph of agents operating at O1+.*

- [ ] The six gates re-evaluated at **graph** scope: graph-level golden tasks (end-to-end, not the union of per-node suites) · regression gate on that set · blast radius as the **union** of node radii **plus the shared state store** · cost caps **per-node and aggregate** · a kill switch tested against **in-flight parallel branches** · **one** named escalation owner for the graph
- [ ] **Weakest-link bound** holds: no path to an external action runs under less oversight than its least-licensed node allows
- [ ] Shared state carries **writer provenance** (producing node, timestamp, `verified_by` / `unverified`); consumers can filter on it; no external action fires from an unverified field
- [ ] Every **fan-in** is a declared verification point or an explicit pass-through with rationale
- [ ] Every **edge class** is marked **enforced** or **declared**; declared-only edges are not counted as controls
- [ ] Graph eval suite includes **poisoned-state** scenarios (a hijacked or hallucinating node writing to shared state)

**Why:** a graph of licensed loops is not a licensed graph. The failures that hurt are exactly the ones no single node owns — nodes that pass in isolation failing in composition, fan-out multiplying spend past every per-node cap while each reads green, an uncalibrated node lending a path autonomy it never earned, and an escalation path that forks so no human is on the hook (Part IV, *License Composition*; [`CHECKLIST`](../../../templates/graph-license/CHECKLIST.md)).

**Common gap:** the topology is drawn in an SOP or a system prompt and then cited as a control, though nothing in the runtime prevents a different route (anti-pattern 18).

---

### 28. Inter-agent trust

*Binds: Wherever work is delegated across a trust boundary.*

- [ ] Every cross-boundary peer is listed with its expected signing keys (or trusted keystore) and the scopes it may receive
- [ ] Agent Card signatures are verified before first use and on every card refresh; expired or revoked keys are rejected
- [ ] A test with a forged, re-signed, or unsigned card fails closed
- [ ] Delegated credentials are down-scoped to the task and never exceed the delegator's own
- [ ] Peer responses are untrusted input — injection cases for the peer channel live in the eval suite

**Why:** A2A v1.0 lets agents sign their cards but leaves verification a SHOULD and does not bind the key URL to the card's origin. Inside your trust boundary an orchestrator calls functions; across it, an unverified card is an unauthenticated principal you are about to hand work — and possibly data — to.

**Common gap:** fetching a partner's Agent Card over HTTPS and treating TLS as proof of who operates the agent.

---

## Governance and regulation

### 31. Regulatory classification record

*Binds: Wherever the product is exposed to a regulated jurisdiction, e.g. EU users.*

- [ ] Jurisdictions in scope are listed (where users are, where outputs are used)
- [ ] The EU AI Act role (provider, deployer, or both) and risk class are recorded with the reasoning, including whether any Annex III use case applies
- [ ] Art. 50 transparency duties are identified (AI-interaction disclosure, machine-readable marking of synthetic content) with owners and dates
- [ ] Application dates are recorded — Art. 50 from 2 Aug 2026 (marking grace to 2 Dec 2026 only for systems already on the market); Annex III high-risk from 2 Dec 2027; Annex I from 2 Aug 2028
- [ ] A change of intended purpose, user base, or model triggers re-review — and so does each major release
- [ ] The record lives in version control (e.g. the `regulatory` block of `aps-conformance.yaml`)

**Why:** the Digital Omnibus (Regulation (EU) 2026/1744, in force 27 Jul 2026) fixed the high-risk dates, and Art. 50 already applies. Classification is the input every other obligation depends on, and an agent's intended purpose drifts faster than a legal review cycle. The record is the engineering input to a legal assessment — not a substitute for one.

**Common gap:** nobody can say whether the product is a provider or a deployer, because the classification lived in a slide deck from the launch review.
