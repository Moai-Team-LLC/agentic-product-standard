# AITM-SMB Evidence Standard

## 1. Purpose

AITM-SMB must remain evidence-backed without becoming enterprise bureaucracy.

Evidence exists to support transformation decisions.

---

## 2. Evidence hierarchy

Evidence strength depends on the claim.

Common sources:

```text
system records
transaction data
financial data
logs
observed workflow
customer behavior
documented policy
stakeholder interview
expert judgment
external benchmark
controlled experiment
```

No source is universally strongest.

---

## 3. Evidence record

```yaml
evidence:
  id: EVD-###
  source_type:
  source:
  date:
  scope:
  claim_supported:
  limitations:
  confidence:
```

---

## 4. Triangulation

Material diagnosis SHOULD avoid reliance on one stakeholder statement when behavioral or system evidence exists.

Prefer:

```text
interview
+ observed process
+ system data
```

when feasible.

---

## 5. Evidence debt

If a critical decision is made without sufficient evidence, record:

```yaml
evidence_debt:
  claim:
  decision_affected:
  missing_evidence:
  risk_if_wrong:
  validation_plan:
  deadline_or_gate:
```

Evidence debt is allowed.

Hidden evidence debt is not.

---

## 6. Evidence proportionality

Do not require enterprise-scale evidence for reversible low-risk decisions.

Evidence rigor SHOULD increase with:

```text
irreversibility
cost
risk
authority delegation
customer impact
legal impact
architecture lock-in
```
