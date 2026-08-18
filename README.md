# LLM-101

完全不懂 AI？从这里开始。

`LLM-101` 是一套面向中文零基础读者的 AI / 大语言模型教程。它不要求数学或编程背景，也不把一百多个名词扔给你自己拼。

我们从真实小白会问的问题出发，沿着连续追问，一步一步建立完整心智模型。

> 当前正在进行 v2 全量重构。旧版文章保留作参考，但除前三篇 Style Checkpoint 外，统一标记为 `Needs Rewrite`。

## 你可以怎样使用这个项目？

### 我是完全小白

按主学习路线开始。第一站：[AI 到底是什么？](./docs/01-AI与大模型/01-AI到底是什么.md)

主路线只保留“跳过后会明显影响后续理解”的概念，目标控制在 25～35 篇。

### 我已经知道几个概念

打开 [知识网络](./知识网络.md)，从“模型”“Token”“Agent”或“RAG”等任意节点开始探索。

### 我脑子里刚好有一个问题

打开 [小白问题库](./FAQ/小白问题库.md)。例如：

- 参数量就是训练数据吗？
- 数据是喂给模型的，那模型在被喂之前从哪来？
- Agent 和模型到底差在哪？
- Skill、Tool、MCP、Agent 是什么关系？

### 我想系统学一个专题

- [AI 与大模型](./docs/01-AI与大模型/)
- [Token 与上下文](./docs/02-聊天Token与上下文/)
- [模型原理与训练](./docs/03-模型原理与训练/)
- [模型能力](./docs/04-模型能力/)
- [幻觉与模型局限](./docs/05-幻觉与模型局限/)
- [工具与函数调用](./docs/06-工具与Function-Calling/)
- [Agent](./docs/07-Agent/)
- [RAG 与知识库](./docs/08-RAG与知识库/)
- [MCP](./docs/09-MCP/)
- [Skill](./docs/10-Skill/)
- [Coding Agent](./docs/11-Coding-Agent/)
- [Memory](./docs/12-Memory/)

## 主学习路线

主学习路线是阅读顺序，不是写作顺序。v2 当前规划如下：

```text
AI
 ↓
机器学习与深度学习
 ↓
模型 → 语言模型 → 大语言模型
 ↓
参数 → Prompt → Token → 上下文
 ↓
模型生命周期 → 训练与推理 → Transformer
 ↓
泛化 → 推理能力 → 幻觉与验证
 ↓
API → Tool → Agent
 ↓
RAG → MCP → Skill → Coding Agent
 ↓
聊天记录与 Memory
 ↓
AI 全景图
```

当前 Style Checkpoint：

1. [AI 到底是什么？](./docs/01-AI与大模型/01-AI到底是什么.md)
2. [AI、机器学习和深度学习是什么关系？](./docs/01-AI与大模型/02-AI机器学习和深度学习是什么关系.md)
3. [模型到底是什么？](./docs/01-AI与大模型/03-模型到底是什么.md)

前三篇通过人工风格确认后，才会继续全量重写。

## 扩展学习路线

扩展路线负责解释主线中可以先略过、但系统学习时值得深入的内容，例如：

- Tokenizer、上下文窗口、Attention；
- Loss、Gradient、SFT、RLHF、DPO；
- Embedding、向量数据库、Rerank；
- MCP 客户端/服务端、Resource、Prompt；
- Agent Loop、Project Context、Prompt 与 Skill 的区别。

完整规划见 [内容地图](./内容地图.md)。

## 先看懂四张关系图

一棵树不能准确表达所有 AI 概念。下面四张图分别回答四个问题。

### 1. AI、机器学习、模型和 LLM 是什么关系？

```mermaid
flowchart TD
    AI["人工智能 AI"] --> ML["机器学习"]
    ML --> DL["深度学习"]
    ML --> Model["训练得到模型"]
    DL --> Transformer["可使用 Transformer 等架构"]
    Transformer --> LM["语言模型"]
    LM --> LLM["大语言模型 LLM"]
```

机器学习是实现 AI 的一种重要路线，但不是唯一路线。不是所有机器学习都属于深度学习，也不是所有模型都是语言模型。

### 2. 一个典型 Agent 应用由什么组成？

```mermaid
flowchart TD
    Goal["用户目标"] --> Agent["Agent 系统"]
    Agent --> Model["模型"]
    Agent --> Context["上下文"]
    Agent --> Tool["工具"]
    Agent -.可选.-> Memory["Memory"]
    Agent -.可选.-> Skill["Skill"]
    Tool --> API["API"]
    Tool -.可通过.-> MCP["MCP"]
```

Agent 不是一种模型。它是围绕目标组织模型、上下文、工具和状态的系统。

### 3. RAG 回答问题时发生了什么？

```mermaid
flowchart LR
    Q["用户问题"] --> Retrieve["检索资料"]
    Source["知识库或其他来源"] --> Retrieve
    Retrieve --> Context["把相关资料加入上下文"]
    Context --> LLM["模型生成回答"]
    LLM --> Verify["引用与验证"]
```

RAG 不会把知识永久写进模型参数，也不能自动保证答案正确。

### 4. 知识网络怎样连接正文？

```mermaid
flowchart LR
    Data["知识网络.yml"] --> Matrix["概念矩阵"]
    Data --> Routes["Main / Extended Path"]
    Data --> Graphs["子网络与全景图"]
    Matrix --> Article["唯一概念主页面"]
    Article --> Related["前置、后续、易混、使用者"]
```

关系数据与文章正文分开维护，文件改名也不会改变概念 ID。

## 这个项目怎样保证质量？

每篇 v2 文章都要经过：

- Accuracy Review
- Beginner Review
- Beginner Depth Review
- Chinese Language Review
- Architecture Review
- Terminology Review
- Knowledge Graph Review
- Cross-link Review
- Duplication Review
- Source Review
- Link Review

关键事实优先使用原始论文、官方规范、官方文档和权威教材。聊天记录只提供小白问题与追问顺序，不作为事实来源。

## 项目管理入口

- [项目进度](./项目进度.md)
- [内容地图](./内容地图.md)
- [知识网络](./知识网络.md)
- [术语表](./术语表.md)
- [文章模板](./文章模板.md)
- [目录结构](./目录结构.md)
- [小白问题库](./FAQ/小白问题库.md)

## 自动检查

```bash
python3 scripts/build_knowledge_graph.py
python3 scripts/check_links.py
python3 scripts/check_concepts.py
git diff --check
```

只有自动检查和全部 Review 通过后，文章才能标记为 `Done`。

---

`LLM-101` 的目标不是让你背会术语，而是让你能把这些概念用自己的话讲清楚，并知道它们为什么会连接在一起。
