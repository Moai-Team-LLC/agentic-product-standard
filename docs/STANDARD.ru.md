# The Agentic Product Standard v1.0
*Канонический стандарт построения современных agentic-продуктов*

---

## Философия стандарта

**Agentic-продукт — это не "продукт с ИИ". Это продукт, где часть процесса дина­мически направляется LLM в рамках детерминированной архитектуры с явными границами доверия.**

Стандарт построен на пяти принципах, которые независимо сошлись в production-практиках Anthropic, OpenAI, Cognition, Sierra, LangChain в 2024–2026:

1. **Детерминизм по умолчанию, агентность по необходимости** — каждая степень автономии должна быть заработана, не выдана авансом.
2. **Архитектура важнее фреймворка** — паттерны переживают библиотеки.
3. **Harness > модель** — 98% надёжности живёт в коде вокруг LLM, а не в самой LLM.
4. **Context engineering — основная инженерная дисциплина** — то, что попадает в окно контекста, определяет всё.
5. **Eval-driven development обязателен** — без измерения нет улучшения; без trace-обзора нет понимания.

---

## Часть I. Архитектурный канон

### Канон 1. Лестница автономии (Autonomy Ladder)

Любой agentic-продукт строится поэтапно по этой лестнице. **Подниматься на следующий уровень — только когда предыдущий доказал value на eval'ах.**

| Уровень | Описание | Когда использовать |
|---|---|---|
| **L0. Single LLM call** | Один промпт, один ответ | Классификация, экстракция, суммаризация |
| **L1. Augmented LLM** | + retrieval, + tools, + memory | Q&A над документами, простые ассистенты |
| **L2. Workflow** | Детерминированный код оркестрирует LLM-шаги | Известный путь выполнения; нужна предсказуемость |
| **L3. Orchestrator-Worker** | LLM динамически декомпозирует, но граф ограничен | Параллелизуемые задачи (research, breadth-first) |
| **L4. Autonomous Agent Loop** | LLM сама выбирает следующий шаг до termination | Путь невозможно перечислить; терпимы стоимость и компаундирующиеся ошибки |

**Правило перехода:** не поднимайся на L+1, пока L не даёт ≥90% pass rate на curated eval set.

### Канон 2. Пять композиционных паттернов

Это словарь индустрии. Любой agentic-продукт собирается из них как из Lego:

1. **Prompt Chaining** — последовательная декомпозиция (outline → draft → polish)
2. **Routing** — классификатор + диспетчер к специалисту
3. **Parallelization** — fan-out независимых подзадач + агрегация
4. **Orchestrator-Workers** — центральный планировщик + динамические воркеры
5. **Evaluator-Optimizer** — generator + critic в цикле до acceptance

**Метапринцип:** сначала пытайся решить задачу композицией этих паттернов на детерминированном коде. Полноценный agent loop — последнее средство.

### Канон 3. Single vs Multi-Agent — разрешённый вопрос

| Тип задачи | Архитектура | Почему |
|---|---|---|
| **Breadth-first, параллелизуемая** (research, exploration, multi-source synthesis) | Multi-agent (orchestrator + isolated sub-agents) | Изолированные context-windows; параллелизм; ~90% lift у Anthropic |
| **Depth-first, когерентная** (coding, long-form writing, stateful editing) | Single-agent | Shared context критичен; sub-agents создают "telephone game" |

**Sub-agents возвращают синтез, не транскрипт.** Никогда не пробрасывай raw output sub-agent'а в parent.

### Канон 4. Harness Architecture

Harness — всё, что окружает LLM-цикл. **В production-агенте harness — это 98% кода.** Минимальный harness содержит семь слоёв:

```
┌─────────────────────────────────────────────┐
│  7. Observability & Tracing                 │ ← логируется ВСЁ
├─────────────────────────────────────────────┤
│  6. Evaluation Layer (CI gates)             │ ← блокирует регрессии
├─────────────────────────────────────────────┤
│  5. Human-in-the-Loop (notify/ask/review)   │ ← approval gates
├─────────────────────────────────────────────┤
│  4. Guardrails (input/output validation)    │ ← defense in depth
├─────────────────────────────────────────────┤
│  3. Durable Execution (Workflow + Activity) │ ← pause/resume/retry
├─────────────────────────────────────────────┤
│  2. Context & Memory Management             │ ← write/select/compress/isolate
├─────────────────────────────────────────────┤
│  1. Agent Loop (gather → act → verify)      │ ← собственно "агент"
└─────────────────────────────────────────────┘
              ↕ MCP / function calling
       ┌──────────────────────────┐
       │   Tools & Resources      │
       └──────────────────────────┘
```

