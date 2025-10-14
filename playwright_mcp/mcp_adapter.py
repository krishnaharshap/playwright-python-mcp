# playwright_mcp/mcp_adapter.py

import asyncio
from .mcp_client import MCPClient

async def run_mcp_test_flow():
    client = MCPClient("wss://mcp.openai.com/v1")
    await client.connect()
    response = await client.send_context({"page": "https://example.com"})
    print("MCP Response:", response)
    await client.close()
