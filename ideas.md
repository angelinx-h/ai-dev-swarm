# Ideas (Draft)

This is the starting point for an AI-assisted project kickoff. Keep it rough, honest, and incomplete. You and the AI agent will iterate together to refine it into professional documentation.

## How We'll Brainstorm Together

- You write quick, imperfect notes
- The AI proposes clearer structure, gaps, and options
- You confirm, correct, or add details
- We repeat until it's ready for formal stages

---

## Project Snapshot (Draft)

**Working title:** MCP to Skills Bridge

**One-line idea:** Converts MCP tools into on-demand agent skills that load only when needed, eliminating the token overhead of loading all MCP tool definitions into context.

**Problem to solve:** AI agents burn excessive tokens when loading MCP tool definitions into context, making operations expensive and slow.

**Target users:** Developers using AI agents with MCP servers

**Why now:** The recent introduction of agent skills enables a more efficient approach—agents can load specific tool contexts on-demand rather than loading entire MCP server definitions upfront.

---

## Goals and Outcomes (Draft)

**Primary goal:**
- Build a working MCP-to-agent-skill converter that reads MCP configs and generates skill files
- Publish as an npm package for easy adoption

**Secondary goals:**
- Achieve wide adoption among developers using AI agents
- Provide a fast, efficient, and simple conversion tool
- Reduce token consumption significantly for MCP-based workflows

**Non-goals:**
- This is NOT an MCP server implementation
- This does NOT replace MCP - it makes MCP tools available as agent skills
- No UI/dashboard for managing skills (CLI only)

---

## Requirements and Constraints (Draft)

**Must have:**
- Load `mcp_settings.json` configuration and connect to MCP servers
- Fetch tool definitions from servers (stdio, http, sse transports)
- Generate one `SKILL.md` file per tool in `mcp-skills/<server-id>-<tool-name>/`
- Manage symlinks in `skills/` folder based on enabled/disabled servers
- Track changes with lock file (`mcp_settings.lock`)
- Provide a Bridge class to forward JSON requests to MCP tools
- **HTTP server** (`mcp-bridge start`) to accept skill invocations via POST requests
- **Written in TypeScript and published to npm** (IMPORTANT)
- Create GitHub repository with GitHub Actions/workflows for automated testing
- Auto-publish to npm on GitHub release (version tags)

**Constraints:**
- Keep budget minimal (open source project)
- Complete initial version within one day
- Single-file implementation (~800-900 lines including HTTP server)
- Package name: `mcp-skills-bridge` (unscoped)

**Dependencies:**
- Zod (schema validation)
- Commander.js (CLI framework)
- Express (HTTP server)
- Node.js 18+ built-in APIs

---

## Risks and Unknowns (Draft)

**Biggest risks:**
- Windows symlink support may require admin privileges (could fail silently)
- MCP server connection failures during skill generation
- Port conflicts for HTTP server (default 3333)

**Open questions:**
- Should we support Windows symlinks or provide copy-mode fallback? → **Yes, provide fallback**
- [Add more as they arise]

**Assumptions:**
- Developers have basic familiarity with MCP and agent skills
- TypeScript port will match Python implementation behavior 1:1
- HTTP server runs on localhost only (no remote access needed)

---

## Technical Design (Draft)

### Core Components

**1. MCP Clients**
- `StdioClient`: Subprocess-based JSON-RPC communication
- `HttpClient`: HTTP/SSE transport support
- Both implement: `listTools()`, `callTool()`, `request()`

**2. MCP Manager**
- Lazy-load connections to MCP servers
- Route requests to appropriate client
- Support 3 transport types: stdio, http/streamable-http, sse

**3. Skill Generator**
- Convert tool definitions to markdown files
- Naming: camelCase → kebab-case (e.g., `backgroundProcess` → `background-process`)
- Template includes: frontmatter, usage example, arguments schema, background task polling

