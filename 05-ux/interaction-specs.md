# Interaction Specifications - MCP Skills Server

## Overview

This document defines interaction patterns, command formats, error messages, and logging specifications for the MCP Skills Server CLI.

---

## 1. Command-Line Interface (CLI) Specifications

### Base Command

```bash
mcp-skills-server [FLAGS] [OPTIONS]
```

### Required Flags: None

All configuration can use defaults or environment variables.

### Optional Flags

| Flag | Short | Type | Default | Description |
|------|-------|------|---------|-------------|
| `--skills-dir` | `-s` | path | `./dev-swarms/skills` | Skills directory path |
| `--project-root` | `-p` | path | `.` (current dir) | Project root for path resolution |
| `--log-level` | `-l` | string | `INFO` | Log level (DEBUG, INFO, WARNING, ERROR) |
| `--oauth-client-id` | | string | From env var | OAuth 2.1 client ID |
| `--oauth-provider-url` | | string | From env var | OAuth provider URL |
| `--validate-config` | | boolean | `false` | Validate configuration and exit |
| `--version` | `-v` | boolean | `false` | Show version and exit |
| `--help` | `-h` | boolean | `false` | Show help and exit |

### Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `MCP_SKILLS_DIR` | Skills directory | `./dev-swarms/skills` |
| `MCP_PROJECT_ROOT` | Project root | `/Users/maya/projects/dev-swarms` |
| `MCP_LOG_LEVEL` | Logging level | `DEBUG` |
| `MCP_OAUTH_CLIENT_ID` | OAuth client ID | `your-client-id` |
| `MCP_OAUTH_CLIENT_SECRET` | OAuth client secret | `your-client-secret` |
| `MCP_OAUTH_PROVIDER_URL` | OAuth provider URL | `https://accounts.google.com` |

**Priority**: CLI flags > Environment variables > Defaults

### Usage Examples

**Basic Usage** (defaults):
```bash
mcp-skills-server
```

**With Custom Skills Directory**:
```bash
mcp-skills-server --skills-dir /path/to/skills
```

**With Multiple Flags**:
```bash
mcp-skills-server \
  --skills-dir ./dev-swarms/skills \
  --project-root /Users/maya/projects/dev-swarms \
  --log-level DEBUG
```

**Validate Configuration**:
```bash
mcp-skills-server --validate-config
```

**Show Version**:
```bash
mcp-skills-server --version
# Output: MCP Skills Server v0.1.0
```

**Show Help**:
```bash
mcp-skills-server --help
```

### Help Output Format

```
MCP Skills Server v0.1.0
Enterprise-grade MCP server for dev-swarms skills

USAGE:
    mcp-skills-server [FLAGS] [OPTIONS]

FLAGS:
    -h, --help               Show this help message
    -v, --version            Show version information
        --validate-config    Validate configuration and exit

OPTIONS:
    -s, --skills-dir <PATH>           Skills directory path
                                      [default: ./dev-swarms/skills]
                                      [env: MCP_SKILLS_DIR]

    -p, --project-root <PATH>         Project root for path resolution
                                      [default: current directory]
                                      [env: MCP_PROJECT_ROOT]

    -l, --log-level <LEVEL>           Logging level
                                      [default: INFO]
                                      [possible values: DEBUG, INFO, WARNING, ERROR]
                                      [env: MCP_LOG_LEVEL]

        --oauth-client-id <ID>        OAuth 2.1 client ID
                                      [env: MCP_OAUTH_CLIENT_ID]

        --oauth-provider-url <URL>    OAuth provider URL
                                      [env: MCP_OAUTH_PROVIDER_URL]

EXAMPLES:
    # Start server with defaults
    mcp-skills-server

    # Custom skills directory
    mcp-skills-server --skills-dir /path/to/skills

    # Debug logging
    mcp-skills-server --log-level DEBUG

    # Validate configuration
    mcp-skills-server --validate-config

For more information, visit: https://github.com/org/mcp-skills-server
```

---

## 2. Logging Specifications

### Log Format

**Standard Format**:
```
[TIMESTAMP] [LEVEL] [COMPONENT] Message
```

**Example**:
```
[2025-12-26 16:30:45] [INFO] [server] MCP Skills Server v0.1.0 starting...
```

