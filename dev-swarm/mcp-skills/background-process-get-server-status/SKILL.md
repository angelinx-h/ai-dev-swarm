---
name: background-process-get-server-status
description: "Gets the current status of the Background Process Manager server."
---

# MCP Tool: get_server_status
Server: backgroundProcess

## Usage
Use the MCP tool `dev-swarm.request` to send the payload as a JSON string:

```json
{"server_id":"backgroundProcess","tool_name":"get_server_status","arguments":{}}
```

## Tool Description
Gets the current status of the Background Process Manager server.

## Arguments Schema
The schema below describes the `arguments` object in the request payload.
```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

## Background Tasks
If the tool returns a task id, poll the task status via the MCP request tool:

```json
{"server_id":"backgroundProcess","method":"tasks/status","params":{"task_id":"<task_id>"}}
```
