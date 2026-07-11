#!/usr/bin/env bash
#
# Stand up the whole AgenticProduct family with one command — the paved road,
# running locally. Clones each reference implementation into ./family/, brings
# up the three long-lived services through *their own* compose + run scripts
# (this script never re-implements a member's setup), and prints how to use the
# two non-server members. Vendor-neutral by Principle 2: this is a convenience,
# not a requirement — bring your own for any surface you'd rather run yourself.
#
#   ./family.sh up        # clone (if needed) + bring up Mind, Performance, Gateway
#   ./family.sh down      # stop the services + their Docker DBs (volumes preserved)
#   ./family.sh status    # health of every service
#   ./family.sh logs <mind|perf|gateway>
#
# Prerequisites: git, docker (with `docker compose`), bun (>=1.3), curl, openssl.
# The family map, licenses, and per-member docs: ECOSYSTEM.md and the
# `reference-stack` skill.

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FAMILY="$ROOT/family"
RUN="$FAMILY/.run"                 # pidfiles + logs for the processes we start
ORG="https://github.com/Moai-Team-LLC"

# Clone every member so the whole family is present; the three below plus the
# two run-on-use ones (Ops, Assurance).
REPOS=(AgenticMind AgenticPerformance AgenticGateway AgenticOps AgenticAssurance)

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
need() { command -v "$1" >/dev/null 2>&1 || { echo "ERROR: '$1' is required but not installed." >&2; return 1; }; }

check_prereqs() {
  local ok=0
  for c in git docker bun curl openssl; do need "$c" || ok=1; done
  docker compose version >/dev/null 2>&1 || { echo "ERROR: 'docker compose' (v2) is required." >&2; ok=1; }
  return $ok
}

healthy() { curl -fsS --max-time 2 "http://localhost:$1/health" >/dev/null 2>&1; }

# Retry a command a few times — absorbs a Postgres container still warming up
# before it accepts connections (the compose files have no wait-for gate).
retry() { # tries cmd…
  local tries="$1" i=1; shift
  while [ "$i" -le "$tries" ]; do "$@" >/dev/null 2>&1 && return 0; sleep 2; i=$((i+1)); done
  return 1
}

# Set KEY to a value in an env file only if it is currently empty or a
# placeholder. The value is passed via the environment (not argv) and is never
# printed — generated secrets stay out of stdout and `ps`.
upsert_secret() { # file KEY   (generates a random 32-byte hex secret in place)
  local file="$1" key="$2" tmp
  tmp="$(mktemp)" || return 1
  # Only replace an empty value or an <angle-bracket> placeholder — this covers
  # every real .env.example placeholder and can never clobber a value a user
  # (or a prior run) already set, including hex secrets.
  SECRET="$(openssl rand -hex 32)" \
  awk -v k="$key" '
    index($0, k"=") == 1 {
      val = substr($0, length(k) + 2)
      if (val == "" || val ~ /^</) { print k"=" ENVIRON["SECRET"]; next }
    }
    { print }
  ' "$file" > "$tmp" && mv "$tmp" "$file" || { rm -f "$tmp"; return 1; }
  # if the key was absent entirely, append it
  grep -qE "^${key}=" "$file" || printf '%s=%s\n' "$key" "$(openssl rand -hex 32)" >> "$file"
}

clone_all() {
  mkdir -p "$FAMILY" "$RUN"
  for r in "${REPOS[@]}"; do
    if [ -d "$FAMILY/$r/.git" ]; then
      echo "  $r: already cloned"
    else
      [ -e "$FAMILY/$r" ] && rm -rf "${FAMILY:?}/$r"   # clear a partial/failed clone so the retry is clean
      echo "  $r: cloning…"
      git clone --depth 1 "$ORG/$r.git" "$FAMILY/$r" >/dev/null 2>&1 \
        || { echo "  $r: CLONE FAILED (network? or run: rm -rf family/$r)" >&2; return 1; }
    fi
  done
}

# start a long-lived process, recording its pid + log under $RUN.
# no-op if we already have a live process under this name (avoids double-spawn).
spawn() { # name  command…
  local name="$1" pf; shift
  pf="$RUN/$name.pid"
  if [ -f "$pf" ] && kill -0 "$(cat "$pf" 2>/dev/null)" 2>/dev/null; then return 0; fi
  nohup "$@" >"$RUN/$name.log" 2>&1 &
  echo $! > "$pf"
}

