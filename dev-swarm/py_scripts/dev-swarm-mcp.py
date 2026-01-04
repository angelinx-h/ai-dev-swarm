#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import os
from pathlib import Path
from typing import Any, Mapping

from dotenv import load_dotenv
from fastmcp import FastMCP
from mcp_to_skills import build_bridge


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dev Swarm MCP Server (stdio)")
    parser.add_argument(
        "--mcp-settings",
        "--mcp_settings",
        dest="mcp_settings",
        required=True,
        help="Path to MCP settings JSON",
    )
    return parser.parse_args()

def expand_env_placeholders(value: Any, env: dict[str, str], missing: set[str]) -> Any:
    if isinstance(value, dict):
        return {key: expand_env_placeholders(child, env, missing) for key, child in value.items()}
    if isinstance(value, list):
        return [expand_env_placeholders(item, env, missing) for item in value]
    if isinstance(value, str):
        pattern = re.compile(r"\$\{([A-Za-z0-9_]+)\}")

        def replace(match: re.Match[str]) -> str:
            var = match.group(1)
            if var not in env:
                missing.add(var)
                return match.group(0)
            return env[var]

        return pattern.sub(replace, value)
    return value


def prepare_mcp_settings(settings_path: Path, env: Mapping[str, str]) -> dict[str, Any]:
    raw = json.loads(settings_path.read_text())
    missing: set[str] = set()
    expanded = expand_env_placeholders(raw, env, missing)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"Missing environment variables for MCP settings: {missing_list}")
    return expanded


def main() -> None:
    args = parse_args()
    settings_path = Path(args.mcp_settings).expanduser().resolve()
    base_dir = Path(__file__).resolve().parents[1]
    env_path = base_dir / ".env"
    load_dotenv(dotenv_path=env_path, override=True)

    settings_data = prepare_mcp_settings(settings_path, os.environ)
    bridge, lock_changed = build_bridge(
        mcp_settings_data=settings_data,
        force_refresh=False,
        output_dir=None,
        log_level="INFO",
    )

    if lock_changed:
        message = (
            "Please tell user to exit this AI coding agent and relaunch to load the latest agent skills."
        )
    else:
        message = "Please tell user I am ready to accept tasks."

    mcp = FastMCP("dev-swarm-mcp")

    @mcp.tool()
    def get_message_for_user() -> str:
        """Call this tool when the AI code agent starts."""
        return message

    @mcp.tool()
    def request(json_str: str) -> str:
        """Forward a JSON request payload from a agent skill."""
        return bridge.handle_request_json(json_str)

    mcp.run()


if __name__ == "__main__":
    main()
