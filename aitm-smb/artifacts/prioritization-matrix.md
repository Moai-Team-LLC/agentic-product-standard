---
artifact_type: prioritization-matrix
framework_version: 1.1.0
status: canonical
owner_module: methodology/04-prioritization.md
produced_by: [05-prioritize-initiatives]
---

# Prioritization Matrix

## Purpose

Select transformation Initiatives from candidate Interventions based on explicit trade-offs, and record the decision on every candidate.

## Record

For each candidate:

```yaml
candidate:
  intervention_ids: []        # INT-### assessed together as one candidate
  initiative_id:              # INI-###, created when decision is select (CORE_MODEL.md §7)
  assessment: {}              # every dimension below → {value, rationale}: an ordinal value, or not_relevant with the reason
  decision: select | defer | reject | investigate
  rationale:
  evidence_ids: []
  assumption_ids: []
  major_risks:                # material ones also as Risk records (RSK-###, artifacts/decision-assumption-log.md)
  human_decision_owner:
  decision_id:                # DEC-### recording the selection; closes HG-INITIATIVE when material
```

Dimensions (`assessment` keys):

```text
Business Value            cite the Initiative's economic_hypothesis where one exists (economics/TRANSFORMATION_ECONOMICS.md §5)
Strategic Relevance
Frequency / Volume
Evidence Strength
Data / Knowledge Readiness
Implementation Complexity
Change Burden
Operational Risk
Reversibility
Time to Evidence
Constraint Relevance      where a System Constraint exists (design/CONSTRAINT_ANALYSIS.md §6)
portfolio criteria        Portfolio profile (portfolio/PORTFOLIO_PRIORITIZATION.md §2)
```

## Rules

AITM-SMB does not require a universal weighted formula.

Every material Initiative carries an economic hypothesis (`economic_hypothesis` in [`artifacts/transformation-roadmap.md`](transformation-roadmap.md); [`economics/TRANSFORMATION_ECONOMICS.md`](../economics/TRANSFORMATION_ECONOMICS.md) §5) before `HG-BUDGET`; its candidate's Business Value rationale cites it.

A numeric score MAY support discussion but MUST NOT conceal judgment.

`investigate` means the evidence is insufficient to decide: the Interventions stay `status: candidate`, an Evidence Debt item names what must be learned, and the rationale names it or the Experiment that will resolve it.

## Validation

- [ ] every candidate names its Interventions and a `decision` with written rationale
- [ ] every dimension assessed with an ordinal value and rationale, or marked `not_relevant` with a reason; no score replaces judgment
- [ ] every `select` has an Initiative record (`initiative_id`) with its System Effect Assessment ([`artifacts/system-effect-assessment.md`](system-effect-assessment.md)) and, when material, an approved `HG-INITIATIVE` Decision (`decision_id`)
- [ ] every `investigate` keeps its Interventions at `status: candidate` and names the Evidence Debt or Experiment that resolves it
- [ ] before `HG-BUDGET`, every material Initiative has an economic hypothesis, cited in its Business Value rationale
- [ ] Constraint Relevance assessed where a System Constraint exists; Portfolio: stop condition checked, any override approved by the portfolio owner ([`portfolio/PORTFOLIO_PRIORITIZATION.md`](../portfolio/PORTFOLIO_PRIORITIZATION.md) §5)
