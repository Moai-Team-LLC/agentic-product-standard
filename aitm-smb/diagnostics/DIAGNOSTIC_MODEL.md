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

Records: Observations and Symptoms in the Diagnostic Record ([`artifacts/diagnostic-record.md`](../artifacts/diagnostic-record.md); optional in Compact, where they MAY sit on the Gap); Gaps in the Capability Diagnosis ([`artifacts/capability-diagnosis.md`](../artifacts/capability-diagnosis.md)); Cause Hypotheses as Hypothesis records ([`artifacts/decision-assumption-log.md`](../artifacts/decision-assumption-log.md)); Evidence and Evidence Debt in the Evidence Register ([`artifacts/evidence-register.md`](../artifacts/evidence-register.md)). Agents follow [`AGENT_DIAGNOSTIC_PROTOCOL.md`](../AGENT_DIAGNOSTIC_PROTOCOL.md).

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

A material difference between current Capability behavior and required behavior ([`CORE_MODEL.md`](../CORE_MODEL.md) §4).

Example:

```text
Current:
qualification requires manual review by founder.

Required:
routine qualification can be completed within 15 minutes
without founder participation.
```

### Cause Hypothesis

A proposed explanation for a Gap (defined in [`diagnostics/ROOT_CAUSE_ANALYSIS.md`](ROOT_CAUSE_ANALYSIS.md) §1).

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

A cause supported by sufficient evidence to justify intervention design ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](ROOT_CAUSE_ANALYSIS.md) §1). It keeps its `HYP-###` ID.

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

Every capability diagnosis SHOULD inspect the twelve dimensions defined in [`diagnostics/DIAGNOSTIC_DIMENSIONS.md`](DIAGNOSTIC_DIMENSIONS.md), as far as they are relevant to the transformation boundary.

---

## 5. Confidence levels

These levels apply to every `confidence: low | medium | high` field in AITM-SMB records (Hypotheses, Evidence, Gaps, Capabilities, uncertainties).

### Low

Evidence is weak, indirect, contradictory, or based primarily on stakeholder interpretation.

### Medium

Multiple evidence points support the hypothesis or claim, but alternative explanations remain plausible.

### High

Evidence consistently supports the cause or claim and competing explanations have been materially reduced.

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

The last condition holds when the Gap's `cause_status` is `validated` or `accepted_as_testable` ([`CORE_MODEL.md`](../CORE_MODEL.md) §4). Explicit acceptance is a Decision of the Capability or Outcome owner, never the agent's own ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](ROOT_CAUSE_ANALYSIS.md) §7).

If not, continue diagnosis or design an experiment rather than a transformation initiative, and record the missing Evidence as Evidence Debt ([`evidence/EVIDENCE_STANDARD.md`](../evidence/EVIDENCE_STANDARD.md) §5).
