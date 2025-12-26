# Edge Cases - MCP Skills Server

## Overview

This document defines edge cases, boundary conditions, and error scenarios for the MCP Skills Server, along with expected system behavior.

**Total Edge Cases**: 35+ scenarios documented

---

## 1. Configuration Edge Cases

### EC-001: Empty Skills Directory

**Scenario**: Skills directory exists but contains no skill folders or SKILL.md files

**Expected Behavior**:
- Server starts successfully (does not crash)
- Logs warning: `[WARNING] No skills found in directory: ./dev-swarms/skills`
- `list_tools` returns empty tools array
- Server remains running and responsive

**User Impact**: No skills available to invoke

**Error Message**:
```
[WARNING] ERR_DISCOVERY_200: No skills found in directory

No SKILL.md files were found in the skills directory:
  Path: ./dev-swarms/skills

This is not a critical error, but the server will have no skills to offer.
```

**Recovery**: User adds skills to directory (and restarts server or waits for hot reload in v1.0)

---

### EC-002: Skills Directory Path with Spaces

**Scenario**: Skills directory path contains spaces: `/path/to/my skills/dev-swarms`

**Expected Behavior**:
- Server correctly handles path with spaces
- Path is properly quoted internally
- Skill discovery works normally
- Logs show quoted path: `Skills directory: "/path/to/my skills/dev-swarms"`

**User Impact**: None (should work transparently)

**Platform Notes**:
- Unix/Linux: Spaces allowed, properly handled
- Windows: Spaces common, must be handled

---

### EC-003: Skills Directory is a Symlink

**Scenario**: `--skills-dir` points to a symbolic link to actual directory

**Expected Behavior**:
- Server follows symlink
- Skill discovery works on target directory
- Logs show both symlink and resolved path (DEBUG level)
- No warnings or errors

**User Impact**: None (should work transparently)

---

### EC-004: Skills Directory is Read-Only

**Scenario**: User has read-only access to skills directory

**Expected Behavior**:
- Server can read SKILL.md files (read-only is sufficient)
- Server starts successfully
- Skills discovered and registered normally
- Hot reload (v1.0) disabled automatically with warning

**User Impact**: None for normal operation, hot reload unavailable

---

### EC-005: OAuth Credentials in Config File (Insecure)

**Scenario**: User puts OAuth client secret in configuration file instead of environment variable

**Expected Behavior**:
- Server accepts credentials
- Logs warning: `[WARNING] [security] OAuth client secret detected in config file. Use environment variables for secrets.`
- Security documentation recommends env vars
- Server works but security risk documented

**User Impact**: Security risk if config file committed to version control

**Recommendation**: Use environment variables for secrets

---

### EC-006: Multiple Environment Variable Sets

**Scenario**: User has conflicting environment variables set (e.g., both `MCP_LOG_LEVEL` and legacy `LOG_LEVEL`)

**Expected Behavior**:
- Server uses MCP-prefixed variables only
- Ignores non-prefixed variables
- Logs which variable was used (DEBUG level)

**User Impact**: Clear precedence prevents confusion

---

### EC-007: Extremely Long File Paths

**Scenario**: Skills directory path > 255 characters (OS limit on some systems)

**Expected Behavior**:
- Server attempts to use path
- If OS rejects (path too long error), server shows clear error
- Error message: `Path too long (OS limit: 255 characters): [truncated path]...`
- Server exits with code 1

**User Impact**: Cannot start server

**Recovery**: User moves skills to shorter path

---

## 2. Skill Discovery Edge Cases

### EC-008: Skill Folder Without SKILL.md

**Scenario**: Folder in skills directory doesn't contain SKILL.md file

**Expected Behavior**:
- Server scans folder
- Logs debug message: `[DEBUG] [discovery] Folder has no SKILL.md, skipping: folder-name`
- Folder ignored (not registered as skill)
- Server continues discovery

**User Impact**: None (folder correctly ignored)

---

### EC-009: SKILL.md with No Frontmatter

**Scenario**: SKILL.md file has no YAML frontmatter (missing `---` delimiters)

**Expected Behavior**:
- Parser detects missing frontmatter
- Logs warning: `[WARNING] [discovery] Skipping skill: folder-name (no frontmatter found)`
- Skill skipped
- Server continues

**User Impact**: Skill not available

