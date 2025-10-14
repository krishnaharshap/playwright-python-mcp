# playwright_mcp/mcp_client.py

from mcp import Client, connect_websocket
import asyncio
import json

class MCPClient:
    def __init__(self, server_url: str):
        self.server_url = server_url
        self.client = None

    async def connect(self):
        print(f"[MCP] Connecting to {self.server_url}...")
        self.client = await connect_websocket(self.server_url)
        print("[MCP] Connected.")

    async def send_context(self, context_data: dict):
        """Send context (like page title or state) to MCP model for reasoning."""
        if not self.client:
            raise RuntimeError("MCP client not connected.")
        response = await self.client.query({"context": context_data})
        return response

    async def close(self):
        if self.client:
            await self.client.close()
