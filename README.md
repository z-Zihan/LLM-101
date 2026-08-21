# LLM-101

完全不懂 AI？从这里开始。

`LLM-101` 是一套面向中文零基础读者的 AI / 大语言模型教程。它不要求数学或编程背景，也不把一百多个名词扔给你自己拼。

我们从真实小白会问的问题出发，沿着连续追问，一步一步建立完整心智模型。

> 当前发布范围已经闭环：86 篇已发布文章与图谱资产达到当前标准，194 个已入库真实问题全部有答案；长期路线图 B1～B9 的内容交付已完成，正在执行最终全项目审查。

## 当前完成度与边界

| 维度 | 当前状态 |
|---|---|
| 已发布正文与图谱资产 | 86 篇；其中 51 篇原有正文完成 V3 重写，新增 35 篇扩展正文与图谱资产 |
| 真实问题 | 194 条已入库，194 条 `answered`，High 未回答为 0 |
| 知识网络 | 73 个节点、130 条语义关系 |
| 内容地图 | 182 个覆盖项 `Done`，`Deferred` 与 `Verify` 均已清零 |
| 自动检查 | 链接、概念、问题严格检查、生成确定性与 Python 语法均通过 |

这里的“完成”指**当前发布范围闭环**，不是以后再也没有内容可写。`Done` 也不等于每个子概念都单独成文：只要某个问题已经在通过审查的主页面中完整回答，就不再为了凑数量拆一篇短文。

仍需继续处理的工作主要有两类：

- 对 B1～B9、全部入口和生成资产执行新的 Final Project Review；
- 两轮 130 条公开候选中，20 条达到 A 级正文核验，110 条受 Reddit、牛客等访问限制而保留为 B 级。B 级证明链已记录，但不宣称完成了实时正文复核；技术答案仍使用论文、官方文档或权威资料独立核验。

完整状态见[项目进度](./项目进度.md)，逐项范围见[内容地图](./内容地图.md)，分批顺序、依赖与验收门槛见[长期内容路线图](./长期内容路线图.md)。

## 你可以怎样使用这个项目？

### 我是完全小白

按主学习路线开始。第一站：[AI 到底是什么？](./docs/01-AI与大模型/01-AI到底是什么.md)

主路线只保留“跳过后会明显影响后续理解”的概念，目标控制在 25～35 篇。

### 我已经知道几个概念

打开 [知识网络](./知识网络.md)，从“模型”“Token”“Agent”或“RAG”等任意节点开始探索。

### 我脑子里刚好有一个问题

打开 [真实问题矩阵](./真实问题矩阵.md)。这里的问题来自用户原始聊天或可追溯的公开讨论，并与概念和答案页面双向连接。例如：

- 参数量就是训练数据吗？
- 数据是喂给模型的，那模型在被喂之前从哪来？
- Agent 和模型到底差在哪？
- Skill、Tool、MCP、Agent 是什么关系？
- 为什么 Attention 要分 Q、K、V？
- 多 Agent、RLHF 和分布式训练什么时候真的有用？

候选处理过程可查阅[第一轮审计](./候选问题审计-2026-08-19.md)与[第二轮 78 条审计](./候选问题审计-2026-08-20-第二轮.md)；来源受限或被补正的情况会明确标记。

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

主学习路线是阅读顺序，不是写作顺序。V3 当前规划如下：

```text
AI
 ↓
机器学习与深度学习
 ↓
模型 → 语言模型 → 大语言模型 → GPT → ChatGPT 产品
 ↓
参数 → Prompt → Token → 上下文
 ↓
模型生命周期 → 模型架构 → Transformer → 训练与推理
 ↓
泛化 → 推理能力 → 幻觉与验证
 ↓
API → Tool → Agent
 ↓
RAG → MCP → Skill → Coding Agent
 ↓
聊天记录
```

已经按当前质量基线完成：

