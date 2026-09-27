<!-- Generated from canon/ by tools/aps.py — edit the canon, not this file. -->

# Regulatory & framework crosswalk

*Standard v4.0.0-rc.1 · as of September 2026.*

Each Definition of Done item produces evidence — a test, a trace, a record, a gate. This page maps that evidence onto the external frameworks teams are asked about: the **EU AI Act**, the **OWASP Top 10 for Agentic Applications**, the **NIST AI RMF**, and Singapore **IMDA**'s Model AI Governance Framework for Agentic AI.

> **This is a crosswalk, not a compliance claim, and not legal advice.** A mapping means *the evidence this item produces supports that obligation or practice* — nothing more. Whether an obligation applies to you depends on your role and risk class; that assessment starts from the regulatory classification record (DoD 31) and ends with your counsel.

## EU AI Act — dates that bind

Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744 of 8 July 2026 (Digital Omnibus on AI; in force 27 July 2026). Consolidated text: [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng); amending act: [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng).

| From | What applies |
|---|---|
| 2025-08-02 | Obligations for general-purpose AI models apply (models placed on the market before that date comply by 2 Aug 2027) |
| 2026-08-02 | Art. 50 transparency obligations apply; Commission enforcement powers over general-purpose AI models begin |
| 2026-12-02 | Art. 50(2) marking of synthetic content applies to systems placed on the market before 2 Aug 2026 (a grace period for that obligation only); prohibition of nudification apps (non-consensual intimate imagery and CSAM) applies |
| 2027-08-02 | Deadline for national AI regulatory sandboxes |
| 2027-12-02 | High-risk obligations apply to Annex III systems (e.g. employment, education, essential services, law enforcement) |
| 2028-08-02 | High-risk obligations apply to Annex I systems (AI in products under EU product-safety legislation, e.g. machinery, toys, lifts) |

*Articles 9–15, 17 and 72–73 are obligations of providers of high-risk AI systems; Article 26 binds deployers of high-risk systems; Article 50 binds certain systems whatever their risk class. For a product that is not high-risk, the mapping shows which evidence would carry over if its classification changed — and which practices the Act treats as the benchmark.*

Date sources: [1](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force) · [2](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) · [3](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/).

## Definition of Done → frameworks

