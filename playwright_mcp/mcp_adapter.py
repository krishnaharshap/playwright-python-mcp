from playwright_mcp.config import DEFAULT_SMOKE_URL
from playwright_mcp.mcp_client import MCPClient


async def run_mcp_test_flow(url: str = DEFAULT_SMOKE_URL):
    async with MCPClient() as client:
        navigate_result = await client.send_context({"url": url})
        title_result = await client.call_tool(
            "browser_evaluate",
            {"function": "() => document.title"},
        )

    print("[MCP NAVIGATE RESPONSE]", navigate_result)
    print("[MCP TITLE RESPONSE]", title_result)
    return title_result
