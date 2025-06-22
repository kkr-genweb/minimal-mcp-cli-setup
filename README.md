🧠 MCP Server Demo (via pixi, uv, cmcp, mcp[cli])

This project sets up a lightweight Model Context Protocol (MCP) server using uv and pixi, and enables JSON-RPC tool calls via the cmcp CLI.

⸻

📦 Prerequisites

Ensure the following are installed:
	•	Pixi
	•	uv (Pixi handles this automatically)
	•	Python ≥3.11

⸻

⚙️ Project Setup

# Create a Pixi-managed project
pixi init mcp-server-demo
cd mcp-server-demo/

# Initialize Python environment
uv init

# Add dependencies
uv add "mcp[cli]"
uv add cmcp  # ensure compatibility with mcp version (e.g. 1.8.0)


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

⸻

📁 Optional: requirements.txt (if used)

mcp[cli]==1.8.0
cmcp==0.2.0

Install using:

uv pip install -r requirements.txt


⸻

🧾 Optional: cmcp_commands.sh

#!/bin/bash

# List all tools
uv run cmcp 'mcp run server.py' tools/list

# Call example
uv run cmcp 'mcp run server.py' tools/call name=add arguments:='{"a": 1, "b": 2}'