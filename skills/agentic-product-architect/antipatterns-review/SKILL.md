---
name: antipatterns-review
description: Review existing agentic code, designs, or plans through the lens of the canonical antipatterns of the Agentic Product Standard. Diagnose what's likely to fail in production. Use whenever the user asks you to review their agent code, asks "what's wrong with this design," is debugging mysterious failures, or wants a second opinion on an architecture. Also use proactively when you notice one of the antipatterns in a conversation, even if the user didn't ask for review.
---

# Antipatterns Review

This skill is your code-review mode. Walk through the user's design, code, or plan and check for each of the 20 canonical antipatterns. For each found, name it, explain the failure mode it produces, and propose the fix.

This is not a generic "review my code." It's a targeted scan against the 20 known failure patterns that have hit real production agentic products.

## How to apply this skill

When invoked, do this:

1. Ask the user to share what you're reviewing (code, design doc, screenshot, description)
2. Walk through the 20 antipatterns in order
3. For each: pass / present / unclear, with evidence
4. For each "present": name it, explain the failure, propose the fix
5. Prioritize by severity (critical > high > medium > low)
6. Summarize the top 3 to fix first

## The 20 antipatterns

*Generated from `canon/antipatterns.yaml` in the standard repo — the same list `STANDARD.md` Part VIII and the README carry.*

<!-- canon:begin:skill.antipatterns.items -->
### 1. Multi-agent before a single-agent baseline

**Signal:** the design has 3+ agents from day one; no single-agent version was tried.

**Failure mode:** complexity tax without proven value. Sub-agents lose context to each other; coordination overhead dominates; debugging is hard.

**Fix:** rebuild as single-agent. If it works at 80%+ pass rate, you have a baseline. Add a second agent only when the single-agent version demonstrably hits a wall (context exhaustion or genuine parallelizable subtasks).

**Severity:** High — almost always over-engineering

---

### 2. Framework abstractions before understanding the raw API

**Signal:** code uses LangGraph / CrewAI / etc. but the engineer can't explain what the underlying LLM calls look like or what gets sent over the wire.

**Failure mode:** debugging becomes reverse-engineering the framework. Performance issues invisible. Bugs misattributed to the model.

**Fix:** rebuild v0 in raw SDK calls. Once you understand the call shape, decide if the framework still earns its place. Many teams discover they don't need it.

**Severity:** High — compounds every future bug

---

### 3. LLM judges without calibration against human labels

**Signal:** team has LLM judges in evals; no one has measured TPR/TNR against a human-labeled set.

**Failure mode:** scores look good while quality degrades; or scores look bad while quality is fine. Either way, team loses trust in evals and reverts to vibe check.

**Fix:** get 100 human labels for each judge. Run the judge. Compute TPR/TNR. Iterate the judge prompt to > 80% on both. Re-run calibration whenever the judge prompt changes.

**Severity:** Critical — invalidates the entire eval system

---

### 4. Permissions enforced through prompts

**Signal:** system prompt has instructions like "do not delete production data" or "always ask before sending email."

**Failure mode:** model under pressure / prompt injection / context loss ignores the instruction. Replit case ([Fortune, 23 Jul 2025](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/)): a production database holding records on 1,206 executives and 1,196+ companies deleted despite an explicit "code freeze."

**Fix:** the agent must literally not have credentials that bypass the boundary. Destructive actions route through a separate approval service that the LLM cannot call directly. OAuth scopes constrain what's even possible.

**Severity:** Critical — Replit-class incident risk

---

### 5. Memory as an afterthought

**Signal:** memory was added late; it's bolted on to an existing agent loop; no policy for what gets written or evicted.

**Failure mode:** memory grows without bound; agent retrieves irrelevant junk; personalization is inconsistent or wrong.

**Fix:** treat memory as architecture (see `memory-architecture/`). Define types, vendor, write/read discipline, eviction, privacy. Sometimes the right answer is "remove memory until we need it."

**Severity:** Medium-High — hard to retrofit

---

### 6. Generic evals ("helpfulness," "correctness")

**Signal:** eval suite has "is this response good?" or "is this correct?" as the primary metric.