### Structured Logging Format (Optional - v1.0)

**JSON Format** (for production monitoring):
```json
{
  "timestamp": "2025-12-26T16:30:45.123Z",
  "level": "INFO",
  "component": "server",
  "message": "MCP Skills Server v0.1.0 starting...",
  "version": "0.1.0",
  "pid": 12345
}
```

### Log Levels

| Level | Purpose | When to Use | Example |
|-------|---------|-------------|---------|
| **DEBUG** | Detailed diagnostic info | Development, troubleshooting | `[DEBUG] [discovery] Scanning directory: ./dev-swarms/skills` |
| **INFO** | General informational messages | Normal operation | `[INFO] [server] Server ready (startup time: 1.2s)` |
| **WARNING** | Potentially problematic situations | Recoverable issues | `[WARNING] [discovery] Skipping malformed skill: my-skill (invalid YAML)` |
| **ERROR** | Error events | Failures that need attention | `[ERROR] [config] OAuth Client ID not configured` |

### Log Component Names

| Component | Purpose | Example Messages |
|-----------|---------|------------------|
| `server` | Server lifecycle | "Server starting", "Server ready", "Shutting down" |
| `config` | Configuration loading | "Configuration loaded", "OAuth configured" |
| `discovery` | Skill discovery | "Discovering skills", "Found 3 skills" |
| `registry` | Tool registration | "Registering MCP tools", "3 tools registered" |
| `mcp` | MCP protocol handling | "Received list_tools request", "Skill invoked" |
| `oauth` | Authentication | "Token validated", "OAuth provider connected" |
| `io` | File I/O operations | "Reading SKILL.md", "File path resolved" |

### Startup Log Sequence

```
[INFO] [server] MCP Skills Server v0.1.0 starting...
[INFO] [config] Configuration loaded
[DEBUG] [config] Skills directory: ./dev-swarms/skills
[DEBUG] [config] Project root: /Users/maya/projects/dev-swarms
[DEBUG] [config] Log level: INFO
[INFO] [oauth] OAuth 2.1 provider: https://accounts.google.com
[DEBUG] [oauth] OAuth client ID configured: abc***xyz (masked)
[INFO] [discovery] Discovering skills in: ./dev-swarms/skills
[DEBUG] [discovery] Scanning directory...
[DEBUG] [discovery] Found folder: dev-swarms-init-ideas
[DEBUG] [discovery] Reading SKILL.md: dev-swarms-init-ideas/SKILL.md
[DEBUG] [discovery] Parsed skill: init-ideas
[DEBUG] [discovery] Found folder: dev-swarms-code-development
[DEBUG] [discovery] Reading SKILL.md: dev-swarms-code-development/SKILL.md
[DEBUG] [discovery] Parsed skill: code-development
[DEBUG] [discovery] Found folder: dev-swarms-draft-commit-message
[DEBUG] [discovery] Reading SKILL.md: dev-swarms-draft-commit-message/SKILL.md
[DEBUG] [discovery] Parsed skill: draft-commit-message
[INFO] [discovery] Found 3 skills: init-ideas, code-development, draft-commit-message
[INFO] [registry] Registering 3 MCP tools...
[DEBUG] [registry] Registered tool: init-ideas
[DEBUG] [registry] Registered tool: code-development
[DEBUG] [registry] Registered tool: draft-commit-message
[INFO] [registry] MCP tools registered successfully
[INFO] [mcp] Starting stdio transport listener...
[INFO] [server] Server ready (startup time: 1.2s)
[INFO] [mcp] Listening on stdio for MCP requests
```

### Skill Invocation Logs

**INFO Level**:
```
[INFO] [mcp] Skill invoked: init-ideas
[INFO] [mcp] Skill invocation complete: init-ideas (response time: 45ms)
```

