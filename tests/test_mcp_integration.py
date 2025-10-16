# tests/test_mcp_integration.py

import asyncio
from playwright_mcp.mcp_adapter import run_mcp_test_flow

def test_mcp_integration():
    """Ensure MCP and Playwright integration flow runs end-to-end."""
    asyncio.run(run_mcp_test_flow())
