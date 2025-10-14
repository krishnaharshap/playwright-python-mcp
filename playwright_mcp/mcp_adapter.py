# playwright_mcp/mcp_adapter.py

import asyncio
from playwright.sync_api import sync_playwright
from playwright_mcp.mcp_client import MCPClient

async def run_mcp_test_flow():
    """Run Playwright test with MCP reasoning support."""
    # Connect to a local MCP server or model endpoint
    mcp = MCPClient("wss://mcp.openai.com/v1")  # Example placeholder
    await mcp.connect()

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        title = page.title()

        print(f"[Playwright] Page title: {title}")

        # Send the title as context to MCP
        response = await mcp.send_context({"title": title})
        print(f"[MCP] Response: {response}")

        browser.close()

    await mcp.close()

if __name__ == "__main__":
    asyncio.run(run_mcp_test_flow())
