# Transformation Portfolio

## 1. Purpose

AITM-SMB treats multiple Initiatives as a coordinated transformation portfolio.

The portfolio exists to optimize system-level outcomes, not initiative count.

---

## 2. Portfolio record

```yaml
portfolio:
  id: PTF-###
  outcome_ids: []
  initiatives: []
  current_constraint:
  major_dependencies: []
  shared_enablers: []
  shared_risks: []
  resource_constraints: []
  governance_gates: []
  metric_ids: []
```

---

## 3. Portfolio categories

### Constraint initiatives

Directly relax the current system constraint.

### Enabler initiatives

Create data, knowledge, integration, governance, or observability required by later changes.

### Capability initiatives

Transform a specific business capability.

### Risk initiatives

Reduce material transformation risk.

### Learning initiatives

Produce evidence needed before larger commitment.

---

## 4. Portfolio health

A healthy portfolio SHOULD avoid:

```text
too many simultaneous initiatives
many AI experiments with no shared architecture
enablers with no linked business Outcome
capability changes that compete for the same scarce resource
```

---

## 5. WIP rule

AITM-SMB SHOULD make transformation Work In Progress explicit.

SMBs often fail transformation by opening too many initiatives rather than by lacking ideas.