**Failure mode:** misses product-specific failure modes. "Helpfulness" is high while users complain about the specific things that matter.

**Fix:** read 20–50 production traces. Identify 5–10 named, product-specific failure modes ("missed handoff," "stale data," "wrong tool"). Each becomes an eval. Drop generic metrics or keep them as supplementary.

**Severity:** High — wasted eval investment

---

### 7. Likert scales in an LLM judge (binary only)

**Signal:** LLM judges output scores 1–5 or "rate the quality."

**Failure mode:** scores don't align with human raters; noise dominates signal; teams can't act on a 3.4 vs 3.6.

**Fix:** binary outputs only. True/false. Pass/fail. Each judge checks one specific criterion. If you need multiple dimensions, use multiple binary judges.

**Severity:** Medium-High — produces unactionable metrics

---

### 8. >100 tools per agent

**Signal:** tool count is in the high tens or hundreds; agent often picks the wrong tool.

**Failure mode:** tool descriptions overlap; model can't disambiguate; selection accuracy drops sharply past ~20 active tools.

**Fix:** Three options (see `tool-design-mcp/`):
- Routing — classifier dispatches to specialist with ~5–10 tools
- RAG-MCP — retrieve only relevant tools per turn (3.2× accuracy lift)
- Hierarchical tools — meta-tools that internally dispatch

**Severity:** High — tool selection failures cascade

---

### 9. One agent for both breadth and depth

**Signal:** the same agent handles both "research X across many sources" and "write coherent long document about X."

**Failure mode:** wrong architecture for at least one of the tasks. Multi-agent for the depth-first work loses context; single-agent for the breadth-first work serializes parallelizable work.

**Fix:** split. The breadth-first task gets multi-agent (orchestrator + sub-agents). The depth-first task gets single-agent. They can share tools and memory; they shouldn't share architecture.

**Severity:** High — fundamental architectural mismatch

---

### 10. Deploying without trace monitoring

**Signal:** agent is in production; only logs are application logs (errors, generic info).

**Failure mode:** most agent failures (routing errors, tool selection errors, retrieval misses) are invisible in app logs. Visible only in step-by-step traces. You debug by guesswork.

**Fix:** instrument on the OpenTelemetry GenAI semantic conventions at a pinned revision (OpenInference and OpenLLMetry emit them); ship traces to Langfuse, LangSmith, Braintrust, or Arize. 100% of production traffic traced. Stable run IDs. Trace retention 30–90 days minimum — at least six months where the EU AI Act's high-risk logging duties apply. Content capture off by default (DoD 29).

**Severity:** Critical — blind in production

---

### 11. Hardcoded prompts without version control

**Signal:** prompts live in Python string literals across the codebase; changes are made without diff review.

**Failure mode:** can't roll back; can't A/B test; can't attribute eval changes to prompt changes; can't audit when a regulator asks.

**Fix:** prompts in version control as separate files (Markdown, YAML, JSON). Diff-reviewed. Versioned. Loaded with explicit version IDs in production. Eval scores tagged with prompt version.

**Severity:** Medium-High — invisible until it matters

---

### 12. Treating single-vendor benchmarks as ground truth

**Signal:** team cites "90% improvement" from a vendor blog post or marketing material as justification for an architectural choice.

**Failure mode:** vendor numbers are directionally correct but not absolute truth. Anthropic's 90.2% multi-agent lift, Letta's "500+ interactions," Mem0's benchmarks vs competitors — all real but with measurement bias and selection effects.

**Fix:** treat vendor benchmarks as hypotheses to test on your data. Build evals on your actual use case. Compare on your data, not theirs.

**Severity:** Medium — leads to wrong choices justified by impressive numbers

---

### 13. Trusting community MCP servers without pinning or scanning (rug pulls)

**Signal:** MCP servers are installed straight from a URL or a community list; tool definitions are approved once and never re-checked; no hash pin, no change alert.

**Failure mode:** the tool description you approved is not the one running next week. A server can mutate its tool definitions after you trust it (rug pull) — the model now follows instructions you never reviewed. The supply chain is the attack surface.

