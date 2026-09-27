# Reference Architecture — AI-Native SMB

This is a logical reference architecture, not a required technology stack.

```text
BUSINESS OUTCOMES
        │
BUSINESS CAPABILITIES
        │
VALUE STREAMS / PROCESSES
        │
┌───────┴───────────────────────────┐
│ HUMAN SYSTEM                     │
│ roles / decisions / approvals    │
└───────┬───────────────────────────┘
        │
EXPERIENCE & APPLICATION LAYER
        │
┌───────┼───────────────┐
│       │               │
Copilots  Workflows    Agents
│       │               │
└───────┼───────────────┘
        │
AI CAPABILITY LAYER
models / gateway / retrieval / memory /
orchestration / tools / evals / guardrails
        │
DATA & KNOWLEDGE LAYER
operational data / documents / events /
business rules / semantic context
        │
PLATFORM LAYER
identity / APIs / storage / compute /
queues / observability / secrets
        │
GOVERNANCE & ECONOMICS
authority / audit / risk / cost / SLOs
```

## Principle

The reference architecture is decomposed by responsibility so that implementations can remain portable across GCP, AWS, Azure, SaaS, and hybrid environments.
