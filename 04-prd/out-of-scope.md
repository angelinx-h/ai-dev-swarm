# Out of Scope - MCP Skills Server PRD

## Purpose

This document explicitly defines what is NOT included in the MCP Skills Server product requirements to prevent scope creep, align stakeholder expectations, and maintain focus on core value delivery.

---

## Features Explicitly Excluded

### 1. AI Agent / MCP Client Implementation

**What's NOT Being Built:**
- We are building an MCP **SERVER**, not an MCP **CLIENT**
- No AI agent implementation
- No LLM integration
- No prompt engineering or AI model management

**Why Excluded:**
- Users bring their own MCP clients (Claude Code, Cursor, custom agents)
- Building a client would be a different product
- MCP protocol ensures interoperability with any client

**Alternative:**
- Users can use Claude Code, Cursor, or build custom MCP clients
- Documentation will provide client configuration examples

---

### 2. Skills Authoring Tool or Editor

**What's NOT Being Built:**
- No GUI or web interface for creating skills
- No visual skill builder or designer
- No SKILL.md template wizard or generator (MVP/v1.0)
- No integrated development environment (IDE) for skills

**Why Excluded:**
- Users edit SKILL.md files in their preferred text editor
- Adds significant complexity for limited value in MVP/v1.0
- Dev-swarms skills already exist in text format

**Alternative:**
- Users edit SKILL.md files directly (VS Code, vim, etc.)
- P2 may include skill templates/generator (FR-040)
- Documentation provides SKILL.md format guidelines

---

### 3. Cloud Hosting / SaaS Offering

**What's NOT Being Built:**
- No hosted MCP Skills Server service
- No cloud infrastructure management
- No multi-tenancy support
- No subscription or billing system
- No managed service / platform-as-a-service

**Why Excluded:**
- MVP is self-hosted by users
- Building SaaS is different business model
- Focus on software product first, service later

**Alternative:**
- Users self-host on their infrastructure
- Deployment guides provided for common platforms (Docker, cloud)
- Future: Could offer hosted service as separate product

---

### 4. Authentication Provider

**What's NOT Being Built:**
- No OAuth provider / identity provider
- No user account management
- No user registration or login system
- No password management
- No user database

**Why Excluded:**
- Server validates OAuth 2.1 tokens, doesn't issue them
- Users bring their own OAuth provider (Google, GitHub, Azure, etc.)
- We're not building an identity service

**Alternative:**
- Users configure existing OAuth provider (Google, GitHub, Azure)
- Documentation provides setup examples for common providers
- Server validates tokens from any OAuth 2.1 provider

---

### 5. Skills Marketplace or Registry

**What's NOT Being Built:**
- No skills marketplace or directory
- No skill discovery service
- No skill ratings or reviews
- No skill sharing platform
- No centralized skill repository

**Why Excluded:**
- MVP focuses on serving local skills
- Marketplace is a different product
- Skills are managed in local file system

**Alternative:**
- Users manage skills in their dev-swarms/skills directory
- Users can share skills via GitHub or other version control
- Future: Community could build marketplace on top

---

### 6. LangChain or Framework Integration

**What's NOT Being Built:**
- No LangChain integration or adapters
- No integration with other AI frameworks (AutoGPT, BabyAGI, etc.)
- No framework-specific bindings

**Why Excluded:**
- MCP is the protocol; provides standard interface
- Users can integrate LangChain separately if needed
- Avoid coupling to specific frameworks

**Alternative:**
- MCP protocol is framework-agnostic
- Users can build LangChain → MCP client if desired
- Focus on clean MCP implementation

---

### 7. Skill Versioning Across Git

**What's NOT Being Built:**
- No Git integration for skill versioning
- No automatic skill updates from Git repositories
- No skill version management across branches
- No skill rollback to previous versions

**Why Excluded:**
- Skills are local files; users manage with version control
- Adds complexity for limited MVP value
- Users already have Git for version control

**Alternative:**
- Users manage skill versions with Git directly
- Server serves whatever skills are in directory
- P2 may add basic skill versioning (FR-039) within server

---

### 8. Multi-Repository Skill Loading

**What's NOT Being Built:**
- No loading skills from multiple directories
- No fetching skills from remote repositories
- No skill dependencies from external sources
- No skill package manager

**Why Excluded:**
- MVP serves skills from single local directory
- Multi-source loading adds significant complexity
- Remote fetching introduces security and reliability concerns

