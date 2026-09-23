"""
ryan-bowlin-mcp — a tiny Model Context Protocol (MCP) server.

Companion to the post "You down with MCP?"
https://rcbowlin1.github.io/posts/you-down-with-mcp/

The point of this file is how SHORT it is: a working MCP server in ~30 lines.
The protocol is boring on purpose — that's the feature.

Quickstart
----------
1) pip install mcp
2) Add it to your MCP client (Claude Desktop / Claude Code / Cursor, etc.).
   Example client config:

     {
       "mcpServers": {
         "ryan-bowlin-starter": {
           "command": "python",
           "args": ["/full/path/to/ryan-bowlin-mcp.py"]
         }
       }
     }

3) Restart the client. Your agent now has the tools defined below.
   No LLM API key needed to run the server — it just exposes tools.
"""

from mcp.server.fastmcp import FastMCP
import random

mcp = FastMCP("ryan-bowlin-starter")


@mcp.tool()
def roll_dice(sides: int = 6, count: int = 1) -> str:
    """Roll `count` dice with `sides` sides each; returns the rolls and their total."""
    rolls = [random.randint(1, sides) for _ in range(count)]
    return f"Rolled {count}d{sides}: {rolls}  (total: {sum(rolls)})"


@mcp.tool()
def about_ryan() -> str:
    """A short bio for Ryan Bowlin and where to find his work."""
    return (
        "Ryan Bowlin — Senior Product Manager who builds and ships production AI. "
        "Writes at https://rcbowlin1.github.io. "
        "This is the starter MCP server from his post 'You down with MCP?'."
    )


if __name__ == "__main__":
    mcp.run()  # stdio transport by default
