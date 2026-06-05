# Red-team & supply-chain kit

Runnable starting points for the controls in **Principle 6 / Harness Layer 8 / Doctrine 7 (Security Is Structural)**. Copy them into your agent repo and wire to your stack — they are deliberately small, dependency-light, and framework-neutral.

| File | Control | Maps to |
|---|---|---|
| `lethal_trifecta_check.py` | Fails CI if an agent has private-data access **and** untrusted-content exposure **and** external egress, with no mitigation declared. | Lethal trifecta · DoD 13 · Rule 21 |
| `injection_cases.yaml` | Indirect-prompt-injection test cases (poisoned document / tool output), Promptfoo-style. | Guardrails · indirect injection |
| `pin_mcp_tools.sh` | Hash-pins MCP tool definitions and detects rug pulls (a server mutating tool descriptions after approval). | MCP supply chain · DoD 14 · Rule 22 |

See also `../ci/eval-gate.yml` — a CI workflow that blocks merges on eval pass-rate (DoD 12).

## Quick start

```bash
# 1. Declare what your agent can touch, then gate on the trifecta:
python3 lethal_trifecta_check.py agent-capabilities.json

# 2. Pin your MCP server's tools today; re-run in CI to catch rug pulls:
./pin_mcp_tools.sh tools.json .mcp-tools.lock     # first run writes the lock
./pin_mcp_tools.sh tools.json .mcp-tools.lock     # later runs fail on any change

# 3. Run the injection suite with Promptfoo (https://promptfoo.dev):
promptfoo eval -c injection_cases.yaml
```

These are tripwires, not a guarantee. Structural mitigation (break a trifecta leg, scope identity, isolate tenants) comes first; these tools check that you actually did it.
