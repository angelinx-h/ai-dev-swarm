# Out of Scope - MCP Skills Server MVP

This document explicitly defines what will NOT be included in the MVP. This prevents scope creep and keeps the team focused on delivering core value quickly.

## P1 Features Deferred (Should-Have, but not MVP)

These features are important for a complete v1.0 product but are not critical for validating the core hypothesis.

### P1-01: Complete 10-Stage Dev-Swarms Methodology

**What:** Access to all 15+ dev-swarms skills covering the full methodology
**Why Deferred:** MVP only needs 3 core skills to prove the concept works. Additional skills add value but don't validate the core technical approach or user need.
**When to Add:** After MVP validation, in v1.0 (Sprint 4+)
**Rationale:** Better to ship quickly with 3 working skills than delay for 15 skills

---

### P1-02: Performance Optimization

**What:** Optimization for 10-20 concurrent skill invocations, caching, memory optimization
**Why Deferred:** MVP targets single-user testing. Performance optimization matters for scale, but we need to validate the approach first.
**When to Add:** After MVP shows adoption, before multi-team rollout
**Rationale:** Premature optimization. Validate first, optimize later.

---

### P1-03: Deployment Guide with Examples

**What:** Docker, docker-compose, systemd service, cloud deployment guides
**Why Deferred:** MVP beta users can run locally for testing. Production deployment guides matter for scale, not validation.
**When to Add:** v1.0 when production deployments begin
**Rationale:** MVP focuses on local development and testing first

---

### P1-04: Skill Metadata and Discovery API