**Error Message**:
```
[WARNING] ERR_DISCOVERY_201: Skipping skill due to missing frontmatter

SKILL.md file must have YAML frontmatter enclosed in --- delimiters:
  Skill: my-custom-skill
  File: ./dev-swarms/skills/my-custom-skill/SKILL.md

Expected format:
  ---
  name: "skill-name"
  description: "Description here"
  ---

  [Skill content here...]
```

---

### EC-010: SKILL.md with Malformed YAML

**Scenario**: SKILL.md frontmatter contains invalid YAML syntax

**Expected Behavior**:
- YAML parser raises exception
- Server catches exception
- Logs warning with parse error details and line number
- Skill skipped
- Server continues

**User Impact**: Skill not available until YAML fixed

**Error Message**:
```
[WARNING] ERR_DISCOVERY_201: Skipping skill due to YAML parse error

Failed to parse YAML frontmatter:
  Skill: my-custom-skill
  File: ./dev-swarms/skills/my-custom-skill/SKILL.md
  Error: YAML parsing error at line 3: unexpected character ':'

Check YAML syntax in frontmatter.
```

---

### EC-011: Duplicate Skill Names

**Scenario**: Two skill folders have SKILL.md with same `name` field

**Expected Behavior**:
- Server detects duplicate during registration
- First skill registered normally
- Second skill triggers warning: `[WARNING] [registry] Duplicate skill name: skill-name (already registered from folder1, ignoring folder2)`
- Only first skill available

**User Impact**: Second skill not available

**Recovery**: User renames one of the skills

---

### EC-012: Skill Name with Special Characters

**Scenario**: SKILL.md `name` field contains special characters: `"my-skill-#1-@-test"`

**Expected Behavior**:
- Server validates skill name against allowed pattern
- Pattern: alphanumeric + hyphens + underscores only (`^[a-zA-Z0-9-_]+$`)
- Invalid characters trigger warning
- Skill skipped

**User Impact**: Skill not available until name corrected

**Error Message**:
```
[WARNING] ERR_DISCOVERY_202: Invalid skill name

Skill name contains invalid characters:
  Name: "my-skill-#1-@-test"
  Allowed: alphanumeric, hyphens, underscores only

Valid examples: "my-skill", "skill_name", "skill-123"
```

---

### EC-013: Very Large SKILL.md File

**Scenario**: SKILL.md file is 500KB (much larger than typical 10-50KB)

**Expected Behavior**:
- Server reads file (up to 1MB limit per NFR-007)
- Logs warning: `[WARNING] [io] Large SKILL.md file: 500KB (skill-name)`
- Skill registered and works
- Performance may be degraded (logged)

**User Impact**: Slower invocation response time

**Recommendation**: Keep SKILL.md files under 100KB

---

### EC-014: SKILL.md File with Non-UTF-8 Encoding

**Scenario**: SKILL.md file contains non-UTF-8 characters or different encoding

**Expected Behavior**:
- Server attempts to read as UTF-8
- Decoding error triggers warning
- Skill skipped

**User Impact**: Skill not available

**Error Message**:
```
[WARNING] ERR_IO_401: Unable to read SKILL.md file

File encoding error (expected UTF-8):
  File: ./dev-swarms/skills/my-skill/SKILL.md
  Error: 'utf-8' codec can't decode byte 0xff in position 123

Ensure SKILL.md files are saved as UTF-8.
```

---

### EC-015: Nested Skill Directories (Deep Hierarchy)

**Scenario**: Skills organized in deeply nested structure: `skills/category/subcategory/skill/SKILL.md`

**Expected Behavior**:
- Server recursively scans directories (up to reasonable depth, e.g., 10 levels)
- Discovers skills at any level
- Logs full path for each discovered skill (DEBUG)
- Works normally

**User Impact**: None (should work transparently)

**Performance Note**: Very deep hierarchies may slow discovery slightly

---

## 3. Skill Invocation Edge Cases

### EC-016: Skill Invoked Multiple Times Concurrently

**Scenario**: Same skill invoked by 10 MCP clients simultaneously

**Expected Behavior**:
- Server handles concurrent invocations
- Each invocation independent (stateless)
- File reads may be cached (v1.0 optimization)
- All invocations complete successfully
- Response times may increase under heavy load

**User Impact**: Possible performance degradation under heavy concurrent load

**Performance Target**: 10 concurrent requests (P0), 20 concurrent (P1)

---

### EC-017: Skill Invocation During Server Startup