1. [AI 到底是什么？](./docs/01-AI与大模型/01-AI到底是什么.md)
2. [AI、机器学习和深度学习是什么关系？](./docs/01-AI与大模型/02-AI机器学习和深度学习是什么关系.md)
3. [模型到底是什么？](./docs/01-AI与大模型/03-模型到底是什么.md)
4. [大语言模型到底是什么？](./docs/01-AI与大模型/04-什么是大语言模型.md)
5. [GPT 和 ChatGPT 有什么区别？](./docs/01-AI与大模型/05-GPT和ChatGPT有什么区别.md)
6. [参数到底是什么？](./docs/03-模型原理与训练/06-参数到底是什么.md)
7. [Prompt 到底是什么？](./docs/02-聊天Token与上下文/01-Prompt到底是什么.md)
8. [Token 到底是什么？](./docs/02-聊天Token与上下文/04-Token到底是什么.md)
9. [上下文和上下文窗口是什么？](./docs/02-聊天Token与上下文/07-上下文和上下文窗口是什么.md)
10. [一个大模型到底是怎么诞生的？](./docs/03-模型原理与训练/01-一个大模型到底是怎么诞生的.md)
11. [模型架构是什么？](./docs/03-模型原理与训练/02-模型架构是什么.md)
12. [Transformer 到底是什么？](./docs/03-模型原理与训练/03-Transformer到底是什么.md)
13. [训练和推理有什么区别？](./docs/03-模型原理与训练/18-训练和推理有什么区别.md)
14. [为什么预测下一个 Token 能学到能力？](./docs/03-模型原理与训练/10-为什么预测下一个Token能学到能力.md)
15. [泛化是什么？](./docs/04-模型能力/01-泛化是什么.md)
16. [推理能力是什么？](./docs/04-模型能力/03-推理能力是什么.md)
17. [幻觉是什么？](./docs/05-幻觉与模型局限/01-幻觉是什么.md)
18. [为什么 LLM 不是数据库？](./docs/05-幻觉与模型局限/02-为什么LLM不是数据库.md)
19. [怎么验证 AI 的回答？](./docs/05-幻觉与模型局限/04-怎么验证AI的回答.md)
20. [API 到底是什么？](./docs/06-工具与Function-Calling/01-API到底是什么.md)
21. [AI 工具到底是什么？](./docs/06-工具与Function-Calling/02-AI工具到底是什么.md)
22. [Agent 到底是什么？](./docs/07-Agent/01-Agent到底是什么.md)
23. [RAG 到底是什么？](./docs/08-RAG与知识库/01-RAG到底是什么.md)
24. [知识库是什么？](./docs/08-RAG与知识库/02-知识库是什么.md)
25. [MCP 到底是什么？](./docs/09-MCP/01-MCP到底是什么.md)
26. [Skill 到底是什么？](./docs/10-Skill/01-Skill到底是什么.md)
27. [Coding Agent 是什么？](./docs/11-Coding-Agent/04-Coding-Agent是什么.md)
28. [聊天记录是什么？](./docs/12-Memory/01-聊天记录是什么.md)

已经完成的扩展节点：