**Alternative:**
- Users copy/organize all skills in one directory
- Users can symlink if they need skills from multiple locations
- Future: May support multiple skill directories (configuration)

---

### 9. Visual Skill Builder / Designer

**What's NOT Being Built:**
- No drag-and-drop skill builder
- No graphical skill flow designer
- No visual workflow editor
- No low-code/no-code skill creation

**Why Excluded:**
- Text-based SKILL.md is simple and flexible
- Visual builder is significant development effort
- Target users (developers) comfortable with text

**Alternative:**
- Users write SKILL.md in markdown
- Documentation provides templates and examples
- P2 may add skill template generator (FR-040)

---

### 10. Advanced Permissions / RBAC

**What's NOT Being Built:**
- No role-based access control (RBAC)
- No fine-grained permissions (which users can access which skills)
- No access control lists (ACLs)
- No user groups or roles

**Why Excluded:**
- OAuth 2.1 validates identity, but no role management
- All authenticated users have same permissions in MVP/v1.0
- RBAC adds significant complexity

**Alternative:**
- All authenticated users can access all skills
- Users deploy separate instances for different access levels
- Future: May add basic permissions in v2.0+

---

## Platform Exclusions

### 11. Platforms Not Supported

**What's NOT Supported in MVP/v1.0:**
- No native mobile apps (iOS, Android)
- No native desktop apps (Electron, native GUI)
- No browser extensions
- No IDE plugins (beyond MCP client configuration)

**Why Excluded:**
- MCP server runs as command-line process
- Mobile/desktop apps are different products
- Focus on core server functionality

**Alternative:**
- MCP clients (like Claude Code) can be mobile/desktop apps
- Server provides backend functionality via MCP protocol
- Future: Could build UI as separate project

---

### 12. Browsers Not Supported

**What's NOT Supported:**
- N/A - Server has no browser UI in MVP/v1.0
- (Web UI is P2 feature, if built would support modern browsers only)

---

### 13. Legacy Systems

**What's NOT Supported:**
- No support for Python 2.x (Python 3.8+ required)
- No support for Internet Explorer or other legacy browsers (if Web UI built)
- No support for outdated operating systems (Windows 7, macOS 10.14 or earlier)

**Why Excluded:**
- Legacy systems lack modern security and features
- Maintaining backwards compatibility increases complexity
- Focus on current and future platforms

---

## Integration Exclusions

### 14. Third-Party Integrations Deferred

**What's NOT Included in MVP/v1.0:**
- No Slack integration
- No Microsoft Teams integration
- No GitHub Actions integration (beyond standard CI/CD)
- No Jira / project management tool integration
- No monitoring service integration (Datadog, New Relic, etc.)

**Why Excluded:**
- Core functionality doesn't require these integrations
- Can be added later based on user demand
- Keep MVP scope focused

**Alternative:**
- Users can build integrations on top of MCP API
- P2 may add specific integrations based on demand

---

### 15. External Services Not Included

**What's NOT Included:**
- No external analytics service (Google Analytics, Mixpanel, etc.)
- No error tracking service (Sentry, Rollbar, etc.)
- No CDN or hosting service
- No cloud storage integration (S3, GCS, Azure Blob)

**Why Excluded:**
- Keep dependencies minimal
- Avoid vendor lock-in
- Users can add if needed

**Alternative:**
- Server logs locally (users can forward to external services)
- Users deploy monitoring/analytics separately
- P1 documentation may cover integration patterns

---

## Technical Exclusions

### 16. Advanced Features Deferred

