#!/usr/bin/env python3
"""Check an OTLP/JSON trace export against the telemetry contract (DoD 29). Stdlib only.

    python3 check_genai_trace.py trace.json [--allow-content] [--revision-attr KEY] [--identity-attr KEY]

Exit 0 when the contract holds, 1 with one line per violation otherwise.
"""
import argparse
import json
import sys

OP = "gen_ai.operation.name"
INFERENCE = ("chat", "generate_content", "text_completion")   # model calls: token usage required
USAGE = ("gen_ai.usage.input_tokens", "gen_ai.usage.output_tokens")
CONTENT = ("gen_ai.input.messages", "gen_ai.output.messages",
           "gen_ai.system_instructions", "gen_ai.tool.definitions")


def attrs(obj):
    out = {}
    if not isinstance(obj, dict):
        return out
    for a in obj.get("attributes", []) or []:
        if not isinstance(a, dict):
            continue
        v = a.get("value", {})
        out[a.get("key")] = next(iter(v.values()), None) if isinstance(v, dict) and v else v
    return out


def operation(span):
    op = attrs(span).get(OP)
    if op:
        return op
    return (span.get("name") or "").split(" ")[0]


class NotATrace(ValueError):
    pass


def _list(obj, key, where):
    v = obj.get(key) if isinstance(obj, dict) else None
    if v is None:
        return []
    if not isinstance(v, list):
        raise NotATrace(f"{where}.{key} must be a list")
    return v


def load_spans(doc):
    if not isinstance(doc, dict):
        raise NotATrace("the export must be a JSON object with resourceSpans")
    spans, resources = [], []
    for rs in _list(doc, "resourceSpans", "export"):
        if not isinstance(rs, dict):
            raise NotATrace("each resourceSpans entry must be an object")
        res = attrs(rs.get("resource", {}))
        resources.append((res, rs.get("schemaUrl")))
        for ss in _list(rs, "scopeSpans", "resourceSpans[]"):
            for sp in _list(ss, "spans", "scopeSpans[]"):
                if not isinstance(sp, dict):
                    raise NotATrace("each span must be an object")
                spans.append(sp)
    return spans, resources


def check(doc, allow_content=False, revision_attr="aps.semconv.genai.revision", identity_attr="gen_ai.agent.id"):
    problems = []
    try:
        spans, resources = load_spans(doc)
    except NotATrace as exc:
        return [f"not an OTLP/JSON trace export: {exc}"]
    if not spans:
        return ["no spans in the export"]
    by_id = {s.get("spanId"): s for s in spans}

    def has_agent_ancestor(span):
        seen = set()
        parent = by_id.get(span.get("parentSpanId"))
        while parent is not None and parent.get("spanId") not in seen:
            if operation(parent) == "invoke_agent":
                return True
            seen.add(parent.get("spanId"))
            parent = by_id.get(parent.get("parentSpanId"))
        return False

    agents = [s for s in spans if operation(s) == "invoke_agent"]
    if not agents:
        problems.append("no invoke_agent span — each run needs one top-level agent span")
    for s in agents:
        if not attrs(s).get(identity_attr):
            problems.append(f"invoke_agent span {s.get('spanId')} lacks the identity attribute {identity_attr!r} (DoD 27)")
    for s in spans:
        op = operation(s)
        a = attrs(s)
        if (op in INFERENCE or op == "execute_tool") and not has_agent_ancestor(s):
            problems.append(f"{op} span {s.get('spanId')} has no invoke_agent ancestor")
        if op in INFERENCE:
            missing = [k for k in USAGE if a.get(k) is None]
            if missing:
                problems.append(f"{op} span {s.get('spanId')} is missing token usage: {', '.join(missing)}")
        if not allow_content:
            # content can ride on the span or on its events (gen_ai.client.inference.operation.details)
            carriers = [a] + [attrs(e) for e in (s.get("events") or []) if isinstance(e, dict)]
            leaked = sorted({k for c in carriers for k in CONTENT if k in c})
            if leaked:
                problems.append(f"span {s.get('spanId')} captures content ({', '.join(leaked)}) — off by default; pass --allow-content only under a written policy")
    if not any(res.get(revision_attr) or schema for res, schema in resources):
        problems.append(f"no pinned conventions revision: set resource attribute {revision_attr!r} or export a schemaUrl")
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("trace")
    ap.add_argument("--allow-content", action="store_true")
    ap.add_argument("--revision-attr", default="aps.semconv.genai.revision")
    ap.add_argument("--identity-attr", default="gen_ai.agent.id")
    args = ap.parse_args()
    try:
        doc = json.load(open(args.trace, encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"::error::telemetry contract: cannot read {args.trace}: {exc}")
        return 1
    problems = check(doc, args.allow_content, args.revision_attr, args.identity_attr)
    for p in problems:
        print(f"::error::telemetry contract: {p}")
    if not problems:
        print("telemetry contract holds")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
