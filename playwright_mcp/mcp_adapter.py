# playwright_mcp/mcp_adapter.py

import asyncio
import os
from .mcp_client import MCPClient

async def run_mcp_test_flow():
    # Use environment variable or fallback to default
    server_url = os.getenv("MCP_SERVER_URL", "ws://localhost:8000")
    
    client = MCPClient(server_url)
    try:
        await client.connect()
        response = await client.send_context({"page": "https://example.com"})
        print("MCP Response:", response)
    finally:
        await client.close()
