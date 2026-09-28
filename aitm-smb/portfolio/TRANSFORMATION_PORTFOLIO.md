# Transformation Portfolio

## 1. Purpose

AITM-SMB treats multiple Initiatives as a coordinated transformation portfolio.

The portfolio exists to optimize system-level outcomes, not initiative count.

---

## 2. Portfolio record

Transformation Portfolio records (`PTF-###`): record contract [`artifacts/transformation-portfolio.md`](../artifacts/transformation-portfolio.md).

The record classifies each Initiative by a §3 category (`initiative_categories`) and holds the WIP limit (§5) and change capacity ([`portfolio/PORTFOLIO_PRIORITIZATION.md`](PORTFOLIO_PRIORITIZATION.md) §4).

Required by the Portfolio profile ([`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md)).

---

## 3. Portfolio categories

Record values: `CONSTRAINT | ENABLER | CAPABILITY | RISK | LEARNING`.

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

AITM-SMB SHOULD make transformation Work In Progress explicit: a WIP limit (`wip_limit`) on concurrently active Initiatives.

SMBs often fail transformation by opening too many initiatives rather than by lacking ideas.
