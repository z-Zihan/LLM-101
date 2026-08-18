# MCP Tools、Resources、Prompts 是什么？

> Level: `Core` · Path: `Main`
>
> 最后核验：2026-08-18

## 先说人话

MCP Server 可以提供三类核心能力：Tool 用于执行操作，Resource 用于提供可读取内容，Prompt 用于提供可复用的提示模板。

它们用途不同，不能全部叫 Tool。

## 一张表分清

| Primitive | 主要作用 | 规范中的交互意图 |
|---|---|---|
| Tool | 执行查询或操作 | Model-controlled |
| Resource | 暴露可读取的 Context 数据 | Application-controlled |
| Prompt | 提供可选择的提示模板 | User-controlled |

这些“controlled”标签描述推荐的交互方式，不表示模型、应用或用户能绕过 Host 的权限与确认。

## MCP Tool

Tool 通常有名称、描述和输入 Schema。模型可以请求调用，Host 验证后由 Server 执行。

```text
Model 建议调用
  ↓
Host 检查权限与参数
  ↓
Client 请求 Server 执行
  ↓
结果返回 Host 与 Model
```

MCP Tool 与普通 AI Tool 的职责相同，区别在于它通过 MCP 的发现和调用协议暴露。

## MCP Resource

Resource 是 Server 暴露的可读取内容，通过 URI 标识。它可以表示文件、数据库记录、应用状态或其他 Context 数据。

Resource 更像“可以读取什么”，不等于自动检索、RAG 或永久 Memory。Host 决定何时读取以及是否把内容放进模型 Context。

## MCP Prompt

Prompt 是 Server 提供的可复用提示模板，可以带参数并生成供用户或应用使用的消息内容。

MCP Prompt 不等于平台隐藏的 System Prompt，也不是 Server 可以强制覆盖 Host 规则的通道。它应由用户选择或应用明确使用。

## 为什么要分三类？

```text
读取项目说明 → Resource
执行创建工单 → Tool
套用代码审查模板 → Prompt
```

分开后，Host 可以针对读取、执行和模板选择设计不同的界面、权限与确认策略。

## Tool 的安全边界

Server 声明 Tool 不代表 Host 必须调用。Host 应：

- 展示工具来源与用途；
- 验证输入 Schema 之外的业务权限；
- 对破坏性或外部副作用操作确认；
- 清洗和限制返回内容；
- 记录失败、超时与调用日志。

## Resource 的安全边界

Resource 可能包含隐私、凭证或恶意指令。读取前要检查访问权限，进入 Context 前要控制范围。URI 可访问也不表示当前用户有权读取。

## 最容易搞混的东西

### MCP Tool ≠ Function Calling

MCP Tool 是通过 MCP 暴露的能力；Function Calling 是模型生成结构化调用请求的机制。Host 可以把两者连接起来。

### Resource ≠ Tool Result

Resource 是可被读取的内容；Tool Result 是一次操作执行后的返回。某些内容可能相似，但生命周期和交互意图不同。

### MCP Prompt ≠ Skill

Prompt 是可复用消息模板；Skill 通常还包含完成一类任务的方法、材料或脚本。后文会完整比较。

## 你只需要记住

1. Tool 执行操作，Resource 提供内容，Prompt 提供提示模板。
2. MCP Tool 是普通 Tool 的协议化暴露方式，不等于 Function Calling。
3. Resource 不自动等于 RAG，Prompt 也不等于 System Prompt 或 Skill。
4. 三类能力都必须经过 Host 的权限、同意与 Context 管理。

## 继续学习

- [上一篇：MCP Client 和 Server 是什么](./02-MCP客户端和服务端是什么.md)
- [下一篇：MCP 和 API 有什么区别](./04-MCP和API有什么区别.md)

## 资料与核验

- [MCP Specification: Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- [MCP Specification: Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources)
- [MCP Specification: Prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts)