**DEBUG Level**:
```
[DEBUG] [mcp] Received JSON-RPC request: {"jsonrpc": "2.0", "method": "call_tool", "params": {"name": "init-ideas"}, "id": 1}
[DEBUG] [mcp] Parsed method: call_tool
[DEBUG] [mcp] Tool name: init-ideas
[DEBUG] [registry] Looking up tool: init-ideas
[DEBUG] [registry] Tool found: init-ideas -> ./dev-swarms/skills/dev-swarms-init-ideas
[DEBUG] [io] Reading SKILL.md: ./dev-swarms/skills/dev-swarms-init-ideas/SKILL.md
[DEBUG] [io] File size: 12,543 bytes
[DEBUG] [io] Parsing YAML frontmatter...
[DEBUG] [io] Frontmatter fields: name, description, category
[DEBUG] [io] Resolving file paths (project root: /Users/maya/projects/dev-swarms)
[DEBUG] [io] Found 3 file references
[DEBUG] [io] Resolved: 00-init-ideas/README.md -> /Users/maya/projects/dev-swarms/00-init-ideas/README.md
[DEBUG] [io] Resolved: 00-init-ideas/problem-statement.md -> /Users/maya/projects/dev-swarms/00-init-ideas/problem-statement.md
[DEBUG] [io] Resolved: 00-init-ideas/value-proposition.md -> /Users/maya/projects/dev-swarms/00-init-ideas/value-proposition.md
[DEBUG] [mcp] Response time: 47ms
[INFO] [mcp] Skill invocation complete: init-ideas (response time: 45ms)
```

### Shutdown Logs

```
[INFO] [server] Received shutdown signal (SIGTERM)
[INFO] [server] Shutting down gracefully...
[DEBUG] [mcp] Closing stdio listener...
[DEBUG] [registry] Unregistering 3 MCP tools...
[INFO] [server] Shutdown complete
```

---

## 3. Error Message Specifications

### Error Message Format

```
[ERROR] ERROR_CODE: Error Title

Detailed explanation of what went wrong.

To fix this issue:
1. Step 1
2. Step 2
3. Step 3

For more help: [link to documentation]
```

### Error Code System

**Format**: `ERR_[COMPONENT]_[NUMBER]`

| Component | Code Range | Example |
|-----------|------------|---------|
| CONFIG | 001-099 | `ERR_CONFIG_001` |
| OAUTH | 100-199 | `ERR_OAUTH_100` |
| DISCOVERY | 200-299 | `ERR_DISCOVERY_200` |
| MCP | 300-399 | `ERR_MCP_300` |
| IO | 400-499 | `ERR_IO_400` |
| REGISTRY | 500-599 | `ERR_REGISTRY_500` |

### Common Error Messages

#### ERR_CONFIG_001: Skills Directory Not Found

```
[ERROR] ERR_CONFIG_001: Skills directory not found

The configured skills directory does not exist:
  Path: ./dev-swarms/skills

To fix this issue:
1. Check that the path is correct
2. Ensure the directory exists: mkdir -p ./dev-swarms/skills
3. Or specify a different path: --skills-dir /path/to/skills

For setup help: https://docs.example.com/setup#skills-directory
```

#### ERR_CONFIG_002: Skills Directory Not Readable

```
[ERROR] ERR_CONFIG_002: Skills directory not readable

Permission denied when accessing skills directory:
  Path: /restricted/path/skills

To fix this issue:
1. Check directory permissions: ls -la /restricted/path
2. Ensure you have read access: chmod +r /restricted/path/skills
3. Or run with appropriate permissions: sudo mcp-skills-server

For permissions help: https://docs.example.com/troubleshooting#permissions
```

#### ERR_OAUTH_100: OAuth Client ID Not Configured

```
[ERROR] ERR_OAUTH_100: OAuth Client ID not configured

The OAuth client ID is required for authentication.

To fix this issue:
1. Set the MCP_OAUTH_CLIENT_ID environment variable:
   export MCP_OAUTH_CLIENT_ID="your-client-id"

2. Or pass it via command-line flag:
   mcp-skills-server --oauth-client-id "your-client-id"

3. Get your client ID by creating an OAuth app:
   - Google: https://console.cloud.google.com/apis/credentials
   - GitHub: https://github.com/settings/developers
   - Azure: https://portal.azure.com/

For OAuth setup: https://docs.example.com/oauth-setup
```

#### ERR_OAUTH_101: OAuth Provider URL Invalid