**What:** API endpoint to list all available skills with metadata, filtering by category
**Why Deferred:** Nice for tooling but not needed to prove MCP server works
**When to Add:** v1.1+ when building skill browsers or dashboards
**Rationale:** YAGNI (You Aren't Gonna Need It) for MVP

---

### P1-05: Configuration File Support

**What:** YAML/JSON config file, environment variable overrides
**Why Deferred:** MVP can use command-line arguments or environment variables. Config file is convenience, not necessity.
**When to Add:** v1.0 when configuration becomes complex
**Rationale:** Keep MVP simple - command-line flags suffice initially

---

### P1-06: Health Check and Status Endpoint

**What:** Health check mechanism for monitoring and production readiness
**Why Deferred:** MVP runs locally for testing - health checks matter for production deployments
**When to Add:** v1.0 when production monitoring is needed
**Rationale:** Not needed for local testing and validation

---

### P1-07: Helpful Error Messages for Common Issues

**What:** Enhanced error messages with troubleshooting links and error codes
**Why Deferred:** MVP has basic error handling (P0-09). Enhanced errors are polish, not blocking.
**When to Add:** v1.0 based on common issues discovered in beta
**Rationale:** Can't predict all errors until real usage reveals them

---

### P1-08: Skill Dependency Handling

**What:** Declare and validate dependencies between skills
**Why Deferred:** Current dev-swarms skills have minimal dependencies. Add when needed.
**When to Add:** v1.1+ if dependencies become an issue
**Rationale:** Current skills don't require this feature

---

### P1-09: Example MCP Client Configurations

**What:** Example configs for Cursor, Claude Code, generic MCP clients
**Why Deferred:** Documentation is important but examples can be added post-MVP
**When to Add:** v1.0 as documentation enhancement
**Rationale:** Basic setup docs (P0-08) are sufficient for beta testing

---

### P1-10: Security Best Practices Documentation

**What:** Comprehensive security documentation with OWASP guidelines
**Why Deferred:** OAuth 2.1 implementation (P0-05) includes basic security docs. Comprehensive guide is enhancement.
**When to Add:** v1.0 before wider enterprise adoption
**Rationale:** MVP docs cover setup; deep security docs are for production

---

### P1-11: Community Contribution Guidelines

**What:** CONTRIBUTING.md, code of conduct, PR templates, issue templates
**Why Deferred:** MVP is pre-release. Community infrastructure matters when accepting external contributions.
**When to Add:** v1.0 when open sourcing for community contributions
**Rationale:** Internal development first, community later

---

### P1-12: Skill Update and Reload Mechanism

**What:** Watch skills directory for changes and reload without restart
**Why Deferred:** MVP users can restart server during testing. Hot reload is convenience, not necessity.
**When to Add:** v1.1+ for developer experience improvement
**Rationale:** Server restart is acceptable for MVP testing

---

## P2 Features Excluded (Nice-to-Have)

These features would be nice to have but are clearly post-MVP enhancements.

### P2-01: Custom Skills Support and Documentation

**What:** Documentation and examples for creating custom organization-specific skills
**Why Excluded:** MVP focuses on existing dev-swarms skills. Custom skills support is natural extension but not needed to validate core value.
**When to Add:** v2.0+ for extensibility

---

### P2-02: Skill Usage Analytics

**What:** Track skill invocation counts, generate reports, export analytics
**Why Excluded:** Nice for understanding usage but not needed to prove the server works
**When to Add:** v2.0+ for product insights

---

### P2-03: Skill Versioning Support

**What:** Handle multiple versions of same skill, version metadata
**Why Excluded:** Dev-swarms skills will evolve but versioning adds complexity. Defer until it's a problem.
**When to Add:** v2.0+ if versioning becomes necessary

---

### P2-04: Web UI for Skill Browser

**What:** Web-based UI to browse skills and view documentation
**Why Excluded:** Significant development effort for a feature that's not core. MCP clients provide UI.
**When to Add:** v2.0+ or never (may be better solved by MCP client UIs)

---

### P2-05: SSE Transport Support

**What:** Server-Sent Events transport as alternative to stdio
**Why Excluded:** Stdio is simpler and works for local/containerized deployments. SSE adds complexity.
**When to Add:** v2.0 if remote deployment becomes priority
**Rationale:** Stdio meets MVP requirements; SSE is optimization

---

### P2-06: CLI Helper Tools

**What:** CLI commands to list skills, invoke skills, validate config, test auth
**Why Excluded:** Useful for debugging but not essential for MVP validation
**When to Add:** v2.0+ for developer experience

---

### P2-07: Docker Compose Setup for Development

**What:** Docker compose with MCP server, example client, monitoring stack
**Why Excluded:** Great for demos but not needed for MVP validation
**When to Add:** v1.0+ for demo purposes

---

### P2-08: Skill Templates and Generator

**What:** Tool to scaffold new custom skills with templates
**Why Excluded:** Focus is on existing skills; custom skill creation is future enhancement
**When to Add:** v2.0+ when custom skills become priority

---

## Technical Shortcuts Acceptable for MVP

These are conscious technical decisions to ship faster while documenting the debt.

### 1. Stdio Transport Only

**Decision:** Only implement stdio transport, not SSE
**Technical Debt:** Stdio has scalability limitations (0.64 req/sec under heavy load per research)
**Why Acceptable:** MVP targets single-user testing, not production scale
**When to Address:** v2.0 when remote deployment or high concurrency needed

---

### 2. Simple File Path Resolution

**Decision:** Basic string replacement for file paths, no advanced path handling
**Technical Debt:** May not handle edge cases (symlinks, spaces in paths, Windows UNC paths)
**Why Acceptable:** Works for 90% of cases; can enhance based on real issues
**When to Address:** v1.0 if beta users report path issues

---

### 3. In-Memory Skill Cache (Optional)

**Decision:** May cache SKILL.md content in memory without invalidation
**Technical Debt:** Changes to SKILL.md require server restart
**Why Acceptable:** During testing, server restarts are acceptable
**When to Address:** P1-12 (hot reload) addresses this in v1.1+

---

### 4. Basic Error Messages

**Decision:** Standard Python exception messages, not custom error codes
**Technical Debt:** Harder to debug without structured error codes
**Why Acceptable:** MVP targets technical users who can debug; enhanced errors are P1-07
**When to Address:** v1.0 based on common error patterns from beta

---

### 5. Manual OAuth Provider Configuration

**Decision:** Users manually configure OAuth provider details
**Technical Debt:** No OAuth provider auto-detection or setup wizard
**Why Acceptable:** Target users (AI platform engineers) are comfortable with OAuth config
**When to Address:** v2.0+ if non-technical users need setup

---

### 6. Minimal Test Coverage

**Decision:** Tests cover core paths (discovery, invocation, path resolution) but not edge cases
**Technical Debt:** ~60-70% code coverage instead of 90%+
**Why Acceptable:** Core functionality tested; edge cases revealed through beta usage
**When to Address:** v1.0 - expand test coverage based on bug reports

---

### 7. No Performance Benchmarking

**Decision:** Manual testing for performance, no automated benchmarks
**Technical Debt:** Can't track performance regressions systematically
**Why Acceptable:** MVP performance requirements are modest (<2s startup, <100ms invocation)
**When to Address:** P1-02 (performance optimization) includes benchmarking

---

## Design Polish Deferred

### MVP Uses Basic, Functional Design

**What's Deferred:**
- Fancy logging formats (MVP uses standard Python logging)
- Detailed progress indicators (MVP logs are functional but basic)
- Rich CLI output (MVP is server-focused, minimal CLI)
- Polished documentation site (MVP uses GitHub markdown)

**Why Acceptable:**
Target users (AI platform engineers) prioritize functionality over polish. Can enhance based on feedback.

**When to Add:**
v1.0 for broader audience appeal

---

## Explicit Exclusions

Features that might seem related but are definitively OUT of scope for this product:

### NOT Building:

1. **AI Agent / MCP Client**
   - We build the MCP SERVER, not the client
   - Users bring their own MCP clients (Cursor, Claude Code, custom)

2. **Skills Authoring Tool**
   - We serve existing dev-swarms skills, not a skill editor
   - Users edit SKILL.md files directly

3. **Cloud Hosting / SaaS**
   - MVP is self-hosted by users
   - Not building hosted service or cloud infrastructure

4. **Authentication Provider**
   - We validate OAuth 2.1 tokens, not issue them
   - Users bring their own OAuth provider (Google, GitHub, Azure, etc.)

5. **Skills Marketplace**
   - Not building a marketplace or registry for skills
   - Users manage skills in their dev-swarms/skills directory

6. **LangChain Integration**
   - MCP is the protocol; not building LangChain adapters
   - Users can integrate LangChain separately if needed

7. **Skill Versioning Across Git**
   - Not integrating with Git to track skill versions
   - Skills are local files; users manage versions themselves

8. **Multi-Repository Skill Loading**
   - MVP loads skills from single dev-swarms/skills directory
   - Not fetching skills from remote repos or multiple sources

9. **Visual Skill Builder / Designer**
   - No GUI for creating or editing skills
   - Text-based SKILL.md editing only

10. **Advanced Permissions / RBAC**
    - OAuth 2.1 validates identity, but no role-based access control
    - All authenticated users have same permissions in MVP

---

## Feature Request Management

**How We Handle Scope Creep:**

When new feature requests come up during MVP development:

1. **Ask:** Does this help validate the core hypothesis?
   - If NO → defer to P1/P2 or reject

2. **Ask:** Can we ship without it?
   - If YES → defer it

3. **Ask:** Is there a simpler MVP-appropriate version?
   - If YES → implement simple version, document debt

**Decision Framework:**

| Feature Request | Include in MVP? | Rationale |
|----------------|----------------|-----------|
| "Add skill X" | Only if it's one of the 3 core skills | P0-07 specifies 3 minimum |
| "Support Windows paths" | Yes (part of P0-04) | Cross-platform is requirement |
| "Add skill search" | No (P1-04) | Discovery API is P1 |
| "Improve error messages" | Basic only (P0-09) | Enhanced errors are P1-07 |
| "Add skill templates" | No (P2-08) | Custom skills are P2 |
| "Support SSE transport" | No (P2-05) | Stdio is sufficient for MVP |

---

## Summary: What Makes This the Right MVP Scope

**Why This Is Minimum:**
- Remove any P0 feature → core value broken or adoption blocked
- Example: Remove OAuth 2.1 → can't pass security review → no enterprise adoption

**Why This Is Viable:**
- All P0 features present → Maya can integrate, pass security review, access skills
- Enough skills (3) to prove usefulness
- Enough documentation to enable adoption

**Why This Is Product:**
- Not a prototype or proof-of-concept
- Production-ready: secure, tested, documented, reliable
- Real users can adopt and use it today

**Why Defer Everything Else:**
- P1/P2 features add value but don't validate core hypothesis
- Better to ship in 6 weeks with 3 skills than 12 weeks with 15 skills
- Can iterate based on real user feedback

---

**Decision:** This MVP scope represents the absolute minimum to deliver and validate core value. Everything else is post-MVP enhancement.

---

Last updated: 2025-12-26
