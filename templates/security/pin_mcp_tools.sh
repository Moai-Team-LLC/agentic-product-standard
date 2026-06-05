#!/usr/bin/env bash
# Pin MCP tool definitions by hash and detect rug pulls.
#
# A community MCP server can mutate a tool's name / description / input schema
# AFTER you approved it (tool poisoning, rug pull). Pin the definitions to a
# lockfile on first run; on every later run (locally and in CI) fail if any
# tool's hash changed or a tool appeared/disappeared.
#
# Usage:
#   ./pin_mcp_tools.sh <tools.json> <lockfile>
#
# <tools.json> is the server's tool list — the `tools` array from an MCP
# `tools/list` response (capture it once you trust the server). Requires `jq`
# and a SHA-256 tool (`sha256sum` on Linux/CI, `shasum -a 256` on macOS).
set -euo pipefail

TOOLS="${1:?usage: pin_mcp_tools.sh <tools.json> <lockfile>}"
LOCK="${2:?usage: pin_mcp_tools.sh <tools.json> <lockfile>}"

command -v jq >/dev/null || { echo "error: jq is required"; exit 2; }
if command -v sha256sum >/dev/null; then SHA() { sha256sum | cut -d' ' -f1; }
elif command -v shasum   >/dev/null; then SHA() { shasum -a 256 | cut -d' ' -f1; }
else echo "error: need sha256sum or shasum"; exit 2; fi

# Canonical hash per tool: name + description + input schema, key-sorted so
# cosmetic reordering doesn't trip the diff but any semantic change does.
current="$(
  jq -cS '(.tools // .) | sort_by(.name)[] | {name, description, inputSchema}' "$TOOLS" \
  | while IFS= read -r tool; do
      name="$(printf '%s' "$tool" | jq -r '.name')"
      hash="$(printf '%s' "$tool" | SHA)"
      printf '%s  %s\n' "$hash" "$name"
    done
)"

if [ ! -f "$LOCK" ]; then
  printf '%s\n' "$current" > "$LOCK"
  echo "pinned $(printf '%s\n' "$current" | grep -c . ) tool definition(s) to $LOCK"
  echo "commit $LOCK and re-run this in CI to detect rug pulls."
  exit 0
fi

if diff -u "$LOCK" <(printf '%s\n' "$current") >/tmp/mcp-pin.diff 2>&1; then
  echo "OK: MCP tool definitions match $LOCK (no rug pull)."
  exit 0
fi

echo "::error::MCP tool definitions changed since pinning — possible rug pull / tool poisoning."
cat /tmp/mcp-pin.diff
echo "Review the change. If legitimate, re-pin: rm $LOCK && ./pin_mcp_tools.sh $TOOLS $LOCK"
exit 1