**Scenario**: MCP client sends `call_tool` request before server finishes skill discovery

**Expected Behavior**:
- Server queues request or returns error
- Error: "Server not ready, still initializing"
- Client should retry after server ready
- Once ready, requests succeed

**User Impact**: Brief initialization period where invocations fail

---

### EC-018: SKILL.md File Deleted After Discovery

**Scenario**: SKILL.md file deleted from disk after server startup but before invocation

**Expected Behavior**:
- Server attempts to read file
- File not found error
- Returns error to client: `[ERROR] ERR_IO_400: SKILL.md file not found`
- Server continues running (does not crash)

**User Impact**: Specific skill unavailable

**Recovery**: Restore file and restart server (or wait for hot reload in v1.0)

---

### EC-019: SKILL.md File Modified During Read

**Scenario**: SKILL.md file being modified while server reads it

**Expected Behavior**:
- OS handles file locking
- Server gets consistent read (either old or new version)
- No corruption
- Next invocation gets new version

**User Impact**: Possible brief inconsistency

**v1.0 Note**: Hot reload detects changes and reloads

---

### EC-020: File Path Resolution with Circular Symlinks

**Scenario**: File referenced in SKILL.md has circular symlink: `A -> B -> A`

**Expected Behavior**:
- Path resolution detects circular reference
- Logs warning: `[WARNING] [io] Circular symlink detected: path/to/file`
- Uses original path without resolving
- Returns content with warning comment

**User Impact**: Path may not resolve correctly

---

## 4. OAuth Edge Cases

### EC-021: OAuth Provider Temporarily Unavailable

**Scenario**: OAuth provider (Google, GitHub, etc.) is down during startup

**Expected Behavior**:
- Server attempts OAuth validation
- Connection timeout (configurable, default 30s)
- Logs error: `[ERROR] [oauth] Unable to connect to OAuth provider (timeout after 30s)`
- Server exits with error code 2 (startup error)

**User Impact**: Server cannot start

**Recovery**: Wait for provider to recover, retry startup

---

### EC-022: OAuth Access Token Expired

**Scenario**: MCP client sends request with expired access token

**Expected Behavior**:
- Server validates token
- Detects expiration
- Returns OAuth error: "Token expired"
- HTTP status 401 Unauthorized (if using HTTP transport)
- Logs: `[WARNING] [oauth] Token validation failed: token expired`

**User Impact**: Request rejected

**Recovery**: Client obtains new token and retries

---

### EC-023: OAuth Access Token Revoked

**Scenario**: User revokes OAuth token via provider console

**Expected Behavior**:
- Server validates token with provider
- Provider returns "token revoked" error
- Server rejects request with error
- Logs: `[WARNING] [oauth] Token validation failed: token revoked`

**User Impact**: Request rejected

**Recovery**: Client re-authenticates and obtains new token

---

### EC-024: OAuth Client Secret Incorrect

**Scenario**: `MCP_OAUTH_CLIENT_SECRET` environment variable has wrong value

**Expected Behavior**:
- Server attempts OAuth flow
- Provider rejects due to incorrect secret
- Server logs error: `[ERROR] [oauth] OAuth configuration invalid: client authentication failed`
- Server exits with error code 2

**User Impact**: Server cannot start

**Recovery**: Correct the client secret

---

## 5. MCP Protocol Edge Cases

### EC-025: Malformed JSON-RPC Request

**Scenario**: MCP client sends invalid JSON: `{"jsonrpc": "2.0", "method": "call_tool", "params":` (truncated)

**Expected Behavior**:
- JSON parser raises exception
- Server catches exception
- Returns JSON-RPC error response: `-32700 Parse error`
- Logs: `[WARNING] [mcp] Received malformed JSON-RPC request`
- Server continues running

**User Impact**: Single request fails, client should retry with valid JSON

---

### EC-026: Unknown MCP Method

**Scenario**: Client sends request for unsupported method: `{"method": "unsupported_method"}`

**Expected Behavior**:
- Server receives request
- Method not found in handler registry
- Returns JSON-RPC error: `-32601 Method not found`
- Logs: `[WARNING] [mcp] Unknown method requested: unsupported_method`

**User Impact**: Request fails, client should use supported methods

---

### EC-027: Missing Request ID

**Scenario**: JSON-RPC request missing `id` field

