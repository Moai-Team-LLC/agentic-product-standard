---
artifact_type: decision-assumption-log
framework_version: 1.1.0
status: canonical
owner_module: DECISION_MODEL.md
produced_by: [01-discover-transformation, 03-diagnose-capabilities, 05-prioritize-initiatives, 06-design-target-system, 07-build-roadmap, 08-design-operating-model, 09-measure-evolution, 12-separate-symptoms-gaps-causes, 16-validate-root-cause, 36-select-application-profile]
---

# Decision & Assumption Log

## Purpose

Hold the engagement's Decisions (`DEC-###`), Assumptions (`ASM-###`), Hypotheses (`HYP-###`), and Risks (`RSK-###`), including every human-gate approval. Besides the listed producers, any skill that records a Decision (including gate approvals and demotions), an Assumption, a Hypothesis, or a Risk appends to it.

Semantics: Decision `DECISION_MODEL.md`; Assumption `evidence/EVIDENCE_STANDARD.md` §7; Hypothesis and Cause `diagnostics/ROOT_CAUSE_ANALYSIS.md`; Risk `ontology/ONTOLOGY.md`.

## Record

Decision:

```yaml
decision:
  id: DEC-###
  statement:
  owner:                # accountable role
  gate:                 # HG-* when this decision closes a STANDARD.md §8 gate; empty otherwise
  subject_ids: []       # IDs this decision approves, selects, rejects, or changes
  alternatives: []
  rationale:
  evidence_ids: []
  assumption_ids: []
  consequences: []
  review_trigger:
  status: proposed | approved | rejected | superseded
  approved_by:          # named human; required when gate is set and status is approved
  date:
```

Assumption:

```yaml
assumption:
  id: ASM-###
  statement:
  impact_if_wrong:
  validation_path:
  owner:
  status: open | validated | invalidated
```

Hypothesis:

```yaml
hypothesis:
  id: HYP-###
  kind: cause | intervention | value | other
  statement:
  gap_ids: []
  cause_class:              # kind: cause only; classes per diagnostics/ROOT_CAUSE_ANALYSIS.md
  alternative_hypothesis_ids: []
  evidence_for: []          # EVD ids
  evidence_against: []      # EVD ids
  test:                     # validation method
  confidence: low | medium | high
  status: hypothesized | testing | validated | rejected | accepted_as_testable
```

Status meaning for cause Hypotheses: `diagnostics/ROOT_CAUSE_ANALYSIS.md` §7. Confidence levels: `diagnostics/DIAGNOSTIC_MODEL.md` §5.

Risk:

```yaml
risk:
  id: RSK-###
  statement:                # the potential failure and the IDs it concerns
  owner:                    # one accountable role
  impact:                   # customer, financial, security, legal, or operational effect if it occurs
  likelihood: low | medium | high
  controls: []              # controls that prevent, detect, or recover from it
  acceptance_decision_id:   # DEC-### accepting it; for a material Risk the DEC closes HG-RISK
  status: open | mitigated | accepted | closed
```

## Rules

Decisions, assumptions, hypotheses, and risks are different object types and MUST NOT be merged.

Gate approvals follow `STANDARD.md` §8 and `AGENTS.md` §4: `gate` set, approved IDs in `subject_ids`, and the human in `approved_by`. An agent MUST NOT fill `approved_by` unless the named human explicitly gave the approval.

The Application Profile selection (skill 36) is a Decision whose `statement` names the selected profiles and whose `review_trigger` states the escalation triggers (`PROFILE_SELECTION.md` §5, §6). `HG-OUTCOME` confirms it.

A Risk is `accepted` only when `acceptance_decision_id` names an approved Decision; accepting a material Risk requires `HG-RISK` (`STANDARD.md` §8), and that Decision lists the `RSK-###` in `subject_ids`.

A Hypothesis keeps its ID when validated. A replaced record keeps its ID and gets `status: superseded` (`ontology/ONTOLOGY.md`).

## Validation

- [ ] every record has a registered ID, and its record type is identifiable
- [ ] every gate Decision has `gate` and `subject_ids`, and, when approved, a named human in `approved_by`
- [ ] every Assumption states `impact_if_wrong` and `validation_path`
- [ ] every cause Hypothesis has `gap_ids` and `cause_class`; `validated` only with Evidence in `evidence_for`
- [ ] material Decisions carry a `review_trigger`
- [ ] every Risk names one `owner`; every accepted material Risk cites an approved `HG-RISK` Decision in `acceptance_decision_id`
