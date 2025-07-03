[🇨🇳 查看中文版 (中文文档)](README_ZH.md)

## 🌐 What is MCP (Model Context Protocol)?

MCP (Model Context Protocol) is an open protocol that standardizes how applications provide context to large language models (LLMs). Think of MCP as the "USB-C port" for AI applications, offering a unified way to connect models to various data sources and tools.

### Why MCP?

- A growing list of pre-built integrations that LLMs can directly plug into
- Flexibility to switch between different LLM providers and vendors
- Best practices for securing both local and remote data

### General Architecture

MCP follows a client-server architecture, including:

- **MCP Hosts**: Programs like Claude Desktop, IDEs, or AI tools that want to access data through MCP
- **MCP Clients**: Protocol clients that maintain 1:1 connections with servers
- **MCP Servers**: Lightweight programs that expose specific capabilities through the standardized protocol
- **Local Data Sources**: Your computer's files, databases, and services
- **Remote Services**: External systems available over the internet (e.g., APIs)

### Typical Use Cases

- Building agents and AI workflows that integrate multiple data sources and tools
- Allowing LLMs to securely access local or remote resources via a standard protocol
- Rapidly integrating and switching between different LLMs and their capabilities

For more details, see the [official MCP documentation](https://modelcontextprotocol.io/introduction).

# 🚀 OmniMCP Platform: Unique Integration & API Conversion Features

## ⭐ Add Your MCP Project to the OmniMCP Platform (omnimcp.ai)

**OmniMCP is not just a deployment platform—it is a showcase and integration hub for the entire MCP ecosystem!**

If you are a developer or user and want to add your MCP project (or any MCP you are interested in) to the [OmniMCP platform](https://omnimcp.ai), please follow these steps:

### Submission Process
1. **Prepare your project repository** (on GitHub, Gitee, or any accessible code hosting platform).
2. **Go to [https://omnimcp.ai](https://omnimcp.ai)** and submit the repository link through the platform's add-project interface.

   ![image](https://github.com/user-attachments/assets/9e524017-d9cd-4d95-a55c-fb373f67c891)


### Requirements
1. **MCP Protocol Compliance:**
   - Your project must implement the MCP protocol.
2. **Stdio Mode Support:**
   - Your project must be able to start in `stdio` mode (support for `sse` and `streamable-http` is planned for the future).
3. **Dockerfile (Optional but Recommended):**
   - It is recommended to provide a `Dockerfile` for easy deployment. If you do not provide one, the platform will automatically generate a Dockerfile for deployment.

**By following these guidelines, your MCP project can be easily integrated and showcased on the OmniMCP platform, making it accessible to a wider audience.**

---

## 🌟 [EXCLUSIVE] Instantly Convert Any API to an MCP Server on OmniMCP

**OmniMCP offers a unique, industry-leading feature: Instantly convert any OpenAPI 3.0-compatible API into a fully functional MCP server—no code changes required!**

### How to Use This Feature
1. **Prepare an OpenAPI 3.0 Specification**
   - If your API already has an OpenAPI 3.0 (Swagger) document, you can use it directly. If not, generate one for your API.
   - Example OpenAPI 3.0 JSON:

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Simple API",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "http://localhost:3000"
    }
  ],
  "paths": {
    "/users": {
      "post": {
        "summary": "Create a new user",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/User"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "User created"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "User": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "email": {
            "type": "string",
            "format": "email"
          }
        },
        "required": ["name", "email"]
      }
    }
  }
}
```

2. **Submit the OpenAPI Document Link**
   - Make your OpenAPI 3.0 document accessible via a public URL (e.g., GitHub raw link, web server, etc.).
   - Go to [https://omnimcp.ai](https://omnimcp.ai), paste the link in the API-to-MCP submission form, and click submit.

   ![image](https://github.com/user-attachments/assets/8bbf984a-7586-4c88-9103-3a14921364ec)

3. **Automatic Conversion and Enhancement**
   - After submission, the OmniMCP platform will automatically convert your API into an MCP server.
   - The platform will also analyze and enhance your API documentation (e.g., API descriptions, parameter descriptions) to optimize it for AI agent usage.

Within a short time, your API will be available as an MCP server on the platform, ready for integration and use by AI agents and other clients.

  ![image](https://github.com/user-attachments/assets/f92b4cd2-7320-4304-886e-2df0164c53d3)

**These features make OmniMCP the most developer-friendly and AI-ready MCP platform available—empowering you to share, deploy, and transform your tools and APIs with unprecedented ease!**

---

# mcp-demo

This project is a minimal [fastmcp](https://github.com/jlowin/fastmcp) demo, using Python 3.12 and [uv](https://github.com/astral-sh/uv) for dependency and process management. It provides a simple MCP service with an addition tool, and supports deployment via Docker.

## 1. Project Overview

- Built with fastmcp framework for MCP protocol support.
- Provides a simple addition tool (`add`).
- Uses `uv` for both dependency management and process running.
- Exposes the service via HTTP (default: `0.0.0.0:8000/mcp`).

## 2. Development Environment

- Python 3.12
- uv (for virtual environment, dependency, and process management)
- fastmcp (installed as a dependency)

### Install Dependencies (with Version Pinning)

1. **Create the virtual environment and install dependencies:**

   ```bash
   uv venv --python=3.12
   uv pip install -r requirements.txt
   ```

2. **Activate the virtual environment:**

   - On Unix/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```cmd
     .\.venv\Scripts\activate
     ```

   After activation, you can use `uv run server.py` or other commands in the virtual environment.

## 3. How to Develop and Add New Tools

1. Define your tool function in `server.py` using the `@mcp.tool()` decorator. For example:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

2. Start the service, and the tool will be available via MCP clients.

## 4. How to Start the Service

Activate the virtual environment (see above) and run the server using uv:

```bash
uv run server.py
```

The service will be available at `http://0.0.0.0:8000/sse` inside the container.

**Note:**
- The Dockerfile installs `uv` and uses `uv run server.py` as the default command, ensuring consistency with local development.
- If you add a `requirements.txt`, Docker will use it to install dependencies via `uv pip install -r requirements.txt`.

---

To add more tools, simply extend `server.py` with new `@mcp.tool()` functions as needed.

## 5. Docker Deployment

### Set Startup Mode in Dockerfile

You can specify the startup mode (transport) directly in the Dockerfile by editing the `CMD` instruction. For example, to use stdio mode:

```dockerfile
CMD ["uv", "run", "server.py", "--transport", "stdio"]
```

To use SSE mode:

```dockerfile
CMD ["uv", "run", "server.py", "--transport", "sse"]
```

To use streamable-http mode:

```dockerfile
CMD ["uv", "run", "server.py", "--transport", "streamable-http"]
```

With this setup, you can start the container with a simple command:

```bash
docker run -d -p 8000:8000 --name mcp-demo mcp-demo:latest
```

No extra arguments are needed at runtime. To change the mode, just edit the Dockerfile and rebuild the image.

### Build the Docker Image

```bash
docker build -t mcp-demo:latest .
```

### Run the Container

```bash
docker run -d -p 8000:8000 --name mcp-demo mcp-demo:latest
```

The service will be available at `http://0.0.0.0:8000/sse` inside the container.
