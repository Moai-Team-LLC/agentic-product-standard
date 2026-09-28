# ADR-0003: A machine-readable canon, and prose generated from it

- **Status:** Accepted (v4.0.0-rc.1) — amends ADR-0002
- **Date:** 2026-09-27

## Context

ADR-0002 kept two representations of one canon — `STANDARD.md` as prose, the skills as operators — and accepted the obligation that they must not drift. They drifted anyway. By v3.3 the same facts lived in up to seven places, and every release fixed some copies and missed others: the harness was "nine layers" in text and eight in every diagram; `STANDARD.md` listed 17 anti-patterns while the README and the review skill listed 19; the master skill listed 12; the Definition of Done was "25 items" plus two unnumbered ones that no grid could show; the scorecard had no item for DoD 25 at all. None of these were disagreements about the standard — they were copies nobody could keep in sync by hand.

At the same time the standard's users asked for something the prose could not give them: a way to check conformance mechanically, in CI, against the exact version they claim.

## Decision

1. **Everything enumerable lives once, in `canon/*.yaml`** — principles, the autonomy × oversight ladder, the patterns, the harness and stack, the checklist, the Definition of Done (normative text, binding conditions, audit points, crosswalk), the anti-patterns, the scorecard, and the regulatory frameworks — with JSON Schemas in `canon/schema/`.
2. **Documents carry generated regions** (`<!-- canon:begin:NAME -->`), and a few files are generated whole (`CROSSWALK.md`, the production-readiness `DOD.md`, the conformance template, `skills-lock.json`). `tools/aps.py render` writes them; `tools/aps.py check` fails CI on any drift, and a prose lint fails on any count written in free text that disagrees with the canon.
3. **Identifiers are stable.** DoD and anti-pattern numbers and scorecard ids are never reused or renumbered; a group may list its numbers out of order.
4. **The same canon drives conformance.** `tools/aps.py conformance` and the `aps-conformance` GitHub Action score a product's `aps-conformance.yaml` against `canon/scorecard.yaml`, so the tool and the documents cannot disagree.

ADR-0002's split stands — prose for reasoning, skills for acting — with a third representation underneath both for the parts that must never differ.

## Consequences

- A change to the canon is one YAML edit plus a render; reviewers see the canon diff and the regenerated text together.
- Prose outside generated regions is still hand-written, and the explanatory weight of the standard stays there. The prose lint catches counts, not meaning — reviews still matter.
- Contributors need Python and PyYAML to change enumerable content. Pure prose edits need nothing new.
- The canon becomes a public interface: products reference scorecard ids and DoD numbers in their conformance files, so renumbering is now a breaking change by construction — which is the point.

## Alternatives considered

- **Keep hand-syncing with a checklist in the PR template.** It was the v3.x practice, and the drift above is its record. Rejected.
- **Generate the whole standard from data.** Would turn the canon into a database and the prose into boilerplate. Rejected — only enumerable facts are generated.
- **A general-purpose static-site generator.** More machinery than the problem needs, and it would move the documents away from plain Markdown on GitHub. Rejected.
