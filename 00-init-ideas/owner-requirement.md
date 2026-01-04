# Owner Requirements

Extracted from ideas.md and classified by priority.

## Critical Requirements (Must Have)

### Core Functionality
- Load `mcp_settings.json` configuration and connect to MCP servers
- Fetch tool definitions from servers supporting all transport types: stdio, HTTP, SSE
- Generate one `SKILL.md` file per tool in `mcp-skills/<server-id>-<tool-name>/` directory
- Manage symlinks in `skills/` folder based on enabled/disabled servers
- Track changes with lock file (`mcp_settings.lock`) to avoid unnecessary regeneration
- Provide Bridge class to forward JSON requests to MCP tools
- HTTP server (`mcp-bridge start`) to accept skill invocations via POST requests
- Windows compatibility with symlink fallback (copy-mode if symlinks fail)

### Technical Constraints
- **Language**: TypeScript only (not Python)
- **Packaging**: Published to npm as `mcp-skills-bridge` (unscoped package)
- **Implementation**: Single-file (~800-900 lines including HTTP server)
- **Dependencies**: Zod (schema validation), Commander.js (CLI), Express (HTTP server), Node.js 18+ built-ins

### Repository Requirements
- Create GitHub repository with proper structure
- GitHub Actions workflows for automated testing on PR
- Auto-publish to npm on GitHub release (version tags)
- Standard open source files: README.md, LICENSE, package.json, tsconfig.json

## Important Requirements (Should Have)

### Performance
- SHA256 hash-based change detection (skip regeneration if unchanged)
- Support `--force-refresh` flag to regenerate all skills
- Lazy-load MCP server connections (connect only when needed)

### CLI Commands
- `mcp-bridge sync` - Generate skills only (one-time)
- `mcp-bridge start` - Generate skills + run HTTP server
- `--mcp-settings=<path>` - Custom settings file path
- `--port=<number>` - Custom HTTP server port (default: 3333)
- `--output-dir=<path>` - Custom output directory
- `--log-level=<level>` - Debug logging support

### Bridge Behavior
- Accept JSON requests: `{server_id, tool_name, arguments}` or `{server_id, method, params}`
- Return standardized responses: `{status, result}` or `{status, error, detail}`
- POST `/invoke` endpoint for skill invocations
- Localhost only (no remote access needed)

## Nice to Have (Optional)

### Developer Experience
- Clear error messages for connection failures
- Port conflict detection and reporting
- Progress indicators during skill generation

### Future Enhancements (Explicitly Out of Scope for v1.0)
- UI/dashboard for managing skills (CLI only for v1.0)
- Skill analytics or usage tracking
- Multi-user or remote access modes
- Skill marketplace or discovery features

## Budget and Timeline Constraints

- **Budget**: Minimal (open source project)
- **Timeline**: Complete initial version within one day
- **Token Budget**: ~50k-200k tokens (~$2-$10) for full lifecycle
- **Scope**: Single developer, single implementation sprint

## Non-Functional Requirements

### Compatibility
- Node.js 18+ (LTS versions)
- Cross-platform: macOS, Linux, Windows
- All MCP transport types: stdio, http/streamable-http, sse

### Reliability
- Graceful handling of MCP server connection failures
- Safe file operations (atomic writes for lock file)
- Proper cleanup on process termination

### Security
- Localhost-only HTTP server (no external exposure)
- No credential storage (use existing MCP config)
- Safe environment variable expansion in MCP configs

## Explicit Out of Scope

- MCP server implementation (this is a client/bridge only)
- Replacing MCP protocol (this makes MCP more efficient)
- Authentication or authorization (relies on MCP server security)
- Distributed or multi-machine deployments
- Skill execution (skills invoke the bridge, bridge invokes MCP)

## Reference Implementation

- Python reference: `dev-swarm/py_scripts/mcp_to_skills.py`
- Concept doc: `dev-swarm/dev-skills/mcp-to-skills.md`
- Agent skill spec: `dev-swarm/docs/agent-skill-specification.md`
- MCP spec: https://modelcontextprotocol.io/
