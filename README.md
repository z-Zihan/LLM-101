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
AI / ML / DL / LLM
        ↓
Prompt / Token / Context
        ↓
模型怎么诞生
        ↓
模型为什么会有能力
        ↓
幻觉与局限
        ↓
Tool / API / Function Calling
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
AI 世界全景图
```

第一次学习时，只需要按照这个顺序阅读 Core 内容。

历史、厂商、GPU、训练工程、并行计算等内容全部放在扩展区域，不会阻塞主学习路线。

---

# AI 世界总览

```text
                         AI
                          │
                    Machine Learning
                          │
                     Deep Learning
                          │
                    Transformer
                          │
                         LLM
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
      Prompt            Context            Tools
                                             │
                                     Function Calling
                                             │
                        ┌────────────────────┴─────────────────┐
                        │                                      │
                       RAG                                   Agent
                        │                                      │
              Embedding / Vector DB                       Skills
                                                               │
                                                              MCP
                                                               │
                                                        Coding Agent
```

这张图只是帮助建立第一层关系。后续章节会逐步修正和细化其中的概念。

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

# 内容等级

每篇内容会标记为：

- **Core**：第一次学习必须理解
- **Advanced**：理解主线后继续深入
- **Appendix**：硬件、训练、生态等扩展知识

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

当前：**v0.1 第一批 Core 已完成并通过批次 Review**

第一批优先完成：

1. [AI 是什么](./docs/01-ai-and-llm/01-what-is-ai.md)（Done）
2. [AI、ML、DL 到底什么关系](./docs/01-ai-and-llm/02-ai-ml-dl.md)（Done）
3. [什么是模型](./docs/01-ai-and-llm/03-what-is-model.md)（Done）
4. 什么是 LLM
5. GPT 和 ChatGPT 有什么区别
6. 参数到底是什么
7. 参数量和训练数据有什么区别
8. Token 是什么
9. Context / Context Window 是什么
10. 一个大模型到底是怎么诞生的
11. 为什么“预测下一个 Token”还能学到能力
12. Training 和 Inference 有什么区别

完整内容地图见 [`CONTENT_MAP.md`](./CONTENT_MAP.md)。

---

## License

待确定。
