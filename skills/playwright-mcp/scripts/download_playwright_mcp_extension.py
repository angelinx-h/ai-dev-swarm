#!/usr/bin/env python3
"""Download and extract the Playwright MCP Bridge Chrome extension."""

from __future__ import annotations

import argparse
import json
import os
import re
import zipfile
from pathlib import Path
from urllib.request import Request, urlopen

DEFAULT_REPO = "microsoft/playwright-mcp"
DEFAULT_ASSET_REGEX = r"(extension|chrome).*(\\.zip)$"


def _latest_release(repo: str) -> dict:
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    req = Request(url, headers={"User-Agent": "playwright-mcp-downloader"})
    with urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _pick_asset(release: dict, asset_regex: str) -> dict:
    pattern = re.compile(asset_regex, re.IGNORECASE)
    assets = release.get("assets", [])
    for asset in assets:
        name = asset.get("name", "")
        if pattern.search(name):
            return asset
    for asset in assets:
        name = asset.get("name", "")
        if name.lower().endswith(".zip"):
            return asset
    raise RuntimeError("No suitable .zip asset found in the latest release")


def _download_asset(url: str, dest: Path) -> None:
    req = Request(url, headers={"User-Agent": "playwright-mcp-downloader"})
    with urlopen(req) as resp, dest.open("wb") as handle:
        handle.write(resp.read())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo",
        default=DEFAULT_REPO,
        help="GitHub repo for Playwright MCP releases (owner/name)",
    )
    parser.add_argument(
        "--asset-regex",
        default=DEFAULT_ASSET_REGEX,
        help="Regex to select the extension zip asset",
    )
    parser.add_argument(
        "--output-dir",
        default=os.path.expanduser("~/.codex/playwright-mcp-extension"),
        help="Directory to extract the extension into",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    release = _latest_release(args.repo)
    asset = _pick_asset(release, args.asset_regex)
    zip_path = output_dir / asset["name"]
    _download_asset(asset["browser_download_url"], zip_path)

    with zipfile.ZipFile(zip_path) as archive:
        archive.extractall(output_dir)

    print(str(output_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
