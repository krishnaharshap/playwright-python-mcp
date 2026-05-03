import asyncio

import pytest

from playwright_mcp.config import DEFAULT_SMOKE_URL
from playwright_mcp.mcp_client import DEFAULT_MCP_ARGS, MCPClient


class FakeSession:
    def __init__(self):
        self.calls = []

    async def call_tool(self, name, arguments):
        self.calls.append((name, arguments))
        return {"ok": True, "name": name, "arguments": arguments}


def test_client_uses_playwright_mcp_stdio_defaults():
    client = MCPClient(command="npx")
    params = client.server_params()

    assert params.command == "npx"
    assert params.args == DEFAULT_MCP_ARGS
    assert "@playwright/mcp@latest" in params.args
    assert "--headless" in params.args


def test_send_context_navigates_with_playwright_mcp_tool():
    client = MCPClient(command="npx")
    client.session = FakeSession()

    result = asyncio.run(client.send_context({"url": DEFAULT_SMOKE_URL}))

    assert result["name"] == "browser_navigate"
    assert result["arguments"] == {"url": DEFAULT_SMOKE_URL}


def test_send_context_requires_url():
    client = MCPClient(command="npx")
    client.session = FakeSession()

    with pytest.raises(ValueError, match="url"):
        asyncio.run(client.send_context({}))
