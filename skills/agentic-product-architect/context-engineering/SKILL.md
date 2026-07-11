---
name: context-engineering
description: Engineer what goes into the LLM context window — system prompts, retrieved docs, tool schemas, conversation history, memory, examples. Apply the four operations write/select/compress/isolate to manage context as a finite resource. Enforce the 40% rule on context utilization. Use whenever the user is designing system prompts, debugging quality degradation in long conversations, hitting context limits, managing per-step retrieval, dealing with sub-agent context isolation, or asking about "context engineering" / "prompt engineering" / CLAUDE.md / AGENTS.md / instruction files.
---

# Context Engineering for Agents

Context engineering has displaced prompt engineering as the core skill. Coined by Tobi Lütke, amplified by Karpathy and Willison: it covers everything that enters the context window across a session — system prompt, retrieved content, tool descriptions, history, memory, examples.

The framing comes from LangChain's Lance Martin: context engineering is **four operations applied to a finite resource**.

## The four operations

### Write — externalize state outside the context window

When state must survive across steps but doesn't need to be visible every step, write it out:

- **Scratchpads / working memory:** the agent saves intermediate work to a file or store, reads it back when needed
- **Plans:** Anthropic's Research feature has the LeadResearcher save the plan to memory before spawning sub-agents, so the plan survives compaction
- **Repo-resident knowledge:** `CLAUDE.md`, `AGENTS.md`, `docs/` directory — version-controlled, human-editable, agent-readable
- **Memory store:** Mem0 / Zep / Letta (see `memory-architecture/`) for cross-session persistence

**Rule:** if it's not actively driving the current decision, don't carry it in context. Externalize.

### Select — retrieve only what's needed for this step

The default is to dump everything potentially relevant. The discipline is to select only what this specific step needs.

Three places to apply selection:

- **Documents:** RAG over your knowledge base. Standard.
- **Tools:** when you have many tools, RAG over tool descriptions. RAG-MCP showed +3.2× accuracy on tool selection vs dumping all tool descriptions (cuts prompt tokens by ~50%, lifts tool selection from ~13% to ~43%).
- **Memory:** RAG over past interactions, not "load entire user history."

**Rule:** the selection function is part of the architecture. Document it, test it, and have evals on its precision/recall.

### Compress — keep length below the degradation threshold

Long conversations decay. The "40% rule" from Dex Horthy: **past ~40% context-window utilization, model recall degrades nonlinearly.** Past 60–70%, you're in the "dumb zone."

Compaction is a pipeline, not a single operation. Claude Code's 5-layer reference design:

1. Drop low-value content first (verbose tool outputs, intermediate work)
2. Summarize old turns into 1–2 sentences each
3. Replace tool call sequences with a condensed result
4. Summarize entire conversation segments
5. Hard truncate with summary if all else fails

**Rule:** the compaction trigger should fire at 40%, not 90%. Compacting late is compacting badly.

### Isolate — separate concerns across context windows

When two tasks need different framing or would interfere, give them separate windows. This is the architectural argument for sub-agents.

- **Sub-agent isolation:** breadth-first research with 5 sub-agents each gets a clean window for their slice
- **Tool-call isolation:** complex tools can run inside their own LLM call rather than polluting the main loop
- **Phase isolation:** plan in one context, execute in another, verify in a third

**Rule:** isolation is not free — coordination overhead grows. Use it where parallelism or independent framing earns its cost.

## The 40% rule (operational)

Track context utilization at every turn. Three thresholds:

| Utilization | Status | Action |
|---|---|---|
| < 30% | Healthy | Continue |
| 30–40% | Watch | Schedule compaction at next natural break |
| > 40% | Degrading | Compact now |
| > 60% | Dumb zone | You're already losing quality; compact aggressively, consider session restart |

Most production agents track this as a live metric, like memory pressure.

## What belongs in the system prompt

The system prompt is precious context. Audit it ruthlessly. Required elements (in this order):

