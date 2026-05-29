---
name: harness-engineering
description: Design the harness — the 7-layer scaffolding around the LLM loop that makes agents reliable. Covers the agent loop itself (gather/act/verify), context management, durable execution, guardrails, human-in-the-loop, evals, and observability. In production agents, the harness is 98% of the code. Use whenever the user is structuring code around an agent loop, asks "how do I make this reliable / production-ready," is implementing verification, retry logic, sub-agent delegation, permission systems, approval gates, or wants to understand what makes Claude Code / Codex / Devin work beyond the model.
---

# Harness Engineering

OpenAI's "Harness Engineering" post and Liu et al.'s Claude Code analysis (arXiv:2604.14228) converge on the same finding: in a production agent, ~98% of code is *not* the model loop. It's the harness — context management, permission systems, verification, sub-agent delegation, tool routing, recovery.

LangChain's empirical finding (March 2026): holding model constant at gpt-5.2-codex, their coding agent moved from Top 30 to Top 5 on Terminal Bench 2.0 (52.8% → 66.5%) **only by changing the harness**. As model capability converges, harness quality is the durable competitive advantage.

## The 7-layer harness model

Every production agent has these layers. Build them in this order; skipping is technical debt:

```
┌─────────────────────────────────────────────┐
│  7. Observability & Tracing                 │
├─────────────────────────────────────────────┤
│  6. Evaluation Layer (CI gates)             │
├─────────────────────────────────────────────┤
│  5. Human-in-the-Loop (notify/ask/review)   │
├─────────────────────────────────────────────┤
│  4. Guardrails (input/output validation)    │
├─────────────────────────────────────────────┤
│  3. Durable Execution (Workflow + Activity) │
├─────────────────────────────────────────────┤
│  2. Context & Memory Management             │
├─────────────────────────────────────────────┤
│  1. Agent Loop (gather → act → verify)      │
└─────────────────────────────────────────────┘
              ↕ MCP / function calling
       ┌──────────────────────────┐
       │   Tools & Resources      │
       └──────────────────────────┘
```

## Layer 1: The agent loop

The actual loop. Anthropic's canonical form:

```
gather context → propose action → execute → verify → repeat
```

Production loops add four things to the naive version:

- **State as a first-class object.** The loop is a pure function `(state, event) → new_state`. This makes it resumable, testable, replayable.
- **Explicit termination conditions.** Step limit, time limit, success criterion, escalation. Never "loop until LLM says done."
- **A verification step before commit.** Outcome check: did the action achieve what we intended?
- **Compaction trigger.** Loop calls compaction when context utilization crosses 40%.

```python
# Schematic — production loops add error handling, durability, etc.
def agent_loop(state, max_steps=20):
    for step in range(max_steps):
        if termination_condition(state):
            return state
        if context_utilization(state) > 0.4:
            state = compact(state)
        action = propose_action(state)
        if requires_approval(action):
            action = await_human(action)
        result = execute(action)
        verified = verify(action, result)
        state = state.update(action, result, verified)
        trace(state, action, result, verified)
    return state  # hit step limit — log this
```

## Layer 2: Context & memory management

Covered in depth by `context-engineering/SKILL.md`. The harness responsibilities:

- Track context utilization as a metric
- Trigger compaction below the degradation threshold
- Manage the selection function for retrieval
- Maintain isolation boundaries for sub-agents
- Persist long-term state outside the window

## Layer 3: Durable execution

Long-running agents fail mid-flight. The pattern:

- Agent loop is a **Workflow** (deterministic, replayable from event log)
- LLM calls and tool calls are **Activities** (non-deterministic, retryable)
- State is checkpointed on each transition

Three implementation choices:

- **Temporal** — industry standard; first-party integrations for OpenAI Agents SDK, Pydantic AI, mcp-agent
- **Inngest / Restate** — simpler operationally, popular with TypeScript teams
- **LangGraph checkpointer** (Postgres) — built-in if you're on LangGraph

See `durable-execution/SKILL.md` for the full pattern.

## Layer 4: Guardrails

Defense in depth on inputs and outputs. Multiple cheap guardrails beat one perfect one.

**Input guardrails:**
- PII detection
- Jailbreak / prompt injection classifier
- Schema validation on structured inputs
- Rate limiting / cost limits per user

**Output guardrails:**
- Structured output validation (JSON schema)
- Content policy classifier
- Citation / source presence check
- Hallucination check (LLM-as-judge on factuality)

