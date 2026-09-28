# Target State Design Method

## 1. Purpose

Target State Design defines how the transformed capability should behave: its Capability Target State, a State of type TARGET (`CORE_MODEL.md` §3, §12). Record contract: `artifacts/capability-target-state.md`.

It is not a system diagram first.

The design order is:

```text
Outcome
→ Capability behavior
→ Decision model
→ Human / AI roles
→ Process / workflow
→ Information / knowledge
→ Application behavior
→ Automation / AI
→ Platform
→ Governance
```

---

## 2. Target capability statement

Every target capability SHOULD have a short statement (record field `statement`):

```text
The organization can <perform ability>
at <required quality/speed/cost>
under <constraints>
without <current structural limitation>.
```

Example pattern:

```text
The organization can qualify routine inbound demand
within 15 minutes,
using current commercial rules and customer context,
without requiring founder review.
```

---

## 3. Design dimensions

### People
What human expertise remains essential?

### Decisions
Which decisions exist in the target state?
Who or what makes them?

### Process
What work disappears?
What work changes?
What new work appears?

### Data
What structured facts are required?

### Knowledge
What contextual expertise must be accessible?

### Applications
What systems remain systems of record?
What interfaces are required?

### Automation
What deterministic work should execute automatically?

### AI
Where is probabilistic intelligence justified?

### Controls
What actions are constrained?

### Metrics
How is capability performance measured?

---

## 4. Human-AI system patterns

Common patterns:

### Human with AI

```text
Human
↔ AI
```

AI assists; human retains control.

### AI inside workflow

```text
Trigger
→ deterministic workflow
→ AI step
→ deterministic validation
→ action
```

### AI with approval

```text
AI proposes
→ Human approves
→ system executes
```

### Bounded agent

```text
Goal
→ Agent
→ Tools
→ Policy
→ Evaluation
→ Escalation
```

### Multi-agent

Use only when distinct bounded responsibilities justify additional coordination complexity.

A pattern does not set authority. Authority is the autonomy level per action class (`diagnostics/AUTONOMY_SUITABILITY.md` §2), bounded by the approved Authority Ceiling.

---

## 5. Design rule

Do not preserve current process steps merely because they exist.

Ask:

```text
If this capability were designed today
with current technology and constraints,
what would the simplest reliable system look like?
```

---

## 6. Target-state completeness

A Target State is incomplete unless it defines:

```text
linked Outcomes
diagnosed Gaps it closes
desired behavior
ownership
decision rights
required information
required knowledge
system boundaries
AI role
AI authority
controls
metrics
```

The Validation of `artifacts/capability-target-state.md` applies this list.
