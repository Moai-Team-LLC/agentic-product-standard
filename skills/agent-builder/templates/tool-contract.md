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

| Tier | Type | Examples | Approval |
|---|---|---|---|
| P0 | Read | retrieve document, inspect state | No |
| P1 | Draft | create draft, suggest plan | No |
| P2 | Internal Write | save draft, update internal task state | Usually no |
| P3 | External Write | publish page, update external CRM | Yes |
| P4 | Financial | create charge, change price, issue refund | Yes |
| P5 | Communication | send email, message user, notify customer | Yes |
| P6 | Destructive | delete data, revoke access, overwrite production | Always yes |

> Permission tiers (P0–P6) describe *how dangerous* a tool is. They are distinct from
> autonomy levels (L0–L4), which describe *how much control flow the model owns*.
> Enforce tiers in code, never in the prompt.