**Fix:** install only from an allow-listed registry. Pin tool definitions by hash and alert on any change — including on every refetch after a cached tool list expires. Scan tool descriptions for injected instructions before first use and after each version bump.

**Severity:** Critical — silent compromise through a trusted dependency

---

### 14. Deploying the lethal trifecta with no mitigation

**Signal:** the agent has access to private data, ingests untrusted content (web, email, documents), and can communicate externally (send, post, call out) — and all three legs are live with nothing breaking the chain.

**Failure mode:** injected content reads a secret and exfiltrates it. The three capabilities are individually reasonable; together they are an exfiltration channel. Prompt-level "don't leak data" does not hold.

**Fix:** run the lethal-trifecta check (Simon Willison). If all three legs are present, break at least one by design — strip untrusted content before it reaches a privileged context, drop the external-comms capability on that path, or gate egress through an allow-list the model cannot edit.

**Severity:** Critical — direct data-exfiltration risk

---

### 15. Token passthrough / over-scoped OAuth (confused deputy)

**Signal:** the agent forwards the user's token to downstream services, or holds OAuth scopes far broader than the task needs ("full access, to be safe") — or an MCP client can only register through Dynamic Client Registration and never validates the issuer.

**Failure mode:** confused deputy. A coerced or injected agent acts with the user's full authority across systems; one over-scoped token turns a small compromise into a large one. Blast radius is set by the scope, not by the bug.

**Fix:** mint per-integration OAuth 2.1 scoped tokens for exactly what the task needs; never forward the user's token downstream. Treat scope as a security boundary — least privilege, audited, time-bounded where possible. MCP clients use pre-registration or a Client ID Metadata Document, validate `iss`, and bind stored client credentials to their issuer (DoD 26).

**Severity:** Critical — confused-deputy / privilege-escalation risk

---

### 16. No budget ceiling on autonomous sessions

**Signal:** autonomous or long-running sessions have no per-run token/cost cap enforced in code; cost is watched on a dashboard, if at all.

**Failure mode:** one bad loop is an unbounded invoice. A retry storm or a self-prompting cycle runs until someone notices the bill — the dashboard reports the damage, it doesn't stop it.

**Fix:** enforce a hard per-run token/cost ceiling in code (a circuit breaker) that halts a runaway or looping session. Record cost-per-task in traces so the ceiling is tuned from real data — and re-derive it when the model changes.

**Severity:** High — unbounded cost exposure

---

### 17. Peer-to-peer multi-agent buses instead of an orchestrator

**Signal:** agents talk to each other freely on a shared bus or in a group "debate"; there is no single coordinator owning the task and the context.

**Failure mode:** free-form agent-to-agent chatter multiplies context, compounds misunderstandings between sub-agents, and resists evaluation — you cannot score a path no one owns. Coordination overhead dominates; debugging is guesswork.

**Fix:** use an orchestrator with isolated sub-agents. The orchestrator owns the task and the context; sub-agents receive scoped briefs and return results. Communication flows through the coordinator, not a peer mesh.

**Severity:** High — unevaluable, context-multiplying coordination

---

### 18. Prose topology counted as a control (an SOP-defined route is not a guardrail)

**Signal:** the graph's routing is described in an SOP, a skill, or a system prompt — "the researcher hands off to the reviewer, who never writes to production" — and that description is cited in a design review or a license as though it constrained anything. Nothing in the runtime or the code prevents a different route.

**Failure mode:** the topology holds right up until the moment it matters. Under an ambiguous state, a novel input, or an injected instruction, the agent takes an edge the diagram does not have, and every control that assumed the diagram silently no longer applies. The architecture diagram and the running system diverge with no error, because prose cannot fail loudly.

**Fix:** mark every edge class **enforced** or **declared** at architecture time. Enforced means the runtime or the code makes the other routes unavailable. Count only enforced edges as controls in any license; declared edges are documentation. This is the graph-scale form of "permissions enforced by code, not by prompt" (anti-pattern 4) — an instruction-defined route binds exactly as well as an instruction-defined permission.

**Severity:** High — controls that are believed but not enforced

---

### 19. License inheritance by wiring (a graph of licensed loops is not a licensed graph)

