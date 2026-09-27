# AITM-SMB 1.0 Release Notes

AITM-SMB 1.0 freezes the first stable semantic contract of the methodology.

## Stable in 1.x

- Business Capability as the primary transformation unit;
- Outcome → Capability → Gap → Intervention → Initiative → Metric → Evidence trace;
- separation of Symptom, Gap, Cause, and Intervention;
- AI as an optional intervention family;
- separation of AI Suitability and AI Authority;
- Capability Target State vs Target Operating Architecture;
- System Constraint and Constraint Migration;
- explicit Transition States;
- Evidence-before-scale execution;
- Value Realization as the completion criterion;
- Compact / Standard / Governed / Portfolio / Measured profiles;
- agent-readable skills and artifact contracts.

## Compatibility promise

AITM-SMB 1.x may add optional modules, artifacts, skills, and Extensions.

It will not incompatibly redefine the stable semantic objects in `PUBLIC_API.md`.

## Deprecated compatibility aliases

- `artifacts/ai-opportunity-map.md`
- `artifacts/target-architecture.md`

They remain redirect stubs only.

## Recommended default

```text
Standard + Measured
```

Add `Governed` when authority or risk is material.
