# Playwright MCP details

## Extension
- Name: Playwright MCP Bridge
- Releases: https://github.com/microsoft/playwright-mcp/releases
- README: https://github.com/microsoft/playwright-mcp/blob/main/extension/README.md

## Chrome profile paths (macOS)
- Default profile: `~/Library/Application Support/Google/Chrome/Default`
- Profile 1: `~/Library/Application Support/Google/Chrome/Profile 1`

## Codex MCP add command template
```
codex mcp add playwright \
  --env PLAYWRIGHT_MCP_EXTENSION_TOKEN=<token> \
  -- npx "@playwright/mcp@latest" --extension --browser=chrome --user-data-dir=<profile-dir>
```

## Approval and token notes
- On first connect, the extension will show a tab selection UI; pick the tab you want the agent to control.
- Without a token, Chrome will prompt you to approve each connection.
- To bypass approval, copy `PLAYWRIGHT_MCP_EXTENSION_TOKEN` from the extension UI and set it in the MCP config.

## VS Code MCP add command template
```
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```
