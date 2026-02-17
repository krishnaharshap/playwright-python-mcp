# playwright_mcp/mcp_client.py

import os
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession
import asyncio

class MCPClient:
    def __init__(self, server_url: str = None):
        # Use environment variable if not provided
        self.server_url = server_url or os.getenv("MCP_SERVER_URL", "ws://localhost:8000")
        self.session = None

    async def connect(self):
        print(f"[MCP] Connecting to {self.server_url}...")

        # Get the actual MCP server command from environment or use a default
        mcp_command = os.getenv("MCP_SERVER_COMMAND", "python -m mcp.server")
        
        # Define the server parameters with actual command
        server_params = StdioServerParameters(
            command=mcp_command,
            args=[],  # Add actual arguments as needed
        )

        try:
            # Use stdio_client to connect to the server
            async with stdio_client(server_params) as (read_stream, write_stream):
                self.session = ClientSession(read_stream, write_stream)
                await self.session.connect()
            
            print("[MCP] Connected.")
        except FileNotFoundError as e:
            raise RuntimeError(f"MCP server command not found: {mcp_command}. Set MCP_SERVER_COMMAND environment variable.") from e

    async def send_context(self, context_data: dict):
        if self.session is None:
            raise RuntimeError("MCP session not connected.")
        result = await self.session.query({"context": context_data})
        return result

    async def close(self):
        if self.session:
            await self.session.close()
