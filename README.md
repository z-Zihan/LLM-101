# LLM-101

> 从真实小白问题出发，用大白话建立完整的 AI / LLM 心智模型。

`LLM-101` 不是一份“大模型名词大全”，也不是一门要求数学、机器学习背景的课程。

它希望解决的是另一件事：

**让一个完全不懂 AI 的人，按照正确的认知顺序，真正搞清楚 AI、LLM、Token、Context、RAG、Agent、MCP、Skill、Coding Agent 等概念到底是什么，以及它们之间是什么关系。**

---

## 为什么做这个项目？

现在关于大模型的资料很多，但初学者常见的问题不是“资料太少”，而是：

- 每篇文章只解释一个名词，看完以后仍然不知道概念之间是什么关系。
- 教程经常默认读者已经知道“模型、参数、训练、推理、上下文”等基础概念。
- 很多内容为了好懂使用类比，但没有说明类比的边界。
- AI 产品、模型、API、Agent、MCP 经常被混在一起讨论。
- 技术更新很快，产品榜单和厂商参数容易过期，而底层概念其实更值得先学。

`LLM-101` 的内容设计来自一批真实的小白追问，例如：

- 参数量就是训练数据吗？
- 1.5B 到底是什么意思？
- 上下文窗口是什么？
- 数据是“喂给模型”的，那被喂之前的模型从哪来？
- 架构、层数、宽度到底是什么？
- 参数最后长什么样？
- 几个数字为什么会有“智能”？
- GPU 到底在算什么？
- RAG、Agent、MCP、Skill 到底是什么关系？
- 如果两个公司训练条件完全一样，会训练出同一个模型吗？

我们不照着提问顺序直接堆内容，而是把这些真实问题重新组织成一条从零开始的学习路径。

---

# 推荐学习路线

```text
AI
 ↓
Machine Learning / Deep Learning
 ↓
Model
 ↓
Language Model
 ↓
LLM
 ↓
Prompt / Token / Context
 ↓
模型如何训练和推理
 ↓
Capabilities / Limitations
 ↓
Tools
 ↓
Agent
 ↓
RAG
 ↓
MCP
 ↓
Skill
 ↓
Coding Agent
 ↓
Memory
 ↓
AI World Map
```

第一次学习时，只需要按照这个顺序阅读 `Main` 内容；`Optional` 内容可以按兴趣补充。

历史、厂商、GPU、训练工程、并行计算等内容全部放在扩展区域，不会阻塞主学习路线。

---

# AI 世界总览

一棵树无法准确表达所有 AI 概念。先用三张小图分别看技术路线、应用组成和 RAG 流程。

## 1. AI 与模型技术路线

```text
Artificial Intelligence
├── Rules / Search / Planning / …
└── Machine Learning
          ↓
     Deep Learning
          ↓
Transformer 等模型架构
          ↓
   Language Model
          ↓
         LLM
```

这是一条帮助入门的技术路线，不是说 AI 只能由机器学习实现，也不是说所有深度学习模型都是语言模型。

## 2. 现代 AI 应用由什么组成

```text
                     AI Application
                            │
                     Workflow / Agent
                            │
        ┌───────────┬───────┼───────────┐
        │           │       │           │
      Model       Context  Memory      Skills
        │                                   │
        └────────────── Tools ──────────────┘
                            │
               ┌────────────┼──────────────┐
               │            │              │
              API          MCP        Browser /
                                    Computer Use
```

这些是可以组合的系统部件和连接方式，不是严格父子关系。MCP 可以连接工具与数据，Skill 可以组织做事方法；Coding Agent 则是一类把模型、上下文、工具和工作循环组合起来的应用。

## 3. RAG 是一条检索增强流程

```text
Question
   ↓
Retrieval
   ↓
Knowledge Base / Search
   ↓
Relevant Context
   ↓
Model
   ↓
Answer
```

RAG 可以被普通应用或 Agent 使用，但不依赖 Agent，也不属于 Function Calling。

---

# 章节

## 01. AI 与大语言模型

回答：

> AI 到底是什么？LLM 又处在 AI 世界的什么位置？

核心概念：

