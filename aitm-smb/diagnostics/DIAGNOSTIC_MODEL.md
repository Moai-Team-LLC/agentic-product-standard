# AITM-SMB Diagnostic Model

## 1. Purpose

AITM-SMB diagnosis converts observed business friction into an evidence-backed transformation model.

The diagnostic chain is:

```text
Observation
→ Symptom
→ Affected Outcome
→ Affected Capability
→ Gap
→ Cause Hypothesis
→ Cause Validation
→ Intervention Candidate
```

The methodology MUST NOT jump directly from:

```text
Symptom
→ AI solution
```

---

## 2. Diagnostic object types

### Observation

A directly observed or evidenced fact.

Examples:

```text
Average lead response time is 11 hours.
35% of support cases are reopened.
Two people approve every non-standard quote.
Customer history is split across four systems.
```

Observation is descriptive.

It does not explain why something happens.

### Symptom

An observable undesirable condition affecting performance.

Examples:

```text
slow response
high rework
inconsistent quality
decision bottleneck
knowledge loss
```

A Symptom MAY be supported by one or more Observations.

### Gap

A difference between current capability behavior and required capability behavior.

Example:

```text
Current:
qualification requires manual review by founder.

Required:
routine qualification can be completed within 15 minutes
without founder participation.
```

### Cause Hypothesis

A proposed explanation for a Gap.

Examples:

```text
required information is unavailable at decision time
rules are tacit rather than explicit
ownership is unclear
system handoffs lose context
work is batched unnecessarily
```

A Cause Hypothesis MUST NOT be treated as validated truth.

### Validated Cause

A cause supported by sufficient evidence to justify intervention design.

---

## 3. Diagnostic rule

The preferred direction is:

```text
Outcome
↓
Capability
↓
Current behavior
↓
Required behavior
↓
Gap
↓
Possible causes
↓
Evidence
```

not:

```text
pain point
↓
tool
```

---

## 4. Diagnostic dimensions

Every capability diagnosis SHOULD inspect:

```text
1. Demand
2. Flow
3. Decisions
4. Roles
5. Information
6. Knowledge
7. Applications
8. Automation
9. AI
10. Controls
11. Economics
12. Feedback
```

These dimensions are defined in `DIAGNOSTIC_DIMENSIONS.md`.

---

## 5. Confidence levels

### Low

Evidence is weak, indirect, contradictory, or based primarily on stakeholder interpretation.

### Medium

Multiple evidence points support the hypothesis, but alternative causes remain plausible.

### High

Evidence consistently supports the cause and competing explanations have been materially reduced.

Confidence SHOULD describe evidence strength, not analyst conviction.

---

## 6. Diagnosis completion test

A Gap is ready for intervention design when:

```text
affected Outcome is known
AND
affected Capability is known
AND
current behavior is described
AND
required behavior is described
AND
business impact is understood
AND
cause is validated OR explicitly accepted as a testable hypothesis
```

If not, continue diagnosis or design an experiment rather than a transformation initiative.
