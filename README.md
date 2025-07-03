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

1. **Create a requirements.txt** (recommended for version control):

   ```txt
   fastmcp==2.10.1
   # Add other dependencies here, one per line, with version numbers
   ```

2. **Create the virtual environment and install dependencies:**

   ```bash
   uv venv --python=3.12
   uv pip install -r requirements.txt
   ```

3. **Activate the virtual environment:**

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

The service will be available at `http://0.0.0.0:8000/mcp` (by default, using SSE transport as per current `server.py`).

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

**Note:**
- The Dockerfile installs `uv` and uses `uv run server.py` as the default command, ensuring consistency with local development.
- If you add a `requirements.txt`, Docker will use it to install dependencies via `uv pip install -r requirements.txt`.

---

To add more tools, simply extend `server.py` with new `@mcp.tool()` functions as needed.

---

## How to Add Your MCP Project to the OmniMCP Platform

If you are a developer or user and want to add your MCP project (or any MCP you are interested in) to the [OmniMCP platform](https://omnimcp.ai), please follow these steps:

### Submission Process
1. **Prepare your project repository** (on GitHub, Gitee, or any accessible code hosting platform).
2. **Go to [https://omnimcp.ai](https://omnimcp.ai)** and submit the repository link through the platform's add-project interface.
![image](https://github.com/user-attachments/assets/94508a12-7ce1-4143-af35-2b5ce8042be1)

### Requirements
1. **MCP Protocol Compliance:**
   - Your project must implement the MCP protocol.
2. **Stdio Mode Support:**
   - Your project must be able to start in `stdio` mode (support for `sse` and `streamable-http` is planned for the future).
3. **Dockerfile (Optional but Recommended):**
   - It is recommended to provide a `Dockerfile` for easy deployment. If you do not provide one, the platform will automatically generate a Dockerfile for deployment.
  
![image](https://github.com/user-attachments/assets/2d1f28d6-528d-4898-b63f-92cd60746883)


By following these guidelines, your MCP project can be easily integrated and showcased on the OmniMCP platform, making it accessible to a wider audience.
