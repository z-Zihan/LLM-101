# RAG 是什么？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> 模型没学过我的公司资料，为什么还能根据资料回答？
>
> RAG 是搜索、数据库，还是一种训练方法？

## 先说人话

RAG（Retrieval-Augmented Generation，检索增强生成）是一种流程：先从外部资料中找出与问题相关的内容，再把这些内容提供给模型生成回答。

它像“先开卷查资料，再组织答案”。这是帮助理解的类比；严格来说，RAG 是检索系统与生成模型的组合，不保证每次都查对或答对。

## 举个例子

用户问：“公司今年的差旅报销上限是多少？”

模型参数可能没有这份内部政策。RAG 系统可以：

```text
问题
 ↓
检索公司知识库
 ↓
找到差旅政策相关段落
 ↓
把段落加入模型 Context
 ↓
模型根据资料回答并给出来源
```

政策更新时，可以更新外部资料，而不必为每次改动重新训练整个模型。

## 严格来说

原始 RAG 研究把预训练生成模型中的参数化能力，与可检索的外部非参数化记忆结合起来。今天“RAG”常被更宽泛地用于各种“检索 → 提供证据 → 生成”的系统。

典型流程分为两部分：

```text
准备阶段：资料 → 清洗 / 切分 → 建立可检索索引

回答阶段：问题 → 检索相关内容 → 加入 Context → 生成答案
```

具体系统可以使用向量检索、关键词搜索、SQL、知识图谱或混合检索，不限于一种实现。

## 为什么需要 RAG？

只依赖模型参数会遇到几个问题：

- 私有资料可能没有参与训练；
- 新政策和实时信息会变化；
- 参数中的事实不容易逐条更新；
- 回答来源不容易直接检查。

RAG 把一部分知识放在可更新、可授权、可追踪的外部数据源中，并在请求时按需取回。

## 检索结果怎样进入模型？

检索系统返回文本片段、记录或其他证据，应用把它们与用户问题、指令一起组织成当前 Context。

模型仍然是在进行推理并生成 Token。资料被放进 Context，不等于写入模型参数，也不等于模型以后永久记住。

## RAG 依赖 Agent 吗？

不依赖。普通应用可以按固定 Workflow 完成：

```text
接收问题 → 检索 → 生成 → 返回
```

Agent 也可以把检索作为工具，并根据结果决定是否继续搜索。但这是 RAG 与 Agent 的组合，不是 RAG 的必要条件。

## RAG 能消灭幻觉吗？

不能保证。失败可能来自：

- 知识库本身错误、过时或缺失；
- 查询没有表达真正需求；
- 检索到不相关或不完整片段；
- 重要内容被切分或排序丢失；
- 模型忽略、误读或超出证据生成；
- 引用与结论没有真正对应。

因此 RAG 需要分别评估“是否检索到正确证据”和“回答是否忠实使用证据”。

## 最容易搞混的东西

### RAG ≠ Vector Database

向量数据库可以支持语义检索，但只是可能的基础设施。RAG 还包括资料处理、检索策略、Context 组织和生成。

### RAG ≠ Fine-tuning

RAG 在请求时提供外部资料；Fine-tuning 通过训练更新模型参数。两者解决的问题不同，也可以组合。

### RAG ≠ 直接粘贴资料

直接粘贴是手工提供 Context；RAG 多了自动查找和选择相关资料的过程。

### RAG ≠ Function Calling

Function Calling 是结构化请求工具的机制；RAG 是检索增强生成流程。应用可以通过函数调用触发检索，但两者不属于同一个概念。

## 常见误区

### 误区 1：接入知识库以后，模型就知道全部资料

模型通常只看到当前检索出的有限内容。没检索到的资料不会自动进入这次 Context。

### 误区 2：检索数量越多越好

过多低相关内容会占用 Context，并可能干扰回答。数量、相关性、多样性和排序需要平衡。

### 误区 3：答案带引用就已经验证

还要打开来源，检查引用段落是否真实支持对应结论。

## 为什么我要知道它？

RAG 是让模型使用私有、最新和可追踪资料的常见方法。理解它后，你能把模型参数、Context、Knowledge Base、检索和生成放在正确层次。

## 你只需要记住

1. RAG 先检索外部资料，再把相关内容放进 Context 供模型生成。
2. RAG 不等于重新训练，也不依赖 Agent。
3. Vector Database 是可选实现之一，不等于整个 RAG。
4. RAG 能降低部分知识问题，但检索和生成都可能失败，不能保证消灭幻觉。

## 继续学习

- [上一篇：Workflow 和 Agent 有什么区别](../07-Agent/05-Workflow和Agent有什么区别.md)
- [下一篇：Knowledge Base 是什么](./02-知识库是什么.md)
- [相关：Context / Context Window 是什么](../02-聊天Token与上下文/07-上下文和上下文窗口是什么.md)

## 资料与核验

- [Lewis et al.: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Guu et al.: REALM — Retrieval-Augmented Language Model Pre-Training](https://arxiv.org/abs/2002.08909)
- [Microsoft Learn: RAG solution design and evaluation guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide)
