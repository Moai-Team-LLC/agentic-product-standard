# Phase 2 — Diagnose (Capability Diagnosis)

## Objective

Identify why current capabilities do not produce required Outcomes.

## Required inputs

- approved Transformation Intent;
- Capability Map with CURRENT States;
- Business System Map (`artifacts/business-system-map.md`), where the profile requires it;
- Evidence Register and other available evidence.

## Method

Use:

1. `diagnostics/DIAGNOSTIC_MODEL.md`
2. `diagnostics/DIAGNOSTIC_DIMENSIONS.md`
3. `diagnostics/ROOT_CAUSE_ANALYSIS.md`
4. `evidence/EVIDENCE_STANDARD.md`
5. `AGENT_DIAGNOSTIC_PROTOCOL.md` (agents)

## Activities

1. extract observations;
2. identify symptoms;
3. link symptoms to Outcomes and Capabilities;
4. define current versus required capability behavior;
5. create Gaps;
6. generate competing Cause Hypotheses;
7. seek supporting and falsifying evidence;
8. validate causes or record Evidence Debt;
9. set each Gap's `cause_status`.

## Outputs

- Capability Diagnosis (`artifacts/capability-diagnosis.md`): Gap records (`GAP-###`);
- Diagnostic Records (`artifacts/diagnostic-record.md`);
- cause Hypotheses (`HYP-###`, `kind: cause`) in the Decision & Assumption Log; validated causes are Hypotheses with `status: validated`;
- Evidence Register updates: Evidence and Evidence Debt;
- Decision & Assumption Log updates.

## Human gates

None typically. Any `STANDARD.md` §8 gate applies whenever its trigger occurs. Governed profile: Execution Gate A (`execution/EXECUTION_GATE_MODEL.md`).

## Exit condition

Matches `EXECUTION_MODEL.md` §2: material Gaps and their cause Hypotheses are explicit; a Gap proceeds only when intervention-ready; otherwise its Evidence Debt is recorded.

A Gap is intervention-ready only when (`diagnostics/DIAGNOSTIC_MODEL.md` §6):

```text
Outcome known
AND Capability known
AND current behavior known
AND required behavior known
AND impact understood
AND cause validated OR explicitly accepted as testable hypothesis
```

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` (`AGENTS.md` §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

```text
Symptom → AI solution
```
