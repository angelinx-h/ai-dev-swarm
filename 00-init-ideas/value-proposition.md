# Value Proposition

## Core Value

**Convert MCP tools into on-demand agent skills, eliminating token overhead while preserving full MCP functionality.**

## Key Benefits

### 1. Dramatic Token Reduction
- Load only the tools you need, when you need them
- Agent skills load on-demand instead of upfront
- Eliminate wasted tokens from unused tool definitions

### 2. Cost Savings
- Directly reduce LLM API costs
- Scale to dozens of MCP servers without token explosion
- Pay only for tools actually used in each session

### 3. Performance Improvement
- Faster agent startup (smaller initial context)
- Reduced latency for tool selection
- More context space available for actual work

### 4. Zero MCP Changes Required
- Works with existing MCP servers (no modifications needed)
- Supports all transport types (stdio, HTTP, SSE)
- Transparent bridge between skills and MCP tools

### 5. Simple Developer Experience
- Install: `npm install -g mcp-skills-bridge`
- Generate: `mcp-bridge sync --mcp-settings=./mcp_settings.json`
- Run: `mcp-bridge start` (HTTP server for runtime invocations)
- Automatic skill updates when MCP configs change

## Why This Solution Matters

- **Enables MCP at Scale**: Make it practical to use many MCP servers simultaneously
- **Lowers Barrier to Entry**: Reduce cost concerns for AI agent adoption
- **Future-Proof**: As agent skills become standard, provides migration path from MCP
- **Open Source**: Community-driven solution for a common developer problem

## Differentiation

- **Not an MCP replacement**: Complements MCP by making it more efficient
- **Not a framework**: Simple CLI tool with single purpose
- **Not opinionated**: Works with any MCP setup, any agent that supports skills
