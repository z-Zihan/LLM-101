# Function Calling 是什么？

> 你现在的位置：[AI 工具](./02-AI工具到底是什么.md) → **Function Calling** → [Agent](../07-Agent/01-Agent到底是什么.md)
>
> 所属专题：工具与 Function Calling · 主路线衔接：[Agent 到底是什么](../07-Agent/01-Agent到底是什么.md)

一个常见问题是：Function Calling 是不是模型自己立刻执行函数？不是。它是一种让模型按约定结构表达“建议调用哪个函数、参数是什么”的机制；外部应用读取这份请求，完成权限与参数检查，再决定是否真正执行。

这个执行边界是整篇最重要的概念。没有外部程序，模型生成再漂亮的 JSON，也只是文本或结构化数据。

## 从查询订单看完整循环

应用先提供函数定义：`get_order_status` 用订单号查询状态，输入 `order_id` 必须是字符串。用户问“A1024 到哪了”，模型可能返回：

```json
{
  "name": "get_order_status",
  "arguments": {
    "order_id": "A1024"
  }
}
```

此时还没有查订单。宿主要确认当前用户有权访问 A1024，再调用业务函数，把“已发货”或错误状态作为工具结果送回模型。

```text
应用发送：用户请求 + 函数定义
  ↓
模型返回：函数名 + 结构化参数
  ↓
应用：解析、校验、授权、确认
  ↓
函数或 API：真实执行
  ↓
应用回传工具结果
  ↓
模型回答，或请求下一项工具
```

这张图想展示 Function Calling 是一段协议循环。读图时注意两个模型步骤之间夹着真实执行；应用也可以拒绝调用、等待用户确认或在失败后停止。

## Schema 能保证什么

函数定义通常包含名称、用途说明和参数 Schema。Schema 可以规定字段类型、枚举范围、必填项和嵌套结构，帮助模型输出可解析数据，也方便宿主做第一层校验。

它不能证明业务意图正确。`amount: 1000` 是合法数字，不代表用户同意付款；`path: "/data/file"` 是合法字符串，不代表模型有权删除文件。权限检查、业务规则和副作用确认必须在模型之外。

即使平台提供“严格结构化输出”，它通常解决的是格式遵循，不应被理解为事实、权限与安全全部通过。模型仍可能选择错误函数或填入语义上不合理的合法值。

## Tool Calling、Function Calling 和 API

Tool 是系统提供的能力。Function Calling 是用函数名和结构化参数请求能力的一种常见接口。Tool Calling 常是更宽泛的平台术语，可能覆盖函数、搜索、代码执行等多类工具；具体字段应以平台当前文档为准。

API 则负责软件间实际交互。常见链路是：模型把自然语言转成函数参数，宿主再调用外部 API。Function Calling 背后也可以是本地函数，不要求经过网络。

OpenAPI 可以描述一个 HTTP API 的路径和 Schema，MCP 可以让宿主发现并调用远端工具；它们和 Function Calling 处于相邻层，却不是互相替代的同义词。

## 多次调用怎样变成 Agent 行为

一次调用通常是“请求—执行—返回”。Agent 会保留目标和状态，根据结果决定下一步：先搜索订单，再读取物流，发现异常后请求人工处理。循环、停止条件和失败恢复由宿主编排，不是 Function Calling 这一个机制自动提供。

模型可能一次请求多个独立工具，也可能必须等待前一项结果才能生成下一项参数。并行能降低延迟，但有依赖或副作用时要保持顺序。宿主需要为每次调用设置唯一标识，正确匹配请求与结果。

## 安全边界怎样落地

把模型输出视为不可信输入。先验证函数是否在允许列表，再校验 Schema、用户权限、资源范围和业务条件。写操作要考虑幂等、重复执行、超时后的未知状态，以及是否需要明确的人类确认。

工具结果同样是不可信外部数据，不能让网页或文件里的文字越权改变系统指令。日志应区分“模型提出”“宿主批准”“工具执行”“业务确认”四种状态，避免 UI 把建议误报为成功。

## 回答真实问题

**模型返回函数名，就已经执行了吗？** 没有。它只产生调用请求；宿主可能执行、拒绝、等待确认或失败。

**有 JSON 和 Schema 就安全了吗？** 没有。它们主要约束格式，权限、业务含义和副作用仍需独立检查。

**Function Calling 和 Tool Calling 有什么区别？** 常描述相近流程，Tool Calling 往往更宽泛；跨厂商没有完全统一的字段定义。

**为什么它对 Agent 重要？** 它让模型把下一步行动表达成程序可检查的结构，但 Agent 还需要状态、循环、停止条件和验证机制。

## 从这里继续

- 主路线下一站：[Agent 到底是什么](../07-Agent/01-Agent到底是什么.md)
- 回看能力包装：[AI 工具到底是什么](./02-AI工具到底是什么.md)
- 理解软件边界：[API 到底是什么](./01-API到底是什么.md)
- 回看历史位置：[从 RAG、工具调用到 Coding Agent](../../history/03-从RAG工具调用到Coding-Agent.md)
- 返回全局：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [OpenAI: Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [Model Context Protocol Specification: Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- [JSON Schema Core](https://json-schema.org/draft/2020-12/json-schema-core)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
