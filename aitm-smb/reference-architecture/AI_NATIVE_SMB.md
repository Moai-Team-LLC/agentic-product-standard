# Reference Architecture — AI-Native SMB

**Status:** Informative. A logical reference architecture, not a required technology stack.

```text
BUSINESS OUTCOMES
        │
BUSINESS CAPABILITIES
        │
VALUE STREAMS / PROCESSES
        │
┌───────┴──────────────────────────┐
│ HUMAN SYSTEM                     │
│ roles / decisions / approvals    │
└───────┬──────────────────────────┘
        │
EXPERIENCE & APPLICATION LAYER
        │
┌───────┴───────────┬─────────────────────────┐
│                   │                         │
AI Assistance       Deterministic Automation  Agents
│                   │                         │
└───────┬───────────┴─────────────────────────┘
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

The AI Capability Layer and the Agents branch are present only where a selected Intervention justifies AI (INV-05). A Capability without AI (`maturity/MATURITY_MODEL.md` M0) runs on the human system, applications, deterministic automation, and the data and platform layers alone.

## Principle

The reference architecture is decomposed by responsibility so that implementations can remain portable across cloud providers, SaaS, on-premises, and hybrid environments.
