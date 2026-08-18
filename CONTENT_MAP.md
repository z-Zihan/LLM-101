# LLM-101 Content Map

> 这是 `LLM-101` 的内容总蓝图，不等于最终文章目录。

Content Map 的目标是解决四个问题：

1. 这个项目到底要覆盖哪些概念？
2. 每个概念应该放在哪里？
3. 哪些是 Core，哪些是 Advanced / Appendix？
4. 哪些内容来自真实小白问题，哪些内容需要后续联网核验？

---

## 状态说明

| 状态 | 含义 |
|---|---|
| Todo | 尚未开始 |
| Draft | 已有草稿 |
| Verify | 需要事实核验 |
| Review | 等待内容评审 |
| Done | 已完成 |

等级：

- `Core`：主学习路线必须掌握
- `Advanced`：进阶理解
- `Appendix`：硬件 / 训练 / 生态等扩展

---

# 01. AI 与大语言模型

| 内容 | 等级 | 状态 | 主要解决的问题 |
|---|---|---|---|
| AI | Core | Done | AI 到底是什么？ |
| Narrow AI / Weak AI | Core | Todo | “弱 AI”是不是能力很弱？ |
| AGI | Core | Todo | AGI 和现在的大模型有什么区别？ |
| Generative AI | Core | Todo | 什么是生成式 AI？ |
| AIGC | Core | Todo | AIGC 和 Generative AI 是一回事吗？ |
| Machine Learning | Core | Done | ML 和 AI 什么关系？ |
| Deep Learning | Core | Done | DL 和 ML 什么关系？ |
| Model | Core | Done | 模型和算法、数据、产品有什么区别？ |
| NLP | Core | Todo | NLP 是模型吗？ |
| Computer Vision | Advanced | Todo | CV 和 NLP 是什么关系？ |
| Foundation Model | Core | Todo | 什么叫“基础模型 / 底座模型”？ |
| Language Model | Core | Todo | 语言模型到底在建模什么？ |
| LLM | Core | Todo | Large 到底“大”在哪里？ |
| GPT | Core | Todo | GPT 是产品还是模型？ |
| Model / API / Product / Company | Core | Todo | GPT、ChatGPT、OpenAI 为什么不能混为一谈？ |

---

# 02. Chat / Prompt / Token / Context

| 内容 | 等级 | 状态 | 真实问题 / 目标 |
|---|---|---|---|
| Prompt | Core | Todo | Prompt 到底是什么？ |
| System Prompt | Core | Todo | 为什么 AI 会有“隐藏规则”？ |
| Prompt Engineering | Core | Todo | 怎么把需求表达得更清楚？ |
| Zero-shot / Few-shot | Advanced | Todo | 为什么给示例会更稳定？ |
| Token | Core | Todo | Token 是字还是单词？ |
| K / M / B / T | Core | Todo | 1K、1M、1B、1T 到底是多少？ |
| Tokenizer | Core | Todo | 文本是怎么变成 Token 的？ |
| Input / Output Token | Core | Todo | API 为什么分输入和输出计费？ |
| Context | Core | Todo | Context 到底是什么？ |
| Context Window | Core | Todo | 上下文窗口是什么意思？ |
| Long Context | Advanced | Todo | 窗口越大就一定记得越好吗？ |
| Sampling | Advanced | Todo | 模型怎么选下一个 Token？ |
| Temperature | Advanced | Todo | 为什么同一个问题答案不一样？ |
| Top-p | Advanced | Todo | Top-p 和 Temperature 有什么区别？ |
| Autoregressive Generation | Core | Todo | 为什么 AI 一个 Token 一个 Token 输出？ |
| KV Cache | Advanced | Todo | 缓存到底缓存了什么？ |

---

# 03. 模型诞生与训练

