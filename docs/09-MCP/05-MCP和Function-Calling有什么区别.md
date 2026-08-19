# MCP 和 Function Calling 有什么区别？

> 所属专题：MCP · 前置：[MCP 和 API 有什么区别](./04-MCP和API有什么区别.md) · 后续：[MCP 和 Agent 有什么区别](./06-MCP和Agent有什么区别.md)
>
> 最后核验：2026-08-19

Function Calling 解决模型怎样把“我要使用哪个工具、参数是什么”表达成结构化请求；MCP 解决 Host 怎样发现并连接外部 Server 提供的能力。它们位于一条调用链的不同边界，最常见的关系不是二选一，而是组合。

## 一次调用怎样穿过两个边界

MCP Client 先从 Server 发现 Tool 描述和输入 Schema。Host 把这些信息转换成模型平台支持的工具定义；模型生成调用意图后，Host 再通过 MCP 请求 Server 执行。

```text
Model
  ↓ Function Calling：工具名与参数
Host Application
  ↓ MCP Client：协议请求
MCP Server
  ↓ 执行 Tool 或后端 API
结果逐层返回
```

这张图想说明模型不必直接生成 MCP JSON-RPC，也不直接连接 Server。读图时注意 Host 负责映射两侧格式，并在中间实施授权、确认和错误处理。

## 两者真正不同在哪里

| 维度 | Function Calling | MCP |
|---|---|---|
| 主要边界 | Model 与 Host | MCP Client 与 Server |
| 主要目的 | 产生结构化调用意图 | 发现、连接和请求外部能力 |
| 范围 | 模型侧工具选择与参数 | Tools、Resources、Prompts、生命周期和传输 |
| 是否完成业务 | 模型没有执行 | Server 可执行，但仍受 Host 与后端授权 |

模型原生支持 Function Calling，不等于应用原生支持所有 MCP Server。Host 仍需实现 Client、能力映射、连接生命周期和权限管理。

反过来，使用 MCP 也不必每次经过模型。用户可以在界面选择 Prompt，应用可以主动读取 Resource；只有需要模型选择 Tool 时，Function Calling 才常进入链路。

## 安全不能被格式与协议替代

结构化参数可能语义错误，协议兼容的 Server 也可能不可信。Host 要检查工具是否允许、参数是否符合业务规则、用户是否确认副作用；Server 与后端 API还要验证凭证和资源权限。

Tool Result 可能包含恶意指令或敏感数据，返回模型前要控制范围。日志应区分模型建议、Host 批准、Server 执行与业务确认，不能把“请求已生成”显示为“操作已完成”。

## 回答常见误区

**Function Calling 和 MCP 是同一种协议吗？** 不是，前者描述模型侧结构化调用，后者连接 Client 与 Server。

**发现 MCP Tool 就已经执行了吗？** 没有，发现只得到能力描述，真实执行还要经过请求与授权。

**没有 MCP 能使用 Function Calling 吗？** 可以，Host 可直接调用本地函数或 API。

**没有 Function Calling 能使用 MCP 吗？** 可以，应用能读取 Resource 或让用户选择 Prompt。

## 从这里继续

- [MCP 和 Agent 有什么区别](./06-MCP和Agent有什么区别.md)
- [Function Calling 是什么](../06-工具与Function-Calling/03-Function-Calling是什么.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [MCP Specification: Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [Microsoft Learn: Function calling](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/function-calling)
