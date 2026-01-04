---
name: dev-swarm-refine-mcp-skill-descriptions
description: Review and refine MCP skill descriptions to follow the agent skill specification, and record approved overrides in dev-swarm/mcp_descriptions.json. Use when the user asks to update one MCP skill description, all skills from a server, or all MCP skills.
---

# AI Builder - Refine MCP Skill Descriptions

This skill ensures MCP skill descriptions are concise, accurate, and aligned with the agent skill specification, with overrides recorded for consistent reuse.

## When to Use This Skill

- User asks to refine a specific MCP skill description.
- User asks to refine all MCP skills for a server.
- User asks to refine all MCP skills under dev-swarm/mcp-skills.

## Your Roles in This Skill

- **Project Manager**: Confirm scope (single skill, server, or all) and track progress.
- **Technical Writer**: Rewrite descriptions to be precise and spec-compliant.
- **Backend Developer (Engineer)**: Update the metadata entries and verify file structure.

## Role Communication

As an expert in your assigned roles, you must announce your actions before performing them using the following format:

As a {Role} [and {Role}, ...], I will {action description}

This communication pattern ensures transparency and allows for human-in-the-loop oversight at key decision points.

## Instructions

Follow these steps in order:

### Step 1: Identify Scope

Clarify whether the request targets:
- One MCP skill
- All MCP skills for a specific server
- All MCP skills under `dev-swarm/mcp-skills/`

### Step 2: Inspect Current Descriptions

For each target `dev-swarm/mcp-skills/**/SKILL.md`:
- Read the YAML frontmatter `description`
- Verify it follows the agent skill specification:
  - Explains what the tool does
  - Explains when to use it
  - Includes relevant keywords
  - 1-1024 characters, concise and single-paragraph

### Step 3: Refine Descriptions

If the description is too long, too short, or missing context:
- Rewrite it to be concise and precise
- Preserve any critical constraints (e.g., required prerequisites)
- Avoid multi-line or overly verbose wording
If the description already meets the specification, do not modify the skill or add an override entry.

### Step 4: Record Overrides

Update or create `dev-swarm/mcp_descriptions.json` with:

```json
{
  "skill-name": "Updated description"
}
```

- Use the skill name from the `name:` field in the SKILL.md frontmatter.
- Add or update entries for every refined description.

### Step 5: Save Changes

Apply edits to the relevant `SKILL.md` files and ensure the JSON file is valid.

## Expected Output

- Updated MCP skill descriptions in `dev-swarm/mcp-skills/**/SKILL.md`
- `dev-swarm/mcp_descriptions.json` containing the refined descriptions
