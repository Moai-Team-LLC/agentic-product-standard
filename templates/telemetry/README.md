# Telemetry contract checker (DoD 29)

*From [The Agentic Product Standard](../../STANDARD.md), Stack 6. A tripwire, not an observability stack: run it in CI against a trace your agent exported, and it fails when the telemetry contract breaks.*

DoD 29 asks for four things, and [`check_genai_trace.py`](check_genai_trace.py) checks each one on an **OTLP/JSON** trace export (the format the OpenTelemetry Collector's file exporter and most SDK exporters write):

| Check | What it asserts | Flag |
|---|---|---|
| **Structure** | at least one `invoke_agent` span, and every `chat` / `execute_tool` span has an `invoke_agent` ancestor | — |
| **Token usage** | every `chat` span records `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens` | — |
| **No content by default** | none of `gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions`, `gen_ai.tool.definitions` is present | `--allow-content` when a written policy enables capture |
| **Pinned revision** | the resource carries the conventions revision you pin, under an attribute you name, or the export carries a `schemaUrl` | `--revision-attr` (default `aps.semconv.genai.revision`) |
| **Identity on spans** | each `invoke_agent` span carries the agent identity attribute you use (DoD 27) | `--identity-attr` (default `gen_ai.agent.id`) |

```bash
# in CI, after a smoke run that exported traces to trace.json:
python3 check_genai_trace.py trace.json
python3 check_genai_trace.py trace.json --allow-content --revision-attr service.semconv.genai
```

Why these four: the GenAI conventions are still in *Development* status and moved to their own repository (`open-telemetry/semantic-conventions-genai`) at semconv v1.42.0 — so a revision you do not pin is a contract that can change under you; and the conventions themselves make prompt and completion content opt-in, because traces are a data store. Bump the pinned revision only together with a migration test — this checker, run against a trace from the new instrumentation, is that test's floor.

The attribute names follow the conventions as of this release; if the conventions rename one, update the constants at the top of the script in the same change that bumps your pin.
