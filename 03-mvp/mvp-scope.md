# MVP Scope - MCP Skills Server

## MVP Definition

**What is the Minimum Viable Product?**

The MVP is a fully functional MCP server that:
1. Automatically discovers dev-swarms skills from the skills directory
2. Exposes them as MCP tools via stdio transport
3. Implements OAuth 2.1 security for enterprise use
4. Correctly handles file path resolution and context injection
5. Provides at least 3 core dev-swarms skills to AI agents
6. Includes documentation for setup and basic testing

**What does "Viable" mean for this product?**

Viable means Maya (AI Platform Engineer) can:
- Install and configure the MCP server in under 30 minutes
- Integrate it with her custom AI platform
- Pass her security team's review (OAuth 2.1 requirement)
- Access critical dev-swarms skills from any MCP-compatible agent
- Debug issues with clear error messages and logs

## Core Value Proposition

**What is the ONE main problem this MVP solves?**

AI agents that aren't Claude Code cannot access dev-swarms skills. This MVP solves that by providing a standardized MCP server that makes dev-swarms methodology available to any MCP-compatible AI agent.

**How does it solve the problem differently than alternatives?**

| Alternative | Limitation | Our MVP Advantage |
|-------------|-----------|-------------------|
| Claude Code Skills | Only works with Claude Code | Works with ANY MCP client (Cursor, custom agents, etc.) |
| LangChain Integration | Requires custom code, no MCP | Drop-in MCP server, standard protocol |
| Manual Prompts | No structure, inconsistent | Structured 10-stage methodology |
| DIY MCP Server | Months to build, no OAuth | Production-ready with OAuth 2.1 |
| GitHub MCP Server | Just tools, no methodology | Comprehensive development workflows |

**Why would early adopters choose this MVP?**

- **Security First**: Only MCP server with OAuth 2.1 built-in (enterprise requirement)
- **Methodology Rich**: Proven 10-stage development framework, not just tools
- **Platform Independent**: Works across different AI agents via open MCP standard
- **Production Ready**: Built with FastMCP, tested, documented, reliable

## P0 Features Only (Must-Have)

These 10 features are the absolute minimum to deliver the core value proposition. Each is essential to solve the core problem.

### P0-01: MCP Server Implementation with Stdio Transport

**Feature Description:**
Implement a functional MCP server using stdio transport that complies with MCP 2025-06-18 specification.

**Serves Persona:** Maya (AI Platform Engineer)

**Why Essential for MVP:**
This is the foundation - without a working MCP server, nothing else matters. Stdio transport is the simplest, most compatible option for MVP.

**Acceptance Criteria:**
- MCP server runs as subprocess with stdin/stdout communication
- Implements MCP 2025-06-18 specification correctly
- Handles JSON-RPC messages according to spec
- Starts up in under 2 seconds
- Properly handles shutdown and cleanup
- Works with standard MCP clients (Claude Code, custom agents)

**Technical Notes:**
- Use FastMCP framework for Python implementation
- Follow MCP specification for stdio transport
- Test with MCP Inspector and Claude Code

---

### P0-02: Automatic Skill Discovery and Registration

**Feature Description:**
Server automatically discovers all skills in dev-swarms/skills directory on startup and registers each as an MCP tool.

**Serves Persona:** Maya (AI Platform Engineer)

**Why Essential for MVP:**
Manual configuration is brittle and doesn't scale. Auto-discovery makes the server self-configuring and future-proof as skills are added.

**Acceptance Criteria:**
- Server reads dev-swarms/skills directory on launch
- Discovers all skill folders containing SKILL.md files
- Parses SKILL.md YAML frontmatter (name, description)
- Registers each skill as an MCP tool
- Logs discovered skills for debugging
- Handles missing or malformed SKILL.md files gracefully

**Technical Notes:**
- Skills directory path should be configurable
- Support nested skill folders
- Validate SKILL.md format before registration

---

### P0-03: Skill Invocation with SKILL.md Context Injection

**Feature Description:**
When a skill is invoked, server returns the complete SKILL.md content so AI agent receives all instructions and context.

