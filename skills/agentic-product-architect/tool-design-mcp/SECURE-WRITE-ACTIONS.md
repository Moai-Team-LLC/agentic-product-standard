# Secure Write Actions

*Companion to `SKILL.md`. The permission model says destructive actions need approval; this is **how** the approval actually works — the operational pattern for the write path of an agent or MCP server.*

"Require approval for writes" is necessary but underspecified. An agent that can be prompt-injected will, given a standing write capability, eventually be talked into using it. The fix is to make write capability **earned, narrow, time-bounded, and confirmed out-of-band** — never a property the session simply has.

This pattern is distilled (vendor-neutral) from Descope's MCP-server design and OAuth 2.1; see Sources.

---

## The core stance: read-only by default, writes are elevated

A session starts with **no write capability**. Reads (P0) are always available; any mutation (P3+) requires the agent to *enter an elevated state*, and that state is:

- **explicit** — the agent must request elevation; it is never implicit in being authenticated;
- **scoped** — elevation is to a specific resource/operation, not "writes" in general;
- **time-bounded** — it auto-expires (e.g., 15 minutes) and must be re-earned;
- **confirmed out-of-band** — by a human, through a channel the agent cannot read.

```
┌── read-only (default) ──┐   request + human OOB confirm   ┌── elevated (≤15 min, scoped) ──┐
│ P0 reads only           │ ──────────────────────────────▶ │ one P3+ op on the cited target │
│ writes rejected         │ ◀────────── auto-revoke ──────── │ then drops back to read-only   │
└─────────────────────────┘                                  └────────────────────────────────┘
```

## The five-step write workflow

Every P3+ action follows the same sequence, so there are no silent mutations:

1. **Identify** — the agent names the operation and why it's needed.
2. **Build arguments** — it assembles the exact parameters.
3. **Cite the exact target and stop** — it states the precise resource + operation (*"delete bucket `prod-invoices`"*, not *"clean up storage"*) and waits. No blanket "approve all writes."
4. **Out-of-band confirmation** — a human approves via a separate channel (one-time passcode by email/SMS, a console click). **The agent never sees the code or secret** — it cannot be the one to "confirm."
5. **Execute, then audit** — the action runs once, the elevation is consumed, and the event is written to an immutable log.

## Hard rules

- **Default deny on writes.** No-elevation = reject, fail closed. There is no ambient write scope.
- **One confirmation, one action.** Approval is for the cited target only; the next write re-enters the workflow. Never grant "yes to everything for this session."
- **The agent cannot self-confirm.** The confirmation secret travels a channel the agent has no read access to. If the agent can fetch the OTP, the control is theater.
- **Time-box elevation.** Auto-revoke after a short window; a compromised session can't sit on standing write power.
- **Never return secrets to the agent.** Read operations on credentials return *metadata only* (created-at, scope, last-used) — never the bearer token / key / hash. Rotate secrets through dedicated operations that don't echo the new value into context or logs.
- **Dry-run before destructive or bulk/schema changes.** Offer a preview/validation mode that shows the impact (rows touched, files removed, snapshot to be restored) without committing. Destructive (P6) actions always pair a dry-run with the confirmation.
- **Elevation state is inspectable.** The user can ask "what can this session do right now?" and get an honest answer (elevated? scope? expires when?).
- **Immutable audit trail.** Every login, elevation request, confirmation, and write is logged append-only and is queryable for incident response.

## Mapping to the permission tiers (P0–P6)

| Tier | Action | Write-path control |
|---|---|---|
| P0 | Read | Always available; credentials returned as **metadata only** |
| P1–P2 | Draft / internal write | Low blast radius; log, no elevation needed |
| **P3** | External write | **Elevation + out-of-band confirm, scoped to the cited target** |
| **P4** | Financial | Elevation + confirm; amount/recipient cited explicitly |
| **P5** | Communication | Elevation + confirm; recipient + content cited |
| **P6** | Destructive | Elevation + **dry-run preview** + confirm; never standing |

This is the same boundary the rest of the standard enforces — `tenant_id` and permissions come from auth, never the model — extended to the write path with an explicit, expiring, out-of-band gate. It composes with Layer 8 (Security & Identity), the lethal-trifecta check (writes are the "external comms" leg), and the MCP supply-chain controls (`pin_mcp_tools.sh`).

## Checklist

- [ ] Sessions start read-only; writes require explicit elevation.
- [ ] Elevation is scoped to a specific operation/resource, not "writes."
- [ ] Elevation auto-expires (short window) and must be re-earned.
- [ ] Confirmation is out-of-band; the agent cannot read the secret/OTP.
- [ ] Each write cites its exact target before execution; no blanket approval.
- [ ] Credential reads return metadata only; rotation never echoes the secret.
- [ ] Destructive/bulk/schema changes support a dry-run preview.
- [ ] Current elevation state is queryable by the user.
- [ ] All auth + write events are in an immutable, queryable audit log.

## Sources

- Descope — *Building (and securing) an MCP server* (read-only default, time-bounded elevation, out-of-band write confirmation, credential-metadata-without-secrets). Adapted vendor-neutrally.
- OAuth 2.1 + Resource Indicators (RFC 8707); the MCP authorization spec.
- This standard: `SKILL.md` (permission model), `../../../STANDARD.md` (Layer 8), `../../../AGENT_STANDARD.md` (Tool Safety Rules, Doctrine 7).