```
[ERROR] ERR_OAUTH_101: OAuth provider URL invalid

The OAuth provider URL is malformed or unreachable:
  URL: htp://invalid-url (typo: should be https)

To fix this issue:
1. Check the URL format (must start with https://)
2. Common provider URLs:
   - Google: https://accounts.google.com
   - GitHub: https://github.com/login/oauth
   - Azure: https://login.microsoftonline.com

3. Set the correct URL:
   export MCP_OAUTH_PROVIDER_URL="https://accounts.google.com"

For provider URLs: https://docs.example.com/oauth-setup#providers
```

#### ERR_DISCOVERY_200: No Skills Found

```
[WARNING] ERR_DISCOVERY_200: No skills found in directory

No SKILL.md files were found in the skills directory:
  Path: ./dev-swarms/skills

This is not a critical error, but the server will have no skills to offer.

To fix this issue:
1. Check that skills are in the correct location
2. Ensure skill folders contain SKILL.md files
3. Example structure:
   ./dev-swarms/skills/
   ├── dev-swarms-init-ideas/
   │   └── SKILL.md
   └── dev-swarms-code-development/
       └── SKILL.md

For skills setup: https://docs.example.com/skills-setup
```

#### ERR_DISCOVERY_201: Malformed SKILL.md

```
[WARNING] ERR_DISCOVERY_201: Skipping malformed skill

Failed to parse SKILL.md file due to invalid YAML frontmatter:
  Skill: dev-swarms-custom-skill
  File: ./dev-swarms/skills/dev-swarms-custom-skill/SKILL.md
  Error: YAML parsing error at line 5: unexpected character

The skill will be skipped, but the server will continue starting.

To fix this issue:
1. Check SKILL.md YAML frontmatter syntax
2. Required fields: name, description
3. Example frontmatter:
   ---
   name: "custom-skill"
   description: "Description here"
   ---

For SKILL.md format: https://docs.example.com/skill-format
```

#### ERR_MCP_300: Tool Not Found

```
[ERROR] ERR_MCP_300: Tool not found

The requested tool is not registered:
  Tool name: non-existent-skill

Available tools:
  - init-ideas
  - code-development
  - draft-commit-message

To fix this issue:
1. Check the tool name spelling
2. List available tools: see above
3. If the skill should exist, check skills directory configuration

For MCP tools: https://docs.example.com/mcp-protocol
```

#### ERR_IO_400: SKILL.md File Not Found

```
[ERROR] ERR_IO_400: SKILL.md file not found

The SKILL.md file for the requested skill does not exist:
  Skill: init-ideas
  Expected path: ./dev-swarms/skills/dev-swarms-init-ideas/SKILL.md

To fix this issue:
1. Verify the skill directory structure
2. Ensure SKILL.md file exists in the skill folder
3. Check file name spelling (must be exactly "SKILL.md")

For skill structure: https://docs.example.com/skill-structure
```

### Error Message Best Practices

1. **Be Specific**: Explain exactly what went wrong
2. **Be Actionable**: Provide clear steps to fix
3. **Be Helpful**: Include relevant context (paths, values)
4. **Be Consistent**: Use same format for all errors
5. **Be Friendly**: Avoid jargon, explain in simple terms

---

## 4. MCP Protocol Interactions

### JSON-RPC Message Format

**Request Format**:
```json
{
  "jsonrpc": "2.0",
  "method": "method_name",
  "params": {
    "key": "value"
  },
  "id": 1
}
```

**Response Format**:
```json
{
  "jsonrpc": "2.0",
  "result": {
    "key": "value"
  },
  "id": 1
}
```

**Error Response Format**:
```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32600,
    "message": "Invalid Request",
    "data": {
      "details": "Additional error information"
    }
  },
  "id": 1
}
```

### MCP Methods Supported

#### list_tools

**Request**:
```json
{
  "jsonrpc": "2.0",
  "method": "list_tools",
  "id": 1
}
```

**Response**:
```json
{
  "jsonrpc": "2.0",
  "result": {
    "tools": [
      {
        "name": "init-ideas",
        "description": "Initialize project ideas and documentation"
      },
      {
        "name": "code-development",
        "description": "Feature-driven development workflow"
      },
      {
        "name": "draft-commit-message",
        "description": "Draft conventional commit messages"
      }
    ]
  },
  "id": 1
}
```

#### call_tool

**Request**:
```json
{
  "jsonrpc": "2.0",
  "method": "call_tool",
  "params": {
    "name": "init-ideas"
  },
  "id": 2
}
```

