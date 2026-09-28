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

Record contract: Gap `CORE_MODEL.md` §4. Cause Hypotheses are Hypothesis records (`artifacts/decision-assumption-log.md`, `kind: cause`) listed in `hypothesis_ids`; their `status` tells hypothesized from validated causes.

Extends `gap` with:

```yaml
gap:
  assumption_ids: []                # ASM-###
  confidence: low | medium | high   # evidence strength for current_condition and business_impact
```

## Rules

Inspect the diagnostic dimensions in `diagnostics/DIAGNOSTIC_DIMENSIONS.md` that are relevant to the transformation boundary.

Do not diagnose "lack of AI" as a root cause (`diagnostics/ROOT_CAUSE_ANALYSIS.md` §3).

## Validation

- [ ] every Gap links one Capability and its CURRENT State (`current_state_id`)
- [ ] current and required condition are described and business impact is stated
- [ ] every material Gap has competing cause Hypotheses, or the reason there are none is recorded
- [ ] `cause_status` matches the linked Hypotheses; `validated` only when a Hypothesis is validated
- [ ] a Gap proceeds to Phase 3 only when intervention-ready (`diagnostics/DIAGNOSTIC_MODEL.md` §6); otherwise its Evidence Debt is recorded