- AI
- Narrow AI / AGI
- Machine Learning
- Deep Learning
- NLP
- Generative AI
- AIGC
- Foundation Model
- Language Model
- LLM
- GPT
- Model / API / Product / Company

---

## 02. 你和大模型聊天时发生了什么

回答：

> 我输入一句话以后，大模型到底经历了什么？

核心概念：

- Prompt
- System Prompt
- Token
- K / M / B / T
- Tokenizer
- Input / Output Token
- Context
- Context Window
- Sampling
- Temperature / Top-p
- KV Cache

---

## 03. 一个大模型是怎么诞生的

回答：

> 数据是“喂给模型”的，那被喂之前的模型从哪来？

核心概念：

- Architecture
- Transformer
- Layer
- Hidden Size
- Attention
- Parameter
- Parameter Count
- Training Data
- Random Initialization
- Pre-training
- Loss
- Gradient
- Backpropagation
- Post-training
- SFT
- Alignment
- RLHF
- DPO
- Checkpoint
- Deployment
- Inference

---

## 04. 大模型为什么会有能力

回答：

> 一堆数字为什么最后会表现得像“懂”东西？

核心概念：

- Memorization
- Generalization
- Emergence
- In-context Learning
- Reasoning
- Multimodal
- MoE
- Scaling Laws
- Distillation
- Quantization
- LoRA

---

## 05. 幻觉与模型局限

回答：

> 为什么 AI 会一本正经地说错话？

核心概念：

- Hallucination
- Knowledge in Parameters
- LLM ≠ Database
- Verification
- Prompt Injection
- Jailbreak
- Red Team

---

## 06. Tool / API / Function Calling

回答：

> 为什么现在 AI 能搜索网页、读文件、运行代码？

核心概念：

- API
- Tool
- Function Calling
- Tool Calling
- Web Search
- File Tool
- Code Execution
- Browser / Computer Use
- Database Tool
- OCR

---

## 07. Agent

回答：

> Agent 和普通大模型到底差在哪？

核心概念：

- Agent
- Agent Loop
- Planning
- Tool Use
- Workflow
- Copilot
- AI Embedded → Copilot → Agent
- Multi-Agent

---

## 08. RAG

回答：

> 模型不知道我的私有资料，为什么还能“看着资料回答”？

核心概念：

- RAG
- Knowledge Base
- Embedding
- Vector
- Semantic Search
- Vector Database
- Chunk
- Retrieval
- Rerank
- Knowledge Graph
- RAG vs Fine-tuning

---

## 09. MCP

回答：

> MCP 是 API、Tool 还是 Agent？

核心概念：

- MCP
- Client / Server
- Tool
- Resource
- Prompt
- MCP vs API
- MCP vs Function Calling
- MCP vs Agent

---

## 10. Skill

回答：

> Prompt、Skill、Tool、MCP、Agent 到底什么关系？

核心概念：

- Skill
- Prompt vs Skill
- Tool vs Skill
- MCP vs Skill
- Agent vs Skill

---

## 11. Coding Agent

回答：

> 为什么 Codex / Claude Code 这类产品可以直接修改整个代码项目？

核心概念：

- AI Coding
- Code Completion
- Copilot
- Coding Agent
- IDE
- Terminal
- Git
- Project Context
- Context Engineering

---

## 12. Memory

回答：

> AI “记住我”到底是什么意思？

核心概念：

- Conversation History
- Context
- Memory
- Long-term Memory
- RAG
- Cache
- Context vs Memory vs RAG vs Cache

---

## 13. AI 世界全景图

把前面所有概念重新串起来：

```text
Data
 ↓
Training
 ↓
Model
 ↓
Deployment
 ↓
Inference
 ↓
API
 ↓
Application
 ↓
Workflow / Agent
 ↓
Tools / RAG / MCP / Skills / Memory
```

---

# 扩展内容

## AI 发展史

只讲关键节点，不做年份流水账：

```text
Rule-based AI
    ↓
Machine Learning
    ↓
Deep Learning
    ↓
Transformer
    ↓
Foundation Model
    ↓
LLM
    ↓
Instruction / Chat
    ↓
RAG / Tool Calling
    ↓
Agent
    ↓
MCP
    ↓
Coding Agent / Computer Use
```

