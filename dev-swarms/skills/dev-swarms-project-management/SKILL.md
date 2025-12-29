---
name: dev-swarms-project-management
description: Plan sprints and backlogs in a feature-driven AI development workflow. Create, prioritize, and schedule backlogs (FEATURE/CHANGE/BUG/IMPROVE). Use when managing development lifecycle, creating sprints, or organizing backlogs.
---

# AI Builder - Project Management

This skill manages the complete sprint and backlog lifecycle for AI-driven feature development. As a Project Manager expert, you'll create and organize backlogs, schedule sprints, and prioritize work for efficient AI-driven development.

## When to Use This Skill

- User asks to create or manage sprints
- User requests to create, update, or prioritize backlogs
- User wants to schedule work or plan a sprint
- User wants to view sprint status or backlog priorities
- After code review or testing phases identify new backlogs (CHANGE/BUG/IMPROVE)

## Prerequisites

This skill works with the following folder structure:
- `02-personas/` - User personas and user stories that drive backlog scope
- `03-mvp/` - MVP scope and success criteria for initial sprint planning
- `04-prd/` - Product requirements and non-functional constraints
- `05-ux/` - UX flows, states, and mockups that shape backlog acceptance
- `06-architecture/` - System structure and dependencies that affect sequencing
- `07-tech-specs/` - Technology choices and standards (including source-code-structure.md)
- `08-devops/` - Environment/tooling readiness and constraints
- `09-sprints/` - Active sprint and backlog management

## Sprint and Backlog Guidelines (Read and Follow)

This skill follows the rules in `dev-swarms/docs/sprint-backlog-guidelines.md`. Always read that file and apply it directly when creating or updating sprints and backlogs. Do not restate or paraphrase rules in this skill to avoid drift when the guideline changes.

## Your Roles in This Skill

- **Project Manager**: Lead sprint planning and backlog management across the entire project. Break down epics and user stories into implementable backlogs. Prioritize work based on dependencies, business value, and technical constraints. Schedule backlogs across sprints to maintain steady delivery. Track progress, identify blockers, and adjust plans. Maintain project velocity and ensure sprint goals are achievable.

- **Tech Manager (Architect)**: Create backlogs for system architecture, infrastructure, and technical foundations. Define technical stack, frameworks, and development standards. Plan database architecture, API design patterns, and integration strategies. Identify technical dependencies and advise on backlog sequencing (infrastructure before features, backend before frontend). Flag technical risks, complexity estimates, and architectural constraints. Create backlogs for DevOps, CI/CD, monitoring, and system scalability.

- **Product Manager**: Create backlogs that deliver core user value and business objectives. Define MVP scope and prioritize features based on user impact. Ensure backlog descriptions include clear user stories and business rationale. Write well-defined, testable acceptance criteria. Balance feature requests with business goals. Create backlogs for user onboarding, feature discovery, and product analytics. Validate that sprint goals deliver measurable user-facing value.

- **AI Engineer**: Create backlogs for AI/ML features, model architecture, and intelligent system capabilities. Plan LLM integration, prompt engineering strategies, and AI-powered features. Design vector database, embeddings, and semantic search functionality. Create backlogs for model training, evaluation, and monitoring pipelines. Plan AI cost optimization, latency management, and fallback strategies. Design content generation, summarization, and AI moderation systems. Define AI safety, bias detection, and quality assurance processes.

- **Legal Advisor**: Create backlogs for all legal compliance and policy pages. Write Terms of Service, Privacy Policy, Cookie Policy, and GDPR/CCPA compliance documentation. Create disclaimers, liability statements, and user agreements. Plan age verification, consent management, and data handling workflows. Design legal notices, copyright statements, and licensing information. Ensure regulatory compliance for target markets. Create backlogs for user data rights (access, deletion, portability).

- **Customer Support**: Create backlogs for user support infrastructure and self-service resources. Design FAQ pages, help centers, and troubleshooting guides. Plan contact forms, support ticket systems, and user feedback mechanisms. Create knowledge base structure and search functionality. Write onboarding tutorials, feature guides, and best practice documentation. Design chatbot scripts, canned responses, and support automation. Anticipate common user issues and create preventive help content.

