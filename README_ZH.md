[🇺🇸 View English Version (English Doc)](README.md)

## 🌐 什么是 MCP（模型上下文协议，Model Context Protocol）？

MCP（模型上下文协议，Model Context Protocol）是一个开放协议，旨在标准化应用如何为大语言模型（LLM）提供上下文。可以把 MCP 看作 AI 应用的"USB-C 接口"，为模型与各种数据源和工具之间的连接提供统一标准。

### 为什么选择 MCP？

- 提供丰富的预构建集成，LLM 可直接接入
- 灵活切换不同的 LLM 服务商和供应商
- 遵循最佳安全实践，保护本地和远程数据

### 通用架构

MCP 采用客户端-服务器架构，主要包括：

- **MCP Host**：如 Claude Desktop、IDE 或 AI 工具，作为数据访问入口
- **MCP Client**：协议客户端，维护与服务器的 1:1 连接
- **MCP Server**：轻量级服务端，通过标准协议暴露特定能力
- **本地数据源**：如本地文件、数据库和服务
- **远程服务**：如互联网 API、外部系统等

### 典型应用场景

- 构建集成多数据源和工具的智能体/AI 工作流
- 让 LLM 通过标准协议安全访问本地或远程资源
- 快速集成和切换不同的 LLM 及其能力

更多详情请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

# 🚀 OmniMCP 平台：独特的集成与 API 转换特性

## ⭐ 将你的 MCP 项目添加到 OmniMCP 平台（omnimcp.ai）

**OmniMCP 不仅是一个部署平台，更是整个 MCP 生态的展示与集成中心！**

如果你是开发者或用户，想将你的 MCP 项目（或你感兴趣的任何 MCP）添加到 [OmniMCP 平台](https://omnimcp.ai)，请按照以下步骤操作：

### 提交流程
1. **准备你的项目仓库**（GitHub、Gitee 或任何可访问的代码托管平台）。
2. **访问 [https://omnimcp.ai](https://omnimcp.ai)**，通过平台的添加项目界面提交仓库链接。

   ![image](https://github.com/user-attachments/assets/7e26e7e3-86e9-4006-b7bb-f5a9a712681e)

### 要求
1. **MCP 协议兼容：**
   - 你的项目必须实现 MCP 协议。
2. **支持 stdio 模式：**
   - 你的项目必须能以 `stdio` 模式启动（未来将支持 `sse` 和 `streamable-http`）。
3. **Dockerfile（可选但推荐）：**
   - 推荐提供 `Dockerfile` 以便于部署。如果没有，平台会自动生成 Dockerfile 进行部署。

**按照上述要求，你的 MCP 项目将能轻松集成并展示在 OmniMCP 平台，让更多人访问和使用。**

---

## 🌟【独家】一键将任意 API 转换为 MCP 服务器

**OmniMCP 提供独特的行业领先功能：一键将任何兼容 OpenAPI 3.0 的 API 转换为完整的 MCP 服务器，无需修改代码！**

### 如何使用此功能
1. **准备 OpenAPI 3.0 规范文档**
   - 如果你的 API 已有 OpenAPI 3.0（Swagger）文档，可直接使用；否则请为你的 API 生成一个。
   - 示例 OpenAPI 3.0 JSON：

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

2. **提交 OpenAPI 文档链接**
   - 让你的 OpenAPI 3.0 文档可通过公网 URL 访问（如 GitHub raw 链接、Web 服务器等）。
   - 访问 [https://omnimcp.ai](https://omnimcp.ai)，在 API-to-MCP 提交表单中粘贴链接并提交。

   ![image](https://github.com/user-attachments/assets/8bbf984a-7586-4c88-9103-3a14921364ec)

3. **自动转换与增强**
   - 提交后，OmniMCP 平台会自动将你的 API 转换为 MCP 服务器。
   - 平台还会分析和增强你的 API 文档（如 API 描述、参数说明），优化其对 AI Agent 的友好性。

很快，你的 API 就会作为 MCP 服务器在平台上线，供 AI Agent 和其他客户端集成和使用。

![image](https://github.com/user-attachments/assets/f92b4cd2-7320-4304-886e-2df0164c53d3)

**这些特性让 OmniMCP 成为最适合开发者和 AI 场景的 MCP 平台，让你以前所未有的便捷方式分享、部署和转换工具与 API！**

---

# mcp-demo

本项目是一个基于 [fastmcp](https://github.com/jlowin/fastmcp) 的最小化演示，使用 Python 3.12 和 [uv](https://github.com/astral-sh/uv) 进行依赖和进程管理。它提供了一个简单的 MCP 服务（加法工具），并支持 Docker 部署。

## 1. 项目概述

- 基于 fastmcp 框架，支持 MCP 协议
- 提供一个简单的加法工具（`add`）
- 使用 uv 进行依赖管理和进程运行
- 通过 HTTP 暴露服务（默认：`0.0.0.0:8000/mcp`）

## 2. 开发环境

- Python 3.12
- uv（用于虚拟环境、依赖和进程管理）
- fastmcp（作为依赖安装）

### 安装依赖（版本锁定）

1. **创建虚拟环境并安装依赖：**

   ```bash
   uv venv --python=3.12
   uv pip install -r requirements.txt
   ```

2. **激活虚拟环境：**

   - Unix/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - Windows:
     ```cmd
     .\.venv\Scripts\activate
     ```

   激活后即可在虚拟环境中使用 `uv run server.py` 或其他命令。

## 3. 如何开发和添加新工具

1. 在 `server.py` 中用 `@mcp.tool()` 装饰器定义你的工具函数。例如：

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

2. 启动服务后，该工具即可通过 MCP 客户端调用。

## 4. 如何启动服务

激活虚拟环境（见上文）后，使用 uv 启动服务：

```bash
uv run server.py
```

容器内服务地址为 `http://0.0.0.0:8000/sse`

**注意：**
- Dockerfile 会安装 uv 并以 `uv run server.py` 作为默认命令，保证本地开发一致性。
- 如果添加了 `requirements.txt`，Docker 会用 `uv pip install -r requirements.txt` 安装依赖。

---

如需添加更多工具，只需在 `server.py` 中扩展新的 `@mcp.tool()` 函数。

## 5. Docker 部署

### 在 Dockerfile 中设置启动模式

你可以通过编辑 Dockerfile 的 `CMD` 指令直接指定启动模式（transport）。例如，使用 stdio 模式：

```dockerfile
CMD ["uv", "run", "server.py", "--transport", "stdio"]
```

使用 SSE 模式：

```dockerfile
CMD ["uv", "run", "server.py", "--transport", "sse"]
```