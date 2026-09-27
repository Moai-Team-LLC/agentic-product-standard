---
name: production-readiness
description: Audit an agentic product against the Definition of Done before launch — context, tools, permissions, reliability, evals, observability, security and identity (MCP 2026-07-28 auth baseline, per-agent identity, inter-agent trust), cost, the Loop License for operation without per-action approval, success-legitimacy audits, measurement science, human oversight, and the regulatory classification record. Also turns the audit into an aps-conformance.yaml the standard's CI Action can score. Use whenever the user is preparing to launch / ship / deploy an agentic product, asks "is this production-ready," wants a pre-launch checklist or a conformance score, or is doing a code review before going live.
---

# Production Readiness — the Definition of Done

An agentic product is not production-ready until every Definition of Done item that binds to it passes. Each item catches a class of failures that has hit real products. Which items bind depends on the product's **operating point** — autonomy (L0–L4) × oversight (O0–O2) — and on what it contains (MCP, multiple agents, tenants, a regulated market). Establish those first.

This is an audit checklist, not a feature list. Walk through it with the user; mark each as pass, gap, or N/A with explicit reasoning. Gaps must be closed or accepted with eyes open.

> **The paved road.** Many of these points come satisfied out of the box if you run the **[AgenticProduct family](../../../ECOSYSTEM.md)** reference stack — memory (AgenticMind), runtime & fleet ops (AgenticOps), evals & observability (AgenticPerformance), the model & cost plane (AgenticGateway), and Layer-8 red-teaming (AgenticAssurance). It's the fastest way to green, not a requirement — satisfy any point your own way (Principle 2). See the [`reference-stack`](../reference-stack/SKILL.md) skill.

## The items

<!-- canon:begin:skill.readiness.summary -->
**33 items.** Walk them with the checks, the *why*, and the common gap for each in [`DOD.md`](DOD.md) (generated from the canon, bundled with this skill).

| # | Item | Group | Binds | Band |
|---|---|---|---|---|
| 1 | Context budget held | Context and state | always | M1 |
| 2 | State externalized | Context and state | always | M1 |
| 3 | Compaction tested | Context and state | always | M2 |
| 4 | Destructive actions need approval | Tools and permissions | always | M1 |
| 5 | Permissions in code, not prompt | Tools and permissions | always | M1 |
| 6 | Sandboxed tool execution | Tools and permissions | always | M2 |
| 32 | Tenant isolation below the LLM | Tools and permissions | If multi-tenant | M2 |
| 7 | Durable pause/resume/retry | Reliability | always | M2 |
| 8 | Schema-validated outputs | Reliability | always | M1 |
| 9 | Input/output guardrails | Reliability | always | M1 |
| 10 | ≥50 evals per failure mode | Evals and observability | always | M1 |
| 11 | Judges calibrated (TPR/TNR) | Evals and observability | Wherever an LLM judge is used | M2 |
| 12 | CI blocks regression; 100% traced | Evals and observability | always | M2 |
| 29 | Telemetry contract | Evals and observability | always | M2 |
| 13 | Lethal-trifecta check | Security and identity | always | M2 |
| 14 | MCP tool defs pinned; allow-listed registry | Security and identity | Wherever MCP is used | M2 |
| 26 | MCP protocol & auth baseline | Security and identity | Wherever MCP is used | M2 |
| 27 | Per-agent identity | Security and identity | always | M2 |
| 15 | Per-run cost ceiling in code | Cost | always | M2 |
| 16 | Loop License (six gates) | Operating without per-action approval (O1+) — the Loop License | At oversight O1 or O2 | M2 |
| 17 | Stop conditions | Operating without per-action approval (O1+) — the Loop License | At autonomy L3+ or oversight O1+ | M2 |
| 18 | Independent verification | Operating without per-action approval (O1+) — the Loop License | At oversight O1 or O2 | M2 |
| 19 | Loop economics | Operating without per-action approval (O1+) — the Loop License | At oversight O1 or O2 | M2 |
| 30 | Success-legitimacy audit | Operating without per-action approval (O1+) — the Loop License | At oversight O2 | M2 |
| 20 | Judge calibration (ECE/Brier) | Measurement science and human oversight | Wherever an LLM judge gates O1+ operation, auto-apply, or release | M2 |
| 21 | Retrieval metrics | Measurement science and human oversight | Wherever memory or retrieval is used | M2 |
| 22 | Ground-truth provenance | Measurement science and human oversight | always | M2 |
| 23 | Drift monitoring | Measurement science and human oversight | always | M2 |
| 33 | Human oversight as a program | Measurement science and human oversight | always | M2 |
| 24 | No safety gate silenced to pass CI | Gate integrity | always | M1 |
| 25 | Graph License | Composition (multi-agent) | Any graph of agents operating at O1+ | M2 |
| 28 | Inter-agent trust | Composition (multi-agent) | Wherever work is delegated across a trust boundary | M2 |
| 31 | Regulatory classification record | Governance and regulation | Wherever the product is exposed to a regulated jurisdiction, e.g. EU users | M1 |