**Serves Persona:** Maya (AI Platform Engineer)

**Why Essential for MVP:**
This is the core mechanism - the skill instructions must reach the AI agent. Without this, skills don't work.

**Acceptance Criteria:**
- When skill tool is called, server reads corresponding SKILL.md file
- Returns complete SKILL.md content including frontmatter and body
- Content is formatted for injection into AI agent's context
- File reading errors are handled gracefully
- Response time is under 100ms per invocation
- Supports skills with large SKILL.md files (up to 100KB)

**Technical Notes:**
- Consider caching SKILL.md content after first read
- Ensure proper handling of markdown formatting
- Test with actual dev-swarms skills

---

### P0-04: File Path Resolution to Project Root

**Feature Description:**
All file paths referenced in SKILL.md are automatically converted to absolute paths relative to the project root.

**Serves Persona:** Maya (AI Platform Engineer)

**Why Essential for MVP:**
Skills reference files like templates or examples. Without correct path resolution, AI agents can't find these files, breaking the skill workflows.

**Acceptance Criteria:**
- Server identifies all file path references in SKILL.md content
- Converts relative paths to absolute paths from project root
- Handles different path formats (Unix, Windows)
- Preserves paths that are already absolute
- Documents path resolution logic for users
- Works correctly when server runs from subdirectories

**Technical Notes:**
- Project root should be configurable
- Consider using path patterns like `{PROJECT_ROOT}/path/to/file`
- Test on macOS, Linux, and Windows

---

### P0-05: OAuth 2.1 Security Implementation

**Feature Description:**
MCP server implements OAuth 2.1 authentication according to MCP 2025-06-18 specification for enterprise security compliance.

**Serves Persona:** Maya (AI Platform Engineer) - This is her #1 priority

**Why Essential for MVP:**
Maya's security team won't approve without OAuth 2.1. This is a hard blocker for enterprise adoption. No security = no adoption = failed MVP.

**Acceptance Criteria:**
- Implements OAuth 2.1 with PKCE flow
- Validates access tokens properly (per RFC spec)
- Supports resource parameter in token requests (RFC 8707)
- Implements secure, non-deterministic session IDs
- Does not use sessions for authentication (per MCP spec)
- Provides clear documentation on OAuth 2.1 setup and configuration
- Includes examples for common OAuth providers (Google, GitHub, Azure)

**Technical Notes:**
- Reference MCP security best practices
- Use FastMCP 2.0's built-in enterprise auth features
- Avoid "token passthrough" anti-pattern

---

### P0-06: Script Reference Handling

**Feature Description:**
Script files referenced in skills provide execution instructions to AI agent rather than source code.

**Serves Persona:** Maya (AI Platform Engineer)

**Why Essential for MVP:**
Some skills include helper scripts. AI agents need to EXECUTE these, not read/modify them. Wrong behavior breaks the skill.

**Acceptance Criteria:**
- Identifies script files in skill directories (.sh, .py, etc.)
- For scripts, provides execution instructions instead of source code
- Instructions include: script purpose, required arguments, expected output
- Works for common script types (bash, Python, Node.js)
- Documents script invocation pattern in SKILL.md
- Handles cases where scripts don't exist gracefully

**Technical Notes:**
- Scripts should be marked in SKILL.md with special syntax
- Consider adding script metadata (description, args)
- Security: Document that AI agents will execute these scripts

---

### P0-07: Core Dev-Swarms Skills Access

**Feature Description:**
Server exposes at minimum 3 essential dev-swarms skills: init-ideas, code-development, and draft-commit-message.

**Serves Persona:** James (Engineering Team Lead)

**Why Essential for MVP:**
These 3 skills represent the most commonly used workflows. They prove the server works for real use cases. Without actual skills, we can't validate user value.

**Acceptance Criteria:**
- Server exposes at minimum: init-ideas, code-development, draft-commit-message
- Skills work when invoked from different MCP clients
- Each skill returns complete context and instructions
- File references in skills resolve correctly
- Skills produce expected outputs when followed by AI agents