| DoD | Item | EU AI Act | OWASP ASI | NIST AI RMF | IMDA |
|---|---|---|---|---|---|
| 1 | Context budget held | Art. 15 | — | MEASURE 2 | 3 |
| 2 | State externalized | Art. 15 | — | MANAGE 2 | 3 |
| 3 | Compaction tested | Art. 15 | — | MEASURE 2 | 3 |
| 4 | Destructive actions need approval | Art. 14 | ASI02 | MANAGE 2 | 1, 2 |
| 5 | Permissions in code, not prompt | Art. 15 | ASI02, ASI03 | MANAGE 1 | 1, 3 |
| 6 | Sandboxed tool execution | Art. 15 | ASI05 | MANAGE 2 | 3 |
| 7 | Durable pause/resume/retry | Art. 15 | ASI08 | MANAGE 2 | 3 |
| 8 | Schema-validated outputs | Art. 15 | — | MEASURE 2 | 3 |
| 9 | Input/output guardrails | Art. 15 | ASI01, ASI06 | MANAGE 2 | 3 |
| 10 | ≥50 evals per failure mode | Art. 9, Art. 15 | — | MEASURE 1, MEASURE 2 | 3 |
| 11 | Judges calibrated (TPR/TNR) | Art. 15 | — | MEASURE 2, MEASURE 4 | 3 |
| 12 | CI blocks regression; 100% traced | Art. 12, Art. 15, Art. 72 | — | MEASURE 3, MANAGE 4 | 3 |
| 13 | Lethal-trifecta check | Art. 15 | ASI01, ASI02 | MAP 4, MANAGE 1 | 1, 3 |
| 14 | MCP tool defs pinned; allow-listed registry | Art. 15 | ASI04 | GOVERN 6, MANAGE 3 | 3 |
| 15 | Per-run cost ceiling in code | — | — | MANAGE 2 | 1 |
| 16 | Loop License (six gates) | Art. 9, Art. 14, Art. 15 | ASI08, ASI10 | GOVERN 1, MANAGE 1 | 1, 2, 3 |
| 17 | Stop conditions | Art. 14, Art. 15 | ASI08, ASI10 | MANAGE 2 | 1, 3 |
| 18 | Independent verification | Art. 15 | — | MEASURE 2 | 3 |
| 19 | Loop economics | — | — | MEASURE 3 | 1 |
| 20 | Judge calibration (ECE/Brier) | Art. 15 | — | MEASURE 2, MEASURE 4 | 3 |
| 21 | Retrieval metrics | Art. 10, Art. 15 | ASI06 | MEASURE 2 | 3 |
| 22 | Ground-truth provenance | Art. 10 | — | MEASURE 1, MEASURE 4 | 3 |
| 23 | Drift monitoring | Art. 15, Art. 72 | — | MEASURE 3, MANAGE 4 | 3 |
| 24 | No safety gate silenced to pass CI | Art. 9, Art. 17 | — | GOVERN 1, MEASURE 4 | 3 |
| 25 | Graph License | Art. 9, Art. 14, Art. 15 | ASI07, ASI08 | MAP 4, MANAGE 1 | 1, 3 |
| 26 | MCP protocol & auth baseline | Art. 15 | ASI03, ASI04, ASI07 | GOVERN 6, MANAGE 3 | 3 |
| 27 | Per-agent identity | Art. 12, Art. 15 | ASI03 | GOVERN 2, MANAGE 1 | 2, 3 |
| 28 | Inter-agent trust | Art. 15 | ASI03, ASI07 | GOVERN 6, MANAGE 3 | 3 |
| 29 | Telemetry contract | Art. 12, Art. 26 | — | MEASURE 3 | 2, 3 |
| 30 | Success-legitimacy audit | Art. 15, Art. 72 | ASI10 | MEASURE 2, MEASURE 4 | 2, 3 |
| 31 | Regulatory classification record | Art. 6, Art. 26, Art. 50 | — | GOVERN 1, MAP 1, MAP 2 | 1, 4 |
| 32 | Tenant isolation below the LLM | Art. 15 | ASI03, ASI06 | MANAGE 2 | 3 |
| 33 | Human oversight as a program | Art. 14, Art. 26 | ASI09 | GOVERN 2, MANAGE 4 | 2 |

## By framework

### EU AI Act

Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744 of 8 July 2026 (Digital Omnibus on AI; in force 27 July 2026). Source: <https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng>