1. **Role and posture** — who the agent is, what its standards are. One paragraph.
2. **Capabilities** — what it can do (often implicit from tools, don't re-list)
3. **Hard constraints** — what it must never do. Make these short and specific.
4. **Decision rubrics** — how to choose between options. This is where most prompts under-invest.
5. **Output format** — only when consistency matters (structured outputs preferred)
6. **Examples** — 1–3 high-quality examples for non-obvious cases

Anti-patterns in system prompts:

- Long lists of "do this, don't do that" — model attention dilutes
- Restating the obvious ("you are helpful and honest")
- Encoding business logic that should be code
- Including dynamic content that should be retrieved per-step
- More than ~2,000 tokens for most agents (some legitimate exceptions — Claude Code's ~16k system prompt is intentional architectural choice)

## Repo-resident context files (CLAUDE.md / AGENTS.md / docs/)

The strongest pattern for evolving agent context. The principles:

- **Version controlled.** Treat as code. Diff reviews on changes.
- **Human-editable, agent-readable.** No vendor lock-in.
- **Hierarchical.** A short index file pointing into a structured `docs/` directory; the agent navigates only what's needed.
- **Progressive disclosure.** OpenAI's Harness team learned: one monolithic AGENTS.md fails. A ~100-line table of contents → structured tree works.

Reference: `docs/architecture.md`, `docs/patterns.md`, `docs/glossary.md`, etc., with `CLAUDE.md` as the entry pointer.

## Curated context formats: llms.txt and OKF

The **Select** operation needs a *source*. Two emerging, vendor-neutral, Markdown-based formats standardize the curated knowledge an agent consumes — so you publish a source once and any agent can read it, instead of every agent re-scraping your surfaces:

- **`llms.txt`** (Jeremy Howard, 2024) — a single Markdown file at the site root: an H1 name, a blockquote summary, and H2 lists of links to the canonical pages. A **navigation pointer**: "cite these, don't crawl everything."
- **OKF — Open Knowledge Format** (Google Cloud, v0.1, June 2026) — a *directory bundle* of Markdown **concept files**, each with YAML frontmatter (`type` required; `title` / `description` / `resource` / `tags` / `timestamp` recommended), cross-linked into a **knowledge graph**, with a reserved `index.md` for progressive disclosure. The knowledge **library** itself, not just a pointer. Git-distributed, "consumers MUST tolerate broken links," minimal conformance.

They **compose, not compete**: `llms.txt` points to the OKF bundle root (e.g. `/okf/index.md`). Pointer + library.

**Why this belongs in context engineering:** both let the agent do **just-in-time retrieval** — follow the index / walk the graph on demand rather than ingesting everything up front (the 40% rule, again). And the shape is one you already know: Markdown + frontmatter + cross-links + an index file. This very skill set *is* that shape — a master `SKILL.md` index over concept files. Publishing your knowledge as OKF is mostly a matter of frontmatter discipline, not a rewrite.

**Caution (v0.1):** OKF is days old with deliberately minimal conformance. Adopt it as a *source your Select layer reads*; don't restructure your whole knowledge base around a v0.1 spec yet (see `STANDARD.md` Part X, Emerging & deferred). A knowledge/memory layer can also ingest or export OKF bundles — see `memory-architecture`.

## Per-step context budgeting

For each LLM call in the architecture, define a budget:

| Component | Typical share |
|---|---|
| System prompt (cached) | 5–15% |
| Tool schemas (cached) | 5–15% |
| Retrieved content | 20–40% |
| Conversation history | 10–30% |
| Memory excerpts | 5–15% |
| Working / current input | 10–20% |
| Output reserve | 10–20% |

If any component exceeds its share, you have a context engineering problem, not a model problem.

## Prompt caching — always on for stable parts

System prompts and tool schemas are stable across turns. Cache them. Both Anthropic and OpenAI now support this; it pays for itself within ~3 turns of any conversation.

## Failure modes to diagnose

When agent quality drops, work this checklist before reaching for a bigger model:

- [ ] Context utilization above 40% — compact more aggressively
- [ ] System prompt over 2k tokens of guidance — audit for redundancy
- [ ] Tool descriptions stale or vague — rewrite as prompts
- [ ] Retrieved chunks too large or too many — tighten retrieval
- [ ] No caching on stable parts — enable it
- [ ] Sub-agent feeding raw output to parent — switch to condensed findings
- [ ] Memory dumping full history — switch to RAG over memory
- [ ] Important constraints buried in turn 1 of a long conversation — move to system prompt or external file

In most "model isn't smart enough" debugging sessions, the actual problem is context engineering.

## Output of this skill

When the conversation completes, the user should have:

1. A defined system prompt with explicit budget
2. A context flow diagram: what's in window at each step
3. Compaction trigger and pipeline
4. Selection functions (RAG over docs / tools / memory) named explicitly
5. Isolation boundaries marked (where sub-agents own their own windows)
6. Live monitoring on context utilization (% of window used per turn)
