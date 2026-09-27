#!/usr/bin/env python3
"""Check an OTLP/JSON trace export against the telemetry contract (DoD 29). Stdlib only.

    python3 check_genai_trace.py trace.json [--allow-content] [--revision-attr KEY] [--identity-attr KEY]

Exit 0 when the contract holds, 1 with one line per violation otherwise.
"""
import argparse
import json
import sys

OP = "gen_ai.operation.name"
USAGE = ("gen_ai.usage.input_tokens", "gen_ai.usage.output_tokens")
CONTENT = ("gen_ai.input.messages", "gen_ai.output.messages",
           "gen_ai.system_instructions", "gen_ai.tool.definitions")


def attrs(obj):
    out = {}
    for a in obj.get("attributes", []) or []:
        v = a.get("value", {})
        out[a.get("key")] = next(iter(v.values()), None) if isinstance(v, dict) and v else v
    return out


def operation(span):
    op = attrs(span).get(OP)
    if op:
        return op
    return (span.get("name") or "").split(" ")[0]


def load_spans(doc):
    spans, resources = [], []
    for rs in doc.get("resourceSpans", []):
        res = attrs(rs.get("resource", {}))
        resources.append((res, rs.get("schemaUrl")))
        for ss in rs.get("scopeSpans", []):
            for sp in ss.get("spans", []):
                spans.append(sp)
    return spans, resources


def check(doc, allow_content=False, revision_attr="aps.semconv.genai.revision", identity_attr="gen_ai.agent.id"):
    problems = []
    spans, resources = load_spans(doc)
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
        if op in ("chat", "execute_tool") and not has_agent_ancestor(s):
            problems.append(f"{op} span {s.get('spanId')} has no invoke_agent ancestor")
        if op == "chat":
            missing = [k for k in USAGE if a.get(k) is None]
            if missing:
                problems.append(f"chat span {s.get('spanId')} is missing token usage: {', '.join(missing)}")
        if not allow_content:
            leaked = [k for k in CONTENT if k in a]
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
    doc = json.load(open(args.trace, encoding="utf-8"))
    problems = check(doc, args.allow_content, args.revision_attr, args.identity_attr)
    for p in problems:
        print(f"::error::telemetry contract: {p}")
    if not problems:
        print("telemetry contract holds")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
