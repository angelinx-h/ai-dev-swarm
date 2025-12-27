#!/usr/bin/env bash
set -euo pipefail

NAME="${MCP_NAME:-playwright}"
TOKEN="${PLAYWRIGHT_MCP_EXTENSION_TOKEN:-}"
PROFILE_DIR="${CHROME_PROFILE_DIR:-}"

cmd=(npx "@playwright/mcp@latest" --extension --browser=chrome)
if [ -n "$PROFILE_DIR" ]; then
  cmd+=(--user-data-dir="$PROFILE_DIR")
fi

if codex mcp list | grep -E -q "^${NAME}(\s|$)"; then
  codex mcp remove "$NAME"
fi

if [ -n "$TOKEN" ]; then
  codex mcp add "$NAME" --env "PLAYWRIGHT_MCP_EXTENSION_TOKEN=$TOKEN" -- "${cmd[@]}"
else
  codex mcp add "$NAME" -- "${cmd[@]}"
fi
