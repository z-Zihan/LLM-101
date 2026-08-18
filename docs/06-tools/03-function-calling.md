# Function Calling 是什么？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> 模型说要调用函数，是它自己在服务器里执行代码吗？
>
> Function Calling 和 Tool Calling 有什么区别？

## 先说人话

Function Calling 是一种让模型按预先定义的结构表达“我想调用哪个函数、需要哪些参数”的机制。

它通常只产生调用请求。读取请求、验证参数、检查权限并真正执行函数的是模型外部的应用程序。

## 举个例子

应用向模型提供一个函数定义：

```text
名称：get_order_status
用途：根据订单号查询状态
输入：order_id（字符串，必填）
```

用户问：“帮我查 A1024 到哪了。”模型可以输出类似：

```json
{
  "name": "get_order_status",
  "arguments": {
    "order_id": "A1024"
  }
}
```

这时订单还没有被查询。应用检查用户是否有权访问该订单，再调用真实业务函数，把结果送回模型。

## 完整流程

```text
1. 应用把用户请求和函数定义发给模型
2. 模型返回函数名与参数
3. 应用验证结构、参数、权限和风险
4. 应用执行本地函数或外部 API
5. 应用把执行结果发回模型
6. 模型基于结果生成最终回答或提出下一步调用
```

不同平台的消息字段和循环格式会变化，但“模型提出 → 外部执行 → 结果回传”是理解执行边界的关键。

## 函数定义里有什么？

常见信息包括：

- Name：模型用于选择的函数名；
- Description：函数用途与使用条件；
- Parameters / Input Schema：可接受的字段、类型、必填项和限制。

许多系统使用类似 JSON Schema 的方式描述输入结构。Schema 能约束数据形状，却不能证明参数在业务上合理，例如字符串格式正确的订单号仍可能属于另一位用户。

## 谁真正执行函数？

真正执行者通常是 Host Application（宿主应用）、后端服务或 Tool Server，而不是语言模型本身。

```text
Model 输出：
“建议调用 delete_file(path=...)”

Host 决定：
是否允许？路径是否合法？是否需要确认？

Tool 执行：
通过检查后才进行真实操作
```

这就是 Tool Execution Boundary（工具执行边界）：模型输出属于不可信的建议或数据，越过边界前必须由执行系统验证和授权。

## 参数为什么不能直接相信？

模型可能：

- 选择错误函数；
- 漏掉必填字段；
- 生成不存在的参数；
- 把用户文本错误地填入字段；
- 受到 Prompt Injection 影响；
- 请求超出用户权限的操作。

结构化输出能减少格式混乱，但不会自动解决业务权限、安全和事实正确性。

## Function Calling 和 Tool Calling 的关系

在许多平台中，两者表达非常接近的工作流。可以先这样理解：

```text
Tool：模型可使用的能力
Function Calling：用函数名与结构化参数请求这项能力的常见接口
Tool Calling：更宽泛或更新的产品术语，可能覆盖函数之外的工具类型
```

这些词并没有跨所有厂商完全一致的字段定义。使用具体平台时，应以该平台当前官方文档为准。

## Function Calling 和 API 的关系

Function Calling 负责把自然语言意图转换成结构化调用请求；API 负责软件之间实际交互。应用经常把两者串起来：

```text
用户自然语言
   ↓
模型生成函数调用参数
   ↓
应用调用外部 API
   ↓
API 返回数据
   ↓
模型组织最终回答
```

Function Calling 不要求背后一定是网络 API，也可以执行本地函数或受控命令。

## 常见误区

### 误区 1：模型返回调用成功，就代表函数已执行

不对。模型只能生成调用请求；应用还可能拒绝、等待确认、执行失败或超时。

### 误区 2：有 JSON 就是安全的

JSON 只是一种数据格式。路径穿越、越权、危险参数和隐私泄露仍需要专门防护。

### 误区 3：函数描述写得越长越好

描述应清晰区分用途、输入和限制。冗长、冲突或重叠的定义可能让模型更难选择。

## 为什么我要知道它？

Function Calling 是模型从“生成文字”走向“连接软件能力”的关键桥梁。分清调用建议与真实执行后，才能理解 Agent 为什么能做事，也能看见权限、确认和失败恢复应该放在哪里。

## 你只需要记住

1. Function Calling 让模型输出函数名与结构化参数，不等于模型已经执行函数。
2. Host 必须验证参数、权限与风险，再决定是否执行。
3. Schema 约束数据形状，不能替代业务校验与安全策略。
4. Tool 是能力，Function Calling 是请求能力的一种常见接口，API 可以是背后的实际连接方式。

## 继续学习

- [上一篇：AI Tool 是什么](./02-tool.md)
- [下一篇：Agent 是什么](../07-agent/01-what-is-agent.md)
- [相关：API 是什么](./01-api.md)

## 资料与核验

- [Microsoft Learn: Function calling](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/function-calling)
- [Model Context Protocol Specification: Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- [JSON Schema Core](https://json-schema.org/draft/2020-12/json-schema-core)