| Article | Title | DoD items |
|---|---|---|
| Art. 6 | Classification rules for high-risk AI systems | 31 |
| Art. 9 | Risk management system | 10, 16, 24, 25 |
| Art. 10 | Data and data governance | 21, 22 |
| Art. 12 | Record-keeping (automatic logging over the system's lifetime) | 12, 27, 29 |
| Art. 14 | Human oversight (incl. awareness of automation bias; ability to override or stop) | 4, 16, 17, 25, 33 |
| Art. 15 | Accuracy, robustness and cybersecurity | 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 20, 21, 23, 25, 26, 27, 28, 30, 32 |
| Art. 17 | Quality management system | 24 |
| Art. 26 | Obligations of deployers of high-risk AI systems (incl. log retention, competent oversight) | 29, 31, 33 |
| Art. 50 | Transparency obligations for providers and deployers of certain AI systems | 31 |
| Art. 72 | Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems | 12, 23, 30 |
| Art. 73 | Reporting of serious incidents | — *(not covered by the DoD)* |

### OWASP Top 10 for Agentic Applications (2026)

OWASP GenAI Security Project, released 9 December 2025. Source: <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>

| Risk | Title | DoD items |
|---|---|---|
| ASI01 | Agent Goal Hijack | 9, 13 |
| ASI02 | Tool Misuse & Exploitation | 4, 5, 13 |
| ASI03 | Identity & Privilege Abuse | 5, 26, 27, 28, 32 |
| ASI04 | Agentic Supply Chain Vulnerabilities | 14, 26 |
| ASI05 | Unexpected Code Execution (RCE) | 6 |
| ASI06 | Memory & Context Poisoning | 9, 21, 32 |
| ASI07 | Insecure Inter-Agent Communication | 25, 26, 28 |
| ASI08 | Cascading Failures | 7, 16, 17, 25 |
| ASI09 | Human-Agent Trust Exploitation | 33 |
| ASI10 | Rogue Agents | 16, 17, 30 |

### NIST AI Risk Management Framework 1.0

NIST AI 100-1 (26 January 2023) — mapped at category level. Source: <https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf>

*NIST has not published an agent-specific profile of the AI RMF. Its AI Agent Standards Initiative (CAISI, February 2026) and the NCCoE concept paper on software and AI agent identity and authorization (February 2026) are tracked as signals, not mapped.*

| Category | Title | DoD items |
|---|---|---|
| GOVERN 1 | Policies, processes, procedures and practices for AI risk are in place and implemented | 16, 24, 31 |
| GOVERN 2 | Accountability structures empower and train the right people | 27, 33 |
| GOVERN 6 | Third-party software, data and supply-chain risks are addressed | 14, 26, 28 |
| MAP 1 | Context is established and understood | 31 |
| MAP 2 | The AI system is categorized | 31 |
| MAP 4 | Risks and benefits are mapped for all components, including third-party ones | 13, 25 |
| MEASURE 1 | Appropriate methods and metrics are identified and applied | 10, 22 |
| MEASURE 2 | AI systems are evaluated for trustworthy characteristics | 1, 3, 8, 10, 11, 18, 20, 21, 30 |
| MEASURE 3 | Mechanisms track identified AI risks over time | 12, 19, 23, 29 |
| MEASURE 4 | Feedback about the efficacy of measurement is gathered and assessed | 11, 20, 22, 24, 30 |
| MANAGE 1 | AI risks are prioritized, responded to, and managed | 5, 13, 16, 25, 27 |
| MANAGE 2 | Strategies to maximize benefits and minimize negative impacts are planned and documented | 2, 4, 6, 7, 9, 15, 17, 32 |
| MANAGE 3 | Risks and benefits from third-party entities are managed | 14, 26, 28 |
| MANAGE 4 | Risk treatments, response and recovery, and communication plans are documented and monitored | 12, 23, 33 |

### IMDA Model AI Governance Framework for Agentic AI (Singapore)

Launched 22 January 2026; updated 20 May 2026. Source: <https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2026/updated-model-ai-governance-framework-for-agentic-ai>

| Dimension | Title | DoD items |
|---|---|---|
| 1 | Assess and bound the risks upfront | 4, 5, 13, 15, 16, 17, 19, 25, 31 |
| 2 | Make humans meaningfully accountable | 4, 16, 27, 29, 30, 33 |
| 3 | Implement technical controls and processes | 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32 |
| 4 | Enable end-user responsibility | 31 |

## How to use it

- **Answering an assessor:** start from the framework table, follow the DoD numbers, and hand over the evidence those items already produce — the trace, the eval report, the license checklist.
- **Planning a classification change:** if the classification record (DoD 31) moves you into high-risk, the EU AI Act rows show which DoD evidence carries over and where the Act asks for more (e.g. technical documentation and conformity assessment, which this standard does not cover).
- **In CI:** `aps-conformance` tags each SARIF finding with the DoD items and crosswalk entries it touches, so a failing control shows up against the obligation it supports ([docs](docs/conformance.md)).