**Response**:
```json
{
  "jsonrpc": "2.0",
  "result": {
    "content": "---\nname: \"init-ideas\"\ndescription: \"Initialize project ideas\"\n---\n\n# AI Builder - Init Ideas\n\nThis skill transforms non-technical ideas into professional project kickoff documentation...\n\n[Full SKILL.md content with resolved file paths...]"
  },
  "id": 2
}
```

**Error Response** (tool not found):
```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32601,
    "message": "Method not found",
    "data": {
      "tool_name": "non-existent-skill",
      "available_tools": ["init-ideas", "code-development", "draft-commit-message"]
    }
  },
  "id": 2
}
```

### MCP Error Codes

| Code | Message | Description |
|------|---------|-------------|
| -32700 | Parse error | Invalid JSON received |
| -32600 | Invalid Request | JSON-RPC request structure invalid |
| -32601 | Method not found | Requested method doesn't exist |
| -32602 | Invalid params | Invalid method parameters |
| -32603 | Internal error | Server internal error |

---

## 5. Exit Codes

| Exit Code | Meaning | When Used |
|-----------|---------|-----------|
| 0 | Success | Normal shutdown, validation passed |
| 1 | Configuration error | Invalid configuration, missing required settings |
| 2 | Startup error | Server failed to start (OAuth error, binding error) |
| 3 | Runtime error | Unexpected error during operation |
| 4 | Validation failed | --validate-config found issues |
| 130 | User interrupted | User pressed Ctrl+C (SIGINT) |
| 143 | Terminated | Received SIGTERM signal |

### Usage Examples

**Successful Startup and Shutdown**:
```bash
$ mcp-skills-server
[INFO] Server ready...
^C
[INFO] Shutdown complete
$ echo $?
130
```

**Configuration Error**:
```bash
$ mcp-skills-server --skills-dir /nonexistent
[ERROR] ERR_CONFIG_001: Skills directory not found
$ echo $?
1
```

**Validation Success**:
```bash
$ mcp-skills-server --validate-config
✓ Configuration valid
$ echo $?
0
```

**Validation Failed**:
```bash
$ mcp-skills-server --validate-config
✗ OAuth Client ID not configured
✗ OAuth Provider URL not configured
$ echo $?
4
```

---

## 6. Configuration Validation Output

### Validation Command

```bash
mcp-skills-server --validate-config
```

### Validation Output Format

**All Valid**:
```
Configuration Validation

✓ Skills directory configured and accessible
  Path: ./dev-swarms/skills
  Skills found: 3

✓ Project root configured and accessible
  Path: /Users/maya/projects/dev-swarms

✓ OAuth Client ID configured
  Value: abc***xyz (masked for security)

✓ OAuth Client Secret configured
  Value: *** (masked)

✓ OAuth Provider URL configured
  URL: https://accounts.google.com

✓ Log level valid
  Level: INFO

All configuration checks passed ✓
Exit code: 0
```

**Some Invalid**:
```
Configuration Validation

✓ Skills directory configured and accessible
  Path: ./dev-swarms/skills
  Skills found: 3

✓ Project root configured and accessible
  Path: /Users/maya/projects/dev-swarms

✗ OAuth Client ID not configured
  Fix: Set MCP_OAUTH_CLIENT_ID environment variable

✗ OAuth Client Secret not configured
  Fix: Set MCP_OAUTH_CLIENT_SECRET environment variable

✓ OAuth Provider URL configured
  URL: https://accounts.google.com

✓ Log level valid
  Level: INFO

Configuration validation failed: 2 errors
Exit code: 4
```

---

## 7. Progress Indicators

### Startup Progress (Optional - v1.0)

For long startups (many skills), show progress:

```
Starting MCP Skills Server v0.1.0...
[============================----] 70% Discovering skills (7/10)
```

### Skill Discovery Progress (Optional - v1.0)

```
Discovering skills...
  [✓] init-ideas
  [✓] code-development
  [✓] draft-commit-message
  [✗] custom-skill-broken (skipped: invalid YAML)
  [✓] custom-skill-working

Found 4 valid skills (1 skipped)
```

---

Last updated: 2025-12-26
