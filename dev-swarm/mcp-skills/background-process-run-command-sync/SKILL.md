---
name: background-process-run-command-sync
description: "Runs a short-lived shell command synchronously and returns full output."
---

# MCP Tool: run_command_sync
Server: backgroundProcess

## Usage
Use the MCP tool `dev-swarm.request` to send the payload as a JSON string:

```json
{"server_id":"backgroundProcess","tool_name":"run_command_sync","arguments":{}}
```

## Tool Description
Runs a short-lived shell command synchronously and returns full output.

## Arguments Schema
The schema below describes the `arguments` object in the request payload.
```json
{
  "type": "object",
  "properties": {
    "command": {
      "type": "string"
    }
  },
  "required": [
    "command"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

## Background Tasks
If the tool returns a task id, poll the task status via the MCP request tool:

```json
{"server_id":"backgroundProcess","method":"tasks/status","params":{"task_id":"<task_id>"}}
```
