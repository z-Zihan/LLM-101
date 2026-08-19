# MCP 到底是什么？

> 你现在的位置：[知识库](../08-RAG与知识库/02-知识库是什么.md) → **MCP** → [Skill](../10-Skill/01-Skill到底是什么.md)
>
> 课程导航：[上一篇：知识库是什么](../08-RAG与知识库/02-知识库是什么.md) · 第 25 / 31 篇 · [下一篇：Skill 到底是什么](../10-Skill/01-Skill到底是什么.md)
>
> 最后核验：2026-08-19

MCP（Model Context Protocol）既不是模型，也不是 Agent。它是一套开放协议，让 AI 应用用相对统一的方式连接外部工具、资源和提示。协议负责角色、能力发现、消息与生命周期规则；具体业务仍由连接两端的程序完成。

如果每个 AI 应用都为文件系统、数据库和代码平台各写一套专用适配，连接数量增长后会很难维护。MCP 希望把常见连接边界标准化，但不会把所有外部系统变成同一种能力。

## Host、Client、Server 怎样配合

面向用户的 AI 应用通常是 Host。Host 内为每个 Server 建立 Client 连接；Server 暴露受控能力，背后可以连接本地文件、远端 API 或数据库。

```text
AI Application / Host
├── MCP Client ↔ 文件 MCP Server
├── MCP Client ↔ 数据库 MCP Server
└── MCP Client ↔ 代码平台 MCP Server
```

这张图想说明 Client 不是用户界面，Server 也不等于模型服务器。读图时注意，Host 管理模型、用户体验与权限；Server 只暴露它实现并声明的 MCP 能力。

连接建立时，双方会初始化并协商能力。不能因为某程序叫 MCP Server，就假设它支持所有功能或拥有某个外部系统的全部权限。

## Tools、Resources、Prompts 分别是什么

Tools 是可请求执行的操作，例如搜索仓库或查询数据库；Resources 是应用可以读取的内容；Prompts 是 Server 提供的可复用提示模板。三者的控制方式与风险不同，不应统称为“一个工具”。

模型可能通过 Function Calling 选择某个 MCP Tool，但真正调用由 Host 和 Client 发往 Server。Resource 被读取后可以进入模型上下文，仍受上下文窗口和不可信内容风险影响。

## 协议与传输不是一回事

截至 2026-08-19 核验的 2026-07-28 规范，MCP 消息使用 JSON-RPC，并定义标准传输方式。stdio 适合 Host 启动本地 Server 并通过标准输入输出通信；Streamable HTTP 用于基于 HTTP 的连接。

```text
MCP Protocol：消息、角色、能力与生命周期规则
Transport：这些消息经由什么通道传送
```

这张图想避免把 MCP 误写成某个固定网址格式。读图时注意，同一协议可以运行在不同传输上；传输可达也不表示初始化、鉴权和能力发现已经成功。

## MCP、API 和 OpenAPI 的关系

API 是软件接口的广泛概念，OpenAPI 用机器可读文档描述 HTTP API 的路径、参数和响应。MCP 针对 AI Host 与能力提供方的连接，额外约定初始化、能力发现、工具/资源/提示等交互模型。

MCP Server 背后经常调用普通 API。它没有取代所有 API，也不会自动继承底层服务的认证和业务约束。选择 MCP 还是直接 API，要看是否需要跨 Host 的统一发现和交互，而不是追逐协议名称。

## MCP、Function Calling 和 Agent 的关系

Function Calling 让模型生成结构化调用请求；MCP 让 Client 与 Server 发现并调用外部能力；Agent 则围绕目标维护状态并反复决定下一步。三者可以串在一起，但没有谁自动包含另外两者。

普通聊天应用可以连接 MCP Resource，却没有 Agent Loop；Agent 也能直接调用本地工具，完全不使用 MCP。安装一个 MCP Server 更不等于系统获得自主规划。

## 标准连接不等于自动安全

Server 的代码、工具描述和返回内容都可能不可信。Host 仍需让用户知道连接了什么，限制凭证和数据范围，校验参数，并在发送、删除、付款等操作前获得确认。

远端内容可能包含 Prompt Injection；本地 Server 可能读取超出预期的文件。传输安全、用户授权、工具权限和业务审计是不同层，协议兼容不会自动完成它们。

## 回答真实问题

**MCP 是 API、Tool 还是 Agent？** 它是协议。MCP 可以暴露 Tool，背后可以调用 API，也可以被 Agent 使用，但不等于三者。

**OpenAPI 已能描述接口，MCP 多了什么？** MCP 面向 AI Host 约定连接生命周期、能力发现以及 Tools、Resources、Prompts 等交互；OpenAPI 主要描述 HTTP API。

**MCP Server 是模型服务器吗？** 通常不是，它主要暴露外部能力，未必托管语言模型。

**装了 MCP 就安全、就有 Agent 吗？** 都不是。权限与确认仍由实现负责，Agent 还需要目标、状态和循环。

## 从这里继续

- 拆开两端角色：[MCP 客户端和服务端是什么](./02-MCP客户端和服务端是什么.md)
- 拆开三类能力：[MCP 工具、资源和提示是什么](./03-MCP工具资源和提示是什么.md)
- 比较接口：[MCP 和 API 有什么区别](./04-MCP和API有什么区别.md)
- 返回全局：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Model Context Protocol Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28)
- [MCP Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [MCP Specification: Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
