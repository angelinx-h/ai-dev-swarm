# Functional Requirements

Requirements organized by feature area. Source: `00-init-ideas/owner-requirement.md` and `ideas.md`.

---

## FR-1: CLI Commands

### FR-1.1: Sync Command

**Behavior:**
```bash
mcp-bridge sync --mcp-settings=<path> [options]
```

- Load MCP configuration from specified path
- Connect to all enabled MCP servers
- Fetch tool definitions from each server
- Generate SKILL.md files in `mcp-skills/<server-id>-<tool-name>/`
- Manage symlinks in `skills/` folder
- Update lock file with SHA256 hash
- Exit after completion

**Options:**
- `--mcp-settings=<path>` (required): Path to mcp_settings.json
- `--output-dir=<path>` (optional): Custom output directory for skills
- `--force-refresh` (optional): Regenerate all skills even if unchanged
- `--log-level=<level>` (optional): Set logging verbosity (DEBUG, INFO, WARN, ERROR)

**Acceptance Criteria:**
- [ ] Generates skills for all enabled MCP servers
- [ ] Skips disabled servers
- [ ] Creates symlinks only for enabled servers
- [ ] Updates lock file with current hash
- [ ] Skips regeneration if hash unchanged (unless --force-refresh)
- [ ] Exits with code 0 on success, non-zero on error
- [ ] Prints summary: "Generated X skills from Y servers"

---

### FR-1.2: Start Command

**Behavior:**
```bash
mcp-bridge start --mcp-settings=<path> [options]
```

- Perform skill generation (same as sync command)
- Build Bridge instance with MCP Manager
- Start HTTP server on specified port
- Listen for POST requests to `/invoke` endpoint
- Keep server running until terminated (Ctrl+C)

**Options:**
- `--mcp-settings=<path>` (required): Path to mcp_settings.json
- `--port=<number>` (optional): HTTP server port (default: 3333)
- `--output-dir=<path>` (optional): Custom output directory for skills
- `--force-refresh` (optional): Regenerate all skills before starting server
- `--log-level=<level>` (optional): Set logging verbosity

**Acceptance Criteria:**
- [ ] Generates skills before starting server
- [ ] Starts HTTP server on specified port
- [ ] Prints "Server listening on http://localhost:<port>"
- [ ] Handles Ctrl+C gracefully (cleanup and exit)
- [ ] Reports port conflicts clearly
- [ ] Server remains running until terminated

---

## FR-2: MCP Configuration Loading

### FR-2.1: Load mcp_settings.json

**Behavior:**
- Read JSON file from path specified in `--mcp-settings` argument
- Parse MCP server configurations
- Expand environment variables in command/args (e.g., `${HOME}`, `$USER`)
- Filter servers based on `disabled` flag

**Expected Format:**
```json
{
  "mcpServers": {
    "server-id": {
      "command": "command-to-run",
      "args": ["arg1", "arg2"],
      "disabled": false
    }
  }
}
```

**Acceptance Criteria:**
- [ ] Parses valid mcp_settings.json successfully
- [ ] Expands environment variables correctly
- [ ] Filters out disabled servers
- [ ] Reports clear error if file not found
- [ ] Reports clear error if JSON is invalid
- [ ] Reports clear error if format is incorrect

---

## FR-3: MCP Server Connection

### FR-3.1: Connect to Stdio Servers

**Behavior:**
- Spawn subprocess with specified command and args
- Establish JSON-RPC communication over stdin/stdout
- Support MCP protocol initialization handshake
- Maintain connection for multiple requests

**Acceptance Criteria:**
- [ ] Successfully spawns subprocess
- [ ] Completes MCP initialization handshake
- [ ] Can list tools from server
- [ ] Can invoke tools with arguments
- [ ] Handles subprocess termination gracefully

---

### FR-3.2: Connect to HTTP/SSE Servers

**Behavior:**
- Connect to HTTP endpoint specified in config
- Support both `http` and `sse` transport types
- Use streamable HTTP if supported
- Handle authentication headers if provided

**Acceptance Criteria:**
- [ ] Connects to HTTP MCP servers
- [ ] Supports SSE transport for streaming
- [ ] Can list tools from HTTP server
- [ ] Can invoke tools via HTTP POST
- [ ] Handles connection errors gracefully

---

### FR-3.3: Lazy Connection Loading

**Behavior:**
- Do NOT connect to all servers on startup
- Connect to servers only when needed (during sync or tool invocation)
- Cache connections for reuse
- Close unused connections after timeout

**Acceptance Criteria:**
- [ ] No connections established until first use
- [ ] Connections cached for subsequent requests
- [ ] Multiple tool calls reuse same connection
- [ ] Connections closed cleanly on shutdown