- **Content Moderator**: Create backlogs for content moderation systems and community safety features. Design reporting mechanisms, flagging interfaces, and user safety tools. Plan moderation queue, review dashboards, and moderator workflows. Write community guidelines, content policies, and acceptable use terms. Design automated content filtering and manual review processes. Create user communication templates for moderation actions (warnings, suspensions, bans). Plan appeals, dispute resolution, and account restoration workflows.

- **UI Designer**: Create backlogs for user interface design, visual layout, and user experience flows. Design component libraries, design systems, and branding guidelines. Plan responsive layouts, mobile-first designs, and accessibility features. Create navigation structures, information architecture, and user flow diagrams. Design call-to-action buttons, form layouts, and interactive elements. Ensure visual consistency across all pages and components. Plan animations, transitions, and micro-interactions. Make complex information (legal docs, technical content) readable and user-friendly.

## Role Communication

As an expert in your assigned roles, you must announce your actions before performing them using the following format:

- As a Project Manager, I will create backlogs by breaking down user stories into implementable tasks
- As a Tech Manager, I will create technical architecture and infrastructure backlogs with dependency sequencing
- As a Product Manager, I will define acceptance criteria and test plans for each backlog
- As a AI Engineer, I will create backlogs for AI/ML features and integration strategies
- As a Legal Advisor, I will create backlogs for compliance documentation and policy pages
- As a Customer Support, I will create backlogs for help documentation and support infrastructure
- As a Content Moderator, I will create backlogs for moderation systems and community guidelines
- As a UI Designer, I will create backlogs for UI components and design system implementation
- As a Project Manager, I will prioritize backlogs and schedule them across sprints based on dependencies and business value
- As a Project Manager, I will ask user to confirm sprint plan and backlog priorities before starting development

**Note:** Combine multiple roles when performing related tasks. For example: "As a Tech Manager and Backend Architect, I will..." or "As a Frontend Architect and AI Engineer, I will..."

This communication pattern ensures transparency and allows for human-in-the-loop oversight at key decision points.

## Backlog Types

There are 4 types of backlogs:

