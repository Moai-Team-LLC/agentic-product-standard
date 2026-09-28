# AITM-SMB Evidence Standard

## 1. Purpose

AITM-SMB must remain evidence-backed without becoming enterprise bureaucracy.

Evidence exists to support transformation decisions.

Instances of the records below live in the Evidence Register (`artifacts/evidence-register.md`). Evidence labels in artifacts and agent output: `AGENTS.md` §3.

---

## 2. Evidence sources

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
  source_type:          # a §2 source, or another named type
  source:               # where it can be found; for sensitive sources a reference, not a copy (§8)
  date:
  scope:
  claim_supported:      # the claim, or the IDs it supports (e.g. GAP-###, HYP-###, ASM-###, MET-###)
  limitations:
  confidence: low | medium | high   # diagnostics/DIAGNOSTIC_MODEL.md §5
```

Records cite Evidence through their `evidence_ids` (Hypotheses: `evidence_for`, `evidence_against`).

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
  claim:                # statement, or the ASM-### / HYP-### it concerns
  decision_affected:    # DEC-###, HG-* gate, or the GAP / INT / INI record it affects
  missing_evidence:
  risk_if_wrong:
  validation_plan:
  deadline_or_gate:
```

Evidence debt is allowed.

Hidden evidence debt is not.

Agents also list open Evidence Debt in `aitm_output.evidence_debt` (`AGENT_OUTPUT_STANDARD.md`).

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

---

## 7. Assumptions

An Assumption is a statement accepted without sufficient Evidence so that work can proceed.

A material Assumption is recorded as `ASM-###` (`artifacts/decision-assumption-log.md`) with its impact if wrong and its validation path. It stays an Assumption until Evidence validates or invalidates it; it is never silently promoted to fact (`AGENTS.md` §3).

---

## 8. Sensitive sources

Evidence often comes from confidential or personal sources (interviews, financial records, customer cases).

Reference such a source by its Evidence ID and a description in `source`; do not copy personal or confidential content into records. Engagement data handling: `AGENT_CONTEXT_POLICY.md` (Engagement workspace).