### Канон 5. Cycle of Trust

Каждое действие агента проходит через явную проверку доверия:

```
gather context → propose action → check permissions → 
verify preconditions → execute → verify outcome → 
log trace → update memory
```

**Никогда не позволяй модели обходить permission boundary.** Permissions enforced кодом, не промптом. Replit-инцидент 2025 года (агент стёр БД 1,200+ компаний, проигнорировав "code freeze" в промпте) — каноническое доказательство этого принципа.

---

## Часть II. Технологический стек

### Layer 1: Модель и provider

- **Multi-provider от старта.** Завязка на один model API — стратегическая ошибка. Используй фреймворк или абстракцию (Pydantic AI поддерживает 25+ providers; LangGraph model-agnostic).
- **Tiered routing.** Маленькая модель для routing/classification, флагман — для reasoning. Per-agent model assignment.
- **Prompt caching обязательно** для стабильных частей (system prompt, tool schemas).

### Layer 2: Tool integration — **MCP по умолчанию**

- **MCP (Model Context Protocol)** — стандарт agent ↔ tool. К началу 2026: 10,000+ серверов, 177,000+ инструментов.
- **A2A (Agent2Agent)** — стандарт agent ↔ agent (Google → Linux Foundation).
- **Не пиши кастомные интеграции** там, где есть MCP-сервер. Не пиши tool-only код там, где tool должен быть переиспользуем — оберни в MCP.

**Правила дизайна инструментов:**
- <20 активных инструментов на агента (выше — RAG-MCP для подбора relevant subset, +3.2× accuracy на правильный выбор инструмента)
- Названия и описания tool'ов проектируются как промпты
- Структурированные выходы по умолчанию (Pydantic-validated)
- Форматы из training distribution: Markdown diffs, JSON, NL — не кастомные DSL

### Layer 3: Context engineering — четыре операции

| Операция | Когда применять | Реализация |
|---|---|---|
| **Write** | Состояние, которое нужно сохранить | Scratchpad, файлы (CLAUDE.md, AGENTS.md), memory store |
| **Select** | Релевантный контекст под текущий шаг | RAG для документов, RAG для tool descriptions, RAG для memory |
| **Compress** | Длинная история диалога | Многослойная компакция (drop low-value → summarize) |
| **Isolate** | Под-задачи с независимыми контекстами | Sub-agents с собственными windows |

**Правило 40%:** держи использование context window ниже 40% лимита. Деградация после — нелинейная.

### Layer 4: Memory

Выбор по доминирующему требованию:

| Vendor | Сила | Когда выбирать |
|---|---|---|
| **Mem0** | General-purpose, самый большой community | Default; персонализация |
| **Zep** | Temporal knowledge graph; SOC2/HIPAA | Эволюционирующие факты (finance, healthcare) |
| **Letta (MemGPT)** | Tiered self-editing memory | Long-horizon агенты (500+ interactions) |
| **LangMem** | LangChain-native | Уже на LangGraph |
| **Files in repo** | Версионный markdown | Когда memory должна быть human-editable |

### Layer 5: Durable execution — **обязательно**

Stateless агенты теряют всё при крэше. Минимальный стандарт:

- **Agent loop** = Workflow (deterministic, replayable from event log)
- **LLM calls и tool invocations** = Activities (non-deterministic, retryable)
- **State** = первоклассный объект; агент должен быть pure function (state, event) → new_state

Варианты:
- **Temporal** — индустриальный стандарт; first-party интеграции с OpenAI SDK, Pydantic AI, mcp-agent
- **Inngest / Restate** — простее операционно; для TypeScript-команд
- **LangGraph checkpointer** (Postgres) — встроенно, если уже на LangGraph

### Layer 6: Observability & Evals

**Не стартуй продакшен без observability.** Минимальный набор:

| Tool | Когда выбирать |
|---|---|
| **LangSmith** | Глубокая интеграция с LangGraph |
| **Langfuse** | OSS / self-hosted; вендор-нейтральный |
| **Braintrust** | Eval-driven CI/CD блокировка деплоев |
| **Arize Phoenix** | OpenTelemetry-native, ML monitoring lineage |

**Инструментируй через OpenInference / OpenLLMetry** — потом можно менять vendor без переинструментации.

### Layer 7: Framework selection

Решающий фактор — **доминирующий constraint**, не хайп:

