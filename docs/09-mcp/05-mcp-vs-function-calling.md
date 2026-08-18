# MCP 和 Function Calling 有什么区别？

> Level: `Core` · Path: `Main`
>
> 最后核验：2026-08-18

## 先说人话

Function Calling 解决“模型怎样结构化表达要调用什么”；MCP 解决“AI 应用怎样发现并连接外部 Server 提供的能力”。

它们处在不同连接边界，可以串在同一条工具调用链中。

## 一条完整链路

```text
Model
 ↓ Function Calling：函数名与参数
Host Application
 ↓ MCP Client：协议请求
MCP Server
 ↓ 执行 Tool 或调用后端 API
结果返回
```

模型不必直接理解 MCP JSON-RPC。Host 可以把 MCP Tool 的描述和 Schema 转成模型支持的工具定义。

## 核心区别

| 维度 | Function Calling | MCP |
|---|---|---|
| 主要边界 | Model ↔ Host | MCP Client ↔ Server |
| 主要目的 | 生成结构化调用意图 | 发现、连接和调用外部能力 |
| 是否执行 | 模型只提出请求 | Server 可执行 Tool，但 Host 仍控制授权 |
| 范围 | 常围绕函数 / 工具选择 | 还包含 Resources、Prompts、生命周期与 Transport |

## 为什么要组合？

Function Calling 给不同模型提供结构化输出方式；MCP 给 Host 提供相对统一的外部连接方式。

```text
不同 Model 的工具调用格式
          ↓ Host 适配
统一连接多个 MCP Server
```

更换模型时，MCP Server 不一定需要改变；更换 Server 时，模型也不必学习后端 API 细节。

## 只有 MCP 可以调用工具吗？

不是。Host 可以直接调用本地函数或普通 API，也可以使用其他协议。MCP 是一种标准化连接选择。

## 只有 Function Calling 才能使用 MCP 吗？

也不是。应用可以让用户通过界面选择 MCP Prompt，或主动读取 Resource；不一定每次都由模型发起 Function Calling。

## 安全检查在哪里？

每个边界都要检查：

- 模型输出的 Tool 与参数是否合理；
- Host 是否获得用户授权；
- MCP Server 是否可信并使用最小权限；
- 后端 API 是否验证身份与业务权限；
- Tool Result 是否含恶意或敏感内容。

结构化参数和协议兼容都不等于安全。

## 常见误区

### 误区 1：模型原生支持 Function Calling，就原生支持所有 MCP

Host 仍需 MCP Client、能力映射、连接与权限管理。

### 误区 2：MCP Tool 被发现后就已经执行

发现只获得能力描述；真正调用还要经过模型 / 用户选择、Host 授权和 Server 执行。

### 误区 3：二者只能二选一

最常见的关系恰恰是组合：Function Calling 负责模型侧请求，MCP 负责外部连接。

## 你只需要记住

1. Function Calling 连接 Model 与 Host；MCP 连接 Client 与 Server。
2. Host 可把 MCP Tool 映射成模型工具，再把调用转发给 Server。
3. 两者可以组合，但都不代表工具已经安全执行。
4. MCP 还覆盖 Resources、Prompts、生命周期和 Transport，范围更广。

## 继续学习

- [上一篇：MCP 和 API 有什么区别](./04-mcp-vs-api.md)
- [下一篇：MCP 和 Agent 有什么区别](./06-mcp-vs-agent.md)

## 资料与核验

- [MCP Specification: Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [Microsoft Learn: Function calling](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/function-calling)
