---
artifact_type: diagnostic-record
framework_version: 1.1.0
status: canonical
entity: Diagnostic Record
id_prefix: DIA
owner_module: diagnostics/DIAGNOSTIC_MODEL.md
produced_by: [03-diagnose-capabilities, 12-separate-symptoms-gaps-causes, 16-validate-root-cause]
---

# Diagnostic Record

## Purpose

Record one diagnosis path from Observations and Symptoms to a Gap and its cause Hypotheses (`diagnostics/DIAGNOSTIC_MODEL.md` §1).

## Record

```yaml
diagnostic:
  id: DIA-###
  outcome_ids: []
  capability_id:            # CAP-###
  current_state_id:         # STA-### (type CURRENT)
  observations:
    - evidence_id:          # EVD-###
      statement:
  symptoms: []
  gap_id:                   # GAP-###; holds current_condition and required_condition
  hypothesis_ids: []        # HYP-### (kind: cause); cause_class, confidence and status live on the Hypothesis
  evidence_debt: []         # Evidence Debt this diagnosis leaves open (evidence/EVIDENCE_STANDARD.md §5)
  next_action:
```

Evidence Debt entries are also recorded in the Evidence Register (`artifacts/evidence-register.md`).

## Rules

A Diagnostic Record does not contain solution selection unless the diagnosis has reached intervention readiness.

## Validation

- [ ] every observation cites Evidence (`EVD-###`)
- [ ] Observations, Symptoms, Gap, and Cause Hypotheses are kept distinct (`diagnostics/ROOT_CAUSE_ANALYSIS.md` §1)
- [ ] competing cause Hypotheses are linked through `alternative_hypothesis_ids`, or the reason there are none is recorded
- [ ] missing evidence is recorded as Evidence Debt
- [ ] no solution is selected before the Gap is intervention-ready (`diagnostics/DIAGNOSTIC_MODEL.md` §6)