**Expected Behavior**:
- Server detects missing ID
- Treats as notification (no response expected per JSON-RPC spec)
- OR returns error if ID is required
- Logs: `[DEBUG] [mcp] Received notification (no ID): method_name`

**User Impact**: Depends on MCP spec requirements

---

### EC-028: Request ID Integer Overflow

**Scenario**: Client sends request with very large ID: `{"id": 999999999999999999999}`

**Expected Behavior**:
- Server accepts ID as-is (treats as string or big integer)
- Echoes same ID in response
- Works normally

**User Impact**: None (ID is opaque to server)

---

### EC-029: Extremely Long Skill Name in Request

**Scenario**: Client requests skill with 1000-character name: `{"params": {"name": "a" * 1000}}`

**Expected Behavior**:
- Server validates skill name length
- Rejects if over reasonable limit (e.g., 100 characters)
- Returns error: "Skill name too long (max 100 characters)"
- Logs: `[WARNING] [mcp] Invalid skill name: name too long`

**User Impact**: Request rejected

---

## 6. File I/O Edge Cases

### EC-030: Disk Full During Logging

**Scenario**: Disk full, server cannot write logs to stderr

**Expected Behavior**:
- Logging fails silently (stderr write error)
- Server continues running (logging is non-critical)
- Possible OS error logged to system logs
- Server functionality unaffected

**User Impact**: Missing logs, but server works

---

### EC-031: File Path Resolution with Windows Drive Letters

**Scenario**: Path resolution on Windows: `C:\Projects\dev-swarms\00-init-ideas\README.md`

**Expected Behavior**:
- Server correctly handles Windows paths
- Converts backslashes to forward slashes internally (optional)
- Resolves paths relative to project root with drive letter
- Works normally on Windows

**User Impact**: None (cross-platform compatibility)

---

### EC-032: File Path with Unicode Characters

**Scenario**: SKILL.md references file with emoji or non-ASCII: `📁-folder/文件.md`

**Expected Behavior**:
- Server correctly handles Unicode paths
- Path resolution works with UTF-8 encoded paths
- File can be read if it exists
- Works normally

**User Impact**: None (Unicode support)

---

## 7. Performance Edge Cases

### EC-033: Server Startup with 100+ Skills

**Scenario**: Skills directory contains 100 skills (well above typical 3-20)

**Expected Behavior**:
- Server discovers all skills
- Startup time may exceed 2s target (acceptable for large count)
- Logs warning if startup > 5s: `[WARNING] [server] Slow startup (6.2s): consider reducing number of skills or optimizing`
- All skills registered successfully

**User Impact**: Slower startup

**Recommendation**: Organize skills into multiple servers if >50 skills

---

### EC-034: Memory Pressure (Low Available RAM)

**Scenario**: System has limited available memory (<500MB free)

**Expected Behavior**:
- Server attempts to start
- May fail to allocate memory for caching
- OS may kill process (OOM)
- Logs: `[ERROR] [server] Out of memory error`

**User Impact**: Server cannot start or crashes

**Recovery**: Free up system memory or disable caching

---

### EC-035: High CPU Usage from MCP Client

**Scenario**: MCP client sends 100 requests/second (excessive load)

**Expected Behavior**:
- Server processes requests as fast as possible
- May queue requests if over capacity
- Response times increase
- No crashes (graceful degradation)
- Logs: `[WARNING] [server] High request rate detected (100 req/s)`

**User Impact**: Degraded performance

**v1.0**: Rate limiting implemented (FR-017)

---

## Edge Case Summary

| Category | Count | Critical | Warning | Handled |
|----------|-------|----------|---------|---------|
| Configuration | 7 | 2 | 5 | 7/7 ✓ |
| Skill Discovery | 8 | 0 | 8 | 8/8 ✓ |
| Skill Invocation | 5 | 1 | 4 | 5/5 ✓ |
| OAuth | 4 | 2 | 2 | 4/4 ✓ |
| MCP Protocol | 5 | 0 | 5 | 5/5 ✓ |
| File I/O | 3 | 0 | 3 | 3/3 ✓ |
| Performance | 3 | 1 | 2 | 3/3 ✓ |
| **Total** | **35** | **6** | **29** | **35/35 ✓** |

**Key Takeaways**:
- All 35 edge cases have defined behavior
- 6 critical errors that prevent startup (by design)
- 29 warnings that allow server to continue
- Graceful degradation is default (avoid crashes)

---

Last updated: 2025-12-26
