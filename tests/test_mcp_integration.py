# tests/test_mcp_integration.py

import os
import pytest
import asyncio
from playwright_mcp.mcp_adapter import run_mcp_test_flow

@pytest.mark.skipif(not os.getenv("MCP_SERVER_URL"), reason="MCP server not configured")
def test_mcp_integration():
    asyncio.run(run_mcp_test_flow())
