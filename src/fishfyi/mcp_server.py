"""MCP server for fishfyi."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from fishfyi.api import FishFYI

mcp = FastMCP("fishfyi")


@mcp.tool()
def search_fishfyi(query: str) -> dict[str, Any]:
    """Search fishfyi.com for content matching the query."""
    with FishFYI() as api:
        return api.search(query)
