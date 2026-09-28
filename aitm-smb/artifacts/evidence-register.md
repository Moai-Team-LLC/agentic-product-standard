---
artifact_type: evidence-register
framework_version: 1.1.0
status: canonical
entity: Evidence
id_prefix: EVD
owner_module: evidence/EVIDENCE_STANDARD.md
produced_by: [02-map-current-system, 11-discover-capabilities, 12-separate-symptoms-gaps-causes, 16-validate-root-cause]
---

# Evidence Register

## Purpose

Hold the engagement's Evidence, its visible Evidence Debt, and its material Uncertainties, so that every `evidence_ids` reference resolves to one record. Any skill MAY append to it.

## Record

Record contracts: Evidence `evidence/EVIDENCE_STANDARD.md` §3; Evidence Debt `evidence/EVIDENCE_STANDARD.md` §5; Uncertainty `evidence/UNCERTAINTY_MODEL.md` §5.

```yaml
evidence: []        # Evidence records (EVD-###)
evidence_debt: []   # Evidence Debt records
uncertainties: []   # Uncertainty records (UNC-###), where material
```

## Rules

Record the Evidence itself by reference: where it lives, what it supports, and its limits. Do not copy confidential or personal content (`evidence/EVIDENCE_STANDARD.md` §8).

Evidence Debt is allowed; hidden Evidence Debt is not.

## Validation

- [ ] every `evidence_ids`, `evidence_for`, and `evidence_against` entry in the engagement resolves to a record here
- [ ] every Evidence record states source, date, scope, claim supported, limitations, and confidence
- [ ] material diagnosis is triangulated where behavioral or system evidence exists (`evidence/EVIDENCE_STANDARD.md` §4)
- [ ] every critical decision made without sufficient Evidence has an Evidence Debt entry
- [ ] evidence rigor is proportional to irreversibility, cost, risk, and authority delegation (`evidence/EVIDENCE_STANDARD.md` §6)
