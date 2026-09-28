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
  ladder or the 5-pattern vocabulary, adding or changing a Definition of Done item, anti-pattern,
  or scorecard item in [`canon/`](canon/)) — opened as an issue or [ADR](docs/adr/) first,
  discussed in the open, then merged once there's rough consensus and no unresolved objection
  from a maintainer.
- **Breaking the canon** (renaming/removing a core concept, renumbering or reusing a DoD
  number, anti-pattern number, or scorecard id, or tightening what "conformant" means) —
  requires an ADR, a clear migration note in [`CHANGELOG.md`](CHANGELOG.md), and a major
  version.

## Releases

- The version lives in [`canon/meta.yaml`](canon/meta.yaml); every document's badge, title,
  and footer are generated from it. A release is tagged `v<version>` — the release workflow
  refuses a tag that does not match the canon, and publishes the matching `CHANGELOG.md`
  section as the GitHub Release.
- **Major releases ship as a release candidate first** (`vX.0.0-rc.N`, published as a GitHub
  pre-release) with a public comment period — two weeks in GitHub Discussions or an RFC
  issue — before the final tag. The maintainer may shorten the period; the release notes then
  say so, and feedback still open is carried into the next patch or minor release. Patch
  releases (consistency fixes, advisories) can ship directly.
- Products pin the `aps-conformance` Action to the exact tag they conform to, so a tag is a
  contract: never move or delete one.

The architectural canons (the autonomy × oversight ladder, the 5 composition patterns,
single-vs-multi, the 9-layer harness) are deliberately **stable**. Vendor rankings and framework specifics are
expected to churn — those PRs are the easy yes.

## Becoming a maintainer

Sustained, high-quality contributions (several merged PRs, helpful review of others' work)
earn an invitation. There's no application process — do the work in the open and it gets
noticed.

## Changes to this document

Governance changes are themselves substantive changes: propose via PR, with a maintainer
approval required to merge.
