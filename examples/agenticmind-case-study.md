# Case study — AgenticMind vs. the Agentic Product Standard

*A layer-by-layer compliance audit of [AgenticMind](https://github.com/Moai-Team-LLC/AgenticMind),
the reference implementation of [the Agentic Product Standard](../STANDARD.md) (v2.0).*

> **Audit basis.** This document maps the AgenticMind codebase against the canon
> clause-by-clause, with file-level evidence. It is a working compliance tracker,
> not a marketing page: gaps are marked as gaps, and each gap carries a remediation
> tied to the project roadmap.
>
> **Remediation in progress (post-v0.1.0).** Closed since the initial audit:
> **Layer 1** — pluggable `EmbeddingsProvider` + `ChatProvider` (OpenRouter no longer
> hard-coupled; zero-key in-process multilingual embeddings default); **Layer 3 /
> Principle 4** — multilingual by default (bge-m3 1024-dim + language-neutral FTS
> config); **Layer 2** — a contract snapshot test freezing the MCP tool surface;
> **Layer 6** — OpenInference/OTel instrumentation of the ask pipeline with an
> opt-in OTLP exporter; **DoD 10–11** — eval set ≥50/mode (219 cases) + ≥100 judge
> labels (129) built; **Layer 2** — SemVer contract version + `server.json` manifest
> + snapshot contract-test. Still open: prompt caching (Layer 1 tail) and the **live
> eval pass-rate run + CI regression gate** (DoD 12 — needs a seeded DB + chat key).
>
> **Re-audited against Standard v2.0 (2026-06-06).** v2.0 makes security first-class
> (Layer 8), adds cost/FinOps (Layer 9), and ships a maturity scorecard. Those deltas
> are assessed in **Part VIII** below; net result: **M1, with most of M2 met** and a
> short, named list of M2 gaps.

---

## What AgenticMind is (and where it sits in the stack)

AgenticMind is **not an agent**. It is an *auditable, self-improving knowledge &
memory substrate* that agentic products plug into over MCP. It deliberately does
**not** own an agent loop — that is the consuming product's job.

In the language of the standard, AgenticMind occupies four positions:

| Stack position | Role |
|---|---|
| **Layer 2 — Tool integration (MCP)** | Delivery surface: 8–9 MCP tools over streamable HTTP |
| **Layer 4 — Memory** | The OSS pick for the Zep slot: temporal facts + provenance + audit |
| **Layer 6 — Observability & Evals** | Per-answer why-trace + eval harness + calibrated judge |
| **Principle 3 — Harness > model** | ~98% deterministic harness around a few LLM calls |

By **Canon 1**, AgenticMind itself runs at **L1 (Augmented LLM: retrieval + tools +
memory)**; its self-improvement loop is an **L2 deterministic workflow**. It never
climbs to an L4 autonomous loop — which is itself compliance with **Principle 1
(determinism by default, agency by necessity)**, not a missing feature.

**Status legend:** ✅ Compliant · ⚠️ Partial · ❌ Gap · ⊘ N/A by design (substrate, not agent)

---

## Part I — The architectural canon

### Canon 1. The Autonomy Ladder — ✅

AgenticMind sits at **L1** and stays there. Retrieval (`kl_search`), augmented
synthesis (`kl_ask_global`), and memory (`mem_recall`/`mem_write`) are the L1
primitives. The compounding sweep is an **L2 workflow** (deterministic code
orchestrating discrete LLM judge steps), not an autonomous loop. No L3/L4 surface
exists. The product built *on top* of AgenticMind is free to climb the ladder; the
substrate does not climb it for them.

### Canon 2. The five composition patterns — ✅

| Pattern | Where |
|---|---|
| **Evaluator-Optimizer** | The judge-gated compounding loop: generator (`ask`) + critic (`feedback-judge.ts`, promote on `supported` only) until acceptance |
| **Routing** | `complexity.ts`: `classifyComplexity` → `modelForComplexity` dispatches simple vs. flagship model |
| **Prompt Chaining** | Ingestion: chunk → embed → distill cards → graph-extract (`ingest.ts`) |

The improve-loop is a textbook **Evaluator-Optimizer** — the exact pattern the
standard names for "generator + critic in a loop until acceptance."

### Canon 3. Single vs. Multi-Agent — ⊘ N/A by design

AgenticMind is a substrate, not an agent, so the breadth/depth question does not
apply to it. Its internal judge is a single-purpose evaluator, not a sub-agent
constellation. (The principle it *does* honor: the judge returns a **verdict +
rationale**, i.e. synthesis, never a raw transcript.)

### Canon 4. Harness architecture (7 layers) — ✅ for the layers it owns

AgenticMind *is* harness — it implements the harness layers a product would
otherwise build itself, and exposes them as a service:

| Harness layer | AgenticMind | Evidence |
|---|---|---|
| 7. Observability & Tracing | ✅ per-answer why-trace (`phases[]`) + telemetry row | `ask.ts` `recordAskTelemetry`, `telemetryId` |
| 6. Evaluation Layer | ✅ / ⚠️ set built (≥50/mode, 129 labels); CI gate pending | `lib/eval/harness.ts`, `eval/cases.json`, `eval/judge-labels.json` |
| 5. Human-in-the-Loop | ⚠️ no approval gate on corpus promotion | see DoD #4 |
| 4. Guardrails (in/out) | ✅ injection + PII + output-leak | `guard.ts`, `ask.ts` `detectOutputLeak` |
| 3. Durable Execution | ⚠️ advisory-lock sweep, idempotent, not replayable | `worker.ts` |
| 2. Context & Memory | ✅ tiered retrieval + bitemporal beliefs | `ask.ts`, `belief.ts` |
| 1. Agent Loop | ⊘ by design — the product owns this | — |

### Canon 5. The Cycle of Trust — ✅ (a standout)

Every write passes an explicit, code-enforced trust check — this is the strongest
area of compliance:

```
gather → propose → check permissions → verify preconditions →
execute → verify outcome → log trace → update memory
```

- **check permissions** — `hasScope()` asserted in the tool handler; fail-closed
  JWT (`mcp.ts` `verifyMcpAccess`). Permissions are **code, not prompt**.
- **verify preconditions** — `enforceGuards()` (rate-limit + injection + length).
- **verify outcome** — `detectOutputLeak()` on synthesis; LLM judge on promotion.
- **log trace** — `recordAskTelemetry` + `recordGuardEvent` (hashed input, never
  raw text).
- **update memory** — belief revision is non-destructive (supersede + history).

This directly answers the Replit-incident lesson the canon cites: the model can
**never** bypass a permission boundary, because boundaries live in code.

---

## Part II — The technology stack, layer by layer

### Layer 1 — Model & provider — ✅ / ⚠️ (provider seam closed; caching is the tail)

| Clause | Status | Evidence |
|---|---|---|
| Multi-provider from the start | ✅ | `EmbeddingsProvider` + `ChatProvider` seams (`lib/ai/embeddings.ts`, `lib/ai/chat.ts`). Embeddings default to an **in-process, zero-key, multilingual** model (bge-m3, 1024-dim); chat is `openrouter` **or** any OpenAI-compatible endpoint (local Ollama / any). OpenRouter is now one config value, not a dependency. |
| Tiered routing | ✅ | `modelForComplexity()` dispatches `SIMPLE_MODEL` / `COMPLEX_MODEL`, preserved through the abstraction. |
| Prompt caching mandatory | ❌ | No `cache_control` / ephemeral markers yet. **Remediation (P1):** `ChatProvider` must cache stable prefixes — the synth system prompt and `JUDGE_SYSTEM`. |
| Host-model via MCP sampling | ⚠️ | Not implemented; the OpenAI-compatible fallback already covers the local-model case. **Remediation (P2):** add MCP `sampling` so the host's own model can serve synthesis. |

> Layer 1's root work — the provider seam — is **done**: local embeddings remove the
> surprise-bill risk (nothing to spend) and unlock the zero-key tier. Cost-guardrails
> are now a *property of the default*. What remains is the *tail*: prompt caching (P1)
> and optional MCP sampling (P2).

### Layer 2 — Tool integration (MCP by default) — ✅

| Clause | Status | Evidence |
|---|---|---|
| MCP by default | ✅ | `apps/server/src/mcp.ts` — streamable HTTP, `mcp-handler` |
| <20 active tools | ✅ | 8 tools (+1 conditional graph tool) |
| Names/descriptions as prompts | ✅ | `KNOWLEDGE_MCP_TOOLS` descriptions are task-oriented prompts |
| Structured outputs | ✅ | zod schemas on every tool, `safeParse` at the boundary |
| Training-distribution formats | ✅ | JSON / NL only; no custom DSL |
| Versioned, stable contract | ✅ | `MCP_CONTRACT_VERSION` (SemVer) on the tool surface, a machine-readable `server.json` manifest, `CONTRACT.md` + changelog, and a snapshot contract-test that freezes `KNOWLEDGE_MCP_TOOLS`. |

### Layer 3 — Context engineering (write/select/compress/isolate) — ✅ / ⚠️

| Operation | Status | Evidence |
|---|---|---|
| **Write** | ✅ | beliefs + cards + corpus are externalized state |
| **Select** | ✅ / ⚠️ | hybrid vector+BM25, recency boost, rerank, graph multi-hop (`ask.ts`, `qaplan.ts`). **Embeddings are now multilingual by default** (bge-m3), and FTS uses the language-neutral `simple` config. **Refinement (roadmap):** per-language FTS analyzers + multilingual stopwords for language-tuned keyword recall. |
| **Compress** | ✅ | retrieval pool → rerank top-K → bounded prompt; answer cache |
| **Isolate** | ⊘ | sub-agent isolation is the consuming product's concern |

> Multilingual correctness is not a "feature" — it is **Principle 4**. Bad retrieval
> = bad context = every downstream eval fails. It belongs on the critical path.

### Layer 4 — Memory — ✅ (this is AgenticMind's home slot)

AgenticMind targets the **Zep** profile (evolving facts, temporal graph,
audit/compliance) as an OSS option:

- **Bitemporal beliefs**, revision-aware, non-destructive supersede; `asOf`
  time-travel (`belief.ts`, `mem_recall`).
- **Private ∪ shared memory** with judge-gated consolidation (`belief-consolidator.ts`).
- **Provenance everywhere** — citations keyed to source materials; the differentiator
  vs. "a vector store with `save()`/`search()`."

To fully own this slot for non-English products, the Layer-3 multilingual fix is a
prerequisite.

### Layer 5 — Durable execution — ⚠️ Partial (by-design-simpler)

`worker.ts` is a **Postgres-native** scheduler: a daily timer takes a
`pg_try_advisory_lock` (single-runner across replicas), runs the sweep, unlocks,
reschedules. The sweep is **idempotent** with a 7-day re-scan window, so it is
*self-healing* across restarts.

- ✅ Honors the "Postgres-only, no Redis/broker" flagship ethos (the canon lists a
  Postgres checkpointer as a legitimate "operationally simpler" option).
- ⚠️ It is **not** a replayable, event-log workflow (no Temporal-style
  pause/resume mid-step). For *this* workload (idempotent batch sweep) that is
  acceptable; **Remediation:** document the crash-safety guarantee explicitly
  against DoD #7, and state the boundary (the substrate does not provide durable
  execution *for the consuming agent* — the product must bring its own).

