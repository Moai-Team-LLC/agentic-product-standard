# Constraint Analysis

## 1. Purpose

Transformation value is limited by the current system constraint.

AITM-SMB uses constraint analysis to prevent investment in non-limiting parts of the system.

---

## 2. Constraint

A Constraint is the condition that most limits the system's ability to improve a target Outcome.

It may be:

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

---

## 3. Constraint test

A suspected constraint SHOULD satisfy:

```text
If improved materially,
system-level Outcome can improve.

If not improved,
other local improvements have limited effect.
```

---

## 4. Constraint versus bottleneck

A bottleneck is local congestion.

A system constraint is the bottleneck that materially limits the target Outcome.

Not every bottleneck is worth solving.

---

## 5. Constraint migration

When a constraint is improved, another element may become limiting.

Record:

```yaml
constraint:
  id: CST-###
  outcome_ids: []
  capability_ids: []
  type:
  evidence:
  current_effect:
  intervention:
  likely_next_constraint:
  monitoring_metric_ids: []
```

---

## 6. Transformation sequencing implication

Prefer initiatives that:

```text
remove or relax the current system constraint
before optimizing non-constraining capabilities
```

unless a prerequisite requires earlier work.

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
