---
name: 04-design-interventions
description: "Phase 3 orchestrator. Designs candidate Interventions for each intervention-ready Gap across all intervention families, from eliminating and simplifying work to AI, with simpler alternatives considered before AI; assesses AI suitability (skill 13) and autonomy (skill 14) for AI candidates. Use after diagnosis, before prioritization. Produces the Intervention Map, AI Suitability Assessments and Autonomy Assessments with proposed Authority Ceilings. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "3"
human_gate: false
---

# Skill 04: Orchestrate Intervention Design

## Purpose

Design intervention alternatives for diagnosed Gaps; use AI only where justified; assess AI authority separately from AI fit.

## Required inputs

The Required inputs of `methodology/03-intervention-design.md` (intervention-ready Gaps and their cause Hypotheses, constraints, Evidence).

## Normative sources

- `methodology/03-intervention-design.md` and the modules in its Method

## Produces

- `artifacts/intervention-map.md` — candidate Interventions (`INT-###`), including rejected ones with rationale
- `artifacts/ai-suitability-assessment.md` — one per `AI_*` candidate (skill 13)
- `artifacts/autonomy-assessment.md` — one per `AI_*` candidate and action class, with the proposed Authority Ceiling (skill 14)

## Specialist skills

No specialist writes the candidate Interventions: this skill does (Procedure 3 and 5; phase Activities 1–2 and 5–7). The specialists apply only to `AI_*` candidates:

- `skills/13-assess-ai-suitability/SKILL.md` — for each candidate whose `type` is `AI_*`
- `skills/14-assess-autonomy/SKILL.md` — for each `AI_*` candidate: recommends levels and proposes the Authority Ceiling

## Procedure

1. Load the active profiles (`AGENT_CONTEXT_POLICY.md`) and `methodology/03-intervention-design.md`.
2. Verify the phase's Required inputs; stop with `BLOCKED` when no intervention-ready Gap exists.
3. Write the candidate Interventions yourself (phase Activities 1–2): apply `DECISION_MODEL.md` §1 and the families of `design/INTERVENTION_PATTERNS.md`; each candidate links `gap_ids` and the causes it addresses (`hypothesis_ids`).
4. For `AI_*` candidates, invoke skill 13, then skill 14; carry their open gates into the handoff.
5. Complete each candidate's required context, actions, permissions, verification, and risks; record uncertainties, economic assumptions, and rejected candidates with their rationale (phase Activities 5–7).
6. Keep stable IDs and the `TRACEABILITY.md` §4 trace; validate the phase Exit condition (`EXECUTION_MODEL.md` §2) and each produced contract.
7. Stop with `INSUFFICIENT_EVIDENCE` when a candidate would rest on invented business facts (record Evidence Debt); with `HUMAN_DECISION_REQUIRED` at any `STANDARD.md` §8 gate whose trigger occurs.

A proposed Authority Ceiling takes effect only after `HG-AUTHORITY` (skill 14); no downstream step relies on it before then.

## MUST NOT

- start from AI or from a vendor feature instead of the Gap and its causes;
- select Interventions (that is Phase 4);
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
