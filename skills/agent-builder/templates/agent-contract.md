# Agent Contract: {Agent Name}

> Fill every section before writing code. An agent without a complete contract is not ready to implement.

## 1. Mission
One sentence describing the agent's purpose.

## 2. Ownership
The single result this agent owns completely.

## 3. Non-Ownership
What this agent must not do (and who owns it instead).

## 4. Inputs
Required and optional inputs. (Becomes the input schema — see `schemas.ts`/`schemas.py`.)

## 5. Required Context
Minimum context needed to do the job.

## 6. Optional Context
Useful context if available, but not required.

## 7. Tools
Allowed tools and why each is needed. (Each gets a `tool-contract.md`.)

## 8. Forbidden Actions
Actions the agent must never take.

## 9. Output Schema
Structured output format. (Becomes the output schema — never parse critical data from free-form text.)

## 10. Acceptance Criteria
How success is verified. Must be testable.

## 11. Failure Modes
Known, concrete ways this agent can fail (not generic). These seed `eval/cases.json`.

## 12. Escalation Rules
When the agent must stop, ask, hand off, or request human approval (notify / ask / review).

## 13. Logging Requirements
What must be written to trace (see `trace-event.json`).

## 14. Stop Conditions *(required at L3+ or O1+)*
Max iterations; token / time / spend budgets; timeout; escalation after N consecutive failures.

## 15. Memory Model *(required at O1+; recommended at L3+)*
What is persisted, for how long, from where (provenance), and whether a past run can be replayed.

## 16. Operating Point & Determinism Map *(operating point: every agent; determinism map: required at O1+, recommended at L3+)*
The operating point — autonomy `L0–L4` · oversight `O0–O2` — and which consequential (P3+) actions, if any, run without per-action approval. Anything at `O1+` needs a Loop License. Which steps are deterministic and which are model-driven.

## 17. Identity
The agent's own non-human identity, its credential lifetime and scopes, and who can delegate work to it. Never a shared service account or a person's token.

---

### Design rules (delete before shipping)
- One agent owns one primary artifact.
- An agent must not own both generation and final approval.
- No external side effects unless explicitly permitted; destructive actions always require human approval.
- Output must be schema-validatable; acceptance criteria must be testable; failure modes must be concrete.
