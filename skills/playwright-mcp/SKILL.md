---
name: playwright-mcp
description: Install or update the Playwright MCP server and the Playwright MCP Bridge Chrome extension on macOS/Chrome, then configure Codex MCP to use the extension so agents can access the user's browser for research or actions. Use when a user asks to enable Playwright MCP browser access, connect MCP to their Chrome profile, or automate web tasks that require the user's real browser session.
---

# Playwright MCP

## Overview

Set up Playwright MCP with the Chrome extension bridge on macOS, update any existing install, and configure Codex MCP so agents can open real web pages and perform user-approved actions in Chrome.

## Workflow (consent-gated)

Always ask for explicit consent before each numbered step. Stop if the user declines.

### 1) Confirm prerequisites
- macOS + Google Chrome installed.
- Codex CLI is installed and on PATH.
- User confirms which Chrome profile should be used (default or a specific profile).

### 2) Inspect current state
- `codex mcp list` to detect existing MCP entries.
- Ask the user to check `chrome://extensions` for the "Playwright MCP Bridge" extension.
- If anything is already installed, confirm whether to update/replace it.

### 3) Install or update Playwright CLI
- If `npx` is not available, install Node.js and npm.
- The MCP server is invoked with `npx "@playwright/mcp@latest"` (no global install needed).

### 4) Download and install the extension
- Download and extract the latest extension from GitHub Releases:
  - `python3 scripts/download_playwright_mcp_extension.py`
  - This prints the extracted path (default: `~/.codex/playwright-mcp-extension`)
- If the script fails, open the releases page in `references/playwright-mcp-details.md` and download the latest extension zip manually.
- In Chrome, open `chrome://extensions`, enable Developer Mode, and click "Load unpacked" with that folder.

### 5) Configure Codex MCP to use the extension
- Open the extension UI (extension icon or its status page) and copy the `PLAYWRIGHT_MCP_EXTENSION_TOKEN` value.
- Choose the Chrome profile directory (see `references/playwright-mcp-details.md`). If you omit the token, Chrome will prompt you to approve each connection.
- Run:
```
PLAYWRIGHT_MCP_EXTENSION_TOKEN=<token> \
CHROME_PROFILE_DIR=<profile-dir> \
scripts/configure_codex_playwright_mcp.sh
```
- This removes any existing `playwright` entry and re-adds it with the extension config.

### 5b) Optional: VS Code MCP registration
- If the user wants MCP in VS Code instead of Codex CLI:
```
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```

### 6) Verify
- Restart the Codex CLI after configuration.
- Ask the user to confirm a test action (example: open YouTube).

## Safety and consent rules
- Confirm before actions that affect user data (logins, emails, payments, account changes).
- For multi-step tasks, re-confirm at each step boundary.
- If the user wants to send email, ask for explicit approval right before clicking Send.
- Explain the tab-selection prompt on first use and ask the user to choose the tab intentionally.

## Example user requests this should handle
- "Set up Playwright MCP so you can use my Chrome profile."
- "Install the Playwright MCP extension and connect it to Codex."
- "Open Gmail and draft an email with subject 'hi' and body 'hello how are you'."

## Resources

### scripts/
`download_playwright_mcp_extension.py` downloads and extracts the Chrome extension bundle.
`configure_codex_playwright_mcp.sh` replaces or adds the Codex MCP config for Playwright with the extension.

### references/
`playwright-mcp-details.md` stores extension IDs, URLs, and Chrome profile paths.

---
