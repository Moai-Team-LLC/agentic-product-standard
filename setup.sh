#!/usr/bin/env bash
#
# Agentic Product Standard — quick setup.
#
# Installs the Claude Code skill set, then (optionally) stands up AgenticMind —
# the reference implementation — as a runnable knowledge & memory layer your
# agent plugs into over MCP. One run, end to end.
#
#   ./setup.sh                       # install skills here, then ask about AgenticMind
#   ./setup.sh /path/to/project      # install skills into that project
#   ./setup.sh --user                # install skills into ~/.claude/skills (every project)
#   ./setup.sh --with-agenticmind    # non-interactive: also clone + set up AgenticMind
#   ./setup.sh --skills-only         # just the skills, no prompt
#
# AgenticMind setup needs Bun (>=1.3) + Docker; skills install needs neither.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENTICMIND_REPO="https://github.com/Moai-Team-LLC/AgenticMind.git"
SKILL_SRC="$SCRIPT_DIR/skills/agentic-product-architect"

TARGET=""        # where .claude/skills lives (and where AgenticMind is cloned)
MODE="prompt"    # prompt | yes | no  — whether to also set up AgenticMind
USER_LEVEL=0

for arg in "$@"; do
  case "$arg" in
    --with-agenticmind) MODE="yes" ;;
    --skills-only)      MODE="no" ;;
    --user)             USER_LEVEL=1 ;;
    -h|--help)
      sed -n '3,15p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    -*) echo "Unknown flag: $arg" >&2; exit 1 ;;
    *)  TARGET="$arg" ;;
  esac
done
TARGET="${TARGET:-$PWD}"

# ----------------------------------------------------------------------------
# 1. Install the skills
# ----------------------------------------------------------------------------
if [ ! -d "$SKILL_SRC" ]; then
  echo "ERROR: skill source not found at $SKILL_SRC" >&2
  exit 1
fi

if [ "$USER_LEVEL" -eq 1 ]; then
  SKILLS_DEST="$HOME/.claude/skills"
else
  SKILLS_DEST="$TARGET/.claude/skills"
fi

echo "==> Installing the agentic-product-architect skill into $SKILLS_DEST"
mkdir -p "$SKILLS_DEST"
rm -rf "$SKILLS_DEST/agentic-product-architect"
cp -R "$SKILL_SRC" "$SKILLS_DEST/"
echo "    Installed: master skill + 10 sub-skills"

# ----------------------------------------------------------------------------
# 2. Offer AgenticMind — the reference implementation / runnable memory layer
# ----------------------------------------------------------------------------
if [ "$MODE" = "prompt" ]; then
  if [ -t 0 ]; then
    printf "\n==> Also set up AgenticMind now (the reference knowledge & memory layer your agent calls over MCP)? [y/N] "
    read -r reply
    case "$reply" in [Yy]*) MODE="yes" ;; *) MODE="no" ;; esac
  else
    MODE="no"   # non-interactive shell: never block on input
  fi
fi

if [ "$MODE" = "yes" ]; then
  command -v git >/dev/null 2>&1 || { echo "ERROR: git not found — install git first" >&2; exit 1; }
  DEST="$TARGET/AgenticMind"

  if [ -d "$DEST/.git" ]; then
    echo "==> AgenticMind already cloned at $DEST — pulling latest"
    git -C "$DEST" pull --ff-only || echo "    (pull skipped — local changes)"
  else
    echo "==> Cloning AgenticMind into $DEST"
    git clone "$AGENTICMIND_REPO" "$DEST"
  fi

  if command -v bun >/dev/null 2>&1 && command -v docker >/dev/null 2>&1; then
    echo "==> Running AgenticMind setup (deps + Postgres/pgvector + migrations)"
    ( cd "$DEST" && ./setup.sh )
    echo
    echo "AgenticMind is set up. Next:"
    echo "  cd AgenticMind && bun run dev    # headless MCP server on :3000"
    echo "  bun run scripts/issue-mcp-token.ts --label claude-code --ttl-days 365"
    echo "  then point your MCP client at http://localhost:3000/mcp with that bearer"
  else
    echo "==> Cloned only — AgenticMind's setup.sh needs Bun (https://bun.sh) + Docker."
    echo "    Install both, then: cd \"$DEST\" && cp .env.example .env.local && ./setup.sh"
  fi
else
  echo
  echo "Skills installed. To add the runnable memory layer later:"
  echo "  $0 --with-agenticmind"
fi

echo
echo "Done. Open your project in Claude Code — the skill auto-triggers on agentic work."