---

## FR-4: Skill Generation

### FR-4.1: Fetch Tool Definitions

**Behavior:**
- Call `tools/list` method on each connected MCP server
- Receive tool definitions with name, description, inputSchema
- Store tool metadata for skill generation

**Acceptance Criteria:**
- [ ] Fetches all tools from each enabled server
- [ ] Handles servers with zero tools
- [ ] Reports errors if tools/list fails
- [ ] Continues with other servers if one fails

---

### FR-4.2: Generate SKILL.md Files

**Behavior:**
- For each tool, create `mcp-skills/<server-id>-<tool-name>/SKILL.md`
- Convert camelCase tool names to kebab-case directory names
- Generate markdown file with:
  - Frontmatter (name, description, mcp_server_id, mcp_tool_name)
  - Usage instructions
  - Arguments schema (from inputSchema)
  - Example usage
  - Background task polling instructions (if applicable)

**Naming Examples:**
- Tool: `backgroundProcess` → Directory: `background-process`
- Tool: `getUserData` → Directory: `get-user-data`
- Tool: `list-files` → Directory: `list-files` (already kebab-case)

**Acceptance Criteria:**
- [ ] Creates one SKILL.md per tool
- [ ] Uses correct directory naming (kebab-case)
- [ ] Includes all required frontmatter fields
- [ ] Renders inputSchema as readable markdown
- [ ] Includes JSON request format example
- [ ] Handles tools with no inputSchema

---

## FR-5: Symlink Management

### FR-5.1: Create Symlinks

**Behavior:**
- For each enabled server's tools, create symlink:
  - Source: `skills/<tool-directory-name>`
  - Target: `../mcp-skills/<server-id>-<tool-name>`
- Use relative paths (not absolute)
- Create parent directory `skills/` if not exists

**Acceptance Criteria:**
- [ ] Creates symlinks for all tools from enabled servers
- [ ] Uses relative paths
- [ ] Creates skills/ directory if missing
- [ ] Symlinks point to correct targets
- [ ] Overwrites existing symlinks if target changed

---

### FR-5.2: Remove Symlinks for Disabled Servers

**Behavior:**
- Identify symlinks in `skills/` that point to disabled servers
- Remove those symlinks
- Leave symlinks for enabled servers intact

**Acceptance Criteria:**
- [ ] Removes symlinks for disabled servers
- [ ] Keeps symlinks for enabled servers
- [ ] Handles case where symlink target no longer exists
- [ ] Does not delete non-symlink files in skills/

---

### FR-5.3: Windows Symlink Fallback

**Behavior:**
- Attempt to create symlinks on Windows
- If symlink creation fails (requires admin), fall back to copying files
- Copy `mcp-skills/<server-id>-<tool-name>/SKILL.md` to `skills/<tool-name>/SKILL.md`
- Log warning about symlink failure and fallback mode

**Acceptance Criteria:**
- [ ] Tries symlink first on all platforms
- [ ] Falls back to file copy on Windows if symlink fails
- [ ] Copied files have same content as originals
- [ ] Logs clear warning about fallback mode
- [ ] Sync command still completes successfully

---

## FR-6: Change Detection

### FR-6.1: Compute Hash of Skills

**Behavior:**
- After generating all SKILL.md files, compute SHA256 hash
- Hash input: concatenated content of all SKILL.md files (sorted by path)
- Store hash in `mcp_settings.lock` file

**Acceptance Criteria:**
- [ ] Computes consistent hash for same skill content
- [ ] Hash changes if any skill content changes
- [ ] Hash changes if servers are enabled/disabled
- [ ] Writes hash to mcp_settings.lock file

---

### FR-6.2: Skip Regeneration if Unchanged

**Behavior:**
- Before regenerating skills, check if `mcp_settings.lock` exists
- Compare current config hash with stored hash
- If identical and `--force-refresh` not set, skip regeneration
- Log: "Skills up to date, skipping regeneration"

**Acceptance Criteria:**
- [ ] Reads previous hash from lock file
- [ ] Compares with current config hash
- [ ] Skips regeneration if unchanged
- [ ] Regenerates if hash differs
- [ ] Regenerates if --force-refresh flag set
- [ ] Regenerates if lock file missing

---

## FR-7: HTTP Bridge Server

### FR-7.1: Start Express Server

**Behavior:**
- Create Express app
- Listen on port specified by `--port` (default: 3333)
- Bind to localhost only (127.0.0.1)
- Log server URL when ready