**Technical Notes:**
- These skills cover: project kickoff, feature development, and git commits
- Test with actual dev-swarms skill files from the project
- Ensure skill dependencies are handled (if any)

---

### P0-08: Clear Setup and Configuration Documentation

**Feature Description:**
Step-by-step documentation that enables James's team to install and configure the MCP server within 30 minutes.

**Serves Persona:** James (Engineering Team Lead)

**Why Essential for MVP:**
If users can't set it up, it doesn't matter how good it is. Documentation IS the product for adoption.

**Acceptance Criteria:**
- README includes installation instructions (pip install, uv setup)
- Configuration guide explains all required settings
- Quick start guide gets users running in under 30 minutes
- Troubleshooting section covers common issues
- Example configurations provided for different use cases
- Prerequisites clearly listed (Python version, uv, dependencies)

**Technical Notes:**
- Target audience: developers familiar with Python but new to MCP
- Include screenshots or terminal output examples
- Provide example MCP client configuration

---

### P0-09: Error Handling and Logging

**Feature Description:**
Clear error messages and comprehensive logging for troubleshooting integration issues.

**Serves Persona:** Maya (AI Platform Engineer)

**Why Essential for MVP:**
When (not if) something goes wrong during integration, Maya needs to debug quickly. Bad errors = abandoned integration.

**Acceptance Criteria:**
- All errors include actionable error messages
- Logs show skill discovery process
- Logs show skill invocations with timing
- Log levels configurable (DEBUG, INFO, WARNING, ERROR)
- Errors distinguish between configuration issues, skill issues, and runtime errors
- Logs written to stderr (stdout reserved for MCP protocol)

**Technical Notes:**
- Use Python logging module with proper configuration
- Consider structured logging (JSON format) for production
- Document logging configuration options

---

### P0-10: Basic Testing and Validation

**Feature Description:**
Example tests that show how to validate the MCP server is working correctly for CI/CD integration.

**Serves Persona:** Maya (AI Platform Engineer)

**Why Essential for MVP:**
Maya needs to integrate this into her platform's CI/CD. Without tests, she can't verify it works or catch regressions.

**Acceptance Criteria:**
- Test suite covers skill discovery
- Test suite covers skill invocation
- Test suite covers file path resolution
- Tests can run in CI/CD environment
- Documentation explains how to run tests
- Tests use realistic dev-swarms skills

**Technical Notes:**
- Use pytest for Python testing
- Include both unit tests and integration tests
- Mock MCP client for integration tests

---

## MVP User Journey

### Primary Persona: Maya (AI Platform Engineer)

**End-to-End Journey Through MVP:**

1. **Discovery** (5 minutes)
   - Maya searches GitHub for "MCP server skills" or finds it in MCP marketplace
   - Reads README to understand it provides dev-swarms skills via MCP
   - Sees OAuth 2.1 mentioned - continues reading (security requirement met)

2. **Evaluation** (15 minutes)
   - Clones repository
   - Reviews architecture documentation
   - Checks OAuth 2.1 implementation against MCP spec
   - Reads through example tests to understand functionality

3. **Installation** (10 minutes)
   - Installs Python dependencies with uv
   - Configures OAuth 2.1 with her company's provider
   - Points server at dev-swarms/skills directory
   - Starts server and sees skills discovered in logs

4. **Testing** (30 minutes)
   - Connects test MCP client to server
   - Invokes init-ideas skill, verifies SKILL.md content returns
   - Invokes code-development skill, tests file path resolution
   - Reviews logs for any errors or warnings
   - Confirms OAuth 2.1 token validation works

5. **Integration** (2-3 days)
   - Integrates MCP server into her AI platform
   - Configures platform to use the server for dev-swarms skills
   - Tests with real development workflows
   - Monitors performance and error rates

6. **Validation** (1 week)
   - Security team reviews OAuth 2.1 implementation
   - Platform team tests with different AI agents
   - Collects feedback from internal users
   - Confirms skills work as expected

**Critical Path Success:**
Maya successfully integrates the MCP server, passes security review, and internal developers can access dev-swarms skills through the AI platform.

---

## Target Users for MVP

**Early Adopters / Beta Testers:**

