# MCP 和 Agent 有什么区别？

> Level: `Core` · Path: `Main`
>
> 最后核验：2026-08-18

## 先说人话

MCP 是连接外部能力的协议；Agent 是围绕目标选择步骤、使用工具并根据结果继续运行的系统。

MCP 可以给 Agent 提供工具与资料，但不会自动创造目标、计划或 Agent Loop。

## 举个例子

一个 MCP Server 提供“查询工单”和“创建工单”工具。

- 普通聊天应用可以让用户手动选择一次工具；
- Agent 可以为了“处理客户问题”先查询、分析，再决定是否创建或升级工单。

两者使用相同 MCP Server，但只有后者包含围绕目标持续决策的 Agent 系统。

## 核心区别

| 维度 | MCP | Agent |
|---|---|---|
| 类型 | 协议 | 应用 / 运行系统 |
| 解决问题 | 怎样连接与交换能力 | 怎样围绕目标推进任务 |
| 是否包含目标 | 不负责 | 通常需要 |
| 是否包含循环 | 不提供 Agent Loop | 可以观察、行动并继续 |
| 是否必须使用对方 | 否 | 否 |

## Agent 使用 MCP 时发生什么？

```text
Agent 读取目标与状态
   ↓
决定需要某项 Tool / Resource
   ↓
Host 通过 MCP Client 请求 Server
   ↓
结果返回 Agent 状态
   ↓
Agent 决定下一步
```

MCP 负责中间的标准连接，Agent 负责循环与完成判断。

## 没有 MCP 能不能做 Agent？

可以。Agent 可以使用应用内置函数、普通 API、数据库驱动或其他协议。

## 有 MCP 能不能不是 Agent？

也可以。文档阅读器可以让用户选择 Resource，模板界面可以加载 Prompt，一次性助手可以调用 Tool；这些都不必有 Agent Loop。

## 谁负责安全？

Agent 可能连续发起多次调用，MCP Server 可能连接高权限系统。组合后更需要：

- 限制 Agent 可见的 Server 与能力；
- 对副作用操作逐级授权；
- 设置步骤、时间和费用上限；
- 验证 Tool Result 与最终目标；
- 支持取消、日志和人工接管。

MCP 的协议一致性不能替代 Agent 的运行控制。

## 常见误区

### 误区 1：安装 MCP Server 就获得自主 Agent

不对。仍需要 Host、模型、目标、状态和控制循环。

### 误区 2：Agent 必须通过 MCP 使用工具

不对。MCP 是可选的连接方式。

### 误区 3：MCP 越多，Agent 越强

过多能力会增加选择难度、权限和攻击面。应遵守最小能力原则。

## 你只需要记住

1. MCP 是协议，Agent 是围绕目标运行的系统。
2. MCP 提供能力连接，不提供目标、规划或 Agent Loop。
3. Agent 可以不用 MCP，使用 MCP 的应用也不一定是 Agent。
4. 二者组合会扩大能力，也必须加强权限、预算、验证与停止控制。

## 继续学习

- [上一篇：MCP 和 Function Calling 有什么区别](./05-MCP和Function-Calling有什么区别.md)
- [下一篇：Skill 是什么](../10-Skill/01-Skill到底是什么.md)

## 资料与核验

- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [MCP Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
