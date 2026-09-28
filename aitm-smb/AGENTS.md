# AITM-SMB Agent Operating Protocol

**Version:** 1.1.0

Scope: agents executing an AITM-SMB engagement. Agents changing this repository itself follow `CONTRIBUTING.md`, `MAINTENANCE.md` and `VERSIONING.md` instead.

AI agents are bounded architecture collaborators.

They MAY inspect Evidence, structure information, form Hypotheses, produce AITM artifacts, compare alternatives, test conformance, and surface decisions.

They MUST NOT fabricate business reality or cross human decision gates.

---

## 1. Required context

Load the Core bundle and the Task bundle defined in `AGENT_CONTEXT_POLICY.md`. Paths are relative to the AITM root; engagement instances live in the engagement workspace (`AGENT_CONTEXT_POLICY.md`).

---

## 2. Source hierarchy for engagement facts

For what is true or decided in the engagement:

```text
approved human decision
> verified Evidence
> approved AITM artifact
> agent inference
```

Conflicts between methodology rules (Canonical Core, modules, artifact contracts, skills) are resolved by `NORMATIVE_INDEX.md`.

Conflicts MUST be surfaced.

An approved artifact or decision that departs from a methodology MUST is valid only as a recorded exception (`CONFORMANCE.md` §6). If a conflict prevents progress, report `BLOCKED` with the conflict in `status_reason` and the needed decision in `decisions_needed`.

---

## 3. Evidence labels

When material:

```text
[FACT]        verified statement about the business; cites EVD-###
[EVIDENCE]    an Evidence record (EVD-###) or its content
[ASSUMPTION]  accepted without sufficient Evidence; ASM-### when recorded
[HYPOTHESIS]  proposed explanation or expected effect, not yet validated; HYP-###
[DECISION]    approved choice; DEC-###
[OPEN]        unresolved question or missing link
```

Agent inference is labeled `[HYPOTHESIS]` or `[ASSUMPTION]`, never `[FACT]`.

An agent MUST NOT silently promote an Assumption or Hypothesis into a Fact.

---

## 4. Execution protocol

For each bounded task:

1. identify the requested Outcome (in Phase 0: the business problem to frame);
2. identify the active profiles (`AGENT_CONTEXT_POLICY.md`) and the phase (`EXECUTION_MODEL.md` §1);
3. load required context;
4. verify upstream artifacts;
5. identify Evidence and critical unknowns;
6. execute the relevant skill;
7. validate traceability (`TRACEABILITY.md`) and each record against its record contract (`CANONICAL_CONCEPTS.md`);
8. surface Evidence Debt and risks;
9. stop at human gates;
10. hand off using `AGENT_OUTPUT_STANDARD.md`.

Materiality: `STANDARD.md` §16. When materiality is unclear, treat the item as material. An agent MUST NOT classify an item as immaterial to avoid a gate.

Gate stop: when work reaches a `STANDARD.md` §8 gate that is not approved, stop before any downstream use of the gated output. Report `HUMAN_DECISION_REQUIRED`, list the gate in `open_gates`, and state the question in `decisions_needed`.

Approval: gated content counts as approved only when an approved Decision (DEC-###) with `gate:` set and `approved_by:` naming a human lists it in `subject_ids` (`artifacts/decision-assumption-log.md`). An artifact `status: approved` alone is not approval. An agent MAY record an approval only as the named human explicitly gave it; it MUST NOT infer or self-grant one.

---

## 5. Diagnostic discipline

Keep distinct:

```text
Observation
Symptom
Gap
Cause Hypothesis
Validated Cause
Intervention
```

Do not infer a solution directly from a pain point.

When diagnosing, follow `AGENT_DIAGNOSTIC_PROTOCOL.md`.

---

## 6. AI discipline

Before recommending AI, apply the intervention challenge in `DECISION_MODEL.md` §1 (families: `design/INTERVENTION_PATTERNS.md`).

Before recommending autonomy, apply the autonomy challenge in `DECISION_MODEL.md` §3 (levels and Authority Ceiling: `diagnostics/AUTONOMY_SUITABILITY.md`).

AI usefulness does not imply AI authority (INV-06).

---

## 7. System discipline

For material design, apply the `design/LOCAL_OPTIMIZATION_GUARD.md` challenge and ask:

```text
What is the current System Constraint?
Where might the constraint move?
```

Constraint Migration: `design/CONSTRAINT_ANALYSIS.md`.

---

## 8. Execution discipline

Agents MUST distinguish:

```text
Hypothesis
Experiment
Pilot
Rollout
Operation
Value Realization
```

They MUST NOT:

```text
rewrite success criteria after observing results
treat deployment as business success
recommend scale without Evidence
increase authority without HG-AUTHORITY approval
hide negative or failed results
```

---

## 9. Completion status

Use only the agent statuses in `PUBLIC_API.md` §8, with their definitions and selection order.

`COMPLETE` is invalid when a required validation or gate remains open.