**Signal:** "every agent in the graph is production-ready, so the graph is production-ready." Per-node evals exist; there is no end-to-end eval on the composition. Cost caps are per-node with no aggregate ceiling. The kill switch was tested against idle nodes, never against branches in flight. Each node escalates to its own owner.

**Failure mode:** the graph's risks are the ones no node owns. Nodes that pass in isolation fail in composition; fan-out multiplies spend past every per-node cap while each cap reads green; an unlicensed or uncalibrated node on an action path lends the whole path a freedom from oversight it never earned; and when something goes wrong, the escalation path forks and no human is on the hook for the system.

**Fix:** give the graph its own **Graph License** — the six gates re-evaluated at graph scope, plus the weakest-link bound (a path runs under no less oversight than its least-licensed node allows), shared-state provenance, fan-in as a declared verification point, and one named escalation owner. Run [`templates/graph-license/CHECKLIST.md`](../../../templates/graph-license/CHECKLIST.md).

**Severity:** Critical — unearned autonomy on paths that reach production

---

### 20. Counting a pass as a success without legitimacy review

**Signal:** the success rate comes only from automated checks; nobody reviews the path of runs that passed; the agent can write to the tests, graders, or eval sets that score it; the pass rate climbs faster than the product gets better.

**Failure mode:** the agent learns to satisfy the checker instead of the task — editing or skipping tests, special-casing the grader's inputs, hard-coding expected outputs. METR found that on tasks longer than eight hours at least 16% of runs scored as successful were illegitimate on review. The metric rises while real capability does not, and the Loop License is issued on a number that measures gaming.

**Fix:** put checks, graders, eval sets, and thresholds outside the agent's write scope. Each release, review a stratified sample of successful runs — the path, not just the outcome; publish the legitimacy rate next to pass@1 and pass^5 and gate promotion on a declared floor (DoD 30). Turn every illegitimate success into a regression case and, where possible, a deterministic tripwire.

**Severity:** High — Critical at O2, where licenses are issued on the gamed metric

<!-- canon:end:skill.antipatterns.items -->
---

## Severity scale (when reporting)

| Severity | Meaning | Action |
|---|---|---|
| **Critical** | Production incident risk; data loss / security / blindness | Fix before launch |
| **High** | Hurts quality or velocity significantly; compounds over time | Fix in week 1 post-launch |
| **Medium** | Suboptimal but not blocking | Plan for the next sprint |
| **Low** | Style or preference | Address when convenient |

## How to deliver the review

Format the output as:

```
## Antipatterns Review

### Critical
- [#4 Permissions through prompts] — system prompt has "do not delete..." 
  but the agent has DROP TABLE permissions. Fix: ...
  
### High
- [#1 Multi-agent before baseline] — design uses 4 sub-agents without 
  single-agent baseline. Fix: rebuild as single-agent, validate at 80%+ 
  pass rate, then add agents only where bottleneck is proven.

### Medium
- [#11 Prompts not versioned] — prompts in Python string literals. 
  Fix: extract to /prompts/*.md, load by version ID.

### Top 3 to fix this week
1. ...
2. ...
3. ...
```

Be specific. Quote the user's code or design when pointing to a problem.

## Posture when reviewing

- **Be direct, not harsh.** Name the antipattern, explain the failure mode, propose the fix. No softening.
- **Acknowledge what's good.** If they've done #5, #7, #10 well, say so. Calibration matters.
- **Don't pad.** If only a couple of antipatterns are present, the review is short.
- **Propose the smallest viable fix.** Don't recommend rewriting everything when a targeted change closes the issue.

## What this skill is NOT

- It is not a generic code review (style, performance, testing patterns)
- It is not a security audit (use a security review for that)
- It is not a complete production-readiness check (use `production-readiness/` for the full 33-point DoD)

Focus on the 20 antipatterns; route the user to the right place for other concerns.

## Output of this skill

When the review completes, the user should have:

1. A pass/present/unclear scorecard for all 20 antipatterns
2. For each "present": named issue, failure mode, proposed fix
3. Severity ranking
4. Top 3 to fix this week, with concrete next steps
5. A pointer to `production-readiness/` for the full launch audit