**4. Symlink Manager**
- Create relative symlinks: `skills/<name>` → `../mcp-skills/<name>`
- Enable/disable based on server config

**5. Bridge Class**
- Accept JSON requests: `{server_id, tool_name, arguments}` or `{server_id, method, params}`
- Forward to MCP Manager
- Return standardized response: `{status, result}` or `{status, error, detail}`

**6. HTTP Server**
- Express server listening on configurable port (default: 3333)
- POST `/invoke` endpoint accepts Bridge JSON payloads
- Returns Bridge responses as JSON
- Localhost only (no remote access)

**7. Change Detection**
- SHA256 hash of all skill content
- Skip regeneration if hash unchanged (unless `--force-refresh`)

### Project Structure

```
mcp-skills-bridge/
├── src/
│   └── index.ts              # Single file (~800-900 lines)
├── bin/
│   └── mcp-bridge.js         # CLI executable wrapper
├── tests/
│   └── index.test.ts         # Basic tests
├── .github/
│   └── workflows/
│       ├── test.yml          # Run tests on PR
│       └── publish.yml       # Publish to npm on release
├── package.json
├── tsconfig.json
├── README.md
└── LICENSE
```

### Code Organization (Single File)

```typescript
// src/index.ts

// Types
interface ServerConfig { ... }
interface ToolDef { ... }
class MCPError extends Error { ... }

// MCP Clients
abstract class MCPClient { ... }
class StdioClient extends MCPClient { ... }
class HttpClient extends MCPClient { ... }

// Manager
class MCPManager { ... }

// Utilities
function camelToKebab() { ... }
function slugify() { ... }
function expandEnvVars() { ... }

// Config
function loadMcpSettings() { ... }

// Skill Generation
function renderSkill() { ... }
function buildSkillEntries() { ... }
function writeSkills() { ... }

// Symlinks
function manageSymlinks() { ... }

// Bridge
class Bridge { ... }

// HTTP Server
function startServer(bridge, port) { ... }

// Main
function buildBridge() { ... }
async function main() { ... }

// CLI
if (require.main === module) {
  main();
}
```

### Expected Flow

**Skill Generation (`mcp-bridge sync`):**
1. Load `mcp_settings.json`, filter out disabled servers
2. Connect to enabled MCP servers (all 3 transport types)
3. Fetch tool definitions from each server
4. Generate `SKILL.md` files in `mcp-skills/<server-id>-<tool-name>/`
5. Create/remove symlinks in `skills/` based on enabled/disabled status
6. Compute SHA256 hash, update lock file if changed

**Runtime Server (`mcp-bridge start`):**
1. Perform skill generation (steps 1-6 above)
2. Build Bridge instance with MCP Manager
3. Start HTTP server on specified port
4. Accept POST `/invoke` requests with JSON payloads
5. Forward requests to Bridge → MCP Manager → MCP tools
6. Return responses to agent skills

### CLI Commands

```bash
# Generate skills only (one-time)
mcp-bridge sync --mcp-settings=./mcp_settings.json

# Force regenerate all skills
mcp-bridge sync --mcp-settings=./mcp_settings.json --force-refresh

# Start HTTP server (generates skills + runs server)
mcp-bridge start --mcp-settings=./mcp_settings.json --port=3333

# Custom output directory
mcp-bridge sync --mcp-settings=./mcp_settings.json --output-dir=./custom-skills

# Debug logging
mcp-bridge start --mcp-settings=./mcp_settings.json --log-level=DEBUG
```

---

## References

- Python reference implementation: `dev-swarm/py_scripts/mcp_to_skills.py`
- Original concept doc: `dev-swarm/dev-skills/mcp-to-skills.md`
- Agent skill specification: `dev-swarm/docs/agent-skill-specification.md`
- MCP Background Tasks: https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks

---

## Notes and Rough Ideas (Draft)

[Add additional thoughts, alternatives, or open questions here as they come up]