# ---------------------------------------------------------------------------
# service bring-up — each delegates to the member's own compose + run scripts
# ---------------------------------------------------------------------------
# Each runs in a ( subshell ) so its `cd` is scoped and cannot leak into the next.
mind_up() (
  cd "$FAMILY/AgenticMind" || return 1
  [ -f .env.local ] || cp .env.example .env.local
  upsert_secret .env.local AUTH_SECRET
  bun install >/dev/null 2>&1
  if healthy 3000; then echo "  AgenticMind: already up (:3000)"; return 0; fi
  docker compose -f docker-compose.yml -f docker-compose.local.yml up -d >/dev/null 2>&1 \
    || { echo "  AgenticMind: DB failed to start (check: docker compose logs)"; return 1; }
  retry 5 bun run db:migrate-local \
    || { echo "  AgenticMind: migrations failed (retry: cd family/AgenticMind && bun run db:migrate-local)"; return 1; }
  spawn mind bun run dev
  echo "  AgenticMind: DB ready, server starting (:3000)"
)
perf_up() (
  cd "$FAMILY/AgenticPerformance" || return 1
  [ -f .env.local ] || cp .env.example .env.local
  bun install >/dev/null 2>&1
  if healthy 4319; then echo "  AgenticPerformance: already up (:4319)"; return 0; fi
  docker compose up -d >/dev/null 2>&1 \
    || { echo "  AgenticPerformance: DB failed to start (check: docker compose logs)"; return 1; }
  retry 5 bun run db:migrate-local \
    || { echo "  AgenticPerformance: migrations failed (retry: cd family/AgenticPerformance && bun run db:migrate-local)"; return 1; }
  spawn perf bun run ingest
  echo "  AgenticPerformance: DB ready, ingest starting (:4319)"
)
gateway_up() (
  cd "$FAMILY/AgenticGateway" || return 1
  [ -f .env ] || cp .env.example .env
  upsert_secret .env AGW_VAULT_KEY
  upsert_secret .env AGW_ADMIN_TOKEN
  upsert_secret .env AGW_AUDIT_TOKEN
  bun install >/dev/null 2>&1
  if healthy 8787; then echo "  AgenticGateway: already up (:8787)"; return 0; fi
  docker compose -f bifrost/docker-compose.yml --env-file .env up -d >/dev/null 2>&1 \
    || { echo "  AgenticGateway: Bifrost failed to start (check: docker compose logs)"; return 1; }
  spawn gateway bun run dev
  echo "  AgenticGateway: Bifrost ready, edge starting (:8787)"
)

stop_proc() { # name
  local pf="$RUN/$1.pid" pid
  [ -f "$pf" ] || return 0
  pid="$(cat "$pf" 2>/dev/null)"
  # only signal if the PID is still alive (guards against PID reuse)
  [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && kill "$pid" 2>/dev/null
  rm -f "$pf"
}

# ---------------------------------------------------------------------------
case "${1:-status}" in
  up)
    check_prereqs || exit 1
    echo "Cloning the AgenticProduct family into ./family/ …"
    clone_all || exit 1
    echo "Bringing up the services (each via its own compose + run)…"
    mind_up; perf_up; gateway_up
    cat <<EOF

The three long-lived services are starting. Give them ~5s, then: $0 status

  AgenticMind         MCP knowledge & memory   http://localhost:3000/mcp
  AgenticPerformance  OTLP trace ingest        http://localhost:4319/v1/traces
  AgenticGateway      OpenAI-compatible plane  http://localhost:8787   (Bifrost :8080)

The other two members are run on use, not as servers:
  AgenticOps  (library)    bun add github:Moai-Team-LLC/AgenticOps
  AgenticAssurance (CLI)   npx agent-assurance scan <manifest.json> --sarif out.sarif

Add your own model keys where a member needs one (e.g. family/AgenticMind/.env.local
CHAT_API_KEY, family/AgenticGateway/.env OPENAI_API_KEY). Generated secrets were
written into the .env files and never printed. This is the paved road, not a
mandate — swap any member for your own (Principle 2).
EOF
    ;;
  down)
    echo "Stopping services (Docker volumes preserved — data survives)…"
    stop_proc mind; stop_proc perf; stop_proc gateway
    [ -d "$FAMILY/AgenticMind" ]        && ( cd "$FAMILY/AgenticMind"        && docker compose -f docker-compose.yml -f docker-compose.local.yml stop >/dev/null 2>&1 )
    [ -d "$FAMILY/AgenticPerformance" ] && ( cd "$FAMILY/AgenticPerformance" && docker compose stop >/dev/null 2>&1 )
    [ -d "$FAMILY/AgenticGateway" ]     && ( cd "$FAMILY/AgenticGateway"     && docker compose -f bifrost/docker-compose.yml stop >/dev/null 2>&1 )
    echo "  stopped."
    ;;
  status)
    printf "%-24s %s\n" "AgenticMind (:3000)"        "$(healthy 3000 && echo UP || echo DOWN)"
    printf "%-24s %s\n" "AgenticPerformance (:4319)" "$(healthy 4319 && echo UP || echo DOWN)"
    printf "%-24s %s\n" "AgenticGateway (:8787)"     "$(healthy 8787 && echo UP || echo DOWN)"
    printf "%-24s %s\n" "Bifrost data plane (:8080)" "$(healthy 8080 && echo UP || echo DOWN)"
    ;;
  logs)
    case "${2:-}" in
      mind|perf|gateway) tail -40 "$RUN/${2}.log" 2>/dev/null || echo "no log yet for $2" ;;
      *) echo "usage: $0 logs <mind|perf|gateway>" ;;
    esac
    ;;
  -h|--help|help)
    sed -n '3,17p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
    ;;
  *) echo "usage: $0 <up|down|status|logs>"; exit 1 ;;
esac
