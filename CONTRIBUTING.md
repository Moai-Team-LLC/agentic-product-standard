# Contributing

Thanks for helping improve **The Agentic Product Standard**. This is a living document — the field moves fast, and the best contributions keep it honest and current.

## What we're looking for

The standard has two kinds of content, and they invite different contributions:

- **Stable canons** — the autonomy ladder, the five composition patterns, single-vs-multi-agent, the eight-layer harness, the Cycle of Trust. These change rarely. Challenge them only with strong evidence (a production writeup, a reproducible result, a credible primary source).
- **Fast-moving specifics** — vendor rankings, framework recommendations, tool counts, cost figures, reading-list entries. These age quickly. **PRs that update them are exactly what we want.**

Especially welcome:

- **Corrections** — a claim that's wrong, outdated, or missing a source.
- **New exemplars** — a production system whose architecture teaches something the current ones don't.
- **Framework / vendor updates** — the landscape in `framework-selection` and `memory-architecture` shifts quarterly.
- **Translations** — the standard ships in English ([`STANDARD.md`](STANDARD.md)). Translations are welcome under `docs/STANDARD.<lang>.md`.
- **Skill improvements** — sharper routing, clearer diagnostics, better examples in any `SKILL.md`.

## Ground rules

1. **Cite primary sources.** "Anthropic says X" needs a link. Single-vendor benchmarks are directional, not ground truth — frame them that way (this is anti-pattern #12).
2. **Prefer the boring, durable claim** over the exciting, fragile one. The standard tilts toward what survives the next model release.
3. **Keep the standard and the skills in sync.** If you change a canon in `STANDARD.md`, update the matching `SKILL.md` so the guidance doesn't drift.
4. **Don't add code templates.** The skill set teaches judgment, not boilerplate — framework-specific code rots fast and lives better in the framework's own docs.
5. **One topic per PR.** A vendor update and a new exemplar are two PRs.

## How to contribute

1. Fork the repo and create a branch: `git checkout -b fix/framework-rankings`.
2. Make your change. Edit the relevant `STANDARD.md` section and/or the matching `skills/.../SKILL.md`.
3. Commit using [Conventional Commits](https://www.conventionalcommits.org/) — e.g. `docs: update memory-vendor matrix for 2026 Q3`. Running `./setup.sh` wires a dependency-free local hook (`.githooks/commit-msg`) that checks this on commit; CI validates every PR commit with `commitlint`. To enable the hook without a full setup: `git config core.hooksPath .githooks`.
4. Open a PR describing **what changed and why**, with sources for any factual claim.

## Reporting issues without a PR

Open an issue using one of the templates:

- **Content correction** — something is wrong or outdated.
- **New pattern / exemplar** — propose an addition with evidence.

## Code of Conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). Be direct, be kind, argue from evidence.
