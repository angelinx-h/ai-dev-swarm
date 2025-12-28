---
name: dev-swarms-background-process
description: Run background processes and manage the background-process MCP server. Use when an AI agent needs to run a long-running task or connect to a TUI.
---

# Background Process Management

This skill allows the AI agent to run background processes by installing and configuring the `background-process` MCP server.

## When to Use This Skill

- AI agent needs to run a long-running background task
- User wants to connect to a Text User Interface (TUI)
- Need to manage background processes through MCP server
- Running tasks that require persistent background execution

## Prerequisites

- `pnpm` must be installed.

## Your Roles in This Skill

- **DevOps Engineer**: Install and configure background-process MCP server. Set up process management infrastructure. Verify server connectivity and port availability. Troubleshoot connection issues and guide users through TUI setup.

## Role Communication

As an expert in your assigned roles, you must announce your actions before performing them using the following format:

- As a DevOps Engineer, I will check if background-process MCP server is already installed
- As a DevOps Engineer, I will configure MCP server with appropriate port settings
- As a DevOps Engineer, I will guide user through TUI connection process
- As a DevOps Engineer, I will troubleshoot any port conflicts or connectivity issues

**Note:** Combine multiple roles when performing related tasks. For example: "As a Tech Manager and Backend Architect, I will..." or "As a Frontend Architect and AI Engineer, I will..."

This communication pattern ensures transparency and allows for human-in-the-loop oversight at key decision points.

## Instructions

### 1. Check/Install MCP Server

When the AI agent needs to run a background process, it should first check if the `background-process` MCP server is installed. If not, install it using the configuration below:

```json
{
  "mcpServers": {
    "background-process": {
      "command": "pnpm",
      "args": [
        "dlx", "@waylaidwanderer/background-process-mcp@latest", "--port", "31337"
      ]
    }
  }
}
```

### 2. Connect to TUI

After configuration, instruct the user to connect the TUI (Text User Interface) to the running background process server via port `31337`:

```bash
pnpm dlx @waylaidwanderer/background-process-mcp ui --port 31337
```

### 3. Troubleshooting

- If port `31337` is in use, check if the MCP server has already started.
- Try to connect to the existing process rather than killing it.
- If necessary, configure a new port.
