---
artifact_type: capability-diagnosis
framework_version: 1.1.0
status: canonical
entity: Gap
id_prefix: GAP
owner_module: diagnostics/DIAGNOSTIC_MODEL.md
produced_by: [03-diagnose-capabilities, 12-separate-symptoms-gaps-causes]
---

# Capability Diagnosis

## Purpose

Explain why a Capability does not currently produce the required Outcome: its Gaps and their cause Hypotheses.

## Record

Record contract: Gap [`CORE_MODEL.md`](../CORE_MODEL.md) §4. Cause Hypotheses are Hypothesis records ([`artifacts/decision-assumption-log.md`](decision-assumption-log.md), `kind: cause`) listed in `hypothesis_ids`; their `status` tells hypothesized from validated causes.

Extends `gap` with:

```yaml
gap:
  assumption_ids: []                # ASM-###
  confidence: low | medium | high   # evidence strength for current_condition and business_impact
  observations: []                  # Compact without a Diagnostic Record only: {evidence_id, statement}
  symptoms: []                      # Compact without a Diagnostic Record only
```

## Rules

Inspect the diagnostic dimensions in [`diagnostics/DIAGNOSTIC_DIMENSIONS.md`](../diagnostics/DIAGNOSTIC_DIMENSIONS.md) that are relevant to the transformation boundary, including the Capability's `dependencies` under the Flow dimension (Capability Map; the Capability Network where one exists).

From the Standard profile, Observations and Symptoms sit in Diagnostic Records ([`artifacts/diagnostic-record.md`](diagnostic-record.md)); in Compact they MAY sit on the Gap, kept distinct from its conditions and causes ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../diagnostics/ROOT_CAUSE_ANALYSIS.md) §1).

Do not diagnose "lack of AI" as a root cause ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../diagnostics/ROOT_CAUSE_ANALYSIS.md) §3).

## Validation

- [ ] every Gap links one Capability and its CURRENT State (`current_state_id`)
- [ ] current and required condition are described and business impact is stated
- [ ] every material Gap has competing cause Hypotheses, or the reason there are none is recorded (Hypothesis `alternatives_note`)
- [ ] `cause_status` matches the linked Hypotheses; `validated` or `accepted_as_testable` only when a linked Hypothesis has that status ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../diagnostics/ROOT_CAUSE_ANALYSIS.md) §7)
- [ ] a Gap proceeds to Phase 3 only when intervention-ready ([`diagnostics/DIAGNOSTIC_MODEL.md`](../diagnostics/DIAGNOSTIC_MODEL.md) §6); otherwise its Evidence Debt is recorded
