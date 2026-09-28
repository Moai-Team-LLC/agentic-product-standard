---
artifact_type: intervention-map
framework_version: 1.1.0
status: canonical
entity: Intervention
id_prefix: INT
owner_module: design/INTERVENTION_PATTERNS.md
produced_by: [04-design-interventions, 05-prioritize-initiatives]
---

# Intervention Map

## Purpose

Map candidate Interventions of every family against diagnosed Capability Gaps and their causes, including the candidates rejected and why.

AI interventions are a subset of interventions.

## Record

Record contract: Intervention [`CORE_MODEL.md`](../CORE_MODEL.md) §6. `type` is one [`PUBLIC_API.md`](../PUBLIC_API.md) §6 family (definitions: [`design/INTERVENTION_PATTERNS.md`](../design/INTERVENTION_PATTERNS.md); challenge order: [`STANDARD.md`](../STANDARD.md) §5).

Extends `intervention` with:

```yaml
intervention:
  required_context:
  required_actions:
  required_permissions:
  verification:
  status_rationale:        # why selected, deferred, or rejected
```

For an `AI_*` candidate, the non-AI alternative and the AI fit are recorded in its AI Suitability Assessment ([`artifacts/ai-suitability-assessment.md`](ai-suitability-assessment.md)); its authority in the Autonomy Assessment ([`artifacts/autonomy-assessment.md`](autonomy-assessment.md)).

## Rules

An AI intervention MUST NOT be selected before plausible simpler intervention classes are considered.

An `AI_*` type names the kind of AI contribution; authority is set only by the autonomy level.

`status: selected` is set in Phase 4, after `HG-INITIATIVE` where the selection is material ([`STANDARD.md`](../STANDARD.md) §8); an `AI_*` Intervention only once its Authority Ceiling is approved (`HG-AUTHORITY`). Skill 05 changes only `status` and `status_rationale`.

## Validation

- [ ] every Intervention links at least one intervention-ready Gap (`gap_ids`) and the causes it addresses (`hypothesis_ids`)
- [ ] `type` is one [`PUBLIC_API.md`](../PUBLIC_API.md) §6 family
- [ ] simpler alternatives are recorded in `simpler_alternatives_considered`
- [ ] every `AI_*` candidate has an AI Suitability Assessment; every `AI_*` candidate proposed for selection also has an Autonomy Assessment with a proposed Authority Ceiling ([`methodology/03-intervention-design.md`](../methodology/03-intervention-design.md))
- [ ] rejected and deferred candidates carry a `status_rationale`