| 内容 | 等级 | 状态 | 真实问题 / 目标 |
|---|---|---|---|
| Model Lifecycle | Core | Todo | 一个模型从零到上线经历什么？ |
| Architecture | Core | Todo | 架构到底是什么意思？ |
| Transformer | Core | Todo | Transformer 是框架吗？ |
| PyTorch / JAX | Advanced | Todo | 框架和架构有什么区别？ |
| Layer | Core | Todo | “多少层”是什么意思？ |
| Hidden Size / Width | Advanced | Todo | “多宽”是什么意思？ |
| Attention | Core | Todo | Attention 到底在做什么？ |
| Self-Attention | Advanced | Todo | Self-Attention 是什么？ |
| FFN | Advanced | Todo | Transformer 一层里除了 Attention 还有什么？ |
| Parameter | Core | Todo | 参数到底是什么？ |
| Parameter Count | Core | Todo | 1.5B / 7B / 70B 表示什么？ |
| 参数量来源 | Core | Todo | 参数量是工程师直接填进去的吗？ |
| Training Data | Core | Todo | 参数量就是训练数据吗？ |
| Random Initialization | Core | Todo | “模型出生”到底发生了什么？ |
| Symmetry Breaking | Advanced | Todo | 为什么不能所有参数初始化成 0？ |
| Pre-training | Core | Todo | 预训练到底在做什么？ |
| Next-token Prediction | Core | Todo | 为什么猜下一个 Token 能学到知识？ |
| Self-supervised Learning | Advanced | Todo | 没有人标答案，模型怎么知道对错？ |
| Loss | Core | Todo | Loss 是怎么判断模型错了多少？ |
| Forward Pass | Advanced | Todo | 前向传播是什么？ |
| Backpropagation | Advanced | Todo | 反向传播是什么？ |
| Gradient | Advanced | Todo | 梯度到底是什么？ |
| Gradient Descent | Advanced | Todo | 参数怎么一步步被修改？ |
| Post-training | Core | Todo | 预训练之后为什么还要训练？ |
| SFT | Core | Todo | SFT 在教模型什么？ |
| Preference Alignment | Core | Todo | 对齐到底是什么意思？ |
| RLHF | Advanced | Todo | RLHF 怎么利用人类偏好？ |
| DPO | Advanced | Todo | DPO 和 RLHF 是一回事吗？ |
| Checkpoint / Weights | Core | Todo | 参数最后体现成什么？ |
| safetensors / GGUF | Advanced | Todo | 模型文件到底是什么？ |
| Deployment | Core | Todo | 训练完为什么还不能直接用？ |
| Inference | Core | Todo | 推理和训练有什么区别？ |

---

# 04. 模型能力

| 内容 | 等级 | 状态 | 主要问题 |
|---|---|---|---|
| Memorization | Advanced | Todo | 模型是在背答案吗？ |
| Generalization | Core | Todo | 什么叫泛化？ |
| Train / Validation / Test | Advanced | Todo | 怎么判断模型是真的学会？ |
| Overfitting | Advanced | Todo | 什么叫过拟合？ |
| Underfitting | Advanced | Todo | 什么叫欠拟合？ |
| Emergence | Core | Todo | 什么叫涌现？ |
| In-context Learning | Advanced | Todo | 为什么只在 Prompt 里给示例也能“学”？ |
| Reasoning | Core | Todo | 推理能力和知识量是一回事吗？ |
| Reasoning Model | Core | Todo | 什么叫推理模型？ |
| Chain of Thought | Advanced | Todo | CoT 是模型真实完整思考过程吗？ |
| Tree of Thought | Appendix | Todo | ToT 是什么？ |
| ReAct | Advanced | Todo | 推理和行动怎么结合？ |
| Multimodal | Core | Todo | 多模态是什么意思？ |
| MoE | Core | Todo | 为什么模型有“专家”？ |
| Total / Active Parameters | Core | Todo | 总参数和激活参数什么区别？ |
| Scaling Laws | Advanced | Todo | 参数、数据、算力怎么一起扩展？ |
| Distillation | Core | Todo | 大模型怎么“教”小模型？ |
| Quantization | Core | Todo | 量化为什么能让模型变小？ |
| Pruning | Advanced | Todo | 剪枝是什么？ |
| LoRA | Advanced | Todo | LoRA 和蒸馏、量化有什么区别？ |
| Reproducibility | Advanced | Todo | 相同条件能训练出完全相同的模型吗？ |

---

# 05. 幻觉与安全

| 内容 | 等级 | 状态 | 主要问题 |
|---|---|---|---|
| Hallucination | Core | Todo | AI 为什么会一本正经地说错？ |
| LLM ≠ Database | Core | Todo | 模型是不是数据库？ |
| Knowledge in Parameters | Advanced | Todo | “知识存在参数里”到底是什么意思？ |
| Verification | Core | Todo | 怎么降低错误答案风险？ |
| Prompt Injection | Core | Todo | Prompt Injection 是什么？ |
| Jailbreak | Advanced | Todo | Jailbreak 和 Injection 什么区别？ |
| Red Team | Advanced | Todo | 红队测试在测什么？ |

---

# 06. Tools / API / Function Calling

