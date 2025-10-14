# playwright_mcp/mcp_client.py

from mcp import client as mcp_client  # import the lowercase module
import asyncio

class MCPClient:
    def __init__(self, server_url: str):
        self.server_url = server_url
        self.client = None

    async def connect(self):
        print(f"[MCP] Connecting to {self.server_url}...")
        self.client = mcp_client.Client(self.server_url)  # use Client via mcp_client
        await self.client.connect()
        print("[MCP] Connected.")

    async def send_context(self, context_data: dict):
        if not self.client:
            raise RuntimeError("MCP client not connected.")
        response = await self.client.query({"context": context_data})
        return response

    async def close(self):
        if self.client:
            await self.client.close()
