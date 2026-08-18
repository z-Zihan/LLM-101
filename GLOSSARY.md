# LLM-101 Glossary

> 这里只提供一句话解释和主页面链接。完整解释以对应文章为准。

## A

### Agent

中文：智能体 / Agent

一句话：围绕目标组合模型、状态、工具和控制循环，并根据结果继续推进任务的系统。

主页面：[Agent 是什么](./docs/07-agent/01-what-is-agent.md)

### Agent Loop

中文：Agent 循环

一句话：反复执行观察、决定、行动和状态更新，让新结果影响下一步的运行机制。

主页面：[Agent Loop 是什么](./docs/07-agent/03-agent-loop.md)

### API

中文：应用程序编程接口

一句话：让软件之间按照约定请求操作并交换结果的接口。

主页面：[API 是什么](./docs/06-tools/01-api.md)

### Architecture

中文：模型架构

一句话：规定模型由哪些计算组件组成、怎样连接以及信息如何流动的结构设计。

主页面：[模型架构是什么](./docs/03-how-models-work/02-architecture.md)

### Artificial Intelligence（AI）

中文：人工智能

一句话：让机器系统根据输入产生预测、内容、建议或决策等输出的广泛技术领域。

主页面：[AI 是什么](./docs/01-ai-and-llm/01-what-is-ai.md)

### Attention

中文：注意力机制

一句话：根据位置之间的相关性计算权重，并按权重汇总信息的数值计算机制。

主页面：[Attention 是什么](./docs/03-how-models-work/05-attention.md)

## C

### ChatGPT

中文：ChatGPT 产品

一句话：OpenAI 面向用户提供、组合模型与其他系统能力的 AI 产品服务。

主页面：[GPT 和 ChatGPT 有什么区别](./docs/01-ai-and-llm/05-gpt-vs-chatgpt.md)

### Context

中文：上下文

一句话：模型在当前这次计算中可以利用的信息。

主页面：[Context 和 Context Window 是什么](./docs/02-chat-and-context/07-context.md)

### Context Window

中文：上下文窗口

一句话：模型一次能够处理的 Token 容量边界。

主页面：[Context 和 Context Window 是什么](./docs/02-chat-and-context/07-context.md)

## D

### Database

中文：数据库

一句话：按照明确的数据结构保存、查询和更新记录的系统，与按概率生成 Token 的 LLM 职责不同。

主页面：[为什么 LLM 不是数据库](./docs/05-limitations/02-llm-is-not-database.md)

### Deep Learning（DL）

中文：深度学习

一句话：使用多层神经网络从数据中学习表示的一类机器学习方法。

主页面：[AI、ML、DL 到底什么关系](./docs/01-ai-and-llm/02-ai-ml-dl.md)

## E

### Embedding

中文：嵌入表示

一句话：模型把对象转换成可比较的数值向量表示，以支持相似性计算和检索。

主页面：[Embedding 是什么](./docs/08-rag/03-embedding.md)

## F

### Function Calling

中文：函数调用

一句话：让模型用函数名和结构化参数表达调用请求、再由外部程序验证并执行的机制。

主页面：[Function Calling 是什么](./docs/06-tools/03-function-calling.md)

## G

### Generalization

中文：泛化

一句话：模型把训练中学到的模式用于未参与训练的新样本，并继续有效表现的能力。

主页面：[Generalization（泛化）是什么](./docs/04-capabilities/01-generalization.md)

### GPT

中文：GPT 模型家族

一句话：名称来自 Generative Pre-trained Transformer 的 OpenAI 模型家族。

主页面：[GPT 和 ChatGPT 有什么区别](./docs/01-ai-and-llm/05-gpt-vs-chatgpt.md)

## H

### Hallucination

中文：幻觉

一句话：生成模型产出看似合理、却与事实不符或缺乏给定来源与任务条件支持的内容。

主页面：[Hallucination（幻觉）是什么](./docs/05-limitations/01-hallucination.md)

## I

### Inference

中文：推理 / 模型推理

一句话：使用训练好的参数处理新输入并产生预测或生成结果的过程。

主页面：[Training 和 Inference 有什么区别](./docs/03-how-models-work/18-training-vs-inference.md)

## K

### Knowledge Base

中文：知识库

一句话：为了查询、回答或完成任务而组织和管理的一组资料及其元数据、权限和版本边界。

主页面：[Knowledge Base 是什么](./docs/08-rag/02-knowledge-base.md)

## L

### Language Model

中文：语言模型

一句话：对语言序列中的可能性进行建模、可用于预测或生成语言的模型。

主页面：[什么是大语言模型 LLM](./docs/01-ai-and-llm/04-what-is-llm.md)

### Large Language Model（LLM）

中文：大语言模型

一句话：使用大规模数据和计算训练、能够处理与生成语言的大型语言模型。

主页面：[什么是大语言模型 LLM](./docs/01-ai-and-llm/04-what-is-llm.md)

## M

### MCP

中文：模型上下文协议

一句话：让 AI 应用以统一方式连接外部 Tools、Resources 和 Prompts 的开放协议。

