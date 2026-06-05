#!/usr/bin/env python3
"""Lethal-trifecta gate (Simon Willison's "lethal trifecta").

An agent that simultaneously has (1) access to PRIVATE DATA, (2) exposure to
UNTRUSTED CONTENT, and (3) the ability to COMMUNICATE EXTERNALLY can be turned
into an exfiltration tool by prompt injection. If all three legs are present,
at least one must be broken (a declared mitigation) before the agent ships.

Usage:
    python3 lethal_trifecta_check.py agent-capabilities.json

The capabilities file is JSON like:

    {
      "name": "support-agent",
      "private_data": true,        // reads customer records, secrets, internal docs
      "untrusted_content": true,   // ingests web pages, emails, user uploads, tool output
      "external_comms": true,      // can send email / post / call external APIs
      "mitigations": [             // each mitigation breaks one named leg
        {"leg": "external_comms", "control": "egress allow-list + human approval on send"}
      ]
    }

Exit code 0 = safe (trifecta broken or not present); 1 = unmitigated trifecta; 2 = bad input.
Stdlib only — no dependencies. Wire it into CI as a blocking step.
"""
import json
import sys

LEGS = ("private_data", "untrusted_content", "external_comms")


def evaluate(spec):
    name = spec.get("name", "<unnamed agent>")
    present = [leg for leg in LEGS if spec.get(leg) is True]
    if len(present) < 3:
        return 0, f"OK [{name}]: only {len(present)}/3 trifecta legs present ({', '.join(present) or 'none'})."

    mitigated_legs = {m.get("leg") for m in spec.get("mitigations", []) if m.get("control")}
    broken = mitigated_legs & set(LEGS)
    if broken:
        return 0, (
            f"OK [{name}]: full trifecta present, but broken at "
            f"{', '.join(sorted(broken))} via declared mitigation(s)."
        )
    return 1, (
        f"FAIL [{name}]: LETHAL TRIFECTA - private data + untrusted content + external "
        f"comms, with no leg broken. Break one (gate egress, quarantine untrusted input, "
        f"or scope the data) and declare it under 'mitigations'."
    )


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    try:
        with open(argv[1], encoding="utf-8") as fh:
            spec = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: cannot read capabilities file: {exc}", file=sys.stderr)
        return 2

    code, message = evaluate(spec)
    print(message, file=sys.stderr if code else sys.stdout)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
