# Model 和 Agent 有什么区别？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> Agent 是一种更大的模型吗？
>
> 同一个模型接上工具，就会自动变成 Agent 吗？

## 先说人话

Model（模型）是接收输入并计算输出的核心组件；Agent 是围绕目标，把模型与指令、Context、工具、状态和运行循环组合起来的系统。

Agent 可以使用模型，但 Agent 不等于模型，也不一定只使用一个模型。

## 举个例子

同一个语言模型可以被放进不同产品：

```text
场景 A：输入问题 → 模型生成回答

场景 B：输入任务 → 模型选择工具 → 程序执行
       → 模型读取结果 → 继续行动 → 完成任务
```

场景 A 主要是一次模型推理；场景 B 如果由系统围绕目标持续控制多步行动，就更接近 Agent。

模型没有因为进入场景 B 而变成另一种参数文件。变化的是模型外面的系统结构与运行方式。

## 严格来说

可以按职责拆开：

| 层次 | 主要职责 |
|---|---|
| Model | 根据输入与参数计算输出 |
| Tool | 获取外部信息或执行具体操作 |
| Host / Runtime | 管理消息、权限、执行和状态 |
| Agent | 围绕目标组织上述组件并推进多步任务 |

这里的划分是教学模型。具体产品可能把多个层次封装在一起，命名也不完全一致。

## 模型会“自己行动”吗？

单独的模型调用通常只返回 Token 或结构化内容。即使它输出：

```json
{"tool": "send_email", "to": "example@example.com"}
```

邮件也还没有发送。宿主程序必须检查权限、决定是否执行，并调用真实工具。

因此，模型生成行动建议，不等于拥有行动权限。

## Agent 比 Model 多了什么？

常见增加项包括：

- 任务目标与完成标准；
- 可以读取的环境状态；
- 可使用的工具及权限；
- 多步运行与结果回传；
- 失败处理、重试和人工确认；
- 时间、费用与最大步骤限制；
- 日志、验证和停止机制。

这些系统能力会显著影响最终表现。只比较底层模型，无法完整预测两个 Agent 产品谁更可靠。

## 一个 Agent 可以用多个模型吗？

可以。系统可能让不同模型负责分类、生成、视觉理解或验证，也可能在成本和能力之间动态选择。

反过来，同一个模型也可以服务于普通聊天、固定 Workflow、Agent 或 Coding Agent。Model 与 Agent 不是一一对应关系。

## 最容易搞混的东西

### 模型能力 ≠ Agent 权限

模型可能知道如何写删除命令，但 Agent 是否能执行，取决于工具、账户权限、沙箱和确认规则。

### 更强模型 ≠ 更可靠 Agent

Agent 还受工具设计、Context、错误处理、循环和验证影响。强模型不能补偿所有系统缺陷。

### Agent 更新状态 ≠ 模型参数学习

Agent 可以记录步骤、保存文件或写入 Memory，但普通运行通常不会因此更新底层模型参数。

### Agent ≠ 产品界面

界面只是用户接触产品的方式。判断是否为 Agent，要看系统是否围绕目标执行和反馈，而不是按钮或名称。

## 常见误区

### 误区 1：Agent 是一种模型架构

不对。Transformer 是模型架构；Agent 更接近应用与运行系统的组织方式。

### 误区 2：给模型更多 Prompt 就一定成为 Agent

Prompt 可以描述目标和规则，但没有工具执行、状态管理与控制逻辑时，仍可能只是一次模型调用。

### 误区 3：Agent 出错都是底层模型的问题

错误也可能来自错误工具结果、权限配置、Context、业务代码、循环终止或外部服务。

## 为什么我要知道它？

区分 Model 与 Agent，能帮助你排查问题和评估产品：回答质量可能要调模型与 Context；越权操作要修权限；重复执行可能要修 Agent Loop；工具报错则应检查外部系统。

## 你只需要记住

1. Model 是计算输出的组件；Agent 是围绕目标运行的多组件系统。
2. 模型提出行动不等于行动已执行，权限属于宿主系统。
3. 同一模型可用于多种应用，一个 Agent 也可以使用多个模型。
4. Agent 的可靠性由模型、工具、Context、控制逻辑和安全边界共同决定。

## 继续学习

- [上一篇：Agent 是什么](./01-Agent到底是什么.md)
- [下一篇：Agent Loop 是什么](./03-Agent-Loop是什么.md)
- [相关：模型是什么](../01-AI与大模型/03-模型到底是什么.md)

## 资料与核验

- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [OpenAI: A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [Model Context Protocol: Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture)
