from contextlib import asynccontextmanager
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
import os

# Define function to load MCP tools
@asynccontextmanager
async def get_tavily_mcp_tools():
    server_params = StdioServerParameters(
        command="python",
        args=[os.path.join(os.path.dirname(os.path.dirname(__file__)), "tavily_server.py")],
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            
            # Get tools
            tools = await load_mcp_tools(session)
            
            yield tools