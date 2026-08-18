# MCP 是什么？

> Level: `Core` · Path: `Main`

> 最后核验：2026-08-18

## 一个小白真的会怎么问？

> MCP 是 API、Tool，还是 Agent？

## 先说人话

MCP（Model Context Protocol）是一套开放协议，让 AI 应用以统一方式连接外部 Tools、Resources 和 Prompts。

它定义“怎样发现能力、交换消息和请求调用”，不是模型、Agent 或某一个具体工具。

## 举个例子

没有统一协议时，一个 AI 应用连接文件、数据库和代码平台，可能各写一套适配代码。

使用 MCP 后，应用可以作为 Host，通过 MCP Client 连接不同 MCP Server：

```text
AI Application / Host
  ├── MCP Client ↔ 文件 Server
  ├── MCP Client ↔ 数据库 Server
  └── MCP Client ↔ 代码平台 Server
```

统一的是通信方式，不是把所有外部系统变成同一种能力。

## 核心角色

- Host：面向用户的 AI 应用，管理权限、模型和多个连接；
- Client：Host 内与某个 Server 保持协议连接的组件；
- Server：暴露 Tools、Resources、Prompts 等能力的程序。

一个 Host 可以连接多个 Server，通常为每个 Server 建立对应 Client 连接。

## MCP 能暴露什么？

- Tools：可由模型请求调用的操作；
- Resources：应用可读取并提供给模型的内容；
- Prompts：Server 提供的可复用提示模板。

具体可用能力要经过初始化与能力协商，不能假设所有 Server 都支持全部功能。

## MCP 怎样通信？

当前规范使用 JSON-RPC 传递协议消息，并定义 stdio、Streamable HTTP 等标准传输方式。

```text
协议：消息和生命周期规则
传输：消息通过什么通道发送
```

因此 MCP 不是“只能走网络的一个 REST API”，也不等于某一种传输。

## MCP 和 API 的区别

API 是软件接口的广泛概念；MCP 是面向 AI 应用与 Context / Tool 连接场景的具体协议。

MCP Server 背后可以调用普通 API、数据库或本地程序。MCP 没有取代所有 API。

## MCP 和 Function Calling 的区别

Function Calling 让模型输出结构化调用请求；MCP 负责 Client 与 Server 之间发现和调用工具等协议交互。

应用可以把 MCP Tool 转换成模型可用的工具定义，再使用 Function Calling 选择调用。

## MCP 和 Agent 的区别

Agent 围绕目标决定步骤并运行循环；MCP 提供连接外部能力的标准方式。

普通聊天应用也能使用 MCP，Agent 也能完全不使用 MCP。二者不是父子关系。

## 安全由谁负责？

协议连接不自动代表 Server、Tool 或返回内容可信。Host 仍需：

- 展示和获取用户同意；
- 验证 Tool 输入与权限；
- 限制 Server 可访问的数据；
- 对敏感或破坏性操作要求确认；
- 防止凭证泄露和恶意返回内容；
- 记录调用并处理失败。

## 常见误区

### 误区 1：装了 MCP 就拥有 Agent

不对。MCP 提供连接；Agent 还需要目标、模型、状态与控制循环。

### 误区 2：MCP Server 就是模型服务器

不一定。它通常暴露工具或 Context 能力，未必托管语言模型。

### 误区 3：MCP Tool 一定安全

工具来自哪里、使用什么权限和会造成什么副作用，都需要独立审查。

## 你只需要记住

1. MCP 是 AI 应用连接 Tools、Resources 和 Prompts 的开放协议。
2. Host 管理应用与权限，Client 连接 Server，Server 暴露具体能力。
3. MCP 不等于 API、Function Calling、Agent 或模型，但可以与它们组合。
4. 接入 MCP 不自动可信，授权、确认和隔离仍由实现系统负责。

## 继续学习

- [上一篇：RAG 有哪些局限](../08-rag/12-rag-limitations.md)
- [下一篇：MCP Client 和 Server 是什么](./02-client-server.md)
- [相关：AI Tool 是什么](../06-tools/02-tool.md)

## 资料与核验

- [Model Context Protocol Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28)
- [MCP Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [MCP Specification: Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