- [弱 AI、生成式 AI 和 AIGC 有什么区别？](./docs/01-AI与大模型/06-弱AI生成式AI和AIGC有什么区别.md)
- [NLP 和 Computer Vision 是什么关系？](./docs/01-AI与大模型/07-NLP和Computer-Vision是什么关系.md)
- [System Prompt 是什么？](./docs/02-聊天Token与上下文/02-System-Prompt是什么.md)
- [Jailbreak 和 Red Team 是什么？](./docs/05-幻觉与模型局限/03-Jailbreak和Red-Team是什么.md)
- [Attention 到底是什么？](./docs/03-模型原理与训练/05-Attention到底是什么.md)
- [规模定律是什么？](./docs/03-模型原理与训练/08-规模定律是什么.md)
- [RLHF 和 DPO 是什么？](./docs/03-模型原理与训练/11-RLHF和DPO是什么.md)
- [GPU、显存和推理瓶颈](./docs/03-模型原理与训练/19-GPU显存和推理瓶颈.md)
- [分布式训练是什么？](./docs/03-模型原理与训练/20-分布式训练是什么.md)
- [参数量和训练数据有什么区别？](./docs/03-模型原理与训练/07-参数量和训练数据有什么区别.md)
- [为什么参数不能全部初始化成一样？](./docs/03-模型原理与训练/04-为什么参数不能全部初始化成一样.md)
- [safetensors 和 GGUF 是什么？](./docs/03-模型原理与训练/09-safetensors和GGUF是什么.md)
- [记忆训练数据和泛化有什么区别？](./docs/04-模型能力/02-记忆训练数据和泛化有什么区别.md)
- [涌现能力是什么？](./docs/04-模型能力/04-涌现能力是什么.md)
- [多模态模型是什么？](./docs/04-模型能力/05-多模态模型是什么.md)
- [Function Calling 是什么？](./docs/06-工具与Function-Calling/03-Function-Calling是什么.md)
- [AI 怎样搜索、读文件和查数据库？](./docs/06-工具与Function-Calling/04-AI怎样搜索读文件和查数据库.md)
- [代码执行和 Computer Use 有什么风险？](./docs/06-工具与Function-Calling/05-代码执行和Computer-Use有什么风险.md)
- [从 AI Embedded、Copilot 到 Agent](./docs/07-Agent/07-从AI-Embedded和Copilot到Agent.md)
- [模型和 Agent 有什么区别？](./docs/07-Agent/02-模型和Agent有什么区别.md)
- [Agent Loop 是什么？](./docs/07-Agent/03-Agent-Loop是什么.md)
- [Agent 如何规划和恢复？](./docs/07-Agent/04-Agent如何规划和恢复.md)
- [Workflow 和 Agent 有什么区别？](./docs/07-Agent/05-Workflow和Agent有什么区别.md)
- [多 Agent 协作是什么？](./docs/07-Agent/06-多Agent协作是什么.md)
- [Embedding 是什么？](./docs/08-RAG与知识库/03-Embedding是什么.md)
- [向量数据库是什么？](./docs/08-RAG与知识库/05-向量数据库是什么.md)
- [检索是什么？](./docs/08-RAG与知识库/08-检索是什么.md)
- [RAG 和微调有什么区别？](./docs/08-RAG与知识库/11-RAG和微调有什么区别.md)
- [RAG 有哪些局限？](./docs/08-RAG与知识库/12-RAG有哪些局限.md)
- [RAG 和直接把资料放进 Prompt 有什么区别？](./docs/08-RAG与知识库/04-RAG和直接把资料放进Prompt有什么区别.md)
- [知识图谱和向量数据库有什么区别？](./docs/08-RAG与知识库/06-知识图谱和向量数据库有什么区别.md)
- [MCP 客户端和服务端是什么？](./docs/09-MCP/02-MCP客户端和服务端是什么.md)
- [MCP 工具、资源和提示是什么？](./docs/09-MCP/03-MCP工具资源和提示是什么.md)
- [MCP 和 API 有什么区别？](./docs/09-MCP/04-MCP和API有什么区别.md)
- [MCP 和 Function Calling 有什么区别？](./docs/09-MCP/05-MCP和Function-Calling有什么区别.md)
- [MCP 和 Agent 有什么区别？](./docs/09-MCP/06-MCP和Agent有什么区别.md)
- [Prompt 和 Skill 有什么区别？](./docs/10-Skill/02-Prompt和Skill有什么区别.md)
- [Tool 和 Skill 有什么区别？](./docs/10-Skill/03-Tool和Skill有什么区别.md)
- [MCP 和 Skill 有什么区别？](./docs/10-Skill/04-MCP和Skill有什么区别.md)
- [Agent 和 Skill 有什么区别？](./docs/10-Skill/05-Agent和Skill有什么区别.md)
- [AI Coding 是什么？](./docs/11-Coding-Agent/01-AI-Coding是什么.md)
- [项目上下文是什么？](./docs/11-Coding-Agent/08-项目上下文是什么.md)
- [上下文工程是什么？](./docs/11-Coding-Agent/09-上下文工程是什么.md)
- [Shell 和 Command 是什么？](./docs/11-Coding-Agent/02-Shell和Command是什么.md)
- 产品案例：[Codex](./docs/11-Coding-Agent/10-Codex产品案例.md) · [Claude Code](./docs/11-Coding-Agent/11-Claude-Code产品案例.md) · [Cursor](./docs/11-Coding-Agent/12-Cursor产品案例.md)
- [AI 概念全景图](./docs/13-AI全景图/01-AI概念全景图.md) · [AI 应用栈](./docs/13-AI全景图/02-AI应用栈.md) · [AI 概念速查表](./docs/13-AI全景图/03-AI概念速查表.md)
- 流程图：[模型生命周期](./docs/13-AI全景图/04-模型生命周期图.md) · [训练与推理](./docs/13-AI全景图/05-训练与推理对照图.md) · [Agent 架构](./docs/13-AI全景图/06-Agent架构图.md)

