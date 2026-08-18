# Agent 是什么？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> Agent 和普通聊天机器人到底差在哪？
>
> 只要模型会调用工具，就算 Agent 吗？

## 先说人话

在现代 LLM 应用里，Agent 可以先理解成：一个围绕目标运行的系统，由模型根据当前状态决定下一步，必要时使用工具，并根据结果继续行动，直到完成、失败或触发停止条件。

Agent 没有跨论文和厂商完全统一的单句定义。不同产品的自主程度、工具范围和运行时长可能差很多。

## 举个例子

用户说：“找出项目测试失败的原因，并给出修复建议。”

普通一次回答可能只根据 Prompt 猜测。一个 Coding Agent 则可能：

```text
读取项目与报错
   ↓
决定运行哪些测试
   ↓
调用终端执行测试
   ↓
观察失败结果
   ↓
继续读相关代码
   ↓
形成结论或修改建议
```

关键不只是“调用了终端”，而是系统能让模型根据新结果继续选择后续步骤。

## 严格来说

一个常见的 LLM Agent 系统通常组合：

- Model：理解输入、生成判断或下一步；
- Instructions：目标、规则和角色边界；
- Context / State：当前任务、历史步骤与工具结果；
- Tools：搜索、文件、代码、数据库等外部能力；
- Control Loop：让系统执行、观察并再次决策；
- Guardrails：权限、确认、预算、超时和停止规则。

```text
目标 + 当前状态
      ↓
Model 决定下一步
      ↓
回答 / 调用 Tool / 请求帮助
      ↓
系统执行并更新状态
      ↺
```

并非每个 Agent 都必须使用同一套组件名称，也不是工具越多越像 Agent。

## Agent 为什么会出现？

一次模型调用适合完成边界清楚、输入齐全的任务。但现实任务经常需要：

- 先查资料，再决定下一步；
- 根据工具结果调整计划；
- 处理多个文件或系统；
- 在失败后重试、改路或请求人工介入。

Agent 把模型放进可重复获取反馈的系统中，让它不只生成一段文字，还能在受控范围内推进多步任务。

## Agent 有多“自主”？

自主程度是一条连续谱：

```text
每一步都由人确认
        ↓
低风险步骤自动执行，高风险步骤确认
        ↓
在预算和权限内连续执行
```

“Agent”不等于可以无限运行或拥有全部权限。生产系统通常应限制工具、数据范围、步骤数、费用和可执行操作。

## 最容易搞混的东西

### Agent ≠ Model

Model 是计算组件；Agent 是围绕任务组合模型、工具、状态和控制逻辑的系统。下一篇会完整比较。

### Agent ≠ 一次 Function Calling

一次函数调用只完成一个结构化请求。Agent 的关键通常还包括根据执行结果继续决策的循环。

### Agent ≠ Workflow

Workflow 主要由预先写好的流程控制步骤；Agent 更依赖模型动态决定如何推进。实际系统常把两者组合。

### Agent ≠ 自动正确

连续行动会放大能力，也可能累积错误、费用与安全风险。Agent 仍需要验证、权限和停止条件。

## 常见误区

### 误区 1：能聊天的 AI 都是 Agent

不一定。只执行一次输入到输出、没有外部行动或持续控制循环的聊天应用，通常更适合称为模型应用或助手。

### 误区 2：Agent 必须先写出完整计划

不一定。有些系统先规划再执行，有些每一步根据最新结果决定，还有些使用固定 Workflow 包住局部 Agent。

### 误区 3：Agent 可以替用户承担责任

不能。系统的设计者和使用者仍需定义授权、审核、日志和责任边界，高风险决定不能因为由 Agent 执行就无人负责。

## 为什么我要知道它？

理解 Agent，才能判断一个产品是在“生成建议”，还是能够读取环境、调用工具并产生现实影响。它也是继续理解 Agent Loop、Workflow、MCP、Skill 与 Coding Agent 的基础。

## 你只需要记住

1. Agent 是围绕目标组合模型、状态、工具和控制循环的系统。
2. 它能根据工具结果继续决定下一步，而不只生成一次回答。
3. Agent 的定义和自主程度因系统而异，不等于无限权限或自动正确。
4. 工具、确认、预算和停止条件决定 Agent 能做什么、何时必须停下。

## 继续学习

- [上一篇：Function Calling 是什么](../06-tools/03-function-calling.md)
- [下一篇：Model 和 Agent 有什么区别](./02-model-vs-agent.md)
- [相关：AI Tool 是什么](../06-tools/02-tool.md)

## 资料与核验

- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [OpenAI: A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [Wang et al.: A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432)