---

## AI 模型分类

按不同维度理解模型：

- Closed / Open-weight / Open-source
- Dense / MoE
- Text / Vision / Audio / Video / Multimodal
- General / Reasoning / Embedding / Reranker / Generation
- Base / Instruction / Chat / Fine-tuned
- SLM / LLM

---

## AI 产业生态

不做排行榜，只解释产业角色：

- Model Provider
- Cloud Provider
- Application Company
- Model Hub
- Inference Provider
- Hardware Vendor

厂商、产品、价格、具体型号等内容属于易变信息，正式文章中需要单独核验和标注更新时间。

---

## AI 硬件扫盲

放在 `appendix/hardware/`：

- CPU
- GPU
- CUDA
- Tensor Core
- FLOPS
- VRAM
- RAM
- SSD
- HBM
- Bandwidth
- Interconnect
- PCIe / NVLink
- Server
- Cluster
- Data Center
- Distributed Training

---

# 内容等级与学习路径

每篇内容会标记为：

- **Core**：面向零基础读者解释的核心概念
- **Advanced**：理解主线后继续深入
- **Appendix**：硬件、训练、生态等扩展知识

文章还会标记独立的学习路径：

- **Main**：主学习路线，跳过可能影响后文理解
- **Optional**：补充阅读，不阻塞主学习路线

---

# 每篇文章怎么写

`LLM-101` 不采用纯百科式定义。

每篇文章优先按照：

```text
真实问题
   ↓
先说人话
   ↓
举例
   ↓
严格定义
   ↓
工作原理
   ↓
最容易混淆的概念
   ↓
为什么需要知道
   ↓
下一步学习什么
```

详细模板见 [`ARTICLE_TEMPLATE.md`](./ARTICLE_TEMPLATE.md)。

---

# 内容原则

### 1. 先建立心智模型，再补专业术语

如果一个概念可以先用 20 秒讲明白，就不要先上公式。

### 2. 类比不是定义

例如：

> “上下文窗口像短期工作台”

可以帮助理解，但文章必须同时说明：

> 这只是类比，不代表 LLM 拥有人类意义上的短期记忆。

### 3. 不为了简单而写错

简单和准确不是二选一。

### 4. 不把易变信息写成永久事实

厂商排名、具体模型参数、价格、API 行为、产品功能等需要标注时间并重新核验。

### 5. 区分基础概念与具体产品

重点解释长期稳定的概念，再用产品作为案例。

---

# 项目状态

当前：**Main Path 51 篇已完成并通过批次 Review**

当前已完成的 Main Path：