Deferred 与 Verify 已按[长期内容路线图](./长期内容路线图.md)完成处理：Now / Next / Later 共 9 个批次、27 个实际交付物，全部状态行均有可审计结论。每批都按“研究 → 重写 → 真实问题与知识网络更新 → 15 项审查 → 自动检查 → 提交推送”的合同推进。

三篇可选历史专题把概念放回原始论文与官方发布记录中，不改变 28 篇主路线：[从规则系统到深度学习](./history/01-从规则系统到深度学习.md) · [从 Transformer 到 Chat 模型](./history/02-从Transformer到Chat模型.md) · [从 RAG、工具调用到 Coding Agent](./history/03-从RAG工具调用到Coding-Agent.md)。

## 扩展学习路线

扩展路线负责解释主线中可以先略过、但系统学习时值得深入的内容，例如：

- Tokenizer、上下文窗口、Attention、多模态；
- 规模定律、RLHF、DPO、GPU 与分布式训练；
- Embedding、向量数据库、Rerank；
- MCP 客户端/服务端、Resource、Prompt；
- Agent 规划、多 Agent、Project Context、Prompt 与 Skill 的区别。

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

每篇 V3 文章都要经过：

- Accuracy Review
- Beginner Review
- Beginner Depth Review
- Chinese Language Review
- Real Question Review
- Question Coverage Review
- Knowledge Graph Review
- Cross-link Review
- Layout Review
- AI Writing Smell Review
- Architecture Review
- Terminology Review
- Duplication Review
- Source Review
- Link Review

关键事实优先使用原始论文、官方规范、官方文档和权威教材。聊天记录只提供小白问题与追问顺序，不作为事实来源。

## 项目管理入口

- [项目进度](./项目进度.md)
- [内容地图](./内容地图.md)
- [知识网络](./知识网络.md)
- [真实问题矩阵](./真实问题矩阵.md)
- [真实问题库](./真实问题库.yml)
- [排版规范](./排版规范.md)
- [术语表](./术语表.md)
- [文章模板](./文章模板.md)
- [目录结构](./目录结构.md)
- [小白问题库](./FAQ/小白问题库.md)

## 自动检查

```bash
python3 scripts/build_knowledge_graph.py
python3 scripts/check_links.py
python3 scripts/check_concepts.py
python3 scripts/build_question_matrix.py
python3 scripts/check_questions.py
git diff --check
```

只有自动检查和 15 项 Review 全部通过后，文章才能标记为 `Done`。项目终审还会使用 `python3 scripts/check_questions.py --strict`，确保所有高价值问题都已回答。

---

`LLM-101` 的目标不是让你背会术语，而是让你能把这些概念用自己的话讲清楚，并知道它们为什么会连接在一起。
