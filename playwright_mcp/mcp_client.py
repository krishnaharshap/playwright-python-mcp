
# mcp_client.py

import os
import httpx

class MCPClient:
    def __init__(self):
        self.server_url = os.getenv("MCP_SERVER_URL")
        if not self.server_url:
            raise ValueError("MCP_SERVER_URL not set")

        self.client = httpx.AsyncClient(timeout=30)

    async def connect(self):
        print(f"[MCP] Connecting to {self.server_url}...")

        try:
            response = await self.client.get(self.server_url)
            if response.status_code != 200:
                raise RuntimeError(f"Failed to reach MCP server: {response.status_code}")
        except Exception as e:
            raise RuntimeError(f"Connection failed: {e}")

        print("[MCP] Connected.")

    async def send_context(self, context_data: dict):
        response = await self.client.post(
            self.server_url,
            json={"context": context_data}
        )
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
