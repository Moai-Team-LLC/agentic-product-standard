# Governance

This document describes how decisions are made for the Agentic Product Standard. It's
intentionally lightweight — the project is young — and will grow as the community does.

## Roles

- **Maintainer** — reviews and merges PRs, sets direction, cuts releases. Currently
  [@AlexDuchDev](https://github.com/AlexDuchDev), stewarded by [Moai Team LLC](https://moaiteam.com).
- **Contributor** — anyone who opens an issue or PR. No formal status required.

## How decisions are made

- **Editorial changes** (typos, clarifications, broken links, new examples that fit the
  existing canon) — a single maintainer approval merges.
- **Substantive changes** (new sub-skills, changing a recommendation, altering the autonomy
  ladder or the 5-pattern vocabulary) — opened as an issue or [ADR](docs/adr/) first, discussed
  in the open, then merged once there's rough consensus and no unresolved objection from a
  maintainer.
- **Breaking the canon** (renaming/removing a core concept) — requires an ADR and a clear
  migration note in [`CHANGELOG.md`](CHANGELOG.md).

The architectural canons (the autonomy ladder, the 5 composition patterns, single-vs-multi,
the 8-layer harness) are deliberately **stable**. Vendor rankings and framework specifics are
expected to churn — those PRs are the easy yes.

## Becoming a maintainer

Sustained, high-quality contributions (several merged PRs, helpful review of others' work)
earn an invitation. There's no application process — do the work in the open and it gets
noticed.

## Changes to this document

Governance changes are themselves substantive changes: propose via PR, with a maintainer
approval required to merge.
