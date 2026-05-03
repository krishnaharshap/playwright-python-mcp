
# mcp_client.py

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession
import asyncio
import os

class MCPClient:
    def __init__(self):
        self.server_url = os.getenv("MCP_SERVER_URL")

    async def connect(self):
        if not self.server_url:
            raise ValueError("MCP_SERVER_URL not set")

        print(f"[MCP] Connecting to {self.server_url}...")
        # call HTTP endpoint instead of subprocess

        # Define the server parameters
        server_params = StdioServerParameters(
            command="your_command_here",  # Replace with the actual command to run your MCP server
            args=["your", "arguments", "here"],  # Replace with any arguments needed
        )

        # Use stdio_client to connect to the server
        async with stdio_client(server_params) as (read_stream, write_stream):
            self.session = ClientSession(read_stream, write_stream)
            await self.session.connect()

        print("[MCP] Connected.")

    async def send_context(self, context_data: dict):
        if self.session is None:
            raise RuntimeError("MCP session not connected.")
        result = await self.session.query({"context": context_data})
        return result

    async def close(self):
        if self.session:
            await self.session.close()
