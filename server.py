import argparse
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start MCP server with selectable transport.")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
        help="Transport mode: stdio, sse, or streamable-http (default: stdio)"
    )
    parser.add_argument("--host", default="0.0.0.0", help="Host for HTTP modes (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="Port for HTTP modes (default: 8000)")
    parser.add_argument("--path", default="/mcp", help="Path for streamable-http (default: /mcp)")

    args = parser.parse_args()

    if args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port, path=args.path)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        mcp.run(transport="stdio") 