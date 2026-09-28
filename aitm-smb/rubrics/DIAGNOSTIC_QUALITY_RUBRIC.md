# Diagnostic Quality Rubric

**Status:** Informative (`NORMATIVE_INDEX.md` tier 13). A review aid for Phase 2 outputs; the diagnostic chain is normative in `diagnostics/DIAGNOSTIC_MODEL.md` and `diagnostics/ROOT_CAUSE_ANALYSIS.md`. Typical use: `skills/03-diagnose-capabilities/SKILL.md`, `skills/16-validate-root-cause/SKILL.md`.

A diagnosis is strong when it can answer:

## Evidence

- What was directly observed?
- What source supports each material observation?
- What remains inferred?

## Outcome

- Which business Outcome is affected?
- Is the impact measurable?

## Capability

- Which organizational ability is constrained?
- Is the capability boundary appropriate?

## Gap

- What is current behavior?
- What behavior is required?
- What is the material difference?

## Cause

- What competing explanations exist?
- What evidence supports the selected cause?
- What could falsify it?

## Intervention

- Was elimination or simplification considered?
- Was deterministic automation considered?
- What specifically requires AI?

## Autonomy

- Why is the proposed authority level justified?
- Can failures be observed and recovered?

## Failure condition

If the analysis cannot distinguish:

```text
Symptom
Gap
Cause
Intervention
```

the diagnosis is not ready for architecture design.