<!-- canon:end:skill.readiness.summary -->
---

## Audit posture

When running this audit with the user:

- **Pin down the operating point first.** Autonomy L0–L4, oversight O0–O2, and the profile flags (multi-tenant, MCP, multi-agent, cross-boundary delegation, LLM judges, retrieval, regulated market). They decide which items bind — the table above says when each one does.
- **Walk through each point sequentially** (read `DOD.md` for the checks, the *why*, and the common gap). Don't jump around.
- **For each: pass / gap / N/A with reason.** "N/A because we don't have destructive actions" is fine; "N/A because we don't think it matters" is not.
- **Estimate effort to close each gap.** Rank them by risk-adjusted cost.
- **Make the explicit launch decision.** "Launch with these N gaps accepted, address in week 1" is a valid choice. "Launch and hope" is not.
- **Leave a machine-checkable record.** Offer to write the result as an `aps-conformance.yaml` — the scorecard ids, each with `status` and the evidence path — so the standard's `aps-conformance` Action can re-score it on every PR (`docs/conformance.md` in the standard repo). The template is `templates/conformance/aps-conformance.template.yaml`.

## Post-launch hardening (after the Definition of Done)

Once every binding item is met, the next tier of investments:

- **A/B testing infrastructure** — compare new prompts/models/tools against current production
- **Cost telemetry per request, per user, per agent type** — find the expensive calls
- **Failure runbooks** — what to do when each named failure mode fires in production
- **Eval set growth from production** — sample weekly, label, add to eval set
- **Model swap exercise** — verify you can swap the model without breaking: re-run evals, re-measure the context budget, re-derive cost ceilings (items 1, 15); trains the muscle
- **Multi-region deployment** — if availability matters
- **Privacy controls and audit log** — GDPR/CCPA compliance if you serve regulated users

## Common "almost ready" patterns

Teams are usually only a few points short. The common gaps are:

| Gap | Frequency | Severity |
|---|---|---|
| #11 (judge calibration) | Very common | High — invalidates eval scores |
| #5 (code-enforced permissions) | Very common | Critical — Replit-class incident risk |
| #2 (state externalized) | Common | High — first restart loses work |
| #7 (durable execution tested) | Common | High — failure on first real crash |
| #12 (CI gating) | Common | Medium — slow degradation over time |
| #27 (per-agent identity) | Common | High — one shared key means no scoping, no revocation, no attribution |
| #26 (MCP baseline) | Common in 2026 | High — session-bound state and DCR-only clients break on the new revision |

If the user is short on time, prioritize closing these.

## Output of this skill

When the audit completes, the user should have:

1. A pass/gap/N/A result for every binding item — ideally as an `aps-conformance.yaml`
2. Effort estimate to close each gap
3. A risk-adjusted prioritization
4. An explicit launch decision with accepted risks documented
5. A 30-day hardening roadmap for post-launch
