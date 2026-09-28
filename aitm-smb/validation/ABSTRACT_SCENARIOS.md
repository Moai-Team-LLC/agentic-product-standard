# Abstract Validation Scenarios

**Status:** Informative.

These are not examples of how AITM-SMB must be applied.

They exist only to test whether the methodology remains general enough to work across structurally different SMB contexts. A worked example built on Scenario B: `examples/compact-scenario-b/` (fictional, non-normative).

Each scenario names the profile it would likely select (`APPLICATION_PROFILES.md`) and what a correct application must not produce (named anti-patterns: `rubrics/ANTI_PATTERNS.md`).

## Scenario A — Expert-dependent service business

Characteristics:

- delivery quality depends on a small number of experts;
- knowledge is mostly tacit;
- sales and delivery are weakly connected;
- scaling increases coordination overhead.

Likely profile: Standard. Must not produce: Tool-first transformation; Use-case theater.

## Scenario B — Transaction-heavy operational business

Characteristics:

- high task volume;
- many repetitive decisions;
- several legacy tools;
- operational errors create direct cost.

Likely profile: Compact for one bounded Capability; Standard when several are affected. Must not produce: Automation of waste; Big-bang transformation; AI where deterministic automation suffices (INV-05).

## Scenario C — Knowledge-intensive product business

Characteristics:

- customer, product, and operational knowledge are fragmented;
- product decisions depend on incomplete context;
- analytics and feedback loops are slow.

Likely profile: Standard + Measured. Must not produce: Metric substitution; Hidden assumptions.

## Scenario D — Relationship-driven business

Characteristics:

- value depends on matching people, opportunities, or resources;
- relationship data is incomplete;
- outcomes are difficult to attribute;
- network quality matters more than transaction volume.

Likely profile: Standard + Measured. Must not produce: Metric substitution; value declared REALIZED without attribution (`measurement/VALUE_REALIZATION.md`).

## Scenario E — High-authority, irreversible-action business

Characteristics:

- actions commit money, rights, or customer outcomes and are hard to reverse;
- sensitive data is involved;
- external rules constrain the process;
- pressure exists to let AI act without per-action approval.

Likely profile: Governed (+ Measured). Must not produce: Autonomous-by-default. A correct application typically includes at least one AI candidate classified D or E (`diagnostics/AI_SUITABILITY.md` §5) and recorded as rejected, and Authority Ceilings approved through `HG-AUTHORITY`.

## Validation use

A methodology component is stronger when it works across all scenarios without changing its core definitions.

If a phase, artifact, or skill only works for one scenario, it should be treated as an extension rather than core methodology.

Walk a changed component through each scenario and check that it neither requires a core-definition change nor produces a listed anti-pattern. An application may also legitimately end with no AI selected, or with `INSUFFICIENT_EVIDENCE` (`PUBLIC_API.md` §8).
