# Context Engineering 是什么？

> Level: `Core` · Path: `Main`

## 先说人话

Context Engineering（上下文工程）是系统性地决定模型运行时应该看到什么信息、以什么顺序看到、何时更新或压缩这些信息。

它比“把 Prompt 写得更漂亮”范围更大。

## Context 里可能有什么？

- System / developer instructions；
- 用户请求与对话历史；
- 检索到的项目文件和资料；
- Tool 定义与执行结果；
- 计划、状态和 Memory；
- 输出格式与验证规则。

```text
收集候选信息
  ↓
选择相关且可信内容
  ↓
按角色、顺序和结构组织
  ↓
模型计算与工具行动
  ↓
根据新结果更新 / 压缩 Context
```

## 和 Prompt Engineering 的区别

Prompt Engineering 主要关注怎样表达指令、示例和输出要求。Context Engineering 还包含检索、工具结果、历史裁剪、Memory、权限过滤和长任务状态管理。

Prompt 是 Context 的一部分，Prompt Engineering 是 Context Engineering 的一个子问题。

## 为什么更多 Context 不一定更好？

Context Window 有容量限制，模型对不同位置和噪声的利用能力也有限。重复、冲突和无关内容可能让重要证据更难被使用。

因此目标不是“塞满窗口”，而是在正确时间提供完成当前步骤所需的最小充分信息。

## 长任务怎样管理 Context？

常见做法包括：

- 把稳定规则保留在明确位置；
- 按需检索文件，不重复粘贴全仓库；
- 把旧步骤压缩成可核验摘要；
- 将详细证据保存到外部状态，按需读取；
- 保留关键决策、失败和未完成项；
- 工具执行后淘汰已经失效的假设。

摘要也可能丢信息，因此重要原始证据需要可回查。

## 最容易搞混的东西

### Context Engineering ≠ 扩大 Context Window

窗口更大只是容量变化；工程问题是如何选择和组织信息。

### Context Engineering ≠ RAG

RAG 是检索外部资料的一种流程；Context Engineering 还管理指令、工具、历史和状态。

### Context Engineering ≠ Fine-tuning

Context Engineering 改变运行时输入，不更新模型参数。

## 常见误区

### 误区 1：信息重复几遍模型就更重视

重复会消耗容量并可能造成冲突，重要规则应清晰、单一且放在正确层级。

### 误区 2：摘要一定忠实

摘要是有损压缩，需要保留原始来源并验证关键细节。

### 误区 3：Context 只影响回答文字

在 Agent 中，它还会影响 Tool 选择和现实操作，因此权限过滤非常重要。

## 你只需要记住

1. Context Engineering 管理运行时信息的获取、选择、组织、更新和压缩。
2. Prompt Engineering 是其中一部分，不是全部。
3. 更多信息不一定更好，目标是相关、可信、及时的最小充分 Context。
4. Context 变化不等于模型参数变化。

## 继续学习

- [上一篇：Project Context 是什么](./08-project-context.md)
- [下一篇：Conversation History 是什么](../12-memory/01-conversation-history.md)

## 资料与核验

- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [OpenAI: A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [Liu et al.: Lost in the Middle](https://arxiv.org/abs/2307.03172)
