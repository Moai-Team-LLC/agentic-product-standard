# ADR-0005 — Open-Source Release Packaging

## Status

Accepted

## Date

2026-09-27

## Context

AITM-SMB 1.0.0 was an internal release. Its full distribution was imported unchanged into the Agentic Product Standard repository as the folder aitm-smb, and 1.1.0 is its first public release. The imported folder was not ready to be published:

- it carried no license, although `MANIFEST.md` declared it an open methodology; a split of the folder would have been all rights reserved;
- its integrity audits (`audits/`) were produced by internal tooling that was never published, so nobody could rerun them;
- the README, changelog, and release checklist of 1.0.0 named Core and Full distributions, but nothing in the folder defined or built them;
- there was no documented way to install it for an AI agent;
- several paths still carried framing that 0.7.0 had deprecated: skill and phase names built around "AI opportunities" and an undivided "target architecture", and an `evals` folder that was easily confused with the engagement evaluation system in `evaluation/`;
- its short `CONTRIBUTING.md` described no contribution process, and it had no conduct, security, or citation files of its own.

## Decision

1. **License: MIT**, `Copyright (c) 2026 Alex Duchenchuk`, the same license and holder as the hosting repository. `LICENSE` sits in the AITM root; contributions are accepted under the same license (`CONTRIBUTING.md`).
2. **Agent adapter.** A root `SKILL.md` makes the whole AITM root installable as one Agent Skill named `aitm-smb`. It routes to the numbered skills, which are procedures inside the folder and are not installed separately, because every reference in them is relative to the AITM root (`AGENT_CONTEXT_POLICY.md`).
3. **Published tooling.** `tools/validate.py` (framework integrity, and engagement trace integrity with `--engagement`) and `tools/build_dist.py` (distributions) replace the unpublished internal audit tooling. Both use the Python standard library only; CI runs them on every change and before each release (`MAINTENANCE.md` §2).
4. **Renamed paths** remove the deprecated framing. Skill numbers stay the stable identifiers (`skills/INDEX.md` §5):

   ```text
   skills/04-map-ai-opportunities/           → skills/04-design-interventions/
   skills/06-design-target-architecture/     → skills/06-design-target-system/
   methodology/03-ai-opportunities.md        → methodology/03-intervention-design.md
   methodology/05-target-architecture.md     → methodology/05-target-system-design.md
   evals/                                    → rubrics/  (informative quality rubrics)
   RELEASE_NOTES_1.0.md, RC_CHECKLIST.md,
   RELEASE_CANDIDATE.md                      → releases/
   ```

5. **Distributions.** Core is the Canonical Core plus the registries, `LICENSE`, and `CHANGELOG.md`; Full is the whole AITM root (`NORMATIVE_INDEX.md` §Distributions, `MANIFEST.md` `distributions`). `tools/build_dist.py` builds both, and every GitHub release attaches them.
6. **Hosting.** AITM-SMB lives in the Agentic Product Standard repository as a self-contained, split-ready folder: every path is relative to the AITM root and every command runs from inside it. Releases are tagged `aitm-smb-vX.Y.Z` there and `vX.Y.Z` after a split (`VERSIONING.md` §10). The folder's own `.github/` (workflow, issue forms, pull-request template) is inert until a split; the procedure is `MAINTENANCE.md` §6. The host-side decision is recorded in the hosting repository's ADR-0003, "Host AITM-SMB as a split-ready subfolder".
7. **Community files** in the AITM root: `README.md`, `QUICKSTART.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CITATION.cff`, issue and pull-request templates, and an ADR index with a template (`decisions/README.md`, `decisions/ADR-0000-template.md`).
8. **Version 1.1.0** is a MINOR release: compatible additions and clarifications, with field renames listed in the migration table of `releases/1.1.0.md` (`VERSIONING.md` §9). No `PUBLIC_API.md` meaning changes.

## Consequences

- The methodology can be reused, forked, and cited, and it stays licensed after a split without relicensing.
- Anyone can rerun the integrity checks that the 1.0.0 audits reported, and check their own engagement's trace.
- Links to the old paths break. There were no public consumers before 1.1.0; the `CHANGELOG.md` entry for 1.1.0 lists old and new paths.
- Two CI definitions must be kept in step while co-hosted: the host workflow and the folder's standalone copy.
- `tools/validate.py` enforces version alignment across `MANIFEST.md`, version headers, contracts, `CITATION.cff`, `README.md`, and `CHANGELOG.md` (`VERSIONING.md` §8), so a release cannot ship with mismatched versions.

## Alternatives

- **CC BY 4.0.** Considered, because most of the content is documentation. Not chosen: the release also contains executable scripts and agent skills that work as instructions, for which a software license is the usual fit; MIT matches the hosting repository, so the whole repository stays under one license, and a split needs no relicensing. MIT allows the same reuse of the documentation as CC BY 4.0, on the condition that the copyright and permission notice is kept.
- **A separate repository from the start.** Deferred: it adds a second release and governance surface before any external contributor exists. The split-ready layout keeps the option open (hosting repository ADR-0003).
- **Keep the 1.0.0 paths.** Rejected: they kept alive the AI-first framing the method rejects (INV-05) and that 0.7.0 had already deprecated in artifacts. Directory slugs are not stable identifiers; skill numbers are.
- **Install each numbered skill separately.** Rejected: the skills depend on the whole AITM root, and copied skills would lose their references.
