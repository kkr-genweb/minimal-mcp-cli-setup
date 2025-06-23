# 🧠 MCP Server Demo 

This project sets up a lightweight **Model Context Protocol (MCP)** server using uv, enabling JSON-RPC tool calls via the cmcp CLI.
## **📦 Prerequisites**
Install uv if not already installed:
```
curl -Ls https://astro.build/install | bash
```
## 🛠️ Add Your Server
Create a server.py file with your tool definitions. Here’s an example:
```
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run("stdio")
```
## 🧪 Interact with the Server in the Terminal

### List Available Tools
```
uv run cmcp 'mcp run server.py' tools/list
```
### Call a Tool 
```
uv run cmcp 'mcp run server.py' tools/call name=add arguments:='{"a": 1, "b": 2}'
```