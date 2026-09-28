# Application Boundary Design

## 1. Purpose

AITM-SMB defines application responsibilities before selecting products or cloud services.

---

## 2. System roles

Common roles:

```text
System of Record
System of Engagement
System of Intelligence
System of Automation
System of Control
System of Observation
```

One product MAY perform multiple roles, but the responsibilities SHOULD remain explicit.

---

## 3. Boundary questions

For each application ask:

```text
What state does it own?
What state may it read?
What actions may it initiate?
What events does it produce?
What is authoritative?
What happens if it is unavailable?
```

---

## 4. AI boundary

A model SHOULD NOT silently become a System of Record.

Probabilistic output becomes durable business state only through explicit validation and persistence logic.

---

## 5. Integration principle

Prefer explicit boundaries:

```text
source of truth
API / event contract
ownership
failure handling
idempotency
```

over implicit synchronization through people.
