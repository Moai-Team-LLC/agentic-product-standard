# Constraint Analysis

## 1. Purpose

Transformation value is limited by the current System Constraint.

AITM-SMB uses constraint analysis to prevent investment in non-limiting parts of the system.

This module is the canonical source of System Constraint and Constraint Migration ([`CANONICAL_CONCEPTS.md`](../CANONICAL_CONCEPTS.md)). Record contract: [`artifacts/system-constraint.md`](../artifacts/system-constraint.md).

---

## 2. System Constraint

A System Constraint (`CST-###`) is the condition that most limits the system's ability to improve a target Outcome.

Not to be confused with a design Constraint ([`ontology/ONTOLOGY.md`](../ontology/ONTOLOGY.md)): a limit the architecture must respect, recorded in `constraints` fields.

Common types (record `type`):

```text
capacity
decision authority
knowledge
data quality
customer demand
process design
control requirement
technology
cash
skill
coordination
```

A constraint type is not a cause class ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../diagnostics/ROOT_CAUSE_ANALYSIS.md)); the two need not match.

---

## 3. Constraint test

A suspected constraint SHOULD satisfy:

```text
If improved materially,
system-level Outcome can improve.

If not improved,
other local improvements have limited effect.
```

Record the result in `why_system_limiting`.

---

## 4. Constraint versus bottleneck

A bottleneck is local congestion.

A System Constraint is the bottleneck that materially limits the target Outcome.

Not every bottleneck is worth solving.

---

## 5. Constraint Migration

Constraint Migration is the movement of the System Constraint to another element after the current one is relaxed: when a constraint is improved, another element may become limiting.

A new overload is a migrated System Constraint only if it passes the constraint test (§3); otherwise it is a local bottleneck (§4).

Predict the likely next constraint before a change is approved (INV-09; [`design/LOCAL_OPTIMIZATION_GUARD.md`](LOCAL_OPTIMIZATION_GUARD.md) §2) and monitor it after the change. Record both in the System Constraint (`likely_next_constraint`, `monitoring_metric_ids`).

When the constraint has moved, record the new System Constraint as a new `CST-###`; the old record gets `status: superseded` ([`ontology/ONTOLOGY.md`](../ontology/ONTOLOGY.md)).

---

## 6. Transformation sequencing implication

Prefer initiatives that:

```text
remove or relax the current system constraint
before optimizing non-constraining capabilities
```

unless a prerequisite requires earlier work.

Where a System Constraint has been identified, it is an input to Initiative selection ([`methodology/04-prioritization.md`](../methodology/04-prioritization.md)) and to sequencing ([`transition/TRANSFORMATION_SEQUENCING.md`](../transition/TRANSFORMATION_SEQUENCING.md)).

---

## 7. False constraint patterns

Common mistakes:

```text
"we need more leads"
when sales conversion is the true constraint

"we need AI"
when knowledge is fragmented

"we need automation"
when demand is unstable

"we need more people"
when decision rights are centralized
```
