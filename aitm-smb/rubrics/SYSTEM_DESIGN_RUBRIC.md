# System Design Quality Rubric

**Status:** Informative (`NORMATIVE_INDEX.md` tier 13). A review aid for Phases 5 and 6; the rules are normative in the `design/`, `transition/` and `portfolio/` modules. Typical use: `skills/06-design-target-system/SKILL.md`, `skills/24-audit-local-optimization/SKILL.md`.

## Capability network

- Are critical dependencies visible?
- Are shared capabilities visible?
- Is the transformation boundary appropriately limited?

## Constraint

- Is the system constraint distinguished from local bottlenecks?
- Is evidence sufficient?
- Is likely Constraint Migration considered?

## Target operating architecture

- Are target roles explicit?
- Are decision rights explicit?
- Are information and knowledge owners explicit?
- Are application boundaries explicit?
- Are AI roles and authority explicit?

## Local optimization

- Are upstream effects considered?
- Are downstream effects considered?
- Are shared-resource effects considered?
- Could a local KPI improve while system Outcome worsens?

## Transition

- Is every Transition State independently operable?
- Are entry and exit conditions explicit?
- Is evidence collected before increasing commitment?
- Is rollback/recovery defined where required?

## Portfolio

- Are dependencies explicit?
- Is transformation WIP bounded?
- Are shared enablers tied to Outcomes?
- Is change saturation considered?
