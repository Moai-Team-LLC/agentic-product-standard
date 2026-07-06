---
name: production-readiness
description: Audit an agentic product against the 15-point Definition of Done before launch. Covers context, tools, permissions, reliability, evals, observability, security, and cost — the minimum bar for production. Use whenever the user is preparing to launch / ship / deploy an agentic product, asks "is this production-ready," wants a pre-launch checklist, or is doing a code review before going live.
---

# Production Readiness — 15-Point Definition of Done

An agentic product is not production-ready until all 15 points pass. Each point catches a class of failures that has hit real products.

This is an audit checklist, not a feature list. Walk through it with the user; mark each as pass, gap, or N/A with explicit reasoning. Gaps must be closed or accepted with eyes open.

## The 15 points

### Context and state

#### 1. Context utilization < 40% in typical turn
- [ ] Measure context utilization on representative production traces
- [ ] Median below 40%; p95 below 60%
- [ ] If higher: compaction strategy in place that triggers at threshold

**Why:** past 40% utilization, model recall degrades nonlinearly. The "dumb zone" begins.

**Common gap:** dumping conversation history into every turn instead of using selection / compaction.

---

#### 2. State externalized (not living only in context window)
- [ ] State has a defined home (file, DB, memory layer) — not "the conversation"
- [ ] Can recover full agent state from external storage on crash
- [ ] State writes are explicit and traceable

**Why:** in-context state evaporates on session boundary, restart, or compaction.

**Common gap:** "the agent will remember from the conversation" — it won't, reliably.

---

#### 3. Compaction pipeline tested on long sessions
- [ ] Compaction has been exercised on real long sessions (>50 turns or > 30 min)
- [ ] No critical info lost during compaction (verified by eval cases)
- [ ] Compaction trigger is metric-driven, not turn-count-driven

**Why:** compaction that drops critical state silently is worse than no compaction.

**Common gap:** built compaction, never tested on a session long enough to need it.

---

### Tools and permissions

#### 4. Destructive actions require explicit human approval
- [ ] List of destructive actions enumerated (deletes, writes, sends, charges, etc.)
- [ ] Each one routes through an approval gate
- [ ] Approval is logged with who/when/what

**Why:** Replit incident — agent wiped 1,200+ companies' data despite a "code freeze" prompt. Prompts don't enforce.

**Common gap:** "the prompt tells the agent not to delete production data" — insufficient.

---

#### 5. Permissions enforced by code, not by prompt
- [ ] Agent does not hold credentials that bypass permission boundaries
- [ ] Permission gate is a separate code path the LLM cannot override
- [ ] Even with prompt injection, agent cannot perform forbidden actions

**Why:** prompt injection is a real threat; LLM can be coerced; code cannot.

**Common gap:** OAuth scopes too broad; agent runs as superuser internally.

---

#### 6. Tool execution sandboxed
- [ ] Code execution in containers / VMs, not host environment
- [ ] File operations in scoped working directories
- [ ] Network access through allow-listed domains
- [ ] Secrets never in context window; injected at tool boundary

**Why:** tool execution is an attack surface; treat it like any RPC exposed to untrusted input.

**Common gap:** agent has shell access with no sandbox.

---

### Tenant isolation (if multi-tenant)

Skip this whole section if the product is single-tenant or deployed per customer. Otherwise every box must be checked — there is no partial cross-tenant isolation.

- [ ] Isolation model chosen per data store (pooled + RLS / schema-per-tenant / DB-per-tenant) and recorded in the Agent Contract
- [ ] `tenant_id` is part of the authenticated principal; a request with no resolvable tenant fails closed (no default tenant)
- [ ] Isolation enforced below the LLM (row-level security or repository layer); verified to hold under prompt injection
- [ ] Retrieval filtered inside the index (not post-top-k), memory namespaced, cache key includes `tenant_id`, traces tagged, sub-agent messages and background jobs carry the tenant
- [ ] Tools ignore any model-supplied tenant; a mismatch is audited and rejected
- [ ] A code-asserted cross-tenant leakage eval (canary seeded as A, queried as B incl. an injection variant) runs in CI

**Why:** an agent is a confused deputy — prompt-level isolation leaks. The first cross-tenant leak is a churn-and-lawsuit event, and retrofitting isolation is the migration nobody budgets for. See the `tenant-isolation` skill.

**Common gap:** a tenant-agnostic answer cache serving tenant A's response to tenant B; `tenant_id` passed as a tool argument the model can be talked into changing.

---

### Reliability

#### 7. Durable execution: pause/resume/retry works on killed process
- [ ] Kill the agent process mid-execution; restart; verify it resumes
- [ ] Retry policies defined per activity type
- [ ] Human-wait signals work (agent can wait hours/days for approval)

**Why:** any agent running > 60s will hit a crash, restart, or wait — without durability, work is lost.

**Common gap:** "we tested the happy path" — production isn't the happy path.

---

#### 8. Structured outputs validated by schema; assertions on critical path
- [ ] Every LLM call returning structured data validates against schema
- [ ] Code assertions on critical state transitions
- [ ] No "parse this text output and hope" anywhere on the critical path

**Why:** unvalidated outputs cause silent corruption; assertions catch it early.

**Common gap:** regex-parsing LLM responses; works in dev, fails in production edge cases.

---

