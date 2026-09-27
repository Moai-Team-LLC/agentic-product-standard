# Tool Contract: {Tool Name}

## Purpose
What this tool does.

## Input Schema
Typed input.

## Output Schema
Typed output.

## Side Effects
None / internal write / external write / financial / communication / destructive.

## Permission Tier
`P{0–6}` — see table below.

## Preconditions
What must be true before execution.

## Postconditions
What must be verified after execution.

## Failure Cases
Known failures and recovery behavior.

## Audit Requirements
What must be logged (input summary + output summary at minimum).

---

### Permission tiers

| Tier | Type | Examples | Approval at O0 | Approval at O1 / O2 |
|---|---|---|---|---|
| P0 | Read | retrieve document, inspect state | No | No |
| P1 | Draft | create draft, suggest plan | No | No |
| P2 | Internal Write | save draft, update internal task state | Usually no | Usually no |
| P3 | External Write | publish page, update external CRM | Yes, per action | Inside the Loop License's declared blast radius; outside it, per action |
| P4 | Financial | create charge, change price, issue refund | Yes, per action | Inside the declared blast radius and cost ceilings; outside them, per action |
| P5 | Communication | send email, message user, notify customer | Yes, per action | Inside the declared blast radius; outside it, per action |
| P6 | Destructive | delete data, revoke access, overwrite production | Always, per action | Always, per action |

> Permission tiers (P0–P6) describe *how dangerous* a tool is. They are distinct from
> autonomy levels (L0–L4), which describe *how much control flow the model owns*, and
> from oversight modes (O0–O2), which describe *whether a human approves each P3+ action*.
> Enforce tiers in code, never in the prompt.