| 内容 | 等级 | 状态 | 主要问题 |
|---|---|---|---|
| API | Core | Todo | API 是什么？ |
| Tool | Core | Todo | Tool 是什么？ |
| Function Calling | Core | Todo | 模型怎么“调用函数”？ |
| Tool Calling | Core | Todo | Tool Calling 和 Function Calling 什么关系？ |
| Tool Execution Boundary | Core | Todo | 真正执行 API 的是模型还是程序？ |
| Web Search | Core | Todo | AI 怎么联网？ |
| File Tool | Core | Todo | AI 怎么读文件？ |
| Code Execution | Core | Todo | AI 怎么运行代码？ |
| Browser / Computer Use | Advanced | Todo | AI 怎么操作网页和电脑？ |
| Database Tool | Advanced | Todo | AI 怎么查数据库？ |
| OCR | Advanced | Todo | OCR 在 AI 系统里是什么角色？ |

---

# 07. Agent

| 内容 | 等级 | 状态 | 主要问题 |
|---|---|---|---|
| Agent | Core | Todo | Agent 到底是什么？ |
| Model vs Agent | Core | Todo | Agent 和模型差在哪？ |
| Agent Loop | Core | Todo | Agent 为什么能连续做多步？ |
| Planning | Core | Todo | Planning 是什么？ |
| Tool Use | Core | Todo | Agent 怎么使用工具？ |
| Workflow | Core | Todo | Workflow 是什么？ |
| Workflow vs Agent | Core | Todo | Workflow 和 Agent 有什么区别？ |
| Copilot | Core | Todo | Copilot 和 Agent 有什么区别？ |
| AI Embedded → Copilot → Agent | Core | Todo | AI 产品为什么越来越“自主”？ |
| Multi-Agent | Advanced | Todo | 多 Agent 是什么？ |
| Long-running Agent | Advanced | Todo | 长任务 Agent 有什么特殊问题？ |

---

# 08. RAG / Knowledge

| 内容 | 等级 | 状态 | 主要问题 |
|---|---|---|---|
| RAG | Core | Todo | RAG 是什么？ |
| Knowledge Base | Core | Todo | 知识库是什么？ |
| Knowledge Base vs Vector DB | Core | Todo | 知识库就是向量数据库吗？ |
| Embedding | Core | Todo | Embedding 是什么？ |
| Vector | Core | Todo | Vector 为什么能表达语义？ |
| Semantic Similarity | Core | Todo | “意思像不像”是怎么算的？ |
| Vector Database | Core | Todo | 向量数据库是干什么的？ |
| Chunk | Core | Todo | 为什么文档要切片？ |
| Retrieval | Core | Todo | Retrieval 是怎么找到相关资料的？ |
| Rerank | Advanced | Todo | 为什么召回后还要重排？ |
| Knowledge Graph | Advanced | Todo | 知识图谱和向量库有什么区别？ |
| RAG vs Fine-tuning | Core | Todo | RAG 和微调怎么选？ |
| RAG vs Prompt Context | Core | Todo | RAG 和直接把资料贴进 Prompt 有什么区别？ |
| RAG Limitations | Core | Todo | RAG 能消灭幻觉吗？ |

---

# 09. MCP

| 内容 | 等级 | 状态 | 主要问题 |
|---|---|---|---|
| MCP | Core | Todo | MCP 到底是什么？ |
| MCP Client | Core | Todo | Client 做什么？ |
| MCP Server | Core | Todo | Server 做什么？ |
| MCP Tool | Core | Todo | MCP Tool 和普通 Tool 什么关系？ |
| MCP Resource | Advanced | Todo | Resource 是什么？ |
| MCP Prompt | Advanced | Todo | MCP Prompt 是什么？ |
| MCP vs API | Core | Todo | MCP 是不是一种 API？ |
| MCP vs Function Calling | Core | Todo | Function Calling 和 MCP 有什么区别？ |
| MCP vs Agent | Core | Todo | 有 MCP 就等于有 Agent 吗？ |

---

# 10. Skills

| 内容 | 等级 | 状态 | 主要问题 |
|---|---|---|---|
| Skill | Core | Todo | Skill 到底是什么？ |
| Prompt vs Skill | Core | Todo | Skill 只是一个长 Prompt 吗？ |
| Tool vs Skill | Core | Todo | Skill 和 Tool 有什么区别？ |
| MCP vs Skill | Core | Todo | MCP 和 Skill 是什么关系？ |
| Agent vs Skill | Core | Todo | Agent 为什么需要 Skill？ |

---

# 11. Coding Agent

