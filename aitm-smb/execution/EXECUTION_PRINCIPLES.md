# AITM-SMB Execution Principles

## 1. Purpose

AITM-SMB does not treat implementation as a separate activity after architecture.

Execution is part of the transformation method.

The core execution loop is:

```text
Hypothesis
→ Bounded Change
→ Evidence
→ Decision
→ Scale / Revise / Stop
```

Decision vocabularies used in the loop: pilot result [`execution/PILOT_MODEL.md`](PILOT_MODEL.md) §6; evaluation conclusion [`evaluation/EVALUATION_SYSTEM.md`](../evaluation/EVALUATION_SYSTEM.md) §5; value conclusion [`measurement/VALUE_REALIZATION.md`](../measurement/VALUE_REALIZATION.md) §6.

---

## 2. Vertical transformation slice

The preferred unit of implementation is a vertical **Transformation Slice** (`SLC-###`; record: [`execution/DELIVERY_SLICE.md`](DELIVERY_SLICE.md)).

A valid slice crosses the layers required to change one bounded business behavior.

It may include:

```text
process
role
decision right
data
knowledge
application
automation
AI
control
metric
```

A slice SHOULD NOT be defined only as:

```text
"build API"
"create agent"
"add vector database"
"integrate model"
```

unless that technical work is itself a prerequisite with an explicit linked Initiative.

---

## 3. Evidence before scale

AITM-SMB prefers:

```text
small scope
→ real evidence
→ wider scope
```

over:

```text
large build
→ late validation
```

---

## 4. Execution states

A transformation Initiative MAY progress through:

```text
DESIGNED
READY_FOR_PILOT
PILOTING
EVALUATING
APPROVED_FOR_ROLLOUT
ROLLING_OUT
OPERATING
REVISING
STOPPED
```

State changes SHOULD have explicit gates.

These states refine the Initiative `status` ([`CORE_MODEL.md`](../CORE_MODEL.md) §7) between approval and completion. They are read from the Initiative's gates and need no separate field. Typical gates ([`execution/EXECUTION_GATE_MODEL.md`](EXECUTION_GATE_MODEL.md) §2):

```text
DESIGNED              → READY_FOR_PILOT        Gate C
EVALUATING            → APPROVED_FOR_ROLLOUT   Gate D (HG-PROMOTION for a material pilot)
APPROVED_FOR_ROLLOUT  → ROLLING_OUT            Gate E, before each stage
ROLLING_OUT           → OPERATING              Gate F
```

---

## 5. Technical completion is not transformation completion

A feature being deployed does not mean the capability has transformed.

Transformation completion requires:

```text
operational adoption
AND
business behavior changed
AND
controls operate
AND
metrics are observable
AND
effect is measured
```

---

## 6. Stop rule

AITM-SMB allows and expects initiatives to stop.

A pilot SHOULD stop when:

```text
expected effect is absent
risk exceeds acceptable bounds
economics fail
required evidence cannot be produced
organizational adoption fails
or a better intervention is identified
```

Stopping is not failure when it prevents scaling a bad design.
