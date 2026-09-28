# ADR-0003: Host AITM-SMB as a split-ready subfolder

- **Status:** Accepted
- **Date:** 2026-09-27

## Context

AITM-SMB (AI Transformation Methodology for Small and Medium-Sized Businesses)
is a methodology from the same author. It answers the question that comes before
this standard: which business capability should change, whether AI belongs in
that change, and how much authority AI may hold. It reached an internal 1.0.0
and is being released publicly for the first time.

Two forces pull in different directions:

- It is a separate body of knowledge with its own semantic contract (its
  `PUBLIC_API.md`), its own semver line, and a different audience (business
  owners and transformation leads, not only agent builders). Mixing its files
  into this standard's canon would blur both.
- It is most useful next to this standard. An AITM-SMB intervention that calls
  for an AI component hands off to this standard for how to build and license
  it. The two also collide on vocabulary: both use "L3", with different
  meanings.

## Decision

Host AITM-SMB in `aitm-smb/` as a **self-contained, split-ready** folder:

- Everything it needs lives inside the folder: LICENSE (MIT, same holder),
  README, CHANGELOG, CONTRIBUTING, security policy, ADRs (`aitm-smb/decisions/`),
  tooling (`aitm-smb/tools/`), and a standalone workflow copy in
  `aitm-smb/.github/` that is inert until a split. All of its paths are relative
  to the folder root, so `git subtree split --prefix=aitm-smb` produces a working
  repository whose content needs no path changes; only host URLs and the
  CODEOWNERS / commit-lint setup are adapted (`aitm-smb/MAINTENANCE.md` §6).
- It keeps **independent semver**. Releases in this repository are tagged
  `aitm-smb-vX.Y.Z` (the host's own tags stay `vX.Y.Z`) and published by
  `.github/workflows/aitm-smb.yml`, with its Core and Full distributions
  attached.
- The vocabulary collision is resolved by scoping, not renaming. `CONTEXT.md`
  stays authoritative for this standard's skills. AITM-SMB's L0–L5 is a business
  *authority* ladder and this standard's L0–L4 is an *architecture* ladder. In
  mixed contexts they are written AITM-L<n> / APS-L<n>. An informative crosswalk
  (`aitm-smb/docs/crosswalk-agentic-product-standard.md`) maps the two and names
  the hand-off. It adds no requirements to either standard.
- It is listed in `ECOSYSTEM.md` as a *related methodology*, not as a reference
  implementation, because it implements no surface of this standard.

## Consequences

- One repository to watch while the community is small; either artifact can be
  cited on its own.
- CI must keep covering both: the host `validate` workflow checks links and
  skill frontmatter repo-wide, and `aitm-smb.yml` runs the methodology's own
  integrity and trace checks.
- If AITM-SMB grows its own contributor base, splitting it out is mechanical:
  subtree split (the folder's own `.github/` becomes the new repository's),
  adapt CODEOWNERS, commit-message lint and host URLs, and switch to `vX.Y.Z`
  tags — the steps are listed in `aitm-smb/MAINTENANCE.md` §6.

## Alternatives considered

- **Separate repository now.** Cleanest ownership, but it adds a second release
  and governance surface before any external contributor exists. The split-ready
  layout keeps this option open at no cost.
- **Merge AITM-SMB into this standard's canon.** Rejected. Its unit of change is
  a business capability, not an agent, and its authority ladder would have to be
  renamed or would collide with Canon 1.
