# Ideas

This is the starting point for your AI-powered development project.

## Purpose

This file serves as the "start engine" of the AI builder. Document your initial ideas, problems you want to solve, and vision for your project here.

## How to Use

1. Write down your project ideas in plain language
2. Describe the problem you're trying to solve
3. Outline who your target users are
4. Share any requirements or constraints

The AI will use this as the foundation to guide you through the development process, from market research to deployment.

## Your Ideas

Some AI agents don't have built-in skills support, so we need to create an MCP server to implement the dev-swarms agent skills feature.

How the MCP server should work:
1. Using stdio transport
2. When launched, read dev-swarms/skills
3. Each skill will be published as an MCP tool
4. Once the agent calls the tool, it will return the SKILL.md content as a system prompt to inject the skill context into the current agent session contents
5. Since dev-swarms/skills are in the same project that the AI agent is working on, we don't need to include any files in the subfolders, but we need to update the file paths to be relative to the project root before returning to the MCP client, so the AI agent can read the files as needed
6. For any script, tell the AI agent to invoke it as an instruction, and do not read the script content

Using Python FastMCP and uv to manage the Python environment

ref to: https://code.claude.com/docs/en/skills