**Run guardrails in parallel** with the main agent call when latency matters, blocking when risk is high.

```python
# Pattern: parallel guardrails
agent_task = asyncio.create_task(run_agent(input))
guardrail_task = asyncio.create_task(check_guardrails(input))
result, guardrail = await asyncio.gather(agent_task, guardrail_task)
if not guardrail.passed:
    return guardrail.fallback()
return result
```

## Layer 5: Human-in-the-loop

HITL is load-bearing, not an afterthought. Harrison Chase's three patterns:

- **Notify** — agent acts, then tells the human ("I've drafted the response and sent it")
- **Question** — agent stops and asks before acting ("Should I proceed with X?")
- **Review** — agent prepares the action, human approves before commit

**The agent inbox pattern:** for ambient agents (those running on event streams), maintain a queue of actions awaiting human review. User reviews, approves/edits/rejects with feedback. Sierra, HumanLayer, LangGraph all use this.

**Rules:**
- Every destructive action requires explicit approval — code-enforced, not prompt-enforced
- Interrupt happens between tool selection and tool invocation (not after)
- Approval UI shows: what action, what inputs, what consequences, what alternatives the agent considered
- Rejection with feedback feeds back into the loop as new context

## Layer 6: Evaluation Layer (CI gates)

Covered in depth by `eval-driven-dev/SKILL.md`. The harness responsibilities:

- Log every step in a format the eval system can replay
- Tag traces with metadata for slicing (user segment, task type, model version)
- Run eval suite on every PR
- Block deploy on regression vs current production

## Layer 7: Observability & Tracing

Trace **everything**. Most agent failures are not text-quality issues — they're routing errors, tool selection errors, retrieval misses. Only traces reveal them.

**What to log per step:**
- Step ID, parent step ID (for sub-agent calls)
- Model called, input tokens, output tokens, cost
- Tool invoked, tool input, tool output
- Decision made (when LLM chose between options)
- Verification result
- Context utilization at this step
- Latency

**Instrumentation:** use OpenInference / OpenLLMetry so you can switch observability vendors (Langfuse, LangSmith, Braintrust, Arize) without re-instrumenting.

## Cycle of Trust — the meta-pattern

Every action passes through an explicit trust cycle:

```
gather context → propose action → check permissions → 
verify preconditions → execute → verify outcome → 
log trace → update memory/state
```

**Permission boundaries are enforced by code, never by prompt.** The Replit incident (2025) — an agent wiped a production database for 1,200+ companies despite an explicit "code freeze" instruction — is the canonical reference for why. The model will ignore prompt-level restrictions under enough pressure. Code won't.

**Implementation:**
- Tool credentials scoped with OAuth / IAM, not held by the agent
- Destructive actions gated by an approval API the LLM literally cannot call directly
- Sandbox execution (containers, VMs, restricted file systems)
- Audit trail of every action with provenance

## Sub-agent delegation pattern

When the harness spawns sub-agents:

```
parent has plan
  → spawns sub-agent (isolated context, scoped tools, time budget)
    → sub-agent works
    → sub-agent returns CONDENSED FINDINGS (not transcript)
  → parent integrates findings into plan
```

Sub-agents:
- Get isolated context windows
- Get scoped tool access (read-only is the default)
- Have time and step budgets
- Return summaries, never raw output
- Die when their task completes (ephemeral)

This is Claude Code's Task tool. It's Anthropic Research's sub-researcher pattern. The shape repeats because it works.

## Harness as the durable advantage

When the user is choosing where to invest engineering time, redirect this conversation:

- "Should we use GPT-5 or Claude Opus?" → **wrong question.** Both will keep improving. Invest in the harness.
- "Will this work better with a bigger model?" → **measure first.** Most "model isn't smart enough" failures are harness failures: bad context, wrong tools, missing verification.
- "How do we differentiate when everyone uses the same models?" → **harness is the moat.** Context engineering, tool design, verification logic, memory architecture, eval discipline — these compound. Model swaps don't.

## Output of this skill

When the conversation completes, the user should have:

1. The agent loop sketched as `(state, event) → new_state` with explicit termination conditions
2. Decisions for each of the 7 layers — what's in scope for v1
3. Cycle of Trust enforced for at least the top destructive actions
4. Sub-agent boundaries defined (if applicable)
5. A short list of "what could go wrong" mapped to which layer catches it
