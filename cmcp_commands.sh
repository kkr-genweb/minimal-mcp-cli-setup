#!/bin/bash

# This script provides example commands to interact with the MCP server.
# Ensure you have initialized the project with `pixi install` before running this.

echo "Listing available tools..."
pixi run cmcp 'mcp run server.py' tools/list

echo -e "\nCalling the 'add' tool with a=1 and b=2..."
pixi run cmcp 'mcp run server.py' tools/call name=add arguments:='{"a": 1, "b": 2}'

echo -e "\nAccessing the 'greeting' resource for name 'User'..."
pixi run cmcp 'mcp run server.py' resources/get uri=greeting://User