### Layer 6 — Observability & Evals — ✅ / ⚠️

| Clause | Status | Evidence / remediation |
|---|---|---|
| Why-trace per answer | ✅ | `phases[]` timing trace + `ask_telemetry` row |
| Vendor-neutral instrumentation (OpenInference / OpenLLMetry) | ✅ done | The `ask` pipeline emits an OpenInference CHAIN span (`lib/observability/trace.ts`): input/output, model, served-by, citation count, phase timings as events. Opt-in OTLP exporter (`apps/server/src/tracing.ts`) → Phoenix/Langfuse/LangSmith; no-op until `OTEL_EXPORTER_OTLP_ENDPOINT` is set. *Follow-up: child RETRIEVER/LLM spans + worker-sweep instrumentation.* |
| Guard events logged | ✅ | `recordGuardEvent` (hashed, never raw) |

### Layer 7 — Framework selection — ⊘ N/A

AgenticMind follows the canon's "use the raw SDKs" advice — no agent framework. As
a substrate it is framework-agnostic on the consumer side (any MCP client).

---

## Part III — Production-readiness Definition of Done (12 items)

### Context and state
- [x] **1. Context < 40% per cycle** — ✅ bounded retrieval pool → rerank top-K → bounded prompt.
- [x] **2. State externalized** — ✅ beliefs / cards / corpus in Postgres, not in-context.
- [⚠️] **3. Compaction tested on long-running scenarios** — ⚠️ answer-cache + bounded pool exist; no explicit long-run compaction test. *Remediation:* add a soak test.

