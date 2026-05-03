# playwright_mcp/mcp_adapter.py

import os
from playwright_mcp.mcp_client import MCPClient

async def run_mcp_test_flow():
    client = MCPClient()

    await client.connect()

    result = await client.send_context({
        "test": "playwright execution",
        "status": "success"
    })

    print("[MCP RESPONSE]", result)

    await client.close()
