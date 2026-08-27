# MCP 和 Agent 有什么区别？

> 所属专题：MCP · 前置：[MCP 和 Function Calling 有什么区别](./05-MCP和Function-Calling有什么区别.md) · 主路线下一站：[Skill 到底是什么](../10-Skill/01-Skill到底是什么.md)
>
> 最后核验：2026-08-19

MCP 是连接外部能力的协议；Agent 是围绕目标读取状态、选择行动、使用工具并根据结果继续运行的系统。MCP 可以给 Agent 提供能力，但不会自动创造目标、计划、状态或 Agent Loop。

## 同一套 MCP 能力可以被两种应用使用

一个 Server 提供“查询工单”和“创建工单”。普通聊天应用可以让用户手动查询一次；Agent 为完成“处理客户问题”，可能先查工单、读取客户资料、判断是否升级，再请求创建新工单。

```text
Agent：目标 → 决策 → 观察结果 → 下一步
                    ↓
Host 通过 MCP Client 请求 Server
                    ↓
              Tool / Resource
```

这张图想说明 MCP 只覆盖中间的能力连接。读图时注意，任务循环与完成判断在 Agent 系统中，不属于 MCP 协议。

## 没有谁必须使用谁

Agent 可以直接调用应用内函数、SDK、普通 API 或数据库，不需要 MCP。MCP 应用也可以只是文档阅读器、模板选择器或一次性工具助手，没有动态循环。

因此“安装 MCP Server”不等于获得 Agent。还需要模型、目标、状态、工具选择、执行回传、停止条件和安全控制。反过来，一个成熟 Agent 也不因为未使用 MCP 就缺少 Agent 身份。

## 同一次排班请求里看分工

把一个完整请求拆开，两层各自的位置会非常具体。行政同事对 Agent 说：“下周一谁来替休假的张三值班？排好班后通知全组。”

Agent 先分解目标：查张三的休假记录，查下周各组人力，判断替补人选，创建排班，最后发通知。每一步要决定“接下来做什么、做完怎么验证”，这些属于 Agent 系统。而“查休假”“读排班表”“写班次”“发消息”四个动作之所以伸手可得，是因为背后有 HR 系统和消息系统的 MCP Server 把它们声明成了 Tools——MCP 让 Agent 不必关心那些系统各自的认证方式和接口风格。

注意两个常见的归属错位：替换人选的决策逻辑（资历？自愿？轮换规则？）不在任何 Server 里，它是 Agent 按目标推理的部分；反过来，通知发出去了没有，Server 返回的结果说了算，Agent 不能凭感觉宣布成功。分工清楚，排查问题时才知道该去翻技能说明还是该去找接口日志。

## 组合后为什么风险更大

Agent 能连续发起调用，MCP Server 可能连接高权限系统。两者组合会放大选择错误、重复执行和 Prompt Injection 的后果。Host 应限制 Agent 可见的 Server 和能力，按副作用分级确认，并设置步骤、时间和费用上限。

Server 返回成功只说明某一步完成，Agent 仍要验证最终目标。系统还要支持取消、日志、幂等、失败恢复和人工接管；MCP 的协议一致性不能替代这些运行控制。

工具数量也不是能力指标。过多重叠能力会增加模型选择难度、上下文负担和攻击面。按任务提供最小能力集，往往比接入所有 Server 更可靠。

## 回答开头的问题

**有 MCP 就等于有 Agent 吗？** 不等于，MCP 提供连接，Agent 还需要目标、状态和循环。

**Agent 必须通过 MCP 使用工具吗？** 不必须，MCP 只是可选连接方式。

**普通 MCP 应用可以没有 Agent 吗？** 可以，读取 Resource 或一次调用 Tool 都不要求 Agent Loop。

**MCP 越多，Agent 越强吗？** 不一定，能力、权限和选择复杂度会同时增加。

## 从这里继续

- 主路线下一站：[Skill 到底是什么](../10-Skill/01-Skill到底是什么.md)
- 回看系统定义：[Agent 到底是什么](../07-Agent/01-Agent到底是什么.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [MCP Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
