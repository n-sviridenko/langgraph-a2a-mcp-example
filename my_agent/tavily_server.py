from typing import Optional
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the MCP server
mcp = FastMCP("TavilySearch")

@mcp.tool()
async def tavily_search(query: str, max_results: Optional[int] = 1) -> str:
    """Search the internet using Tavily Search API."""
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        return "Error: TAVILY_API_KEY not found in environment variables."
    
    client = TavilyClient(api_key=tavily_api_key)
    response = client.search(query=query, max_results=max_results)
    
    if not response.get("results"):
        return "No results found."
    
    formatted_results = []
    for idx, result in enumerate(response["results"], 1):
        formatted_results.append(f"{idx}. {result['title']}")
        formatted_results.append(f"URL: {result['url']}")
        formatted_results.append(f"{result['content']}")
        formatted_results.append("")
    
    return "\n".join(formatted_results)

if __name__ == "__main__":
    mcp.run(transport="stdio") 