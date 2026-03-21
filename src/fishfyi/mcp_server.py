"""MCP server for fishfyi — AI assistant tools for fishfyi.com.

Run: uvx --from "fishfyi[mcp]" python -m fishfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("FishFYI")


@mcp.tool()
def list_fish(limit: int = 20, offset: int = 0) -> str:
    """List fish from fishfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from fishfyi.api import FishFYI

    with FishFYI() as api:
        data = api.list_fish(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No fish found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_fish(slug: str) -> str:
    """Get detailed information about a specific fish.

    Args:
        slug: URL slug identifier for the fish.
    """
    from fishfyi.api import FishFYI

    with FishFYI() as api:
        data = api.get_fish(slug)
        return str(data)


@mcp.tool()
def list_families(limit: int = 20, offset: int = 0) -> str:
    """List families from fishfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from fishfyi.api import FishFYI

    with FishFYI() as api:
        data = api.list_families(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No families found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_fish(query: str) -> str:
    """Search fishfyi.com for fish species, families, and habitats.

    Args:
        query: Search query string.
    """
    from fishfyi.api import FishFYI

    with FishFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