| 内容 | 等级 | 状态 | 主要问题 |
|---|---|---|---|
| AI Coding | Core | Todo | AI Coding 是什么？ |
| Code Completion | Core | Todo | 自动补全和 Agent 差在哪？ |
| Copilot | Core | Todo | Coding Copilot 是什么？ |
| Coding Agent | Core | Todo | Coding Agent 为什么能修改整个项目？ |
| IDE | Core | Todo | IDE 在 AI Coding 里是什么角色？ |
| Terminal | Core | Todo | 为什么 Agent 需要终端？ |
| Shell / Command | Advanced | Todo | Shell 和命令是什么？ |
| Git | Core | Todo | 为什么 Git 对 Coding Agent 很重要？ |
| Project Context | Core | Todo | Agent 怎么理解整个项目？ |
| Context Engineering | Core | Todo | Context Engineering 是什么？ |
| Codex | Verify | Verify | 产品案例，需要按更新时间核验 |
| Claude Code | Verify | Verify | 产品案例，需要按更新时间核验 |
| Cursor | Verify | Verify | 产品案例，需要按更新时间核验 |

---

# 12. Memory

| 内容 | 等级 | 状态 | 主要问题 |
|---|---|---|---|
| Conversation History | Core | Todo | 聊天记录等于记忆吗？ |
| Context | Core | Todo | Context 和 Memory 一样吗？ |
| Memory | Core | Todo | AI Memory 到底是什么？ |
| Long-term Memory | Advanced | Todo | 长期记忆怎么实现？ |
| RAG vs Memory | Core | Todo | 查知识库和记住用户信息有什么区别？ |
| Cache vs Memory | Core | Todo | Cache 算记忆吗？ |
| Context / Memory / RAG / Cache | Core | Todo | 四个概念怎么一次分清？ |

---

# 13. AI World Map

| 内容 | 等级 | 状态 |
|---|---|---|
| AI Concept Map | Core | Todo |
| Model Lifecycle | Core | Todo |
| Training vs Inference Map | Core | Todo |
| Agent Architecture Map | Core | Todo |
| AI Application Stack | Core | Todo |
| Concept Cheatsheet | Core | Todo |

---

# History

| 内容 | 等级 | 状态 |
|---|---|---|
| Rule-based AI | Appendix | Todo |
| Expert Systems | Appendix | Todo |
| Machine Learning Era | Appendix | Todo |
| Deep Learning Era | Appendix | Todo |
| GPU + Deep Learning | Appendix | Todo |
| Transformer | Core | Verify |
| GPT / Foundation Model | Advanced | Verify |
| Chat / Instruction Models | Advanced | Verify |
| RAG | Advanced | Verify |
| Tool Calling | Advanced | Verify |
| Agent | Advanced | Verify |
| MCP | Advanced | Verify |
| Coding Agent / Computer Use | Advanced | Verify |

> 历史时间线中的年份、论文、首次发布、关键产品节点必须在正式写作时逐条核验。

---

# Ecosystem

## 模型分类

- Closed / Open-weight / Open-source
- Dense / MoE
- Text / Vision / Audio / Video / Multimodal
- General / Reasoning / Embedding / Reranker / Generation
- Base / Instruction / Chat / Fine-tuned
- SLM / LLM

## 产业角色

- Model Provider
- Cloud Provider
- Model Hub
- Inference Provider
- AI Application Company
- Hardware Vendor

> 厂商、产品能力、模型版本、价格、排行榜都属于易变信息，不作为永久事实写死。

---

# Appendix A：Hardware

- CPU
- GPU
- CUDA
- Tensor Core
- FLOPS
- Multiply-Accumulate
- VRAM
- RAM
- SSD
- HBM
- Bandwidth
- Interconnect
- PCIe
- NVLink
- Server
- Cluster
- Data Center
- Distributed Training
- Data Parallelism
- Tensor Parallelism
- Pipeline Parallelism

---

# Appendix B：Training

- Loss Curve
- Generalization
- Overfitting
- Underfitting
- Optimizer
- AdamW
- Learning Rate
- Batch
- Epoch
- Gradient Accumulation
- Mixed Precision
- FP32
- FP16
- BF16
- FP8
- Checkpoint
- Distributed Training

---

# Appendix C：高频易混概念

