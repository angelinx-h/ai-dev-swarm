---
name: playwright-browser-navigate
description: "Navigate to a URL"
---

# MCP Tool: browser_navigate
Server: playwright

## Usage
Use the MCP tool `dev-swarm.request` to send the payload as a JSON string:

```json
{"server_id":"playwright","tool_name":"browser_navigate","arguments":{}}
```

## Tool Description
Navigate to a URL

## Arguments Schema
The schema below describes the `arguments` object in the request payload.
```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "description": "The URL to navigate to"
    }
  },
  "required": [
    "url"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

## Background Tasks
If the tool returns a task id, poll the task status via the MCP request tool:

```json
{"server_id":"playwright","method":"tasks/status","params":{"task_id":"<task_id>"}}
```
