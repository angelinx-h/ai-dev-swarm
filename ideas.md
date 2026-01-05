Goal:
Create a tool that converts mcp tools into ai agent skills 

Why:
While mcp tools are useful, they are loaded into agent context before they need to be used, many tools will be unused and take up context which reduces the capabilities of the ai agent. Using agent skills to instead call on the mcp tools only when they are needed significantly reduces token usage while preserving the utility of mcp tools

Steps:
1. When run, it will load the mcp config and connect to the mcp servers
2. Then, it fetches the mcp tool definitions
3. Generate one `SKILL.md` file for each tool in `mcp-skills/<server-id>->-<tool-name>` making sure to use kebab-case for naming
4. Track changes with a lock file (`mcp-settings.lock`) to avoid unnecessary skill regeneration
5. Create an mcp server that acts as a bridge which forwards JSON requests to the necessary mcp tools, it should also check if the lock file has changed, if it has, tell the user to quit and restart the agent, if not, it is ready to accept tasks

Tasks:
- a new git repository should be generated and added as a submodule to /src 
- it should be written in typescript with the intention of uploading to npm upon git release (completion)
- a ci/cd pipeline should be used to verify all major changes (pull requests and before release)
- this tool is geared towards developers using AI (experts) or simply those are curious about mcp servers and agent skills (accommodates casual users)