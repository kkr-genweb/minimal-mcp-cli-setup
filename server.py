# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("DemoServer") # It's good practice to give your server a unique name


# Example tool: Add two numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# To run the server directly (e.g., for development or simple stdio communication)
if __name__ == "__main__":
    # mcp.run() defaults to "stdio" if no arguments are given
    # "stdio" means it will listen for requests on standard input
    # and send responses to standard output.
    mcp.run()