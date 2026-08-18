# MCP Client 和 Server 是什么？

> Level: `Core` · Path: `Main`
>
> 最后核验：2026-08-18

## 一个小白真的会怎么问？

> MCP Client、Host、Server 为什么有三个角色？
>
> Server 一定是互联网上的一台服务器吗？

## 先说人话

在 MCP 中，Host 是用户使用的 AI 应用；Client 是 Host 内负责一条 MCP 连接的协议组件；Server 通过这条连接提供 Tools、Resources 或 Prompts。

```text
User
 ↓
Host Application
 ├── Client A ↔ Server A
 └── Client B ↔ Server B
```

## 举个例子

一个桌面 AI 应用同时连接本地文件与远程项目管理系统：

- 桌面应用是 Host；
- 它为每个连接创建相应 MCP Client；
- 文件程序和项目管理适配程序分别扮演 MCP Server。

Server 可以是本地进程，也可以通过网络连接，不一定是机房里单独的一台机器。

## 三个角色分别负责什么？

### Host

Host 管理用户体验、模型、权限、多个 Client、用户同意与安全策略。它决定哪些能力可进入模型 Context，哪些调用需要确认。

### Client

Client 与一个 Server 建立有状态连接，完成初始化、能力协商、协议消息交换和通知处理。它不是面向用户的完整产品。

### Server

Server 声明并实现它提供的能力。它可能访问本地文件、普通 API、数据库或其他系统，但只能在获得的权限与实现边界内工作。

## 一条连接怎样开始？

简化流程是：

```text
建立 Transport
   ↓
Client 与 Server 交换版本和能力
   ↓
确认初始化完成
   ↓
发现并使用双方支持的功能
   ↓
连接关闭
```

不能在协商前假定 Server 支持所有 MCP 功能；版本或能力不兼容时应安全失败。

## Transport 是什么？

Transport（传输）负责把 JSON-RPC 消息从一端送到另一端。当前规范定义 stdio 和 Streamable HTTP 等标准传输。

- stdio 常用于 Host 启动并连接本地子进程；
- Streamable HTTP 适合通过 HTTP 连接独立服务。

协议消息、Client / Server 角色与 Transport 是不同层次。使用 HTTP 不会让 MCP 自动等同于 REST API。

## 为什么一个 Server 对应一个 Client？

每条连接有自己的能力、状态和安全边界。Host 可以管理多个 Client，把不同 Server 隔离开，避免一个连接直接拥有其他连接的全部状态。

这不表示 Host 永远只能创建一个连接实例；具体生命周期取决于应用实现。

## 最容易搞混的东西

### MCP Client ≠ 用户使用的 App

App 通常是 Host，Client 是它内部负责协议连接的组件。

### MCP Server ≠ Model Server

MCP Server 主要暴露 Context 与操作能力，不一定托管或运行语言模型。

### Server ≠ 远程机器

Client / Server 是协议角色。本地进程也可以是 MCP Server。

### 连接成功 ≠ 能力可信

初始化成功只说明协议可以通信，不证明 Tool 安全、数据正确或权限合理。

## 常见误区

### 误区 1：Client 能自行绕过 Host 权限

Host 应掌握授权与用户同意。实现若把权限全部交给模型或 Server，会破坏安全边界。

### 误区 2：一个 MCP Server 可以自动看到整个电脑

它只能获得操作系统、凭证和 Host 实际授予的访问。应坚持最小权限。

### 误区 3：所有 MCP Server 都有相同功能

Server 可以只支持 Tools、Resources、Prompts 中的一部分，具体以能力协商和发现结果为准。

## 你只需要记住

1. Host 是 AI 应用，Client 管理一条协议连接，Server 暴露具体能力。
2. Client / Server 是协议角色，不等于独立产品或物理机器。
3. 连接先协商版本和能力，再使用双方支持的功能。
4. Transport 只负责传递消息，安全授权仍由 Host 与实现系统落实。

## 继续学习

- [上一篇：MCP 是什么](./01-what-is-mcp.md)
- [下一篇：MCP Tools、Resources、Prompts 是什么](./03-tools-resources-prompts.md)

## 资料与核验

- [MCP Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [MCP Specification: Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports)
