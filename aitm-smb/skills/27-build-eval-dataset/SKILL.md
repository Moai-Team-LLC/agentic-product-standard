---
name: 27-build-eval-dataset
description: "Builds or extends the evaluation dataset for an AI component: a representative composition (common, rare, edge, policy-sensitive, ambiguous, high-impact cases, historical failures, adversarial cases), every case with task, input, expected and unacceptable behavior, risk class and source, with personal and confidential content minimized, leakage tracked, and maintenance triggers applied. Use in Phase 6 before an AI component is piloted or evaluated, and again when a maintenance trigger or incident requires new cases. Produces eval_dataset records in the datasets section of artifacts/evaluation-plan.md. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: execution-governance
phase: "6"
human_gate: false
---

# Skill 27: Build Evaluation Dataset

## Purpose

Give an AI component a representative, maintained set of cases to be evaluated against, so that quality claims rest on evidence rather than on demos. Invoked by `skills/07-build-roadmap/SKILL.md` for AI components.

## Required inputs

- AI task definition, Capability (CAP) and Autonomy Assessment of the component;
- historical cases and known failure patterns, including Incident records (INC-###, `artifacts/incident-record.md`), where they exist;
- policy constraints;
- the Evaluation Plan whose evaluations use the dataset.

## Normative sources

- `evaluation/EVALUATION_DATASET.md`
- `evaluation/AI_EVALS.md`
- `evidence/EVIDENCE_STANDARD.md` §8 (sensitive sources)

## Produces

- `artifacts/evaluation-plan.md` — `datasets`: eval_dataset records with their eval_case records, or a `location` where the cases live in evaluation tooling.

## Procedure

1. Compose the dataset from the case types of `evaluation/EVALUATION_DATASET.md` §2 that are relevant, including historical failures and adversarial cases; record them in `composition`.
2. Fill every eval_case field (§3) for each case: task, input, expected and unacceptable behavior, risk class, source.
3. Minimize and redact personal or confidential content taken from real cases, or reference the source instead (`evidence/EVIDENCE_STANDARD.md` §8).
4. Record leakage exposure (`evaluation/EVALUATION_DATASET.md` §4), owner, and `last_reviewed`.
5. Add cases when a maintenance trigger of its §5 occurs; for a case derived from an incident, return its `<dataset id>/<case id>` for the incident's `eval_case_added`.
6. Validate against the Validation of `artifacts/evaluation-plan.md` (datasets).
7. Stop with `INSUFFICIENT_EVIDENCE` when representative cases cannot be obtained without inventing them as real (label synthetic cases in `source`), or `BLOCKED` when a required input is missing.

## MUST NOT

- copy personal or confidential content into cases;
- tune prompts or workflows on evaluation cases without recording the leakage;
- drop cases because the component fails them;
- present synthetic cases as historical.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
