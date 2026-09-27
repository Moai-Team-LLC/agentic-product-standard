# Execution Gate Model

## 1. Purpose

Execution gates prevent uncontrolled progression from idea to production autonomy.

---

## 2. Standard gates

### Gate A — Diagnosis Ready

Gap and cause are sufficiently understood.

### Gate B — Design Approved

Intervention and Target State approved.

### Gate C — Pilot Ready

Pilot scope, evidence, guardrails, metrics, and rollback defined.

### Gate D — Pilot Passed

Success threshold met or evidence supports promotion.

### Gate E — Rollout Ready

Operations, monitoring, ownership, recovery, governance ready.

### Gate F — Operational

Target scope runs under approved operating model.

### Gate G — Value Confirmed

Business effect is evidenced.

---

## 3. Gate record

```yaml
gate:
  id: GAT-###
  initiative_id:
  type:
  required_evidence: []
  approver:
  status: open | passed | failed | waived
  decision_record:
```

---

## 4. Waiver

A gate MAY be waived only by an explicit human decision with:

```text
reason
risk
owner
expiration or review trigger
```
