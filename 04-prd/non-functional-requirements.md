# Non-Functional Requirements

Quality attributes and constraints for the MCP Skills Bridge tool.

---

## NFR-1: Performance

### NFR-1.1: Skill Generation Speed

**Requirements:**
- Generate skills from a single MCP server: < 2 seconds (for up to 50 tools)
- Generate skills from 10 MCP servers: < 10 seconds total
- Hash computation: < 100ms for up to 500 skill files
- Lock file read/write: < 50ms

**Rationale:** Developers expect fast CLI tools. Sync should feel instantaneous for typical configurations.

**Acceptance Criteria:**
- [ ] Skill generation completes within 2s per server (50 tools)
- [ ] Hash computation completes within 100ms (500 files)
- [ ] No unnecessary blocking operations

---

### NFR-1.2: HTTP Bridge Response Time

**Requirements:**
- Bridge overhead: < 10ms (time between receiving request and forwarding to MCP)
- Health check endpoint (GET /): < 5ms response time
- Connection reuse: subsequent requests to same server < 5ms overhead

**Rationale:** Bridge should add minimal latency. MCP tool execution time is variable (depends on tool), but bridge itself should be fast.

**Acceptance Criteria:**
- [ ] Bridge processes requests within 10ms overhead
- [ ] Connection caching reduces subsequent request overhead
- [ ] Health check responds in < 5ms

---

### NFR-1.3: Memory Usage

**Requirements:**
- Base memory footprint: < 50 MB (server idle)
- Peak memory during sync: < 100 MB (processing 10 servers, 500 tools)
- No memory leaks during long-running server operation

**Rationale:** CLI tool should be lightweight. Developers often run multiple tools simultaneously.

**Acceptance Criteria:**
- [ ] Memory usage stays under 50 MB when idle
- [ ] Memory usage stays under 100 MB during skill generation
- [ ] No memory growth over 24-hour server run

---

## NFR-2: Compatibility

### NFR-2.1: Node.js Version Support

**Requirements:**
- Minimum: Node.js 18.0.0 (LTS)
- Recommended: Node.js 20.x or later
- Maximum: No upper limit (should work with future Node versions)

**Rationale:** Node.js 18 is current LTS. Requiring latest Node ensures access to modern APIs while maintaining broad compatibility.

**Acceptance Criteria:**
- [ ] Package.json specifies `"engines": { "node": ">=18.0.0" }`
- [ ] Tests pass on Node 18.x, 20.x, 22.x
- [ ] No use of experimental or deprecated APIs

---

### NFR-2.2: Operating System Support

**Requirements:**
- **macOS**: 10.15 (Catalina) and later
- **Linux**: Ubuntu 20.04+, Debian 11+, Fedora 35+, and equivalents
- **Windows**: Windows 10 (1809+) and Windows 11

**Platform-Specific Behaviors:**
- Symlinks: Work natively on macOS and Linux
- Symlinks: Require admin on Windows → fall back to file copy
- Process spawning: Use platform-appropriate shell resolution

**Acceptance Criteria:**
- [ ] Tested on macOS (Intel and ARM)
- [ ] Tested on Linux (Ubuntu, Debian, or Fedora)
- [ ] Tested on Windows (with and without admin)
- [ ] Windows fallback mode works correctly

---

### NFR-2.3: MCP Transport Support

