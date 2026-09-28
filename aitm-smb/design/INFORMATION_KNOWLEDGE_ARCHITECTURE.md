# Information & Knowledge Architecture

## 1. Purpose

AI quality is constrained by the information and knowledge system around it.

AITM-SMB distinguishes:

```text
Data
Information
Knowledge
Context
Memory
```

In ontology terms ([`ontology/ONTOLOGY.md`](../ontology/ONTOLOGY.md)): Data and Information are held in Data Assets; Knowledge and persisted Memory are Knowledge Assets; Context is a per-task selection, not an asset.

---

## 2. Data

Structured facts.

Examples:

```text
customer_id
price
status
timestamp
quantity
```

---

## 3. Information

Data interpreted in a business context.

Example:

```text
customer is overdue
```

---

## 4. Knowledge

Rules, expertise, patterns, documents, constraints, and learned understanding required for competent action.

---

## 5. Context

The subset of data, information, and knowledge relevant to a specific decision or task.

---

## 6. Memory

Persisted interaction or state used across time.

Memory MAY be:

```text
user memory
case memory
workflow state
agent memory
organizational memory
```

---

## 7. Architecture questions

For every AI-enabled capability ask:

```text
What facts are authoritative?
What knowledge is required?
Who owns that knowledge?
How is knowledge updated?
What context is needed at execution time?
What may AI retain?
What must not be retained?
```

---

## 8. Knowledge readiness

AI SHOULD NOT compensate indefinitely for:

```text
contradictory policies
outdated documents
unknown ownership
uncontrolled knowledge sources
missing canonical data
```

In such cases, knowledge architecture itself is part of the transformation.
