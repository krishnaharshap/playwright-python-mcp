
import asyncio
import os
from contextlib import AsyncExitStack
from typing import Any

from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

from playwright_mcp.config import DEFAULT_SMOKE_URL


DEFAULT_MCP_PACKAGE = "@playwright/mcp@latest"
DEFAULT_MCP_ARGS = [
    "-y",
    DEFAULT_MCP_PACKAGE,
    "--headless",
    "--browser",
    "chrome",
    "--isolated",
]


class MCPClient:
    """Python MCP client that starts Playwright MCP over stdio."""

    def __init__(
        self,
        command: str | None = None,
        args: list[str] | None = None,
        env: dict[str, str] | None = None,
    ):
        self.command = command or os.getenv(
            "PLAYWRIGHT_MCP_COMMAND",
            "npx.cmd" if os.name == "nt" else "npx",
        )
        self.args = args or DEFAULT_MCP_ARGS.copy()
        self.env = {**os.environ, **(env or {})}
        self.session: ClientSession | None = None
        self._exit_stack: AsyncExitStack | None = None

    def server_params(self) -> StdioServerParameters:
        return StdioServerParameters(
            command=self.command,
            args=self.args,
            env=self.env,
        )

    async def connect(self):
        if self.session:
            return self.session

        self._exit_stack = AsyncExitStack()
        read, write = await self._exit_stack.enter_async_context(
            stdio_client(self.server_params())
        )
        self.session = await self._exit_stack.enter_async_context(
            ClientSession(read, write)
        )
        await self.session.initialize()
        return self.session

    async def call_tool(self, name: str, arguments: dict[str, Any] | None = None):
        if not self.session:
            raise RuntimeError("MCP not connected")

        return await self.session.call_tool(name, arguments or {})

    async def navigate(self, url: str):
        return await self.call_tool("browser_navigate", {"url": url})

    async def send_context(self, data: dict):
        url = data.get("url")
        if not url:
            raise ValueError("send_context requires a 'url' value")

        return await self.navigate(url)

    async def close(self):
        if self.session:
            try:
                await self.call_tool("browser_close")
            except Exception:
                pass

        if self._exit_stack:
            await self._exit_stack.aclose()

        self.session = None
        self._exit_stack = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()


async def navigate_with_mcp(url: str):
    async with MCPClient() as client:
        return await client.navigate(url)


if __name__ == "__main__":
    asyncio.run(navigate_with_mcp(DEFAULT_SMOKE_URL))