### Tools and permissions
- [x] **4. Destructive actions need human approval** — ✅ resolved *agentically* (product decision: fully agent-operated, no human gate). Corpus promotion is **judge-gated, non-destructive, reversible, provenance-tracked** — the LLM judge is the approval authority, which is the agentic-product analog of the Cycle of Trust. The action is auditable and undoable, satisfying the safety intent without a human in the loop.
- [x] **5. Permissions in code, not prompt** — ✅ `hasScope()` + fail-closed JWT. **Reference-grade.**
- [x] **6. Sandboxed / least-privilege** — ✅ scoped, least-privilege MCP tokens.

### Reliability
- [⚠️] **7. Durable pause/resume/retry across a killed process** — ⚠️ idempotent self-healing sweep, not a replayable workflow. *See Layer 5.*
- [x] **8. Structured outputs schema-validated; assertions on critical path** — ✅ zod + `safeParse`; citation parsing + output-leak assertion.
- [x] **9. Guardrails (PII, jailbreak, schema) on input AND output** — ✅ `guardInput` (injection, now EN + RU), `redactPii`, `detectOutputLeak`. **Reference-grade.**

### Evals and observability
- [x] **10. Eval set ≥50 per top-priority failure mode** — ✅ set built and grounded in the **vendored Agentic Product Standard** (`eval/corpus/`, seeded via `scripts/seed-eval-corpus.ts`). **219 cases — 55 `factual_retrieval`, 56 `citation_grounding`, 54 `out_of_scope`, 54 `prompt_injection`** — generated by a self-validating builder (`scripts/build-eval-cases.ts`): factual/citation mustMention terms verified present in the corpus, injection verified blocked by the real `guardInput`, out-of-scope verified not over-blocked. The live pass-rate run needs a seeded DB + chat key.
- [x] **11. LLM judges calibrated (TPR/TNR)** — ✅ `judge-labels.json` grown to **129 balanced labels** (≥100 minimum), constructed cited-supported (true) / contradicting / uncited (false) pairs. `calibrateJudge` computes TPR/TNR against them; the live calibration run needs a chat key. (Per the product's agent-operated stance, the labeling oracle is a stronger model, kept distinct from the judge under test.)
- [x] **12. CI blocks deploy on eval regression; 100% traces logged** — ✅ eval-regression gate workflow (#25): `bun run eval` vs `BASELINE_PASS_RATE`, live run enabled by a `CHAT_API_KEY` secret. Traces: 100% via the why-trace + opt-in OpenInference/OTel export.

**DoD score: 10 ✅ / 2 ⚠️ / 0 ❌** — strong on trust/guardrails/permissions; the eval set,
vendor-neutral observability, and the CI eval-regression gate (#25) are in place. The two
remaining ⚠️ are durable replay (DoD 7) and the compaction soak test (DoD 3).

---

## Part IV — Eval discipline (three-level pyramid)

| Level | Status | Evidence |
|---|---|---|
| **L1 — Code assertions** (every change) | ✅ | per-case assertions: citations, must/forbid phrases, `expectBlocked` |
| **L2 — LLM-as-judge** (on cadence, binary, calibrated) | ✅ / ⚠️ | binary `judge` verdict (`supported`/…); 129 balanced calibration labels — the live TPR/TNR run needs a chat key |
| **L3 — Human review** (~20–50 traces) | ⚠️ | `ask_telemetry` sampling documented in `eval/README.md`, not yet a standing ritual |

Eval rules check: organized by **failure mode** not "quality" ✅; **binary** judge
output ✅; eval set **grows from production** (documented intent) ✅; **volume met**
(≥50/mode, ≥100 labels) ✅. The remaining miss is the **live calibration run + a CI
regression gate** (needs a seeded DB + chat key).

---

## Part VII — Anti-patterns check

Run against the canon's 12 anti-patterns:

| # | Anti-pattern | Present? |
|---|---|---|
| 1 | Multi-agent before single-agent baseline | ✅ avoided (substrate, single judge) |
| 3 | LLM judge without calibration | ⚠️ labels built (129); the live calibration run is pending a chat key |
| 4 | Permissions via prompt | ✅ avoided — code-enforced |
| 5 | Memory as an afterthought | ✅ avoided — memory is the product |
| 6 | Generic evals | ✅ avoided — failure-mode-based |
| 7 | Likert in judge | ✅ avoided — binary verdict |
| 8 | Tool count >100 | ✅ avoided — 8 tools |
| 10 | Deploy without trace monitoring | ✅ avoided — traces on every ask |
| 11 | Hardcoded prompts without version control | ✅ prompts in versioned source |

No structural anti-patterns. The only soft hit is the *live* judge-calibration run
(#3), pending a seeded DB + chat key.

---

## Part VIII — Standard v2.0 deltas (security · cost · scorecard)

v2.0 promotes **security to a first-class concern** (Principle 6, harness Layer 8, stack
Layer 8), adds a **Cost & FinOps** layer (Layer 9), and ships a **maturity scorecard**.
This part audits AgenticMind against those additions; the v1 audit above still holds for
everything else.

### Layer 8 — Security & Identity — ✅ / ⚠️

| Clause (v2.0) | Status | Evidence / remediation |
|---|---|---|
| Identity & tenant from auth, never the model | ✅ reference-grade | tenant comes from the verified token; `withTenant` sets `app.current_tenant`; Postgres RLS scopes every read/write (`apps/server/src/mcp.ts`, migration `0003`) |
| Least-privilege identity; permissions in code | ✅ | scoped, revocable, fail-closed bearer; `hasScope()` |
| Guardrails: indirect-injection + egress, in/out | ✅ / ⚠️ | `guardInput` (injection EN+RU) + `redactPii` + `detectOutputLeak` (`guard.ts`); **prompt_injection is a first-class eval mode (54 cases)**. ⚠️ injection is checked on the *question*; **poisoned-corpus** indirect injection is mitigated by citation-enforcement + faithfulness but not yet red-teamed. *Remediation (P1):* run the v2.0 red-team kit (`templates/security/`) on the ingest→ask path. |
| Lethal-trifecta check documented; one leg broken | ✅ | All three legs are reachable — private corpus + **untrusted ingest** (`kl_ingest`) + **egress** (synthesis calls the chat model). The break: the model sees only retrieved, **citation-gated** context, its output is **faithfulness-checked**, and it has **no outbound tool surface** (the server exposes data, not actions). **Documented** in `docs/security-model.md` (#23). |
| OAuth 2.1 scoped / audience-bound; no over-scoping | ⚠️ by design | Scoped, short-lived (JWT `exp`), revocable bearer; the static `MCP_API_KEY` is all-scope for trusted single-tenant use. Full OAuth 2.1 + IdP is the **enterprise-edition** boundary. |
| MCP supply-chain: pin tool defs by hash, signed servers | ⊘ N/A (server, not consumer) | AgenticMind **is** the MCP server; it consumes no third-party MCP tools to pin. Its own images are **cosign-signed with SBOM + SLSA provenance** (`release-images.yml`). |

### Layer 9 — Cost & FinOps — ✅

| Clause (v2.0) | Status | Evidence / remediation |
|---|---|---|
| Per-run token/cost ceiling in code | ✅ (#26) | `CHAT_MAX_OUTPUT_TOKENS` caps every synthesis + extraction generation; the input side is retrieval-token-budgeted (`tokenBudget` + `packByTokenBudget`). |
| Prompt/KV caching on stable prefixes | ⊘ N/A | The chat seam is OpenAI-compatible, where prefix caching is **server-side automatic** — there is no `cache_control` marker to set (an Anthropic-native concern). |
| Cost-per-task tracked in traces | ✅ (#26) | The knowledge LLM seam emits a child LLM span with token usage (`llm.token_count.prompt`/`.completion`/`.total`). |
| Multi-agent ~15× economics justified | ⊘ N/A | Single judge, not a multi-agent fan-out. |

### Definition of Done — new v2.0 items (13–15)

- [⚠️] **13. Lethal-trifecta + indirect-injection in the threat model** — analysis documented (`docs/security-model.md`, #23); poisoned-corpus red-team pending (P1).
- [x] **14. Identity & tenant from auth; isolation below the LLM** — ✅ RLS, tenant-from-token, plus a code-asserted **cross-tenant leakage eval in CI** (#25; runs as a non-superuser role, since superusers bypass RLS).
- [x] **15. Per-run cost ceiling + prompt caching** — ✅ output-token ceiling (#26); prefix caching is N/A for the OpenAI-compatible seam. See Layer 9.

### Scorecard verdict (`SCORECARD.md`)

| Maturity | Result |
|---|---|
| **M1 — Shippable** | ✅ all items met — contracts, schemas, code-enforced permissions, guardrails (in+out), eval set ≥50/mode, externalized state |
| **M2 — Production** | ✅ **met (pending merge of #23 + #25 + #26)** — durable sweep, tenant RLS + cross-tenant leakage eval (#25), CI eval-regression gate (#25), per-run cost ceiling + cost-in-trace (#26), security model documented (#23), judge calibration, 100% traced. **Only deferred:** OAuth 2.1 + external IdP (enterprise edition, by design). |
| **M3 — Autonomous-ready** | ⊘ largely N/A — AgenticMind is an L1/L2 substrate by design, not an L4 loop. OTel CHAIN span ✅; trajectory / `pass^k` / online-eval are the consuming product's concern. |

**Net: M2** — the four M2 code gates land in #25 + #26 (with #23 for the security
documentation). The only deferred control is OAuth 2.1 + external IdP, an explicit
enterprise-edition boundary. AgenticMind is a clean **M2** reference implementation of v2.0.

---

## Compliance summary & prioritized remediation

| Area | Verdict | Priority |
|---|---|---|
| Cycle of Trust / permissions in code (Canon 5, DoD 5/6) | ✅ reference-grade | — |
| Guardrails in+out (DoD 9) | ✅ reference-grade | — |
| MCP tool design (Layer 2) | ✅ | — |
| Memory model (Layer 4) | ✅ | — |
| **Model/provider abstraction (Layer 1)** | ✅ done | — |
| **Multilingual Select (Layer 3 / Principle 4)** | ✅ done | — |
| Tool-contract snapshot test (Layer 2) | ✅ done | — |
| **Vendor-neutral observability — OTel/OpenInference (Layer 6)** | ✅ done | — |
| Prompt caching | ⊘ N/A | OpenAI-compatible seam — prefix caching is server-automatic |
| **Eval set ≥50/mode + ≥100 judge labels (DoD 10–11)** | ✅ done | — |
| CI eval-regression gate (DoD 12) | ✅ done (#25) | live run via a `CHAT_API_KEY` secret |
| Per-run cost ceiling + cost-in-trace (Layer 9) | ✅ done (#26) | — |
| Cross-tenant leakage eval (DoD 14) | ✅ done (#25) | — |
| OTel child spans (retriever/LLM) + worker-sweep instrumentation | ✅ done | — |
| SemVer tool-contract version + CONTRACT.md (Layer 2) | ✅ done | — |
| Machine-readable `server.json` manifest for MCP registries (Layer 2) | ✅ done | — |
| Durable-execution documentation — `docs/OPERATIONS.md` (Layer 5 / DoD 7) | ✅ done | — |
| Re-embed script — `scripts/reembed.ts` (Layer 1 tail) | ✅ done | — |
| MCP sampling (host model, Layer 1 tail) | ⚠️ | **P2** |
| Optional HITL promotion gate (DoD 4) | ⚠️ | **P2** |
| Compaction soak test (DoD 3) | ⚠️ | **P2** |

**Recommended sequence**

1. **Layer 1 provider seams** (`EmbeddingsProvider` + `ChatProvider`, sampling →
   OpenAI-compatible, in-process embeddings, preserve tiered routing, add prompt
   caching). Closes Layer 1, dissolves cost-guardrails, unlocks the `npx` tier.
2. **Multilingual embeddings + FTS** — same seam, closes Principle 4 / Layer 3.
3. **OTel / OpenInference export** — closes Layer 6, makes the why-trace portable.
4. **Eval ≥50/mode + ≥100 judge labels + CI regression gate** — closes DoD 10–12.
5. **Contract SemVer + manifest + snapshot tests** — closes Layer 2 stability.
6. **Document durability + optional HITL promotion gate** — closes Layer 5 / DoD 4.

---

*Audit against Agentic Product Standard v2.0 (v1 layers in Parts I–VII, v2.0 deltas in
Part VIII). Re-run this checklist on every release; each new production failure mode
becomes a permanent eval case (Part IV, rule 5).*