| Constraint | Framework |
|---|---|
| Максимум контроля, complex stateful workflows, multi-vendor | **LangGraph** |
| Anthropic-native, especially coding/computer-use | **Claude Agent SDK** |
| OpenAI-native, опинионированный SDK | **OpenAI Agents SDK** |
| Multi-agent с явными ролями, fastest prototype | **CrewAI** |
| Type-safety, FastAPI ergonomics, structured outputs | **Pydantic AI** |
| Document-heavy, RAG в основе | **LlamaIndex Workflows** |
| TypeScript full-stack | **Mastra** |
| Programmatic prompt optimization | **DSPy** |
| MCP-native + Temporal | **mcp-agent (lastmile-ai)** |

**Совет Anthropic, который стоит миллион долларов:** *"Start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code."*

---

## Часть III. Production readiness — Definition of Done

Agentic-продукт **не готов к продакшену**, пока не выполнены все 12 пунктов:

### Контекст и состояние
- [ ] **1.** Context utilization < 40% в типичном цикле
- [ ] **2.** Состояние externalized (не живёт только в context window)
- [ ] **3.** Compaction pipeline протестирован на long-running сценариях

### Tools и permissions
- [ ] **4.** Все destructive actions требуют explicit human approval
- [ ] **5.** Permissions enforced кодом, не промптом
- [ ] **6.** Tool execution в sandbox (containers / OAuth scopes / least privilege)

### Reliability
- [ ] **7.** Durable execution: pause/resume/retry работает на убитый процесс
- [ ] **8.** Structured outputs валидируются schema'ой; assertions на критическом пути
- [ ] **9.** Guardrails (минимум: PII, jailbreak, schema validation) на input и output

### Evals и observability
- [ ] **10.** Eval set ≥50 примеров на каждый top-priority failure mode
- [ ] **11.** LLM-judges откалиброваны против human labels (TPR/TNR трекаются)
- [ ] **12.** CI блокирует деплой при регрессии evals; 100% production traces логируются

---

## Часть IV. Eval Discipline (по Husain/Shankar)

Эта дисциплина — критичнее выбора фреймворка.

### Three-Level Eval Pyramid

```
       ▲
      ╱ ╲     Level 3: Human Review
     ╱   ╲    (на major changes, ~20-50 traces)
    ╱─────╲
   ╱       ╲   Level 2: LLM-as-Judge
  ╱         ╲  (на cadence, бинарный вывод, calibrated)
 ╱───────────╲
╱             ╲ Level 1: Code Assertions
─────────────── (на каждый change, дёшево)
```

### Eval Rules

1. **Error analysis first.** Прочитай 20–50 production traces вручную перед тем, как строить инфраструктуру.
2. **Binary outputs.** LLM-judge всегда возвращает true/false. Likert-шкалы ломают alignment.
3. **Calibrate every judge.** Минимум 100 human-labeled примеров на judge; TPR/TNR в каждом релизе.
4. **Product-specific evals.** Generic "helpfulness" не ловит реальные failures. Eval'ы строятся вокруг наблюдённых failure modes ("missed human handoff", "wrong tool selection").
5. **Eval set растёт от production.** Каждый новый failure mode становится permanent regression test.

---

## Часть V. Канон от лидеров мнений

Минимальный reading list. **Эти источники — не справочники, это операционная база:**

### Must-read (последовательно)
1. **Anthropic — "Building Effective Agents"** (Schluntz & Zhang, Dec 2024) — словарь паттернов
2. **OpenAI — "A Practical Guide to Building Agents"** (PDF, 2025) — production-ориентированный взгляд
3. **HumanLayer — "12 Factor Agents"** (Dex Horthy) — самая прескриптивная практическая методология
4. **Anthropic — "How we built our multi-agent research system"** (Hadfield, Zhang et al.) — multi-agent case study
5. **Cognition — "Don't Build Multi-Agents"** (Walden Yan, June 2025) — оппозиционный взгляд
6. **LangChain — "Context Engineering for Agents"** (Lance Martin) — write/select/compress/isolate
7. **Hamel Husain — "A Field Guide to Rapidly Improving AI Products"** + "Your AI Product Needs Evals" — eval discipline
8. **Anthropic — "Building agents with the Claude Agent SDK"** (Sept 2025) — гайд по harness design

### Reference exemplars для изучения архитектуры
- **Claude Code** — harness design, 5-layer compaction, 7-mode permissions (arXiv:2604.14228)
- **Cognition Devin** — single-threaded coding agent, RPI framework
- **Anthropic Research feature** — orchestrator-worker с отдельным citation pass
- **OpenAI Codex Harness** — agent self-validation, progressive disclosure через docs/
- **Sierra** — Agent Development Life Cycle, multi-model constellation, outcome-based pricing

