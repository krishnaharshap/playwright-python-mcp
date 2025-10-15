"""
main.py
Optional entry point for manual local execution of MCP + Playwright flow.
"""

import asyncio
from playwright_mcp.mcp_adapter import run_mcp_test_flow

def main():
    """Run the MCP + Playwright integration flow manually."""
    print("[INFO] Starting manual MCP + Playwright test flow...")
    asyncio.run(run_mcp_test_flow())
    print("[INFO] Test flow completed.")

if __name__ == "__main__":
    main()
