import os
import asyncio
import subprocess

import pytest

from playwright_mcp.config import DEFAULT_SMOKE_TITLE_TEXT, DEFAULT_SMOKE_URL
from playwright_mcp.mcp_adapter import run_mcp_test_flow


def _result_text(result):
    chunks = []
    for item in getattr(result, "content", []):
        text = getattr(item, "text", None)
        if text:
            chunks.append(text)
    return "\n".join(chunks)


def _node_major_version():
    try:
        completed = subprocess.run(
            ["node", "--version"],
            capture_output=True,
            check=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return 0

    version = completed.stdout.strip().lstrip("v")
    try:
        return int(version.split(".", 1)[0])
    except ValueError:
        return 0


@pytest.mark.skipif(
    os.getenv("RUN_PLAYWRIGHT_MCP_INTEGRATION") != "1",
    reason="live Playwright MCP stdio smoke is opt-in",
)
def test_mcp_integration():
    if _node_major_version() < 20:
        pytest.skip("@playwright/mcp@latest requires Node.js 20+ for this smoke")

    result = asyncio.run(run_mcp_test_flow(DEFAULT_SMOKE_URL))
    assert DEFAULT_SMOKE_TITLE_TEXT in _result_text(result)
