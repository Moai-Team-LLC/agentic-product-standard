# AITM-SMB Maturity Model

**Status:** Informative. Not an assessment instrument, a score, a target, or an input to any profile, conformance check, or gate.

The levels describe how deeply AI is integrated into one Capability. They are descriptive per Capability, not a measure of organizational progress or worth.

## M0 — No AI

The Capability uses no AI. Its work may be manual or fully deterministic (software, automation). Where AI is not justified, M0 is a valid and often correct end state (INV-05).

## M1 — AI-Assisted

Individuals use general AI tools, but AI is not embedded in how the Capability operates.

## M2 — AI-Embedded

AI components are embedded in specific products or workflows of the Capability.

## M3 — AI-Orchestrated

AI coordinates information and actions across multiple business systems with explicit controls.

## M4 — AI-Native

The Capability is intentionally redesigned around human + AI collaboration.

## M5 — Bounded Agentic

Agents pursue bounded business objectives with explicit permissions, verification, observability, escalation, and governance.

## Rules

Higher maturity is not automatically better. No level is a target in itself.

The appropriate level for a Capability follows from its diagnosed Gaps, the intervention challenge (`STANDARD.md` §5), business value, risk, economics, and organizational capacity.

M-levels are not autonomy levels and grant no authority. AI authority is set per action class by the autonomy ladder L0–L5 (`diagnostics/AUTONOMY_SUITABILITY.md` §2) and granted only through `HG-AUTHORITY` (`STANDARD.md` §8).

Autonomy is a revocable operating privilege, not a permanent maturity achievement (`governance/AUTHORITY_ESCALATION_MODEL.md`).
