---
name: eval-driven-dev
description: Build the evaluation discipline that separates production agentic products from demos — error analysis on real traces, the three-level eval pyramid (code assertions / LLM-as-judge / human review), binary judge outputs calibrated against human labels, and CI gates that block regression. Based on the Husain/Shankar methodology. Use whenever the user mentions evals, evaluation, LLM-as-judge, hallucination testing, regression testing for AI, quality measurement, error analysis, "how do I know if my agent works," failure modes, or grading agent outputs.
---

# Eval-Driven Development

Evaluation is the most critical and most under-invested practice in building agentic products. Hamel Husain and Shreya Shankar have codified the discipline; following it separates teams that ship from teams that demo.

The core insight from Husain's "Field Guide to Rapidly Improving AI Products" (after helping 30+ AI products): **the teams who succeed barely talk about tools. They obsess over measurement and iteration.**

## First principle: error analysis before infrastructure

Most teams reach for eval infrastructure (Braintrust, LangSmith, etc.) before they know what to measure. This is backwards.

**Start by reading production traces.** Read 20–50 real outputs manually after each meaningful change. Write down what went wrong in plain language. Cluster the failure modes into 5–10 named buckets. These named buckets are your eval categories — generic "helpfulness" never catches them.

Common failure mode buckets (yours will be different and product-specific):

