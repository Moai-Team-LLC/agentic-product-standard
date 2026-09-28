# ADR-0003 — Stable Identifiers for Human Decision Gates

## Status

Accepted

## Date

2026-09-27

## Context

In 1.0.0, [`STANDARD.md`](../STANDARD.md) §8 listed nine triggers for explicit human approval as unnamed prose lines. [`METHOD_FLOW.md`](../METHOD_FLOW.md) restated the list in different words, and phase files added variants of their own: the Phase 4 file required approval "before an initiative enters the roadmap", where [`STANDARD.md`](../STANDARD.md) said "selecting material Initiatives". Nothing linked an approval to the gate it closed:

- the Decision record had no field for the gate or for the human who approved;
- the agent handoff could report `HUMAN_DECISION_REQUIRED` but not which gate was open;
- skills could not declare which gates their output needed;
- "material" was used in several triggers but defined nowhere, so an agent could argue an item out of a gate;
- "increasing AI authority" left open whether the first grant above L0, or an Authority Ceiling, needed approval.

## Decision

1. [`STANDARD.md`](../STANDARD.md) §8 becomes a table of nine stable identifiers, `HG-OUTCOME` through `HG-VALUE`, one per 1.0.0 trigger. It is the only list; every other normative file references gates by ID and never restates it. Informative summaries (e.g. [`README.md`](../README.md)) MAY list the gate IDs with one-line triggers when they name [`STANDARD.md`](../STANDARD.md) §8 as the binding text.
2. Trigger wording is clarified without changing intent:

   ```text
   1.0.0 wording                                   identifier and clarification
   approving transformation Outcomes               HG-OUTCOME
   selecting material Initiatives                  HG-INITIATIVE
   approving Target Operating Architecture         HG-TOA; in Compact, the Capability Target States
   changing material Decision Rights               HG-DECISION-RIGHTS
   increasing AI authority                         HG-AUTHORITY; granting or increasing, any level
                                                   above L0, including an Authority Ceiling
   accepting material security / legal /          HG-RISK; adds customer and operational risk
     financial risk
   committing material budget                      HG-BUDGET
   promoting a material pilot to rollout           HG-PROMOTION
   declaring value realized                        HG-VALUE; value state REALIZED or SUSTAINED
   ```

3. Rules in [`STANDARD.md`](../STANDARD.md) §8: a gate applies whenever its trigger occurs, in any phase; approval is a Decision ([`artifacts/decision-assumption-log.md`](../artifacts/decision-assumption-log.md)) with `gate:` set and `approved_by:` naming the human; an agent that reaches an open gate stops with `HUMAN_DECISION_REQUIRED` and lists the gate in `open_gates` ([`AGENT_OUTPUT_STANDARD.md`](../AGENT_OUTPUT_STANDARD.md)); reducing AI authority (demotion) never needs a gate.
4. Materiality gets one definition, [`STANDARD.md`](../STANDARD.md) §16: an item is material when being wrong about it could change an approved Outcome or create customer, financial, legal, security, or AI-authority exposure that the accountable Outcome owner would expect to decide personally. The owner MAY record thresholds as a Phase 0 Decision; unclear means material; agents MUST NOT classify an item as immaterial to avoid a gate.
5. Skills declare the gates their output requires in frontmatter (`human_gate`, `gates`; [`skills/INDEX.md`](../skills/INDEX.md) §4). Phase files and [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2 name the gates that typically occur. [`tools/validate.py`](../tools/validate.py) rejects any gate ID not declared in [`STANDARD.md`](../STANDARD.md) §8.

## Consequences

- Approvals are checkable: a validator can confirm that an approved Outcome or Initiative has a Decision closing its gate, signed by a named human.
- Agents report open gates precisely, and humans can see what they are being asked to decide.
- Two gates are worded more broadly. `HG-AUTHORITY` names the first grant above L0 and the Authority Ceiling explicitly. `HG-RISK` adds customer and operational risk (customer impact was already a profile selection dimension, [`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md) §2), so engagements may meet it more often. No [`PUBLIC_API.md`](../PUBLIC_API.md) item changes; the release is MINOR ([`VERSIONING.md`](../VERSIONING.md)).
- Gate IDs now appear in skills, phase files, Initiative `decision_gates`, and engagement records. Renaming or removing one is a material change that needs an ADR and a migration note.
- Demotion stays immediate, so authority can always be reduced faster than it was granted (INV-07).

## Alternatives

- **Keep the prose triggers.** Rejected: they cannot be referenced from records, handoffs, or frontmatter, and restatements drift.
- **Numbered gates (HG-1 to HG-9).** Rejected: numbers carry no meaning in a Decision record, and suggest a sequence, whereas gates are trigger-based and can occur in any phase.
- **Merge human gates into the Execution Gates A–G.** Rejected: Execution Gates are evidence checkpoints on an Initiative, required only under the Governed profile ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md)); human gates are approvals required in every profile. An Execution Gate names the human gates it needs instead.
