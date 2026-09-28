#!/usr/bin/env python3
"""Reference safe-output applier (Loop License gate 3 — declared blast radius).

Reads the agent's typed action requests (JSON Lines), validates each against the closed
schema and the policy, and — only with --apply — executes the accepted ones through one
handler per action type. Dry run is the default. Stdlib only.

    python3 apply_safe_outputs.py safe-outputs.jsonl --policy policy.json [--apply]

Exit code: 0 when every request was accepted, 1 when any was rejected (rejections are
escalations — route them to a human, never retry them into policy).
"""
import argparse
import json
import re
import sys

ALLOWED_TYPES = {"comment", "label", "open_pull_request", "update_record", "send_notification"}
REQUIRED = ("type", "target", "reason")
FIELDS = set(REQUIRED) | {"body"}


def validate_shape(req):
    if not isinstance(req, dict):
        return "request is not an object"
    extra = set(req) - FIELDS
    if extra:
        return f"unexpected fields: {sorted(extra)}"
    for f in REQUIRED:
        if not isinstance(req.get(f), str) or not req[f].strip():
            return f"missing or empty '{f}'"
    if req["type"] not in ALLOWED_TYPES:
        return f"unknown action type {req['type']!r}"
    if len(req["target"]) > 256 or len(req["reason"]) > 2000:
        return "field too long"
    body = req.get("body")
    if body is not None and not isinstance(body, (str, dict)):
        return "body must be a string or an object"
    if isinstance(body, str) and len(body) > 65536:
        return "body too long"
    return None


def decide(requests, policy):
    counts, decisions = {}, []
    total_cap = policy.get("max_requests_per_run", 0)
    for i, req in enumerate(requests):
        problem = validate_shape(req)
        if problem is None:
            rule = policy.get("actions", {}).get(req["type"])
            if rule is None:
                problem = f"action type {req['type']!r} is not in the policy"
            elif not any(re.fullmatch(p, req["target"]) for p in rule.get("targets", [])):
                problem = f"target {req['target']!r} is outside the declared blast radius"
            elif counts.get(req["type"], 0) >= rule.get("max_per_run", 0):
                problem = f"per-run limit for {req['type']!r} reached"
            elif sum(counts.values()) >= total_cap:
                problem = "per-run request limit reached"
        if problem is None:
            counts[req["type"]] = counts.get(req["type"], 0) + 1
        decisions.append({"index": i, "accepted": problem is None, "reason": problem, "request": req})
    return decisions


# One handler per action type. Stubs: replace each with a call made with the APPLIER's
# own credential. Never build shell commands or queries by string concatenation.
def handle(req):
    print(f"APPLY {req['type']} → {req['target']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("requests")
    ap.add_argument("--policy", required=True)
    ap.add_argument("--apply", action="store_true", help="execute accepted requests (default: dry run)")
    args = ap.parse_args()
    policy = json.load(open(args.policy, encoding="utf-8"))
    if not isinstance(policy, dict):
        print("policy must be a JSON object", file=sys.stderr)
        return 2
    requests = []
    for n, line in enumerate(open(args.requests, encoding="utf-8"), 1):
        if line.strip():
            try:
                requests.append(json.loads(line))
            except json.JSONDecodeError as exc:
                requests.append({"_invalid": f"line {n}: {exc}"})
    # Decide every request before applying any: a malformed line late in the file must not
    # leave the run half-applied.
    decisions = decide(requests, policy)
    for d in decisions:
        req = d["request"] if isinstance(d["request"], dict) else {}
        print(json.dumps({"status": "ACCEPT" if d["accepted"] else "REJECT",
                          "type": req.get("type"), "target": req.get("target"), "why": d["reason"]}))
    if args.apply:
        for d in decisions:
            if d["accepted"]:
                handle(d["request"])
    return 0 if all(d["accepted"] for d in decisions) else 1


if __name__ == "__main__":
    sys.exit(main())