**What's NOT in MVP/v1.0:**
- No machine learning or AI within server (server serves skills, doesn't use AI)
- No real-time collaboration features
- No multi-user skill editing
- No skill conflict resolution
- No skill merge tools

**Why Excluded:**
- Skills are files on disk, managed by users
- Advanced features add complexity without clear MVP value

---

### 17. Performance Optimizations Deferred

**What's Deferred to P1/P2:**
- No advanced caching strategies (MVP: optional simple cache)
- No CDN integration
- No HTTP/2 or HTTP/3 optimization
- No connection pooling (stdio transport)
- No load balancing (single instance MVP)

**Why Excluded:**
- MVP targets single-user testing, not production scale
- Performance optimization happens in P1 after MVP validation

**When to Add:**
- P1: Performance optimization (FR-026)
- P2: SSE transport for better scalability

---

### 18. Internationalization (i18n)

**What's NOT Included:**
- No multi-language support
- No localization (l10n)
- No translation of error messages
- No locale-specific formatting

**Why Excluded:**
- English-only for MVP and v1.0
- Target users (developers) typically comfortable with English
- i18n adds significant complexity

**Alternative:**
- All documentation and errors in English
- Future: May add i18n if international adoption grows

---

## Business Exclusions

### 19. Business Models Not Pursued in MVP/v1.0

**What's NOT Included:**
- No freemium model (open source, no tiers)
- No premium features or paid add-ons
- No enterprise licensing (open source license for all)
- No commercial support contracts
- No training or consulting services

**Why Excluded:**
- MVP is fully open source (MIT or Apache 2.0)
- Focus on adoption first, monetization later (if at all)

**Alternative:**
- 100% open source and free
- Community support via GitHub issues
- Future: Could offer commercial support as separate offering

---

### 20. Market Segments Not Targeted in MVP/v1.0

**What's NOT Targeted:**
- Non-technical users (MVP targets developers)
- Enterprise sales (self-service adoption)
- Government/regulated industries (initially)
- Educational institutions (initially)

**Why Excluded:**
- MVP focuses on technical early adopters
- Broader markets require different features/compliance

**When to Add:**
- v1.0+: Enterprise features (compliance documentation)
- v2.0+: May target adjacent markets based on demand

---

### 21. Monetization Features Deferred

**What's NOT Included:**
- No analytics or telemetry for business insights
- No usage tracking for billing
- No license key management
- No payment processing
- No subscription management

**Why Excluded:**
- Open source project, no monetization in MVP/v1.0

---

## Clarifications & Boundaries

### 22. Common Misconceptions

**Clarification: This is NOT a skill execution engine**
- The server delivers skill instructions to AI agents
- AI agents execute skills (not the server)
- Server does not run code from skills (except reading SKILL.md)

**Clarification: This is NOT an AI agent**
- Server provides tools to AI agents via MCP
- Does not make decisions or generate responses
- Clients (AI agents) use the skills

**Clarification: This is NOT a code generator**
- Skills provide instructions, not generated code
- AI agents interpret skills and generate code
- Server is infrastructure, not intelligence

---

### 23. Feature Requests: How We'll Handle

**Process for Scope Creep Prevention:**

When new feature requests arise:

1. **Ask: Is this required to deliver core value?**
   - If NO → defer to P1/P2 or reject

2. **Ask: Can we ship without it?**
   - If YES → defer it

3. **Ask: Is there a simpler version?**
   - If YES → implement simple version, document

4. **Ask: Does this belong in a different product?**
   - If YES → reject, suggest separate project

**Decision Framework:**

| Feature Request | Include? | Rationale |
|----------------|----------|-----------|
| Add skill X | Only if P0 core skill | Defer non-core skills to P1/P2 |
| Support Windows paths | Yes (NFR-020) | Cross-platform is requirement |
| Add skill search | No (P1-04) | Metadata API is P1 |
| Improve error messages | Basic only | Enhanced errors are P1 |
| Add skill templates | No (P2-08) | Custom skills are P2 |
| Support SSE transport | No (P2-05) | Stdio sufficient for MVP |
| Build Web UI | No (P2-04) | Significant effort, not core |
| Add analytics | No (P2-02) | Not core functionality |

---

## Summary: Out of Scope Rationale

**Why These Exclusions Matter:**

1. **Focus**: Enables team to deliver core value faster
2. **Quality**: More time to polish essential features
3. **Validation**: Test core hypothesis before expanding
4. **Resources**: Limited time/budget in MVP/v1.0 phase

**What Makes This the Right Scope:**

- **P0 (MVP)**: Minimum to validate hypothesis (technical feasibility, security, user value)
- **P1 (v1.0)**: Production-ready with complete features
- **P2 (Future)**: Enhancements based on user feedback and adoption

**Core Product Principle:**

> "We are building an MCP server that makes dev-swarms skills accessible to any AI agent through a secure, standardized protocol. Everything else is secondary."

---

## How to Use This Document

**For Product Team:**
- Reference when evaluating feature requests
- Cite when saying "no" to scope creep
- Update when priorities change

**For Stakeholders:**
- Understand what won't be in MVP/v1.0
- Set realistic expectations
- Identify what comes later vs. never

**For Users:**
- Understand product boundaries
- Know what alternatives exist
- Request features with realistic timeline expectations

---

Last updated: 2025-12-26
