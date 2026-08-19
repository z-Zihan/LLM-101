# MCP 工具、资源和提示是什么？

> 所属专题：MCP · 前置：[MCP 客户端和服务端是什么](./02-MCP客户端和服务端是什么.md) · 后续：[MCP 和 API 有什么区别](./04-MCP和API有什么区别.md)
>
> 最后核验：2026-08-19

MCP Server 可以暴露三类用途明显不同的能力：Tool 用来请求操作，Resource 用来读取内容，Prompt 用来提供可复用提示模板。把三者统称为 Tool，会让交互方式、权限和风险混在一起。

| Primitive | 解决的问题 | 典型交互意图 |
|---|---|---|
| Tool | 可以执行什么操作 | 模型可建议调用 |
| Resource | 可以读取什么内容 | 应用选择和管理 |
| Prompt | 可以套用什么提示模板 | 用户明确选择 |

规范中的控制标签描述推荐交互，不是授权捷径。Host 始终需要实施权限、同意与上下文管理。

## Tool：可请求执行的动作

Tool 通常声明名称、描述和输入 Schema。模型可以提出调用，Host 校验权限和参数后，通过 Client 请求 Server 执行。

```text
模型建议 → Host 校验与确认 → MCP Server 执行 → 结果返回
```

这张图想强调模型建议和真实执行之间的边界。读图时注意，Schema 只约束数据形状；删除、付款或发送仍需要业务授权。

MCP Tool 与普通 AI Tool 的职责相同，区别在于它通过 MCP 的发现和调用机制暴露。Host 可以再把它转换成模型平台支持的 Function Calling 定义。

## Resource：可读取的上下文内容

Resource 通过 URI 标识，可以表示文件、数据库记录、应用状态或其他内容。Host 决定何时读取、是否展示给用户、以及哪些部分进入模型上下文。

Resource 不自动等于 RAG 或长期 Memory。它提供读取接口；检索、选择、缓存和上下文组织仍由应用设计。URI 能被列出，也不代表当前用户有权读取内容。

## Prompt：可选择的提示模板

Prompt 可以接收参数，并生成一组供用户或应用使用的消息。例如 Server 提供“代码审查”模板，用户选择后再填入仓库范围。

MCP Prompt 不是平台隐藏的 System Prompt，也不能强制覆盖 Host 规则。它更像协议化提供的可复用入口，应让用户或应用明确选择。

## 为什么拆开后更安全

读取项目说明适合 Resource，创建工单适合 Tool，套用复盘模板适合 Prompt。Host 可以为读取、执行和模板选择设计不同界面：Resource 做访问控制，Tool 做副作用确认，Prompt 展示即将应用的内容。

三类返回都可能不可信。Resource 可能包含 Prompt Injection，Tool Result 可能过时或失败，Prompt 可能夹带不适合当前任务的指令。来源可见、最小权限和日志仍然必要。

## 回答容易混淆的问题

**MCP Tool 就是 Function Calling 吗？** 不是。Tool 是协议暴露的能力，Function Calling 是模型生成结构化请求的机制。

**Resource 就是 Tool Result 吗？** 不一定。Resource 是可主动读取的内容；Tool Result 是一次操作的返回，生命周期不同。

**MCP Prompt 就是 Skill 吗？** 不是。Prompt 是消息模板；Skill 通常还包含流程、材料、脚本和验收方法。

**Resource 进入模型后会永久记住吗？** 不会自动发生，它通常只影响当前上下文。

## 从这里继续

- [MCP 和 API 有什么区别](./04-MCP和API有什么区别.md)
- [MCP 和 Function Calling 有什么区别](./05-MCP和Function-Calling有什么区别.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [MCP Specification: Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- [MCP Specification: Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources)
- [MCP Specification: Prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts)
