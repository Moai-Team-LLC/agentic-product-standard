# Root Cause Analysis

## 1. Purpose

AITM-SMB distinguishes:

```text
Observation
≠ Symptom
≠ Gap
≠ Cause
```

This prevents automating symptoms.

Definitions:

- **Cause** — a condition explaining why a Gap exists ([`CORE_MODEL.md`](../CORE_MODEL.md) §5).
- **Cause Hypothesis** — a proposed explanation for a Gap. It MUST NOT be treated as validated truth.
- **Validated Cause** — a Cause Hypothesis supported by sufficient Evidence to justify intervention design (§7 `validated`).

Every Cause is recorded as a Hypothesis (`HYP-###`, `kind: cause`); its ID is unchanged when it is validated.

---

## 2. Root-cause ladder

For every material Symptom ask:

```text
What directly causes this condition?
What system condition allows that cause to persist?
What architectural condition created that system behavior?
```

Example:

```text
Symptom:
quotes take 3 days

Direct cause:
founder approval queue

System condition:
pricing judgment is centralized

Architectural condition:
pricing rules and exception boundaries are tacit
```

The intervention should address the lowest useful causal layer, not necessarily the visible symptom.

---

## 3. Cause classes

AITM-SMB uses these common cause classes:

```text
DEMAND
FLOW
OWNERSHIP
DECISION_RIGHTS
INFORMATION
KNOWLEDGE
PROCESS_DESIGN
SYSTEM_BOUNDARY
INTEGRATION
AUTOMATION
CONTROL
INCENTIVE
SKILL
CAPACITY
MEASUREMENT
FEEDBACK
```

AI is not a cause class.

"Lack of AI" is generally not a valid root cause.

A failure of an existing AI component is classified by its underlying condition, e.g. CONTROL (unverified output), MEASUREMENT (no evaluation), KNOWLEDGE or INFORMATION (missing context), OWNERSHIP (shadow AI).

---

## 4. Evidence test

For every Cause Hypothesis ask:

```text
What evidence would support this?
What evidence would falsify this?
What competing explanation exists?
What would we observe if this were not the cause?
```

---

## 5. Intervention trap test

Before solving, ask:

```text
If this intervention succeeds technically,
could the business problem remain unchanged?
```

If yes, diagnosis is probably incomplete.

---

## 6. Multi-cause gaps

A Gap may have multiple causes.

Example:

```text
Capability:
Customer Issue Resolution

Gap:
resolution time too high

Causes:
- fragmented knowledge
- poor routing
- unclear escalation authority
- missing customer context
```

A single AI assistant may improve only one cause.

---

## 7. Root-cause record

Record contract: the Hypothesis record in [`artifacts/decision-assumption-log.md`](../artifacts/decision-assumption-log.md), with `kind: cause`, `cause_class` from §3, competing hypotheses in `alternative_hypothesis_ids` (where none is reasonable, the reason in `alternatives_note`), and the validation method in `test`.

`confidence` describes the strength of the Evidence behind the recorded `status`, also for `rejected` ([`diagnostics/DIAGNOSTIC_MODEL.md`](DIAGNOSTIC_MODEL.md) §5).

Status meaning:

```text
hypothesized          proposed; not yet tested
testing               its test is under way
accepted_as_testable  explicitly accepted for intervention design as a testable
                      hypothesis by a Decision (DEC-###); its test states how it
                      will be confirmed or rejected
validated             a Validated Cause (§1): the §4 evidence test was applied and
                      evidence_for cites the Evidence (EVD-###)
rejected              Evidence contradicts it, or a competing hypothesis explains the Gap
```

`accepted_as_testable` requires an approved Decision (`DEC-###`, not a [`STANDARD.md`](../STANDARD.md) §8 gate) by the Capability or Outcome owner that lists the `HYP-###` in `subject_ids`. An agent proposes it in `decisions_needed` and MUST NOT set it without that Decision.

The Gap's `cause_status` summarizes the status of its cause Hypotheses ([`CORE_MODEL.md`](../CORE_MODEL.md) §4). A Gap is intervention-ready only when a cause is `validated` or `accepted_as_testable` ([`diagnostics/DIAGNOSTIC_MODEL.md`](DIAGNOSTIC_MODEL.md) §6).
