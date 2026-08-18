# MCP 和 API 有什么区别？

> Level: `Core` · Path: `Main`
>
> 最后核验：2026-08-18

## 先说人话

API 是软件接口的广泛概念；MCP 是面向 AI 应用连接外部 Context 与 Tools 的具体开放协议。

MCP Server 经常在内部调用现有 API。它不是为了取代所有 API，而是为 AI Host 提供一致的发现、连接和调用方式。

## 举个例子

一个项目管理平台已有 REST API：创建任务、查询项目、修改状态。

MCP Server 可以把这些 API 包装成 MCP Tools：

```text
AI Host
 ↓ MCP
MCP Server
 ↓ 平台 API
项目管理系统
```

MCP 处理 AI 应用侧的协议交互，平台 API 仍定义真正的业务操作与数据。

## 核心区别

| 维度 | API | MCP |
|---|---|---|
| 范围 | 软件接口的广泛概念 | 特定的开放协议 |
| 主要对象 | 任意软件调用方与服务 | AI Host / Client 与 MCP Server |
| 发现能力 | 由具体 API 文档或机制决定 | 定义 Tools、Resources、Prompts 的发现方式 |
| 生命周期 | 因 API 而异 | 定义初始化、能力协商与协议消息 |
| 传输 | HTTP、函数调用、消息队列等多种形式 | 当前规范定义 stdio、Streamable HTTP 等 |

## MCP 是不是一种 API？

从广义上说，MCP 确实定义了程序之间的接口；但教学上更准确的说法是：API 是上位概念，MCP 是为特定场景设计的一套协议。

就像“交通工具”和“地铁”有关，但不能把所有交通工具都叫地铁。

## 为什么不直接让模型调用业务 API？

应用当然可以直接集成 API。MCP 的价值在于把常见连接方式标准化，让 Host 能用相对一致的方法：

- 协商能力；
- 发现 Tools、Resources、Prompts；
- 管理多个 Server 连接；
- 交换结构化协议消息。

是否值得增加 MCP 层，取决于复用、生态、权限和运维需求。单一简单集成不一定需要 MCP。

## 权限放在哪里？

两层都可能需要安全控制：

- Host / MCP 层决定用户是否允许模型请求某项能力；
- 业务 API 层验证身份、资源权限和业务规则。

不能因为 MCP Host 已确认，就让后端 API 跳过授权；也不能因为 API 有鉴权，就省略对模型操作的用户确认。

## 最容易搞混的东西

### MCP ≠ REST

REST 是常见 Web API 风格；MCP 使用 JSON-RPC 消息并可通过不同 Transport 传输。

### MCP Server ≠ API Gateway

两者可能都连接后端服务，但职责和协议不同。MCP Server 面向 MCP 能力，API Gateway 处理 API 路由、鉴权等通用网关问题。

### 标准化 ≠ 零适配

Server 仍要把具体业务 API、数据和权限转换成合适的 MCP 能力。

## 常见误区

### 误区 1：有 MCP 就不需要 API

很多 MCP Server 正是建立在 API 之上，业务系统仍需要自己的接口。

### 误区 2：任何 API 自动就是 MCP Server

必须实现 MCP 生命周期、消息和能力接口，普通 API 才能通过 MCP 被 Host 使用。

### 误区 3：MCP 让所有工具完全兼容

协议格式统一，不代表不同工具的语义、权限和返回质量相同。

## 你只需要记住

1. API 是广泛的软件接口概念，MCP 是面向 AI 连接场景的具体协议。
2. MCP Server 可以包装普通 API，但不会取代业务 API。
3. MCP 标准化能力发现、生命周期和消息交互，不统一所有业务语义。
4. Host 确认与后端 API 授权属于不同安全层，两者都需要。

## 继续学习

- [上一篇：MCP Tools、Resources、Prompts 是什么](./03-tools-resources-prompts.md)
- 下一篇（待完成）：MCP 和 Function Calling 有什么区别？
- [相关：API 是什么](../06-tools/01-api.md)

## 资料与核验

- [Model Context Protocol Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28)
- [MCP Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
