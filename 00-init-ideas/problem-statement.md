# Problem Statement

## The Problem

AI agents burn excessive tokens when loading MCP (Model Context Protocol) tool definitions into context, making operations expensive and slow.

## Current Pain Points

- **Token Overhead**: Every MCP server loads ALL tool definitions into the agent's context upfront
- **Cost Impact**: Wasted tokens translate directly to higher operational costs
- **Performance Impact**: Larger context means slower processing and higher latency
- **Inefficiency**: Most tools are not used in a given session, yet their definitions occupy valuable context space

## Why This Problem Matters

- AI agents are becoming essential development tools
- MCP servers provide powerful integrations but at a high token cost
- Current approach doesn't scale as users add more MCP servers
- Developers need efficient tooling to make AI agents economically viable

## Constraints and Limitations

- Must maintain compatibility with existing MCP servers (stdio, HTTP, SSE transports)
- Must not require changes to MCP server implementations
- Must preserve full functionality of MCP tools
- Windows symlink support may be limited (requires fallback approach)