### Lead voices думающих практиков
- **Harrison Chase** (LangChain) — ambient agents, agent inbox
- **Hamel Husain** (Parlance Labs) — eval methodology
- **Dex Horthy** (HumanLayer) — 12 Factor Agents, harness engineering
- **Andrew Ng** (DeepLearning.AI) — four agentic design patterns
- **Andrej Karpathy** — context engineering, LLM-as-OS framing
- **Simon Willison** — практическая база по LLM tooling
- **Omar Khattab** — DSPy, programmatic prompt optimization
- **Eugene Yan** — patterns for LLM systems & products
- **Bret Taylor** (Sierra) — enterprise agentic operations

---

## Часть VI. Roadmap построения (12 недель)

### Phase 1 — Prove value (weeks 0–2)
- Напиши workflow как deterministic pipeline
- Найди **одну** точку, где LLM обязателен
- Используй raw model SDK; никакого фреймворка
- Curated eval set 20–50 примеров **до** написания кода
- Перечисли failure modes, которые потеряют trust — это твои первые assertions

**Gate to Phase 2:** ≥90% pass rate на eval set

### Phase 2 — Structure & routing (weeks 2–6)
- Выбери framework по доминирующему constraint
- Observability подключи в день первой строки кода
- Routing + structured outputs + guardrail layer
- 100% production traffic traced
- 30 минут в неделю на ручной review traces

**Gate to Phase 3:** router диспетчит >1 specialist; 3 top failure modes идентифицированы из traces

### Phase 3 — Harden for production (weeks 6–12)
- Durable execution **до** первого long-running агента в продакшене
- Human-in-the-loop для любого действия с blast radius
- LLM-as-judge для top-3 subjective failure modes (calibrated)
- CI gates на eval регрессии
- Memory layer (если sessions перерастают conversation)
- MCP для не-проприетарных интеграций

**Gate to Phase 4 (multi-agent):** single-agent доказательно упирается в (а) context exhaustion, (б) breadth-first parallelism, и под-задачи **по-настоящему** независимы.

### Phase 4 — Optimize (ongoing)
- Audit context utilization
- Tiered model routing
- Eval set расширяется от каждого нового production failure
- Harness — твой durable advantage; инвестируй сюда, не в model swap

---

## Часть VII. Антипаттерны

**Не делай этого:**

1. **Multi-agent до single-agent baseline.** Сначала докажи value на одном агенте.
2. **Framework abstractions до понимания raw API.** Иначе debug превращается в reverse engineering чужого кода.
3. **LLM-judges без калибровки на human labels.** Метрика без trust value — не метрика.
4. **Permissions через prompt.** Модель проигнорирует. Enforced только кодом.
5. **Memory как afterthought.** Externalization state — архитектурное решение, ретрофит болезненный.
6. **Generic evals ("helpfulness", "correctness").** Не ловят product-specific failures.
7. **Likert-шкалы в LLM-judge.** Бинарные выходы — единственное, что калибруется.
8. **Tool count >100.** Модель путается. Используй RAG-MCP или routing.
9. **Один agent для breadth + depth.** Specialize: один тип агента — один тип задачи.
10. **Деплой без trace-monitoring.** Большинство failures — routing/tool-selection, видны только в traces.
11. **Hardcoded prompts без version control.** Промпты — это код.
12. **Доверие к single vendor benchmarks.** 90.2% lift от Anthropic, Letta 500+ interactions — directionally correct, не absolute truth.

---

## Часть VIII. Compact Decision Checklist

Перед началом каждого agentic-проекта прогон по чек-листу:

```
□ Какой уровень лестницы автономии минимально достаточен? (L0–L4)
□ Можно ли решить композицией 5 паттернов без полноценного loop?
□ Breadth-first или depth-first? (определяет single vs multi)
□ Какие 3 failure modes потеряют trust первыми?
□ Где permission boundaries? (что НЕ может агент?)
□ Какой constraint доминирует при выборе framework?
□ Где живёт state? (in-context — anti-pattern для long-running)
□ Кто validates? (assertion / LLM judge / human review — для какого слоя?)
□ Trace storage и retention — где, как долго?
□ Eval set: сколько примеров, кто labels, как растёт?
```

---

## Закрытие

Стандарт — не догма. Это **наклон поля** в сторону практик, которые в 2024–2026 годах независимо сходились в Anthropic, OpenAI, Cognition, Sierra, LangChain и у ведущих практиков.

**Главное правило стандарта:**

> *"Архитектура — это то, что остаётся, когда модель улучшается. Модель — переменная, harness — константа. Инвестируй пропорционально."*

---

*v1.0 · собрано на основе production-практик мая 2026*
