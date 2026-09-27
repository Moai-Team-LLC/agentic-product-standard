# Typed safe outputs — the agent proposes, a deterministic applier writes

*From [The Agentic Product Standard](../../STANDARD.md), Part IV (Loop License gate 3, **declared blast radius**). A pattern, not a product: copy it, adapt the action types and handlers to your system.*

An agent that holds a write credential will, under enough adversarial pressure, be talked into using it. The strongest way to enforce a blast radius **below the model** is to never give the model the write credential at all:

```
agent (read-only identity)                 applier (deterministic code, write identity)
  reads, reasons, decides                    validates every request:
  emits typed action requests  ──JSONL──▶     · schema (a closed set of action types)
  (safe-outputs.jsonl)                        · policy (target allow-lists, per-run limits)
                                              · then executes — or rejects and escalates
```

- The agent's output is **data**, not calls: each line of `safe-outputs.jsonl` is one typed request — `{"type": "comment", "target": "issue/123", "body": "…"}` — validated against [`safe-output.schema.json`](safe-output.schema.json).
- The **applier** is ordinary, reviewed code that holds the only write credential. It checks each request against a policy ([`policy.example.json`](policy.example.json)): which action types exist, which targets each may touch, how many may happen per run. Anything outside policy is rejected and escalated, never "best-effort" applied.
- The blast radius is now the policy, and the policy is code — enforced, not asserted. It composes with the rest of the standard: permissions in code (DoD 5), a distinct identity per component (DoD 27 — the agent's identity cannot write), an audit trail per action (DoD 12), and destructive actions still routed to a human (DoD 4).

GitHub Agentic Workflows ship the same primitive under the same name: *"Safe outputs enforce security through separation: agents run read-only and request actions via structured output, while separate permission-controlled jobs execute those requests"* ([gh-aw docs](https://github.com/github/gh-aw/blob/main/docs/src/content/docs/reference/safe-outputs.md)).

## Files

| File | What it is |
|---|---|
| [`safe-output.schema.json`](safe-output.schema.json) | JSON Schema for one action request — a closed enumeration of action types |
| [`policy.example.json`](policy.example.json) | The blast radius as data: allowed types, target patterns, per-run limits |
| [`apply_safe_outputs.py`](apply_safe_outputs.py) | Reference applier: validates each request, applies the policy, dry-runs by default |

```bash
python3 apply_safe_outputs.py safe-outputs.jsonl --policy policy.example.json            # dry run: decisions only
python3 apply_safe_outputs.py safe-outputs.jsonl --policy policy.example.json --apply    # execute accepted requests
```

The handlers in `apply_safe_outputs.py` are stubs that print; wire them to your systems. Keep the applier boring: no model calls, no string-built commands, one handler per action type.
