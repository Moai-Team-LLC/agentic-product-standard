# ADR-0002: Standard as prose, skills as operators

- **Status:** Accepted
- **Date:** 2026-05-30

## Context

The repo serves two audiences with one body of knowledge: humans who want to
*read and reason about* the standard, and agents/editors who want to *apply* it
in a working session. A single artifact optimized for one tends to fail the
other — prose that's pleasant to read makes a poor machine prompt, and a terse
operational checklist makes a poor explainer.

## Decision

Keep two representations of the same canon, deliberately separated:

- **`STANDARD.md`** — the canonical *prose*. Stable, citable, human-first. The
  source of truth for *what* the standard says.
- **`skills/`** — the *operators*. SKILL.md files that turn the canon into
  in-editor behavior (route, apply, review). The source of truth for *how* to
  act on it.

`CONTEXT.md` holds the shared vocabulary both lean on, so a term means the same
thing whether you read it or an agent applies it.

## Consequences

- Each representation can be optimized for its audience without compromising the
  other.
- Obligation: the two must not drift. When the canon changes, both `STANDARD.md`
  and the affected skill(s) update in the same change; `CONTEXT.md` is the lever
  that keeps terminology aligned.
- A reference implementation (`examples/agenticmind-case-study.md`) anchors the
  prose to something runnable, closing the loop from "what" to "how" to "proof."

## Alternatives considered

- **Skills only** — would make the canon hard to read, cite, or review as a
  document. Rejected.
- **Standard only** — leaves application to the reader; no in-editor operators.
  Rejected; the skills are the repo's distribution mechanism.