- "Missed human handoff" (agent should have escalated, didn't)
- "Wrong tool selection" (chose web_search when should have used internal docs)
- "Stale information" (used cached/old data when fresh was required)
- "Lost context across compaction" (forgot user's earlier constraint)
- "Hallucinated citation" (made up a source URL)

Each named failure mode becomes an eval. Generic evals do not.

## The three-level eval pyramid

```
       ▲
      ╱ ╲     Level 3: Human Review
     ╱   ╲    Major changes, ~20-50 traces
    ╱─────╲   Subjective judgment, edge cases
   ╱       ╲
  ╱  L 2:   ╲   Level 2: LLM-as-Judge
 ╱  LLM Judge╲  Cadence, calibrated, binary output
╱─────────────╲
╲             ╱  Level 1: Code Assertions
 ╲   L 1:    ╱   Every change, cheap, mechanical
  ╲ Asserts ╱
   ╲───────╱
```

Build bottom-up. Each level catches what the level below can't, but costs more.

### Level 1: Code assertions

The fastest, cheapest, most reliable evals. Things you can check with code:

- Structured output validates against schema
- Required fields present
- Citations are valid URLs / IDs
- Tool sequence respects preconditions
- Output length within bounds
- No PII in response
- Response in expected language
- Numeric outputs within sensible ranges

**Rule:** if you can check it with code, never use an LLM judge. Code is faster, cheaper, deterministic.

These run on every PR. They block merge on regression.

### Level 2: LLM-as-judge

For failure modes that need judgment but are too expensive for human review on every run.

**Rules of LLM-as-judge:**

1. **Binary outputs only.** True/false. Pass/fail. Likert scales (1–5) fail to align with human raters and create constant noise.

2. **Focused criteria per judge.** One judge checks "is the handoff handled correctly?" — not "is this response good?" Vague judges produce useless scores.

3. **Calibration against human labels.** This is the step most teams skip and pay for. The discipline:
   - Get 100+ human-labeled examples for each judge
   - Run the judge against the same examples
   - Measure TPR (true positive rate) and TNR (true negative rate)
   - Iterate the judge prompt until both > 80%
   - Report TPR/TNR with every release

   Without calibration, you don't know if a 0.8 score means your product is good or your judge is broken.

4. **The judge model can be cheaper than the product model.** Often a small model with a focused prompt outperforms a big model with a vague one. Test.

5. **Version the judge prompt.** Treat it as code. Diff reviews. If the judge prompt changes, all historical scores are invalidated.

6. **The judge is decorrelated from the writer.** Self-check by the model that produced the work does not count as verification — it shares its own blind spots. Use a different model or a materially different prompt/context, and let it see the *artifact*, not the writer's reasoning. For unattended (L3+) loops this is mandatory — see the Loop License and the "Writer / Checker, done right" pattern in `STANDARD.md` Part IV.

### Level 3: Human review

The ultimate authority, but expensive. Reserve for:

- Major product changes (new feature, model upgrade)
- Investigating disagreements between LLM judges
- Building calibration data for judges
- Subjective qualities that resist automation (tone, style fit)
- Edge cases the judges flag as uncertain

**Pattern:** sample 20–50 production traces weekly, review with the team, update the eval set with new failure modes discovered.

## The eval set as a living artifact

The eval set is not built once. It grows from production failures.

The discipline:

1. Each new failure mode discovered in production becomes a permanent test case
2. Test cases are versioned in git alongside the agent code
3. Coverage increases monotonically over time
4. Regression on any existing case blocks deploy
5. Periodically prune cases that all configurations pass trivially (non-discriminating)

A healthy eval set has 100–500 cases organized by failure mode, with new cases added weekly from production.

## CI / CD integration

Evals are useless if they don't block bad deploys.

> **Reference implementation (paved road):** **[AgenticPerformance (APL)](https://github.com/Moai-Team-LLC/AgenticPerformance)** — the family's Evals & observability surface — ships golden-set evals with a CI regression gate, an error taxonomy, and a governed improvement loop over OpenTelemetry, engine-agnostic. Set it up via the [`reference-stack`](../reference-stack/SKILL.md) skill, or bring your own (LangSmith / Langfuse / Braintrust / Phoenix). The standard stays neutral — this is the recommended default, not a requirement.

Minimum CI pipeline:

```
PR opened
  ↓
Run Level 1 (code assertions) on full eval set — fast, ~minutes
  ↓ pass
Run Level 2 (LLM judges) on full eval set — slower, ~tens of minutes
  ↓ pass
Compute aggregate scores vs main branch
  ↓ no regression
Approve merge
```

Block on:

- Any new failure mode added to eval set must pass on the PR introducing it
- No regression on any existing case
- Aggregate pass rate must not drop more than 2% vs main

Document explicitly when regression is accepted (e.g., model upgrade trades latency for quality on some cases).

## The "vibe check" trap

Teams that don't have evals fall back on "vibe check" — engineers manually try a few prompts after each change and feel whether it's better.

This fails predictably:
- Engineers test the cases they remember, not the failure modes
- Improvements in one area mask regressions elsewhere
- Subjective consensus drifts; "better" becomes meaningless over time
- Onboarding new engineers loses all institutional memory

If the team is operating on vibe check, the highest-ROI action is not a better model — it's building Level 1 assertions on the top 10 failure modes.

## Eval failure modes (meta-evals)

Common ways eval systems themselves fail:

| Symptom | Cause | Fix |
|---|---|---|
| Eval scores high, users complain | Eval cases don't reflect real use | Sample from production traces, not your imagination |
| Eval scores volatile | Non-discriminating cases, LLM judge noise | Prune cases all configurations pass; calibrate judges |
| Eval suite slow, devs skip it | Too many redundant cases or expensive judges | Tiered runs: fast subset on every PR, full suite nightly |
| Judges disagree with team | Judges not calibrated; or team disagrees with itself | Calibrate against human-labeled set; surface disagreements |
| Old eval cases keep "passing" but quality drops | Failure mode evolved, cases didn't | Refresh cases quarterly; tag with date introduced |

## Cost of evals

Yes, running evals costs money. Reference figures (mid-2026):

- Level 1 (code) — essentially free
- Level 2 (LLM judges) — typically 1–3× the cost of one production inference per case
- Level 3 (human) — labor cost dominates; budget for it

Total eval spend in a healthy team is 5–15% of production inference spend. If it's < 1%, you're under-investing; if it's > 30%, you're over-investing or running judges too aggressively.

## The compound advantage

Eval discipline compounds. Teams with mature evals:

- Ship more frequently (less fear of regression)
- Make better model swaps (objective comparison)
- Onboard engineers faster (failures are documented, not tribal knowledge)
- Recover from bad deploys faster (regression caught in CI)

The teams that ship great agentic products are the ones that started building evals before they built features.

## Reading list (when the user asks where to learn this)

- Hamel Husain — "Your AI Product Needs Evals"
- Hamel Husain — "A Field Guide to Rapidly Improving AI Products"
- Hamel Husain — "LLM Evals: Everything You Need to Know"
- Husain & Shankar — AI Evals for Engineers & PMs (Maven course)
- Shreya Shankar — "Who Validates the Validators?"
- Eugene Yan — "Patterns for Building LLM-based Systems & Products" (the evals section)

## Output of this skill

When the conversation completes, the user should have:

1. A list of 5–10 named failure modes for their product (from real or anticipated traces)
2. Level 1 code assertions for each failure mode that admits one
3. Level 2 LLM-as-judge prompt for each subjective failure mode, with a calibration plan
4. An eval set seeded with 20–50 cases, organized by failure mode
5. A CI plan: what runs on every PR, what runs nightly, what blocks merge
6. A weekly cadence for trace review and eval set growth