**Requirements:**
- **Stdio transport**: Full support (most common)
- **HTTP transport**: Full support (http:// and https://)
- **SSE transport**: Full support (Server-Sent Events)
- **Streamable HTTP**: Support if server provides it

**Rationale:** MCP specification defines multiple transport types. Tool must support all to be compatible with any MCP server.

**Acceptance Criteria:**
- [ ] Connects to stdio MCP servers
- [ ] Connects to HTTP MCP servers
- [ ] Connects to SSE MCP servers
- [ ] Handles transport-specific errors gracefully

---

### NFR-2.4: Package Manager Compatibility

**Requirements:**
- Install via npm: `npm install -g mcp-skills-bridge`
- Install via pnpm: `pnpm add -g mcp-skills-bridge`
- Install via yarn: `yarn global add mcp-skills-bridge`
- Run via npx: `npx mcp-skills-bridge sync ...`

**Acceptance Criteria:**
- [ ] Published to npm registry
- [ ] Installable with npm, pnpm, yarn
- [ ] CLI available in PATH after global install
- [ ] Works with npx (no global install needed)

---

## NFR-3: Reliability

### NFR-3.1: Error Recovery

**Requirements:**
- **MCP server crashes**: Detect and report, continue with other servers
- **Network failures**: Retry HTTP connections (3 attempts, exponential backoff)
- **File system errors**: Report clearly, suggest remediation, exit gracefully
- **Port conflicts**: Detect and report port in use, suggest alternatives

**Acceptance Criteria:**
- [ ] One failing server doesn't stop entire sync
- [ ] HTTP requests retry on transient failures
- [ ] File errors include remediation suggestions
- [ ] Port conflict error shows which port and suggests `--port` flag

---

### NFR-3.2: Graceful Shutdown

**Requirements:**
- Handle SIGINT (Ctrl+C) gracefully
- Close all MCP connections before exit
- Flush logs and lock file writes
- Exit with appropriate code (0 = success, 1 = error, 130 = SIGINT)

**Acceptance Criteria:**
- [ ] Ctrl+C stops server cleanly
- [ ] MCP connections closed on shutdown
- [ ] Lock file written before exit
- [ ] No orphaned processes

---

### NFR-3.3: Data Integrity

**Requirements:**
- Atomic lock file writes (write to temp file, rename)
- Verify skill file writes (check file exists after write)
- Consistent hash computation (same input = same hash)
- No partial symlink states (create or fail, no half-created)

**Acceptance Criteria:**
- [ ] Lock file updates are atomic
- [ ] Skill generation is all-or-nothing per server
- [ ] Hash computation is deterministic
- [ ] Symlink creation doesn't leave broken links

---

## NFR-4: Security

### NFR-4.1: Network Binding

**Requirements:**
- HTTP server binds to 127.0.0.1 (localhost) ONLY
- Never bind to 0.0.0.0 (all interfaces)
- No remote access support
- No authentication required (localhost-only is security boundary)

**Rationale:** Bridge is intended for local development. Remote access would require authentication, HTTPS, etc. Out of scope for v1.0.

**Acceptance Criteria:**
- [ ] Server listens on 127.0.0.1:<port>
- [ ] Server NOT accessible from other machines
- [ ] Documentation clearly states localhost-only

---

### NFR-4.2: Credential Handling

**Requirements:**
- Do NOT store credentials (rely on MCP server config)
- Do NOT log sensitive data (auth tokens, API keys)
- Support environment variable expansion for secrets in mcp_settings.json
- Pass credentials to MCP servers as-is (no modification)

**Rationale:** Tool is a thin bridge. Security is handled by MCP servers. Tool should not introduce credential risks.

**Acceptance Criteria:**
- [ ] No credential storage in code
- [ ] Sensitive fields not logged (even in DEBUG mode)
- [ ] Environment variables expanded correctly
- [ ] Credentials passed securely to MCP servers

---

### NFR-4.3: Input Validation

**Requirements:**
- Validate all JSON inputs (mcp_settings.json, HTTP POST bodies)
- Sanitize file paths (prevent directory traversal)
- Validate server IDs (alphanumeric, hyphens, underscores only)
- Reject requests with unknown fields (strict schema)

**Acceptance Criteria:**
- [ ] Malformed JSON returns clear error
- [ ] Invalid file paths rejected
- [ ] Server IDs validated against safe character set
- [ ] Unknown JSON fields cause validation error

---

### NFR-4.4: Dependency Security

**Requirements:**
- Use well-maintained, popular npm packages only
- Keep dependencies minimal (Zod, Commander, Express + Node.js built-ins)
- No dependencies with known critical vulnerabilities
- Document security update process

**Rationale:** Fewer dependencies = smaller attack surface. Popular packages = better security scrutiny.

**Acceptance Criteria:**
- [ ] Zero critical vulnerabilities in dependencies (npm audit)
- [ ] All dependencies have > 1M weekly downloads or are standard tools
- [ ] Dependabot enabled for security updates
- [ ] Security policy documented (SECURITY.md)

---

## NFR-5: Maintainability

### NFR-5.1: Code Quality

**Requirements:**
- Single-file implementation (~800-900 lines)
- Clear function separation (MCP clients, Manager, Generator, Bridge, Server)
- Consistent naming conventions (camelCase for functions, PascalCase for classes)
- TypeScript strict mode enabled
- Linting with ESLint, formatting with Prettier

**Acceptance Criteria:**
- [ ] All code in src/index.ts (single file)
- [ ] TypeScript strict mode enabled
- [ ] No ESLint errors or warnings
- [ ] Code formatted with Prettier
- [ ] Clear separation between components

---

### NFR-5.2: Logging

**Requirements:**
- Structured logging (timestamp, level, message)
- Log levels: DEBUG, INFO, WARN, ERROR
- Default level: INFO
- No sensitive data in logs (even DEBUG level)

**Acceptance Criteria:**
- [ ] All logs include timestamp and level
- [ ] Log level controllable via --log-level
- [ ] Errors logged with context (server ID, tool name)
- [ ] No credentials or tokens in logs

---

### NFR-5.3: Documentation

**Requirements:**
- README.md with installation, usage, examples
- CLI help text (`mcp-bridge --help`, `mcp-bridge sync --help`)
- Error messages with remediation suggestions
- Examples for common scenarios

**Acceptance Criteria:**
- [ ] README explains installation and basic usage
- [ ] Each command has --help text
- [ ] Errors suggest next steps
- [ ] Examples cover 80% of use cases

---

## NFR-6: Testability

### NFR-6.1: Test Coverage

**Requirements:**
- Unit tests for core functions (hash computation, naming conversion, config loading)
- Integration tests for CLI commands (sync, start)
- Smoke tests for HTTP bridge
- Test fixtures for MCP mock servers

**Acceptance Criteria:**
- [ ] Core logic has unit tests
- [ ] CLI commands have integration tests
- [ ] Tests run in CI (GitHub Actions)
- [ ] Tests pass on all supported platforms

---

### NFR-6.2: Test Execution Speed

**Requirements:**
- Unit tests: < 5 seconds total
- Integration tests: < 30 seconds total
- CI pipeline: < 2 minutes total (install + test)

**Acceptance Criteria:**
- [ ] Unit tests complete in < 5s
- [ ] Integration tests complete in < 30s
- [ ] CI pipeline completes in < 2min

---

## NFR-7: Deployment

### NFR-7.1: Installation Speed

**Requirements:**
- npm install time: < 30 seconds (on decent connection)
- Package size: < 500 KB (unpacked)
- Zero native dependencies (pure JavaScript/TypeScript)

**Rationale:** Fast installation improves developer experience. No native deps means no compilation step.

**Acceptance Criteria:**
- [ ] Package installs in < 30s
- [ ] Unpacked size < 500 KB
- [ ] No native modules required
- [ ] Works immediately after install

---

### NFR-7.2: Update Mechanism

**Requirements:**
- Follow semantic versioning (semver)
- Publish to npm on GitHub release (automated)
- Notify users of updates (optional check)
- Backward compatible within major version

**Acceptance Criteria:**
- [ ] Versions follow semver (MAJOR.MINOR.PATCH)
- [ ] GitHub releases trigger npm publish
- [ ] Breaking changes only in major versions
- [ ] Release notes document changes

---

## Requirements Traceability

All non-functional requirements sourced from:
- `00-init-ideas/owner-requirement.md` (Non-Functional Requirements section)
- Industry best practices for CLI tools
- MCP specification compatibility requirements

Priority:
- **Critical**: NFR-2 (Compatibility), NFR-4 (Security)
- **Important**: NFR-1 (Performance), NFR-3 (Reliability)
- **Standard**: NFR-5 (Maintainability), NFR-6 (Testability), NFR-7 (Deployment)
