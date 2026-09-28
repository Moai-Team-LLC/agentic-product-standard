# AITM-SMB Diagnostic Dimensions

The dimensions a capability diagnosis inspects (rule: [`diagnostics/DIAGNOSTIC_MODEL.md`](DIAGNOSTIC_MODEL.md) §4).

They are the diagnostic lens over the [`STANDARD.md`](../STANDARD.md) §4 system model: People → Roles; Decision Rights → Decisions; Process → Demand and Flow; Data → Information; Metrics → Feedback; the other dimensions share their names.

## 1. Demand

Questions:

- What triggers the capability?
- What volume and variability exist?
- Are peaks predictable?
- Which requests create disproportionate cost?
- Which cases are routine versus exceptional?

Signals:

```text
queue growth
seasonality
unbounded intake
unqualified work
high variability
```

---

## 2. Flow

Questions:

- What are the actual steps?
- Where does work wait?
- Where does context get lost?
- How many handoffs exist?
- Which work is batched?
- Where is rework introduced?
- Which upstream Capabilities does the work depend on (the Capability's `dependencies`), and where do they delay or degrade it?

Signals:

```text
queue time
handoff count
rework
duplicate entry
manual copy/paste
work-in-progress accumulation
```

---

## 3. Decisions

Questions:

- Which decisions materially change the outcome?
- Who makes them?
- What information is required?
- How often are they repeated?
- Which decisions are rules-based versus judgment-based?
- Which decisions create bottlenecks?

Signals:

```text
approval latency
decision concentration
inconsistent judgment
missing context
founder bottleneck
```

---

## 4. Roles

Questions:

- Who performs the work?
- What requires scarce expertise?
- Which responsibilities are ambiguous?
- Which roles perform work below their leverage?
- Where is tacit coordination required?

Signals:

```text
expert dependency
single point of failure
unclear ownership
management overload
role fragmentation
```

---

## 5. Information

Questions:

- What data is needed?
- Where does it live?
- Is it current?
- Is it structured enough?
- Is identity consistent across systems?
- Is the same fact represented differently?

Signals:

```text
fragmented records
stale data
duplicate truth
manual reconciliation
missing fields
```

---

## 6. Knowledge

Questions:

- What must a competent person know?
- Is knowledge explicit or tacit?
- How is it updated?
- Can it be retrieved at decision time?
- Who is the knowledge bottleneck?

Signals:

```text
tribal knowledge
expert dependency
document sprawl
low retrieval reliability
outdated SOPs
```

---

## 7. Applications

Questions:

- Which systems support the capability?
- Which system is authoritative?
- Where are duplicate functions?
- Where are manual bridges?
- Which system constraints shape process behavior?

Signals:

```text
tool fragmentation
shadow spreadsheets
manual synchronization
legacy constraints
weak APIs
```

---

## 8. Automation

Questions:

- What is deterministic and repeatable?
- What is already automated?
- Where does automation break?
- Are exceptions controlled?
- Are manual steps actually necessary?

Signals:

```text
rule-based repetitive work
manual routing
manual notifications
copy/paste operations
avoidable reconciliation
```

---

## 9. AI

Questions:

- Is AI already used?
- Is usage embedded or ad hoc?
- Which AI outputs influence decisions?
- What context does AI receive?
- Is output evaluated?
- Does AI create hidden operational risk?

Signals:

```text
shadow AI
prompt dependence
unverified generation
context fragmentation
no evaluation
```

---

## 10. Controls

Questions:

- What requires approval?
- What is prohibited?
- What is logged?
- Who can change critical state?
- How are exceptions handled?

Signals:

```text
informal approvals
missing audit trail
over-broad access
unowned exceptions
```

---

## 11. Economics

Questions:

- What does the capability cost?
- What consumes scarce labor?
- What is the cost of delay?
- What is the cost of error?
- Which activity has negative unit economics?

Signals:

```text
high cost per transaction
low-margin manual work
costly rework
expensive expert time
```

---

## 12. Feedback

Questions:

- How does the system learn?
- Are outcomes measured?
- How quickly do failures become visible?
- Does the process improve based on evidence?
- Is knowledge updated after exceptions?

Signals:

```text
no closed loop
repeat failures
slow learning
metrics disconnected from action
```
