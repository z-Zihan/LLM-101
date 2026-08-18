# Context 和 Context Window 是什么？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> 上下文窗口是什么意思？窗口内的内容模型都会记住吗？
>
> Context 和模型参数、Memory 有什么区别？

## 先说人话

Context（上下文）是模型在**当前这次计算中可以利用的信息**。Context Window（上下文窗口）是模型一次能够处理的 Token 容量边界。

可以把 Context 类比成当前工作台，把 Context Window 类比成工作台能放多少材料。这个类比不代表模型拥有人类的短期记忆。

## 举个例子

聊天产品可能把这些内容一起交给模型：

```text
系统规则 + 部分历史对话 + 当前问题 + 附加资料
                         ↓
                    当前 Context
                         ↓
                       模型
                         ↓
                       回答
```

历史消息只有被产品再次放入当前输入，才成为这一次模型可用的 Context。

## 严格来说

对于处理 Token 序列的模型，Context 是本次推理输入中可供模型条件化计算的信息。上下文窗口规定一次请求可容纳的 Token 范围，通常需要同时考虑输入以及计划生成的输出；具体计算规则由模型和服务定义。

窗口是容量上限，不是理解质量保证。内容即使放进窗口，模型也可能忽略、混淆或没有有效利用。

## 内容太多会怎样？

如果准备的信息超过窗口，应用必须采取某种策略，例如：

- 截断一部分内容；
- 先做摘要；
- 分块处理；
- 只检索与问题相关的片段；
- 改用支持更长窗口的模型。

并非所有产品都简单删除最早消息，因此不能把某一种产品策略当作 Context Window 的定义。

## 最容易搞混的东西

### Context ≠ Context Window

Context 是当前实际提供的信息，Context Window 是可容纳信息的容量边界。

### Context ≠ 参数

参数在训练中形成并参与模型计算；Context 是当前推理请求提供的信息。把资料放入 Context 不会自动改写模型参数。

### Context ≠ Memory

Memory 通常指应用跨会话保存并在需要时取回的信息。取回的 Memory 只有被放进当前输入后，才成为模型这次可利用的 Context。

### Context ≠ RAG

RAG 是先检索相关资料、再把结果加入 Context 的流程。Context 是模型最终看到的信息范围，RAG 是准备其中一部分信息的方法。

## 常见误区

### 误区 1：窗口够大，模型就能完美记住全部内容

不对。研究显示，模型对长输入中不同位置的信息利用可能不均匀。容量更大不等于检索和推理一定更可靠。

### 误区 2：聊天记录天然都在模型脑中

不对。产品需要保存并重新发送相关历史，模型才能在当前请求中使用它。

### 误区 3：长窗口的成本永远按同一个公式增长

不对。计算和内存成本取决于架构、注意力方法、缓存和服务实现，不能用一个公式概括所有模型。

## 为什么我要知道它？

Context 决定模型这一次“拿到了什么材料”。它是理解长对话、文档问答、RAG、Memory、提示词和 API 输入限制的共同基础。

## 你只需要记住

1. Context 是本次计算可用的信息；Context Window 是一次处理的 Token 容量边界。
2. 窗口更大不保证所有内容都被有效利用。
3. Context 不等于参数、Memory 或 RAG。
4. 历史对话需要被产品重新放入输入，模型本次才看得到。

## 继续学习

- [上一篇：Token 是什么](./04-token.md)
- [下一篇：一个大模型到底是怎么诞生的](../03-how-models-work/01-model-lifecycle.md)
- [相关：什么是大语言模型 LLM](../01-ai-and-llm/04-what-is-llm.md)

## 资料与核验

- [Vaswani et al.: Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Liu et al.: Lost in the Middle](https://arxiv.org/abs/2307.03172)
- [Jurafsky & Martin: Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/)
