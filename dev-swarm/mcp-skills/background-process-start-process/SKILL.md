---
name: background-process-start-process
description: "Starts a new background process (servers, watchers, etc.)."
---

# MCP Tool: start_process
Server: backgroundProcess

## Usage
Use the MCP tool `dev-swarm.request` to send the payload as a JSON string:

```json
{"server_id":"backgroundProcess","tool_name":"start_process","arguments":{}}
```

## Tool Description
Starts a new background process (servers, watchers, etc.).

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
