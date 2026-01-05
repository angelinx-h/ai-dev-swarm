# Stage 7: Technical Specifications

**Owner:** Tech Manager (Architect)
**Attendances:** Backend Developer, DevOps Engineer

**Project Level:** L2 - Tool with Environment Setup

## Overview

This is an L2 project requiring minimal, focused technical specifications. Following research-specs-rules.md, we keep documentation concise for expert developers - listing decisions and constraints, not tutorials or descriptions.

## Objectives

1. Define the technology stack (language, framework, dependencies)
2. Establish coding standards (linting, formatting, TypeScript strict mode)
3. Document source code structure (single-file organization per project constraints)
4. Define testing standards (unit tests, integration tests, minimum coverage)

## Methodology

**For L2 Projects (Per research-specs-rules.md):**
- **Concise** - List dependencies, don't describe them
- **Decisions over Descriptions** - "Chose X over Y because of Z constraint"
- **Expert Audience** - No tutorials, no generic boilerplate
- **Security** - Focus on input validation and file permission safety (localhost tool)

**Source Requirements:**
- `00-init-ideas/owner-requirement.md` - Technical constraints and dependencies
- `04-prd/non-functional-requirements.md` - Performance, compatibility, security targets
- `ideas.md` - Single-file implementation constraint (~800-900 lines)

## Deliverables Planned

1. **tech-stack.md** - Technology selections with rationale:
   - Language: TypeScript (why: type safety, npm ecosystem)
   - Runtime: Node.js 18+ (why: LTS, modern APIs)
   - Dependencies: Zod, Commander.js, Express (minimal set)
   - Dev Tools: TypeScript compiler, ESLint, Prettier

2. **coding-standards.md** - Code quality rules:
   - TypeScript strict mode enabled
   - Linting: ESLint with recommended rules
   - Formatting: Prettier (2-space indent, single quotes)
   - Naming: camelCase functions, PascalCase classes
   - Single-file constraint (~800-900 lines total)

3. **source-code-structure.md** - Code organization within src/index.ts:
   - Component order: Types → Clients → Manager → Utilities → Generator → Bridge → Server → Main
   - Clear function separation despite single-file constraint
   - Follows dev-swarm/docs/source-code-structure.md guidance

4. **testing-standards.md** - Test requirements:
   - Unit tests for core functions (hash, naming conversion, config loading)
   - Integration tests for CLI commands (sync, start)
   - Smoke tests for HTTP bridge
   - Minimum coverage: 80%
   - Testing framework: Jest or Vitest

## Budget Allocation

**Stage Budget:** 30,000 - 50,000 tokens (~$2-$3)

Activities:
- Define tech stack with rationale
- Specify coding standards and tooling
- Document single-file code organization
- Define testing standards and coverage

## Status

**In Progress** - Awaiting user approval to proceed with documentation creation
