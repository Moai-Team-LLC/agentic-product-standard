# Architecture Decision Records

Why AITM-SMB is shaped the way it is. Each ADR records one decision about the methodology: its context, the choice, its consequences, and the alternatives.

ADRs are framework governance, not engagement rules ([`NORMATIVE_INDEX.md`](../NORMATIVE_INDEX.md)). An ADR explains a rule; the canonical file it names carries the rule. On any difference, the canonical file governs.

## Index

| ADR | Title | Status | Date |
|---|---|---|---|
| [ADR-0000](ADR-0000-template.md) | Template | — | — |
| [ADR-0001](ADR-0001-capability-as-primary-unit.md) | Business Capability is the primary transformation unit | Accepted | not recorded (by 1.0.0) |
| [ADR-0002](ADR-0002-outcome-first.md) | Outcome before technology | Accepted | not recorded (by 1.0.0) |
| [ADR-0003](ADR-0003-human-gate-identifiers.md) | Stable identifiers for human decision gates | Accepted | 2026-09-27 |
| [ADR-0004](ADR-0004-single-record-contracts.md) | One record contract per record shape | Accepted | 2026-09-27 |
| [ADR-0005](ADR-0005-open-source-release-packaging.md) | Open-source release packaging | Accepted | 2026-09-27 |

## When to write one

A material methodology change, and every MAJOR change, should be recorded as an ADR ([`MAINTENANCE.md`](../MAINTENANCE.md) §2, [`CONTRIBUTING.md`](../CONTRIBUTING.md)). Typical cases: a change to a [`PUBLIC_API.md`](../PUBLIC_API.md) item, a human gate, an invariant, a record contract, a profile's content, or the repository's packaging.

Other design decisions made before 1.1.0 are recorded in [`CHANGELOG.md`](../CHANGELOG.md) and in the canonical sources that carry them, for example [`STANDARD.md`](../STANDARD.md) §7 for separating the Capability Target State from the Target Operating Architecture, and INV-06 for separating AI suitability from AI authority. They are not reconstructed as retroactive ADRs.

## Format

- Copy [`ADR-0000-template.md`](ADR-0000-template.md) to a file named ADR-NNNN-kebab-title.md, numbered sequentially. Numbers are never reused.
- Sections: Status, Date, Context, Decision, Consequences, Alternatives.
- Status is one of: Proposed · Accepted · Superseded by ADR-NNNN · Deprecated. A superseded ADR stays in place with its new status.
- One decision per ADR, about one page. Add the ADR to the index above in the same pull request.