1. [AI 是什么](./docs/01-ai-and-llm/01-what-is-ai.md)（Done）
2. [AI、ML、DL 到底什么关系](./docs/01-ai-and-llm/02-ai-ml-dl.md)（Done）
3. [什么是模型](./docs/01-ai-and-llm/03-what-is-model.md)（Done）
4. [什么是 LLM](./docs/01-ai-and-llm/04-what-is-llm.md)（Done）
5. [GPT 和 ChatGPT 有什么区别](./docs/01-ai-and-llm/05-gpt-vs-chatgpt.md)（Done）
6. [参数到底是什么](./docs/03-how-models-work/06-parameter.md)（Done）
7. [参数量和训练数据有什么区别](./docs/03-how-models-work/07-parameter-vs-training-data.md)（Done）
8. [Token 是什么](./docs/02-chat-and-context/04-token.md)（Done）
9. [Context / Context Window 是什么](./docs/02-chat-and-context/07-context.md)（Done）
10. [一个大模型到底是怎么诞生的](./docs/03-how-models-work/01-model-lifecycle.md)（Done）
11. [为什么“预测下一个 Token”还能学到能力](./docs/03-how-models-work/10-next-token-prediction.md)（Done）
12. [Training 和 Inference 有什么区别](./docs/03-how-models-work/18-training-vs-inference.md)（Done）
13. [Prompt 是什么](./docs/02-chat-and-context/01-prompt.md)（Done）
14. [模型架构是什么](./docs/03-how-models-work/02-architecture.md)（Done）
15. [Transformer 是什么](./docs/03-how-models-work/03-transformer.md)（Done）
16. [Attention 是什么](./docs/03-how-models-work/05-attention.md)（Done）
17. [Generalization（泛化）是什么](./docs/04-capabilities/01-generalization.md)（Done）
18. [Reasoning（推理能力）是什么](./docs/04-capabilities/03-reasoning.md)（Done）
19. [Hallucination（幻觉）是什么](./docs/05-limitations/01-hallucination.md)（Done）
20. [为什么 LLM 不是数据库](./docs/05-limitations/02-llm-is-not-database.md)（Done）
21. [怎么验证 AI 的回答](./docs/05-limitations/04-verification.md)（Done）
22. [API 是什么](./docs/06-tools/01-api.md)（Done）
23. [AI Tool 是什么](./docs/06-tools/02-tool.md)（Done）
24. [Function Calling 是什么](./docs/06-tools/03-function-calling.md)（Done）
25. [Agent 是什么](./docs/07-agent/01-what-is-agent.md)（Done）
26. [Model 和 Agent 有什么区别](./docs/07-agent/02-model-vs-agent.md)（Done）
27. [Agent Loop 是什么](./docs/07-agent/03-agent-loop.md)（Done）
28. [Workflow 和 Agent 有什么区别](./docs/07-agent/05-workflow-vs-agent.md)（Done）
29. [RAG 是什么](./docs/08-rag/01-what-is-rag.md)（Done）
30. [Knowledge Base 是什么](./docs/08-rag/02-knowledge-base.md)（Done）
31. [Embedding 是什么](./docs/08-rag/03-embedding.md)（Done）
32. [Vector Database 是什么](./docs/08-rag/05-vector-database.md)（Done）
33. [Retrieval 是什么](./docs/08-rag/08-retrieval.md)（Done）
34. [RAG 和 Fine-tuning 有什么区别](./docs/08-rag/11-rag-vs-finetuning.md)（Done）
35. [RAG 有哪些局限](./docs/08-rag/12-rag-limitations.md)（Done）
36. [MCP 是什么](./docs/09-mcp/01-what-is-mcp.md)（Done）
37. [MCP Client 和 Server 是什么](./docs/09-mcp/02-client-server.md)（Done）
38. [MCP Tools、Resources、Prompts 是什么](./docs/09-mcp/03-tools-resources-prompts.md)（Done）
39. [MCP 和 API 有什么区别](./docs/09-mcp/04-mcp-vs-api.md)（Done）
40. [MCP 和 Function Calling 有什么区别](./docs/09-mcp/05-mcp-vs-function-calling.md)（Done）
41. [MCP 和 Agent 有什么区别](./docs/09-mcp/06-mcp-vs-agent.md)（Done）
42. [Skill 是什么](./docs/10-skills/01-what-is-skill.md)（Done）
43. [Prompt 和 Skill 有什么区别](./docs/10-skills/02-skill-vs-prompt.md)（Done）
44. [Tool 和 Skill 有什么区别](./docs/10-skills/03-skill-vs-tool.md)（Done）
45. [MCP 和 Skill 有什么区别](./docs/10-skills/04-skill-vs-mcp.md)（Done）
46. [Agent 和 Skill 有什么区别](./docs/10-skills/05-skill-vs-agent.md)（Done）
47. [AI Coding 是什么](./docs/11-coding-agent/01-ai-coding.md)（Done）
48. [Coding Agent 是什么](./docs/11-coding-agent/04-coding-agent.md)（Done）
49. [Project Context 是什么](./docs/11-coding-agent/08-project-context.md)（Done）
50. [Context Engineering 是什么](./docs/11-coding-agent/09-context-engineering.md)（Done）
51. [Conversation History 是什么](./docs/12-memory/01-conversation-history.md)（Done）

完整内容地图见 [`CONTENT_MAP.md`](./CONTENT_MAP.md)。

下一批继续完成 Context vs Memory、Memory、RAG vs Memory。

---

## License

待确定。