**Acceptance Criteria:**
- [ ] Starts HTTP server on specified port
- [ ] Listens on localhost only (not 0.0.0.0)
- [ ] Logs "Server listening on http://localhost:3333"
- [ ] Returns 404 for undefined routes
- [ ] Serves health check endpoint (GET /)

---

### FR-7.2: POST /invoke Endpoint

**Behavior:**
- Accept POST requests with JSON body
- Support two request formats:

  **Format 1 - Tool Invocation:**
  ```json
  {
    "server_id": "server-name",
    "tool_name": "toolName",
    "arguments": { "arg1": "value1" }
  }
  ```

  **Format 2 - Direct JSON-RPC:**
  ```json
  {
    "server_id": "server-name",
    "method": "tools/call",
    "params": { "name": "toolName", "arguments": {} }
  }
  ```

- Forward request to appropriate MCP server
- Return response in standardized format

**Response Format (Success):**
```json
{
  "status": "success",
  "result": { ... }
}
```

**Response Format (Error):**
```json
{
  "status": "error",
  "error": "Error message",
  "detail": "Detailed error information"
}
```

**Acceptance Criteria:**
- [ ] Accepts POST requests to /invoke
- [ ] Parses JSON body correctly
- [ ] Validates required fields (server_id, tool_name or method)
- [ ] Forwards requests to correct MCP server
- [ ] Returns standardized success response
- [ ] Returns standardized error response
- [ ] Sets Content-Type: application/json
- [ ] Returns 400 for invalid requests
- [ ] Returns 500 for server errors

---

### FR-7.3: Request Validation

**Behavior:**
- Validate JSON body structure
- Check server_id exists in configuration
- Check server is enabled (not disabled)
- Return clear error for validation failures

**Acceptance Criteria:**
- [ ] Returns 400 if JSON is malformed
- [ ] Returns 400 if server_id missing
- [ ] Returns 400 if tool_name/method missing
- [ ] Returns 404 if server_id not found
- [ ] Returns 403 if server is disabled
- [ ] Error messages are clear and actionable

---

## FR-8: Error Handling

### FR-8.1: MCP Connection Failures

**Behavior:**
- If MCP server fails to connect, log error and continue with other servers
- Report which server failed and why
- Do not halt entire sync/start process
- In HTTP bridge, return error response for failed invocations

**Acceptance Criteria:**
- [ ] Logs clear error message with server ID
- [ ] Continues processing other servers
- [ ] Reports summary at end (X succeeded, Y failed)
- [ ] HTTP bridge returns 502 for connection failures

---

### FR-8.2: Invalid Configuration

**Behavior:**
- If mcp_settings.json is invalid, report error and exit
- Validate required fields (command for stdio, url for http/sse)
- Do not attempt to connect if config is invalid

**Acceptance Criteria:**
- [ ] Exits with code 1 for invalid config
- [ ] Reports which field is missing/invalid
- [ ] Does not start server with invalid config
- [ ] Provides example of correct format

---

### FR-8.3: File System Errors

**Behavior:**
- If unable to write skill files, report error and exit
- If unable to create symlinks and copy fails, report error
- Check write permissions before attempting operations

**Acceptance Criteria:**
- [ ] Reports permission errors clearly
- [ ] Reports disk space errors clearly
- [ ] Suggests remediation (check permissions, free space)
- [ ] Exits gracefully on fatal errors

---

## FR-9: Logging and Output

### FR-9.1: Progress Indicators

**Behavior:**
- Log each major operation:
  - "Loading configuration from <path>"
  - "Connecting to server: <server-id>"
  - "Fetched X tools from <server-id>"
  - "Generated skill: <tool-name>"
  - "Created symlink: <tool-name>"
- Print summary at completion

**Acceptance Criteria:**
- [ ] Logs are clear and informative
- [ ] Progress visible during long operations
- [ ] Summary shows total skills generated
- [ ] Log level controls verbosity

---

### FR-9.2: Debug Logging

**Behavior:**
- With `--log-level=DEBUG`, log:
  - Full MCP JSON-RPC messages
  - Hash computation details
  - File write operations
  - Environment variable expansion

**Acceptance Criteria:**
- [ ] DEBUG level shows detailed information
- [ ] INFO level shows standard progress
- [ ] WARN level shows only warnings and errors
- [ ] ERROR level shows only errors
- [ ] Default level is INFO

---

## Requirements Traceability

All requirements sourced from:
- `00-init-ideas/owner-requirement.md` (Critical, Important, Nice-to-Have)
- `ideas.md` (Technical Design section)

Priority mapping:
- **Critical Requirements** → FR-1 through FR-7 (Must Have)
- **Important Requirements** → FR-6, FR-9 (Performance, DX)
- **Nice to Have** → Enhanced logging, progress indicators
