#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from pathlib import Path

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


def load_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    env: dict[str, str] = {}
    for line in path.read_text().splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("export "):
            stripped = stripped[len("export ") :].lstrip()
        if "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if (value.startswith("'") and value.endswith("'")) or (
            value.startswith('"') and value.endswith('"')
        ):
            value = value[1:-1]
        env[key] = value
    return env


def main() -> None:
    args = parse_args()
    settings_path = Path(args.mcp_settings).expanduser().resolve()
    base_dir = Path(__file__).resolve().parents[1]
    env_path = base_dir / ".env"
    env_vars = load_env_file(env_path)
    for key, value in env_vars.items():
        os.environ.setdefault(key, value)

    bridge, lock_changed = build_bridge(
        mcp_settings_path=settings_path,
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
