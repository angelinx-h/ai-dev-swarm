# Owner Requirements

## Functional Requirements

### FR1: MCP Server Architecture
**Priority**: P0 (Must Have)
- Implement MCP server using stdio transport
- Use Python FastMCP framework for implementation
- Use uv for Python environment and dependency management

### FR2: Skill Discovery and Registration
**Priority**: P0 (Must Have)
- Read dev-swarms/skills directory on server launch
- Automatically discover all skill folders
- Publish each skill as an MCP tool
- Parse SKILL.md files to extract skill metadata

### FR3: Skill Invocation
**Priority**: P0 (Must Have)
- When a skill tool is called, return the SKILL.md content
- Inject SKILL.md as system prompt to the AI agent session
- Preserve skill instructions and context during invocation

### FR4: File Path Management
**Priority**: P0 (Must Have)
- Update all file paths in SKILL.md to be relative to project root
- Ensure AI agents can correctly read referenced files
- Handle paths consistently across different operating systems

### FR5: Script Handling
**Priority**: P0 (Must Have)
- For any script files in skill folders, provide instructions to AI agent
- Do NOT include script source code in the response
- Tell AI agent to invoke scripts as commands/instructions

## Non-Functional Requirements

### NFR1: Performance
**Priority**: P0 (Must Have)
- Server startup time < 2 seconds
- Skill invocation response time < 100ms
- Minimal memory footprint

### NFR2: Reliability
**Priority**: P0 (Must Have)
- Graceful error handling for missing or malformed SKILL.md files
- Clear error messages for debugging
- No crashes on invalid skill invocations

### NFR3: Compatibility
**Priority**: P0 (Must Have)
- Compatible with standard MCP clients
- Works with stdio transport protocol
- Cross-platform support (macOS, Linux, Windows)

### NFR4: Maintainability
**Priority**: P1 (Should Have)
- Clean, documented code
- Easy to add new skills
- Simple configuration and setup
- Follows Python best practices

### NFR5: Documentation
**Priority**: P1 (Should Have)
- README with installation instructions
- Usage examples for different MCP clients
- Troubleshooting guide
- Architecture documentation

## Technical Constraints

1. **Language**: Python (for FastMCP compatibility)
2. **Protocol**: MCP with stdio transport
3. **Framework**: FastMCP
4. **Package Manager**: uv
5. **Skills Source**: dev-swarms/skills directory (same project)

## Reference Materials

- MCP Protocol: https://modelcontextprotocol.io
- FastMCP Framework: https://github.com/jlowin/fastmcp
- Claude Code Skills: https://code.claude.com/docs/en/skills
- Dev Swarms Framework: Current project

## Success Metrics

1. **Functionality**: All dev-swarms skills are accessible via MCP
2. **Adoption**: At least one external AI agent successfully uses the server
3. **Performance**: Meets all NFR performance targets
4. **Quality**: Zero critical bugs in core functionality
5. **Documentation**: Complete setup and usage documentation

## Out of Scope (for Initial Version)

- Skills hosted on remote servers or repositories
- Custom skill formats beyond current dev-swarms structure
- GUI or web-based configuration
- Skill versioning or backward compatibility
- Authentication or authorization
- Rate limiting or usage tracking