- AI vs AGI
- AI vs ML vs DL
- Generative AI vs AIGC
- NLP vs LLM
- GPT vs ChatGPT
- Company vs Model vs API vs Product
- Model vs Agent
- Parameter vs Training Data
- Parameter vs Token
- Token vs Word
- Context vs Context Window
- Context vs Memory
- Memory vs RAG
- RAG vs Fine-tuning
- Knowledge Base vs Vector DB
- Embedding vs LLM
- Vector DB vs Knowledge Graph
- Tool vs Function Calling
- Function Calling vs MCP
- API vs MCP
- MCP vs Agent
- Skill vs Prompt
- Skill vs Tool
- Skill vs MCP
- Workflow vs Agent
- Copilot vs Agent
- Training vs Inference
- Pre-training vs Post-training
- SFT vs Fine-tuning
- RLHF vs DPO
- Dense vs MoE
- Total Parameters vs Active Parameters
- Quantization vs Distillation
- LoRA vs Distillation
- Open Weight vs Open Source
- GPU vs VRAM
- RAM vs VRAM
- Compute vs Memory
- Bandwidth vs Compute

---

# FAQ：真实小白问题池

以下问题来自真实小白学习过程中出现的认知卡点，后续用于驱动文章写作：

1. 1K 是多少 Token？
2. 1M 呢？
3. M 和 T 中间是不是还有一个单位？
4. 1.5B 到底是什么意思？
5. 参数量就是训练数据吗？
6. 参数量能决定什么？
7. 1040 亿为什么是 104B，不是 10B？
8. 上下文窗口是什么意思？
9. 一个模型是怎么诞生的？
10. 数据是“喂给模型”的，那被喂之前的模型从哪来？
11. 设计架构是写代码吗？
12. 架构到底是什么意思？
13. 层是什么意思？
14. 宽度是什么意思？
15. “专家”是框架自带的吗？
16. 随机初始化到底是在初始化什么？
17. 参数最后体现形式是什么？
18. 这些数字为什么会有智能？
19. 模型是真的理解，还是统计规律？
20. 训练时谁知道模型答错了？
21. Loss 到底是什么？
22. 参数到底是怎么被修改的？
23. 训练完模型怎么变成文件？
24. 模型文件为什么要加载到显存？
25. GPU 到底在干什么？
26. “乘加”到底是谁在乘加？
27. 显存和内存有什么区别？
28. 带宽是什么？
29. 卡和卡之间为什么还要互联？
30. 为什么长上下文很吃显存？
31. Cache 是什么？
32. 两个公司所有条件都一样，会训练出完全一样的模型吗？
33. 为什么同一个问题 AI 每次回答不一样？
34. 为什么 AI 会幻觉？
35. RAG 和直接把资料贴给 AI 有什么区别？
36. Agent 和模型到底差在哪？
37. MCP 到底是干什么的？
38. Skill、Tool、MCP、Agent 到底什么关系？

---

# v0.1 第一批文章

第一版只做 12 篇 Core：

| # | 文章 | 状态 |
|---|---|---|
| 01 | AI 是什么 | Done |
| 02 | AI、ML、DL 到底什么关系 | Done |
| 03 | 什么是模型 | Done |
| 04 | 什么是大语言模型 LLM | Todo |
| 05 | GPT 和 ChatGPT 有什么区别 | Todo |
| 06 | 参数到底是什么 | Todo |
| 07 | 参数量和训练数据有什么区别 | Todo |
| 08 | Token 是什么 | Todo |
| 09 | Context / Context Window 是什么 | Todo |
| 10 | 一个大模型到底是怎么诞生的 | Todo |
| 11 | 为什么“预测下一个 Token”还能学到能力 | Todo |
| 12 | Training 和 Inference 有什么区别 | Todo |

---

# 写作前核验规则

任何文章写作前，先判断内容属于哪种：

### 稳定概念

例如：

- Token
- Parameter
- Training
- Inference
- Attention

可以优先依据经典论文、官方文档、教材。

### 易变事实

例如：

- 某模型参数量
- 上下文窗口
- 某产品是否支持某功能
- API 价格
- 模型排行榜
- 某厂商当前产品线

必须：

1. 联网核验；
2. 优先使用官方 / 论文 / Primary Source；
3. 标注更新时间；
4. 不把当期事实写成永久定义。

---

# 核心质量规则

1. 真实问题负责告诉我们“哪里难懂”，不直接承担事实来源。
2. 类比必须明确标注为类比。
3. 每篇先说人话，再给严格定义。
4. 不为了通俗而牺牲关键准确性。
5. 不在核心路线里塞硬件和工程细节。
6. 同一概念只建立一个主页面，其他页面用链接引用，避免重复解释。
7. 产品、厂商、价格、模型规格等易变内容必须重新核验。
