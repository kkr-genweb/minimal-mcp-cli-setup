🧠 MCP Server Demo (uv, cmcp, mcp[cli])

This project sets up a lightweight Model Context Protocol (MCP) server using uv and pixi, and enables JSON-RPC tool calls via the cmcp CLI.

⸻

📦 Prerequisites
Ensure the following are installed:
	•	uv

⸻

🛠️ Add Your Server

Create server.py with your tool definitions. Example tool:

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run("stdio")

⸻

🧪 Interact with the Server

List tools:
uv run cmcp 'mcp run server.py' tools/list

Call a tool (example: add):
uv run cmcp 'mcp run server.py' tools/call name=add arguments:='{"a": 1, "b": 2}'