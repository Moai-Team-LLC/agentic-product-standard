# Case study: AgenticGateway — a reference implementation of *Model & provider* + *Cost & FinOps*

[AgenticGateway](https://github.com/Moai-Team-LLC/AgenticGateway) (Apache-2.0)
is the family's model plane: one OpenAI-compatible key on a
[Bifrost](https://github.com/maximhq/bifrost) data plane, implementing the
Standard's Layer 1 (Model & provider) and Layer 9 (Cost & FinOps) — and only
those two surfaces. Guardrails, judging, red-team policy, and evidence are
composed from AgenticMind, AgenticPerformance, and AgenticAssurance, never
re-implemented (a CI grep gate enforces it).

## Gate → implementation

| SCORECARD gate | AgenticGateway module | How |
|---|---|---|
| Per-run token/cost ceiling in code, circuit breaker (Cost M2) | `src/cost/budgets.ts` | tenant-window + per-run scopes in SQLite; fail-closed (a tenant without a budget is denied); trips the moment a ceiling is crossed; runaway-session test |
| Prompt/KV caching; cost-per-task in traces (Cost M2) | `src/cache/exact.ts` · `src/cost/otel.ts` | tenant-scoped exact LRU at the edge + Bifrost's semantic-cache plugin (tenant-scoped via `x-bf-cache-key`); OTLP spans in APL's GenAI/`apl.*` conventions with `apl.cost_usd` per route |
| Multi-agent 15× economics (Cost M2) | `request_ledger` | N/A by design — the gateway supplies per-run cost evidence; the justification is a product decision |
| One abstraction point; provider = config (Model M2, proposed) | `bifrost/` | pinned Bifrost image + GitOps `config.json`; `agw bifrost-config` regenerates providers from the routing policy |
| Eval-sourced model selection, source recorded (Model M2, proposed) | `src/routing/` | policy built from an AgenticPerformance eval export; `eval_run_id` + `synced_at` stored; ranking → Bifrost `fallbacks`; changing the eval run changes routing (tested) |
| One client credential; upstream keys vaulted (Model M2, proposed) | `src/vault/` | `sk-agw-*` stored as sha256 → per-tenant Bifrost virtual key, AES-256-GCM at rest, rotation without client change; leak-free tests |
| Tenant-scoped everything + leakage test in CI (Model M3, proposed) | `tests/isolation.test.ts` | cache, budgets, vault, routing, ledger, evidence proven tenant-isolated |

## Beyond the gates

- **Fail-closed + hash-not-text throughout** — every denial is a typed outcome
  in the ledger and a hash-only evidence event on the AgenticMind
  `/hooks/audit` wire shape.
- **Two-lane latency, CI-benched** — added P50 overhead ~0.1 ms (gate: < 5 ms
  ex-inference), cache hits < 10 ms, streaming TTFB delta < 5 ms; all
  assurance work (ledger, evidence, OTel, anomaly, sampled judge) runs after
  the response.
- **Cycle of Trust on model output** — tool calls reaching protected control
  paths (AgenticAssurance's pack) are flagged or denied, never rewritten,
  never auto-approved.

## The stack

AgenticOps runs the fleet → its agents' calls flow through **AgenticGateway**
→ grounded by AgenticMind → measured by AgenticPerformance → repaired by
AgenticSelfHealingCode → red-teamed by AgenticAssurance — all conforming to
this standard.