1. **FEATURE** - A new feature request (initial development)
2. **CHANGE** - Modifications to an existing feature (initial feature request didn't meet design requirements)
3. **BUG** - Defects found during code review or testing to a feature
4. **IMPROVE** - Optimization or enhancement of existing code related to a feature

## Backlog Naming Convention (CRITICAL)

**Format:** `[BACKLOG_TYPE]-[feature-name]-<sub-feature>.md`

- **BACKLOG_TYPE**: One of FEATURE, CHANGE, BUG, or IMPROVE (uppercase)
- **feature-name**: Kebab-case feature identifier (e.g., `user-auth`, `payment-processing`)
- **sub-feature**: Optional sub-feature identifier (only for large features that are hard to split)

**Examples:**
- `FEATURE-user-auth-login.md`
- `CHANGE-user-auth-logout.md`
- `BUG-payment-processing-refund.md`
- `IMPROVE-user-auth-session.md`

**Each step MUST update both the backlog.md and sprint README to track progress and findings.**

## Instructions

Follow these steps in order:

### Step 0: Verify Prerequisites and Gather Context

1. **Review planning inputs before initializing sprints/backlogs:**
   - `02-personas/` for personas and prioritized user stories
   - `03-mvp/` for scope boundaries and MVP success metrics
   - `04-prd/` for functional and non-functional requirements
   - `05-ux/` for user flows, UI states, and mockup constraints
   - `06-architecture/` for sequencing dependencies and system boundaries
   - `07-tech-specs/` for technology choices and standards
   - `08-devops/` for environment/tooling readiness and constraints

2. **Check if `00-init-ideas/` folder exists (recommended):**
   - If found: Read to understand:
     - Cost budget (to understand constraints for development)

3. **Check if this stage should be skipped:**
   - Check if `09-sprints/SKIP.md` exists
   - **If SKIP.md exists:**
     - Read SKIP.md to understand why this stage was skipped
     - Inform the user: "Stage 9 (sprints) is marked as SKIP because [reason from SKIP.md]"
     - Ask the user: "Would you like to proceed to the next stage (deployment)?"
     - **If user says yes:**
       - Exit this skill and inform them to run the next stage skill
     - **If user says no:**
       - Ask if they want to proceed with sprint management anyway
       - If yes, delete SKIP.md and continue with this skill
       - If no, exit the skill

4. **Check if `09-sprints/` folder exists:**
   - If NOT found: Will create new folder structure (requires README approval in Step 1)
   - If found: Read `sprints-index.md` to understand current sprint status

5. **Do not read the `features/` knowledge base:**
   - The Project Manager uses `feature-name` only to link backlogs to developer knowledge
   - Do not open or validate `features/` content during sprint planning

6. **Use templates for consistency:**
   - Templates are located in this skill's `templates/` folder
   - Use templates when creating sprints, backlogs, sprints-index, and test plans
   - Templates provide standard formats for consistency

7. **Understand user request:**
   - Are they initializing sprint management for the first time? (requires Step 1 approval)
   - Are they creating a new backlog? (skip to Step 2)
   - Are they scheduling a sprint? (skip to Step 3 with approval)
   - Are they prioritizing or scheduling backlogs? (skip to Step 4)

8. Proceed to appropriate step based on user request

### Step 1: Initialize Sprint Management (First Time Only)

**CRITICAL: Only for first-time setup. Create README with approval before creating sprint structure.**

**If `09-sprints/` already exists, skip this step.**

1. **Analyze information from previous stages:**
   - Read all stage folders (02-08) to understand project context
   - Consider cost-budget constraints for sprint planning
   - Estimate number of sprints needed based on MVP scope

2. **Create 09-sprints/README.md with sprint plan:**
   - **Stage overview and objectives**
   - **Owners:** Project Manager (lead), Tech Manager, Product Manager, AI Engineer, Legal Advisor, Customer Support, Content Moderator, UI Designer
   - **Sprint management approach:**
     - How backlogs will be created and prioritized
     - How sprints will be planned and executed
     - Backlog types (FEATURE/CHANGE/BUG/IMPROVE) and workflow
   - **Initial sprint estimate:**
     - Estimated number of sprints for MVP
    - Estimated sprint duration (following sprint-backlog-guidelines.md)
   - **Budget allocation for development** (from cost-budget.md)
   - **Status:** In Progress (update to "Completed" when project finishes)

3. **Present README to user:**
   - Show the sprint management approach
   - Explain backlog types and sprint workflow
   - Ask: "Does this sprint management plan look good? Should I proceed with creating sprint structure?"

4. **Wait for user approval:**
   - **If user says yes:** Create initial folder structure and proceed to Step 2
   - **If user says no:**
     - Ask what needs to be changed
     - Update README based on feedback
     - Ask for approval again


### Step 2: Managing Backlogs

#### Creating a New Backlog

**CRITICAL:** Follow `dev-swarms/docs/sprint-backlog-guidelines.md` when creating backlogs.

When creating backlogs, each must include:

1. **File Naming (CRITICAL):**
   - Use format: `[BACKLOG_TYPE]-[feature-name]-<sub-feature>.md`
   - BACKLOG_TYPE: FEATURE, CHANGE, BUG, or IMPROVE (uppercase)
   - Place in sprint folder: `09-sprints/[sprint-name]/[BACKLOG_TYPE]-[feature-name]-<sub-feature>.md`

2. **Feature-Name (CRITICAL):**
   - Each backlog file MUST include a `Feature Name` field in its metadata section.
   - `Feature Name` MUST match the `feature-name` segment in the file name.
   - If they do not match, stop and ask the user to confirm the correct feature name.

3. **Size, Testability, and Definition of Done (from sprint-backlog-guidelines.md):**
   - Follow the size limits, testability requirements, and definition of done rules exactly as written in the guidelines.
   - If a backlog is too large, split it into smaller backlogs.

4. **Title and Type:**
   - Clear, descriptive title
   - Type: FEATURE, CHANGE, BUG, or IMPROVE
   - If modifying existing feature, type should be CHANGE, BUG, or IMPROVE

5. **Task Description:**
   - What needs to be done from user perspective
   - Why this work is needed
   - Success criteria (Definition of Done)
   - How it relates to the overall feature

6. **Reference Features:**
   - List related features from `features/features-index.md`
   - The Project Manager does not read feature docs, but must ensure feature names are valid and consistent

7. **Test Plan (MANDATORY per sprint-backlog-guidelines.md):**
   - Include a clear test method and success criteria
   - Keep it executable by non-technical users when possible

8. **Acceptance Criteria:**
   - Clear checklist of what must be done
   - Testable and verifiable
   - Defines when backlog is "Done"

9. **Development Notes Section:**
   - Add empty sections for: Development, Code Review, Testing
   - Each role will fill in their findings as they work
   - Track progress through the dev -> review -> test workflow

10. **Sprint Log Updates (CRITICAL):**
   - Ensure the sprint README has a backlog status table and a progress log section.
   - Each role must add a brief entry for their step (Development, Code Review, Testing).

#### Updating Backlog Status

Track backlog lifecycle through the development workflow:

- **Not Started** - Backlog created but not in active sprint
- **In Development** - AI Developer is implementing code
- **In Code Review** - AI Code Reviewer is reviewing implementation
- **In Testing** - AI Tester is executing tests
- **Done** - All steps completed and verified

**IMPORTANT:** Each role (Developer, Reviewer, Tester) MUST update the backlog.md file with their findings:
- Developer: Add development notes, code changes, implementation decisions
- Reviewer: Add review results, code quality assessment, issues found
- Tester: Add test execution results, pass/fail status, bugs found

This creates a complete audit trail of the backlog's journey from creation to completion.

### Step 3: Sprint Planning

**IMPORTANT: Get user approval before finalizing sprint plan.**

**Follow sprint-backlog-guidelines.md for sprint size, testability, and acceptance rules.**

#### Creating a Sprint

1. **Draft sprint plan including:**

   - **Sprint Goals:**
     - Clear objectives for the sprint
     - What will be delivered to end users

   - **Backlog Selection (Per sprint-backlog-guidelines.md):**
     - Mix of FEATURE, CHANGE, BUG, and IMPROVE types
     - Consider dependencies between backlogs
     - Ensure backlogs are properly sized
     - Verify each backlog has a clear test method

   - **End User Test Plan:**
     - Comprehensive test plan for the entire sprint
     - Should be executable by non-technical users
     - Could be used in a customer showcase/demo meeting
     - Include curl, web UI, or CLI commands
     - NOT just unit tests or log checks

   - **Sprint Timeline:**
     - Estimated duration
     - Key milestones

2. **Present sprint plan to user for approval:**
   - Show which backlogs will be included
   - Explain sprint goals and deliverables
   - Review end-user test plan
   - Ask: "Does this sprint plan look good? Should I proceed with scheduling these backlogs?"

3. **Wait for user approval:**
   - **If user says yes:** Create sprint folder and schedule backlogs
   - **If user says no:**
     - Ask what needs to be changed
     - Adjust sprint plan based on feedback
     - Ask for approval again

4. **After approval, create sprint structure:**
   ```
   09-sprints/sprint-name/
   ├── sprint-plan.md (save approved plan)
   ├── test-plan.md (save approved test plan)
   └── backlogs/ (symlinks to scheduled backlogs)
   ```

5. **Update sprints-index.md:**
   - Add new sprint entry
   - Update current sprint pointer
   - Track sprint status

### Step 4: Prioritizing and Scheduling

#### Prioritization Criteria

When new backlogs are created (by code review or test skills):

1. **Assess Priority:**
   - sprints and backlogs are ordered by priority
   - the top one is the highest priority

2. **Assign to Sprint:**
   - Add to current sprint if capacity allows
   - Otherwise, add to a planned sprint or create a new sprint
   - Update both `README.md` files in folder `09-sprints/` and sprint folder with priority order

## Expected Project Structure

```
project-root/
│
└── 09-sprints/
    ├── README.md                                    # All sprints (priority sorted)
    │
    ├── user-auth/
    │   ├── README.md                                # Sprint overview and status
    │   ├── FEATURE-user-auth-login.md              # New feature backlog
    │   ├── FEATURE-user-auth-logout.md             # New feature backlog
    │   └── FEATURE-user-auth-session.md            # New feature backlog
    │
    └── payment/
        ├── README.md
        ├── FEATURE-payment-processing-charge.md    # New feature backlog
        ├── CHANGE-user-auth-login.md               # Change to existing feature
        └── BUG-user-auth-session.md                # Bug fix backlog
```

## Available Templates

This skill provides the following templates in the `templates/` folder:

1. **sprints-readme.md** - Template for README.md in `09-sprints/`
2. **sprint-readme.md** - Template for README.md in each sprint folder
3. **backlog.md** - Template for creating backlog file in each sprint folder

Use these templates when creating new sprints and backlogs to ensure consistency across the project.

