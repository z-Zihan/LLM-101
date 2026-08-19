# MCP 客户端和服务端是什么？

> 所属专题：MCP · 前置：[MCP 到底是什么](./01-MCP到底是什么.md) · 后续：[MCP 工具、资源和提示是什么](./03-MCP工具资源和提示是什么.md)
>
> 最后核验：2026-08-19

MCP 为什么同时有 Host、Client、Server 三个角色？因为面向用户的 AI 应用、管理一条协议连接的组件、提供具体能力的程序，承担不同责任。把三者都叫“客户端和服务器”，会看不见权限与生命周期边界。

## 一台桌面应用连接两个系统

桌面 AI 应用既要读取本地文件，又要连接远程项目平台。桌面应用是 Host；它为两条连接分别管理 MCP Client；文件适配程序和项目平台适配程序分别扮演 MCP Server。

```text
User
  ↓
AI Application / Host
├── MCP Client A ↔ 本地文件 MCP Server
└── MCP Client B ↔ 项目平台 MCP Server
```

这张图想说明一个 Host 可以管理多个隔离连接。读图时注意，Server 是协议角色，不是物理机器：本地子进程同样可以是 MCP Server。

## 三个角色分别掌握什么

Host 管理用户体验、模型、多个 Client、用户同意和整体安全策略。它决定哪些 Server 可连接、哪些能力展示给模型，以及哪些操作要确认。

Client 位于 Host 内，负责与某个 Server 交换 MCP 消息，完成初始化、能力协商、请求、响应和通知处理。它不是用户独立使用的完整产品，也不应绕过 Host 自行扩大权限。

Server 声明并实现 Tools、Resources 或 Prompts。它可能连接文件、数据库和普通 API，但只能在操作系统、凭证及自身实现授予的范围内工作。连接成功不会让它自动看到整台电脑。

## 一条连接不是打开端口就完成

简化生命周期包括建立传输、交换协议版本与能力、完成初始化、发现和使用双方支持的功能，最后关闭连接。版本不兼容或能力未声明时，应明确失败，而不是猜测 Server 支持什么。

```text
建立 Transport
  ↓ 初始化并协商版本、能力
  ↓ 发现 Tools / Resources / Prompts
  ↓ 请求、响应与通知
  ↓ 关闭连接
```

这张图想区分“能传消息”和“协议已就绪”。读图时注意，Transport 可达只是第一步；能力发现、认证和业务权限仍可能失败。

stdio 常用于 Host 启动本地 Server，通过标准输入输出交换消息；Streamable HTTP 用于 HTTP 连接。Transport 负责搬运 JSON-RPC 消息，不改变 Host、Client、Server 的职责，也不会自动把 MCP 变成 REST API。

## 为什么每条连接要保留边界

不同 Server 有不同来源、权限、能力和故障状态。Host 分别管理连接，能避免一个 Server 直接获得另一条连接的上下文与凭证。是否共享某些结果，应由 Host 明确决定。

Server 返回内容也可能错误或包含恶意指令。Host 在送入模型上下文前要控制范围，并为写入类 Tool 做参数校验和确认。协议握手成功只证明双方能按格式通信，不证明能力可信。

## 回答常见问题

**MCP Client 是用户打开的 App 吗？** 通常不是，App 是 Host，Client 是内部连接组件。

**MCP Server 一定在互联网上吗？** 不一定，本地进程也能扮演 Server。

**MCP Server 是模型服务器吗？** 通常不是，它主要暴露工具或上下文能力。

**所有 Server 功能一样吗？** 不一样，具体能力取决于协商和发现结果。

## 从这里继续

- [MCP 工具、资源和提示是什么](./03-MCP工具资源和提示是什么.md)
- [MCP 和 API 有什么区别](./04-MCP和API有什么区别.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [MCP Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [MCP Specification: Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports)