**Profile:** AI Platform Engineers like Maya
- Building custom AI agent platforms
- Need structured development methodologies
- Require enterprise security (OAuth 2.1)
- Familiar with MCP protocol
- Work at tech companies with 50-500 engineers

**Target Cohort Size:** 10-20 beta users

**Ideal Characteristics:**
- Active in MCP community or AI development tools space
- Have existing AI agent integration experience
- Can provide technical feedback on implementation
- Willing to test pre-release versions
- Can influence adoption at their organizations

**Acquisition Channels:**
- MCP marketplace / directory
- GitHub (topic tags: mcp-server, ai-agents, fastmcp)
- AI development Discord servers
- Tech Twitter (AI/ML tools community)
- Direct outreach to known AI platform engineers

---

## MVP Timeline

**Estimated Development:** 2-3 sprints (4-6 weeks with AI assistance)

### Sprint 1: Core MCP Server (2 weeks)
**Goal:** Working MCP server with skill discovery

**Deliverables:**
- P0-01: MCP server with stdio transport
- P0-02: Automatic skill discovery
- P0-03: Skill invocation with context injection
- P0-08: Basic README and setup docs

**Validation:** Server starts, discovers skills, returns SKILL.md content

---

### Sprint 2: Security & Quality (2 weeks)
**Goal:** Production-ready with OAuth 2.1

**Deliverables:**
- P0-05: OAuth 2.1 implementation
- P0-04: File path resolution
- P0-09: Error handling and logging
- P0-10: Test suite

**Validation:** Passes security review, all tests green, handles errors gracefully

---

### Sprint 3: Polish & Validation (1-2 weeks)
**Goal:** MVP ready for beta users

**Deliverables:**
- P0-06: Script reference handling
- P0-07: Core skills verified working
- P0-08: Documentation complete (troubleshooting, examples)
- Beta testing with 3-5 users

**Validation:** Beta users successfully integrate and use MVP

---

## Key Milestones

| Milestone | Target | Success Criteria |
|-----------|--------|------------------|
| MVP Development Complete | Week 6 | All P0 features implemented and tested |
| Security Review Pass | Week 7 | OAuth 2.1 validated by security expert |
| Beta Launch | Week 8 | 5 beta users onboarded |
| MVP Validation | Week 10 | 3+ beta users actively using server |
| Decision Point | Week 12 | Proceed to P1 features or iterate |

---

## MVP Constraints

### Technical Constraints
- **Transport:** Stdio only (SSE deferred to P1)
- **Language:** Python (FastMCP requirement)
- **Security:** OAuth 2.1 mandatory (no exceptions)
- **Skills:** Minimum 3 (can expand to all 15+ in P1)

### Resource Constraints
- **Development Time:** 4-6 weeks target
- **Team Size:** 1 developer with AI assistance
- **Budget:** Open source, no infrastructure costs for MVP

### Quality Constraints
- **Startup Time:** Must be under 2 seconds
- **Skill Invocation:** Must be under 100ms (95th percentile)
- **Security:** Must pass enterprise security review
- **Documentation:** Users must be able to set up in under 30 minutes

---

## Traceability to User Stories

This MVP includes all 10 P0 user stories from `02-personas/user-stories.md`:

| P0 Story | Included in MVP |
|----------|-----------------|
| P0-01: MCP Server Implementation | ✅ Yes |
| P0-02: Automatic Skill Discovery | ✅ Yes |
| P0-03: Skill Invocation | ✅ Yes |
| P0-04: File Path Resolution | ✅ Yes |
| P0-05: OAuth 2.1 Security | ✅ Yes |
| P0-06: Script Reference Handling | ✅ Yes |
| P0-07: Core Dev-Swarms Skills | ✅ Yes |
| P0-08: Setup Documentation | ✅ Yes |
| P0-09: Error Handling | ✅ Yes |
| P0-10: Basic Testing | ✅ Yes |

**P1 Stories (12):** Deferred to post-MVP (see out-of-scope.md)
**P2 Stories (8):** Deferred to post-MVP (see out-of-scope.md)

---

Last updated: 2025-12-26