主页面：[MCP 是什么](./docs/09-mcp/01-what-is-mcp.md)

### MCP Client

中文：MCP 客户端

一句话：Host 内负责与一个 MCP Server 建立和管理协议连接的组件。

主页面：[MCP Client 和 Server 是什么](./docs/09-mcp/02-client-server.md)

### MCP Prompt

中文：MCP 提示模板

一句话：MCP Server 提供、由用户或应用选择使用的可复用提示模板。

主页面：[MCP Tools、Resources、Prompts 是什么](./docs/09-mcp/03-tools-resources-prompts.md)

### MCP Resource

中文：MCP 资源

一句话：MCP Server 通过 URI 暴露、由应用决定何时读取的 Context 内容。

主页面：[MCP Tools、Resources、Prompts 是什么](./docs/09-mcp/03-tools-resources-prompts.md)

### MCP Server

中文：MCP 服务端

一句话：通过 MCP 连接暴露 Tools、Resources 或 Prompts 的程序角色。

主页面：[MCP Client 和 Server 是什么](./docs/09-mcp/02-client-server.md)

### MCP Tool

中文：MCP 工具

一句话：MCP Server 通过协议声明和执行、可由模型请求调用的操作。

主页面：[MCP Tools、Resources、Prompts 是什么](./docs/09-mcp/03-tools-resources-prompts.md)

### Machine Learning（ML）

中文：机器学习

一句话：让计算机从数据中学习可用于新输入的规律，而不是把每条判断规则都由人写死。

主页面：[AI、ML、DL 到底什么关系](./docs/01-ai-and-llm/02-ai-ml-dl.md)

### Model

中文：模型

一句话：训练后形成的一套计算关系，用来把新的输入转换成预测、分类、内容或其他输出。

主页面：[什么是模型](./docs/01-ai-and-llm/03-what-is-model.md)

## P

### Parameter

中文：参数

一句话：模型内部由训练调整、在推理中参与计算的数值变量。

主页面：[参数到底是什么](./docs/03-how-models-work/06-parameter.md)

### Parameter Count

中文：参数量

一句话：模型中可训练参数的数量，和训练数据的数量不是一回事。

主页面：[参数量和训练数据有什么区别](./docs/03-how-models-work/07-parameter-vs-training-data.md)

### Prompt

中文：提示 / 提示词

一句话：提供给模型、用于影响当前输出的输入内容。

主页面：[Prompt 是什么](./docs/02-chat-and-context/01-prompt.md)

## R

### RAG

中文：检索增强生成

一句话：先检索外部资料，再把相关内容放入 Context 供模型生成回答的流程。

主页面：[RAG 是什么](./docs/08-rag/01-what-is-rag.md)

### Reasoning

中文：推理能力

一句话：组合信息、遵守约束并经过中间步骤解决问题的可观察行为能力。

主页面：[Reasoning（推理能力）是什么](./docs/04-capabilities/03-reasoning.md)

### Retrieval

中文：检索

一句话：根据查询从候选集合中召回并排序可能相关内容的过程。

主页面：[Retrieval 是什么](./docs/08-rag/08-retrieval.md)

## T

### Tool

中文：AI 工具

一句话：AI 应用提供给模型选择使用、由外部程序真实执行的一项能力。

主页面：[AI Tool 是什么](./docs/06-tools/02-tool.md)

### Token

中文：Token / 文本单元

一句话：Tokenizer 将内容转换成、供模型处理的离散单元。

主页面：[Token 是什么](./docs/02-chat-and-context/04-token.md)

### Tokenizer

中文：分词器

一句话：把输入内容编码成 Token 和 Token ID，并把输出解码回内容的组件。

主页面：[Token 是什么](./docs/02-chat-and-context/04-token.md)

### Training

中文：训练

一句话：利用数据和目标计算反馈并调整模型参数的过程。

主页面：[Training 和 Inference 有什么区别](./docs/03-how-models-work/18-training-vs-inference.md)

### Training Data

中文：训练数据

一句话：训练过程用于提供输入、目标或其他学习信号的数据。

主页面：[参数量和训练数据有什么区别](./docs/03-how-models-work/07-parameter-vs-training-data.md)

### Transformer

中文：Transformer 架构

一句话：通过 Attention 等组件处理序列信息的一类神经网络架构。

主页面：[Transformer 是什么](./docs/03-how-models-work/03-transformer.md)

## V

### Vector Database

中文：向量数据库

一句话：面向向量保存、索引、元数据过滤和相似性检索设计的数据库系统。

主页面：[Vector Database 是什么](./docs/08-rag/05-vector-database.md)

### Verification

中文：验证

一句话：把可检查的主张拆开，并用独立证据或可重复方法逐项核对。

主页面：[怎么验证 AI 的回答](./docs/05-limitations/04-verification.md)

## W

### Workflow

中文：工作流

一句话：主要步骤和分支由程序预先规定、按明确路径协调任务的自动化方式。

主页面：[Workflow 和 Agent 有什么区别](./docs/07-agent/05-workflow-vs-agent.md)
