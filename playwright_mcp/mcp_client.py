
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

    # Do NOT enforce GET check — just validate URL exists
    if not self.server_url.startswith("http"):
        raise ValueError("Invalid MCP_SERVER_URL")

    print("[MCP] Connection config valid.")

    async def send_context(self, context_data: dict):
    response = await self.client.post(
        self.server_url,
        json={"context": context_data}
    )

    if response.status_code >= 400:
        raise RuntimeError(f"Request failed: {response.status_code}")

    return response.json()
    
    async def close(self):
        await self.client.aclose()
