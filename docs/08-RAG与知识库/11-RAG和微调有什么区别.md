# RAG 和 Fine-tuning 有什么区别？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> 想让模型懂公司资料，应该做 RAG 还是微调？

## 先说人话

RAG 在回答时检索外部资料并放进 Context；Fine-tuning（微调）继续训练模型，让参数适配特定任务、行为或数据。

```text
RAG：改变本次输入了哪些资料
Fine-tuning：通过训练改变模型参数
```

## 举个例子

如果公司政策每周更新，希望回答能引用当前条款，RAG 通常更适合：更新知识库即可。

如果希望模型稳定使用某种分类标签、输出格式或专业写作风格，Fine-tuning 可能更适合：用示例训练期望行为。

实际系统可以同时使用两者。

## 严格来说

| 维度 | RAG | Fine-tuning |
|---|---|---|
| 改变什么 | 当前 Context 与外部证据 | 模型参数 |
| 何时发生 | 每次请求的检索与生成阶段 | 独立训练阶段 |
| 更新事实 | 更新外部资料与索引 | 需要重新准备数据并训练 |
| 来源检查 | 可保留检索原文与引用 | 参数中的来源难以逐条追踪 |
| 常见目标 | 私有、最新、可引用知识 | 行为、格式、任务或领域适配 |

这只是常见倾向。具体效果取决于数据、模型、训练和系统设计。

## Fine-tuning 能不能把知识写进模型？

训练样本会影响参数，模型可能学到相关模式或事实。但它不是可靠的逐条数据库更新方式：无法保证每条事实都准确记住、稳定取出或只修改目标内容。

对频繁变化、必须引用来源的事实，外部数据源通常更容易维护和审计。

## RAG 能不能教会模型新行为？

Prompt 和检索示例可以影响当前输出，但不改变模型训练参数。若需求是长期、稳定地改变输出格式或任务行为，可能需要更好的 Prompt、Workflow 或 Fine-tuning。

## 怎么选择？

先问需求主要缺什么：

- 缺最新或私有事实 → 优先考虑 RAG；
- 缺稳定行为、格式或任务适配 → 考虑 Fine-tuning；
- 两者都缺 → 可以组合；
- 固定 Prompt 和普通代码已经够用 → 不必增加复杂度。

还要比较数据质量、评测、延迟、成本、权限和维护能力。

## 最容易搞混的东西

### Fine-tuning ≠ Prompt 中给示例

Prompt 示例只影响当前 Context；Fine-tuning 会运行训练并更新参数。

### RAG ≠ 训练

建立索引和检索不会自动训练生成模型。

### RAG vs Fine-tuning ≠ 永久二选一

微调后的模型仍可使用 RAG，RAG 系统也可使用专门训练的 Embedding 或 Reranker。

## 常见误区

### 误区 1：微调后就不会幻觉

不对。微调数据和目标也可能引入错误，生成仍需验证。

### 误区 2：RAG 不需要高质量数据

错误、过时或权限混乱的资料会直接影响检索和回答。

### 误区 3：技术越多，效果越好

组合会增加开发、评测和运维成本。应从可验证需求出发。

## 你只需要记住

1. RAG 在请求时提供外部资料；Fine-tuning 通过训练更新参数。
2. RAG 常用于私有、最新、可引用知识；Fine-tuning 常用于行为和任务适配。
3. Fine-tuning 不是可靠的逐条事实数据库，RAG 也不会自动改变模型行为。
4. 二者可以组合，但都需要独立评测。

## 继续学习

- [上一篇：Retrieval 是什么](./08-检索是什么.md)
- [下一篇：RAG 有哪些局限](./12-RAG有哪些局限.md)
- [相关：Training 和 Inference 有什么区别](../03-模型原理与训练/18-训练和推理有什么区别.md)

## 资料与核验

- [Lewis et al.: Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)
- [Devlin et al.: BERT — Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805)
- [Microsoft Learn: RAG solution design and evaluation guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide)
