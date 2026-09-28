# Application Profile Selection

Subordinate to [`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) ([`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md) tier 8), which defines each profile and its "Use when" list. This file only orders the questions. Executed by [`skills/36-select-application-profile/SKILL.md`](skills/36-select-application-profile/SKILL.md).

## 1. Scoreless selection

AITM-SMB does not require a universal numeric score.

Answer §2 and §3 in order. §2 always returns a base profile; each §3 question is evaluated independently of the base and of the other add-ons.

Materiality: [`STANDARD.md`](STANDARD.md) §16.

---

## 2. Base profile

### Does every Compact "Use when" condition ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) §3) hold?

If yes:

```text
Compact
```

Otherwise:

```text
Standard
```

---

## 3. Add-ons

### Does any Governed "Use when" condition ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) §5) hold?

The list includes high AI authority ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) §2) and irreversible actions, not only material customer, financial, legal, security, or data impact.

If yes, add:

```text
Governed
```

### Does the transformation span what the Portfolio "Use when" list ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) §6) describes, such as several Initiatives coordinated across value streams or competing for shared enablers?

If yes, add:

```text
Portfolio
```

### Must realized economic or business value be formally evidenced ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) §7)?

If yes, add:

```text
Measured
```

---

## 4. Default

When uncertain:

```text
Standard + Measured
```

is the preferred default for meaningful SMB transformation.

At Phase 0, answer from what the Outcome owner knows. Where an answer is unknown:

```text
base profile            Standard
Governed condition      treated as holding (STANDARD.md §16), unless the Outcome
                        owner records otherwise in the profile Decision
Measured                add
Portfolio               not added; re-checked at the Phase 1 exit (§6)
```

---

## 5. Recording

The selected profiles, the rationale per question (unknown answers marked as such), and the triggers that would change them are recorded as a Decision (DEC-###, [`artifacts/decision-assumption-log.md`](artifacts/decision-assumption-log.md)) with `status: proposed`. It is approved together with HG-OUTCOME ([`STANDARD.md`](STANDARD.md) §8): the HG-OUTCOME Decision lists it in `subject_ids`, or a separate approved Decision approves it (skill [`skills/01-discover-transformation/SKILL.md`](skills/01-discover-transformation/SKILL.md)).

Until approved, the selection is provisional ([`AGENT_CONTEXT_POLICY.md`](AGENT_CONTEXT_POLICY.md)).

---

## 6. Profile may change

An engagement MAY escalate or de-escalate profiles when new Evidence changes an answer in §2 or §3. It SHOULD re-check them once at the Phase 1 exit, when Capabilities and systems are mapped.

Example:

```text
Compact
→ discovery reveals sensitive data in scope
→ Compact + Governed
```

A change is recorded as a new Decision that supersedes the previous one (§5).