#### 9. Guardrails on input and output (minimum: PII, jailbreak, schema validation)
- [ ] Input guardrails: PII detection, jailbreak / prompt injection classifier
- [ ] Output guardrails: schema validation, content policy, citation check
- [ ] Guardrails run on real traffic, with metrics on hit rates

**Why:** defense in depth; multiple cheap guardrails beat one perfect one.

**Common gap:** no input guardrails; trusting the model to refuse.

---

### Evals and observability

#### 10. Eval set ≥ 50 examples per top-priority failure mode
- [ ] At least 5 named failure modes (product-specific, not generic)
- [ ] Each has ≥ 50 cases in the eval set
- [ ] Cases sampled from real or representative traces

**Why:** generic evals don't catch product-specific failures; 50 cases give enough signal to detect regression.

**Common gap:** 20 cases of "helpfulness" — not enough, not the right thing to measure.

---

#### 11. LLM-judges calibrated against human labels (TPR/TNR tracked)
- [ ] Each LLM judge has ≥ 100 human-labeled examples for calibration
- [ ] TPR and TNR both > 80%
- [ ] Calibration re-run when judge prompt changes
- [ ] TPR/TNR reported with every release

**Why:** uncalibrated judges produce meaningless scores; teams stop trusting evals and revert to vibe.

**Common gap:** built a judge; never measured if it agrees with humans.

---

#### 12. CI blocks deploys on eval regression; 100% production traces logged
- [ ] CI runs full eval suite on every PR
- [ ] Merge blocked on regression vs main branch
- [ ] 100% of production traffic produces traces
- [ ] Traces include all required fields (see harness-engineering layer 7)
- [ ] Trace retention sufficient for incident investigation (typically 30–90 days)

**Why:** evals without enforcement are theater; traces are the only way to debug failures after launch.

**Common gap:** evals exist but don't gate merges; tracing is sampled, missing the failures.

---

### Security and identity

#### 13. Lethal-trifecta check performed and documented
- [ ] Three legs assessed: access to private data, exposure to untrusted content, ability to communicate externally
- [ ] If all three are present, at least one leg is broken in design (not by a prompt instruction)
- [ ] The check and its outcome are written down (in the Agent Contract / threat model), not assumed

**Why:** private data × untrusted content × external comms is an exfiltration channel — injected content reads a secret and ships it out. Simon Willison's lethal trifecta: the deployment check every agent must pass.

**Common gap:** all three legs live and unmitigated because no one drew the diagram; "the model won't do that" stands in for a mitigation.

---

#### 14. MCP tool definitions pinned; servers allow-listed; OAuth 2.1 scoped tokens
- [ ] Tool definitions pinned by hash, with a change alert (rug-pull detection)
- [ ] MCP servers installed only from an allow-listed registry — never an arbitrary URL
- [ ] OAuth 2.1 scoped tokens per integration; no token passthrough (the user's token is never forwarded)

**Why:** an approved tool description can mutate after you approve it; a forwarded or over-scoped token turns the agent into a confused deputy. The supply chain is part of the attack surface.

**Common gap:** installing a community MCP server by URL and trusting its description forever; minting broad OAuth scopes "to be safe."

---

### Cost

#### 15. Per-run token / cost ceiling enforced in code
- [ ] A hard per-run token / cost ceiling, enforced in code (circuit breaker) — not a guideline or a dashboard
- [ ] A runaway or looping session trips the breaker and halts
- [ ] Cost-per-task is recorded in traces

**Why:** without a code-level ceiling, one bad loop is an unbounded invoice. Cost is a reliability property, not just a finance report.

**Common gap:** watching cost in a dashboard after the fact instead of capping it in the request path.

---

## Audit posture

When running this audit with the user:

- **Walk through each point sequentially.** Don't jump around.
- **For each: pass / gap / N/A with reason.** "N/A because we don't have destructive actions" is fine; "N/A because we don't think it matters" is not.
- **Estimate effort to close each gap.** Rank them by risk-adjusted cost.
- **Make the explicit launch decision.** "Launch with these N gaps accepted, address in week 1" is a valid choice. "Launch and hope" is not.

## Post-launch hardening (after the 15 points)

Once the 15 are met, the next tier of investments:

- **A/B testing infrastructure** — compare new prompts/models/tools against current production
- **Cost telemetry per request, per user, per agent type** — find the expensive calls
- **Failure runbooks** — what to do when each named failure mode fires in production
- **Eval set growth from production** — sample weekly, label, add to eval set
- **Model swap exercise** — verify you can swap the model without breaking; trains the muscle
- **Multi-region deployment** — if availability matters
- **Privacy controls and audit log** — GDPR/CCPA compliance if you serve regulated users

## Common "almost ready" patterns

Teams often have 13 of 15 covered. The common gaps are:

| Gap | Frequency | Severity |
|---|---|---|
| #11 (judge calibration) | Very common | High — invalidates eval scores |
| #5 (code-enforced permissions) | Very common | Critical — Replit-class incident risk |
| #2 (state externalized) | Common | High — first restart loses work |
| #7 (durable execution tested) | Common | High — failure on first real crash |
| #12 (CI gating) | Common | Medium — slow degradation over time |

If the user is short on time, prioritize closing these.

## Output of this skill

When the audit completes, the user should have:

1. A pass/gap/N/A scorecard across all 15 points
2. Effort estimate to close each gap
3. A risk-adjusted prioritization
4. An explicit launch decision with accepted risks documented
5. A 30-day hardening roadmap for post-launch
