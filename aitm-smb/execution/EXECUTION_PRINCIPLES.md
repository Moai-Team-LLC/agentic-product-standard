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

---

## 2. Vertical transformation slice

The preferred unit of implementation is a **Vertical Transformation Slice**.

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
