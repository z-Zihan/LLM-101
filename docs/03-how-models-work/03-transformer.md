# Transformer 是什么？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> Transformer 是模型、算法还是框架？
>
> LLM 为什么几乎总会提到 Transformer？

## 先说人话

Transformer 是一种神经网络架构。它让序列中的不同位置通过 Attention 交换相关信息，再经过多层计算形成适合任务的表示。

它不是 PyTorch 这样的开发框架，也不是某一个具体 LLM。

## 为什么会出现？

在 Transformer 之前，语言序列常用循环结构按顺序处理：前一步的结果传给后一步。长距离信息需要经过很多步，训练中的并行也受到限制。

2017 年的 *Attention Is All You Need* 提出 Transformer，核心计算不再依赖这种逐位置循环，让训练时许多序列位置能更充分地并行处理，并通过 Attention 建立位置之间的联系。

这不表示生成时可以一次得到整段答案。自回归语言模型推理时仍通常一个 Token 接一个 Token 地生成。

## 一层里大致有什么？

先看不带公式的简化图：

```text
Token 表示 + 位置信息
          ↓
Attention：不同位置交换相关信息
          ↓
前馈网络：每个位置继续变换信息
          ↓
残差连接与归一化帮助信息和训练稳定
          ↓
进入下一层
```

Attention 可以先理解成：处理当前位置时，模型会计算序列中哪些位置与它相关，并组合那些信息。完整的 Query、Key、Value 和多头机制留到 Attention 主页面。

前馈网络（Feed-Forward Network）是在各位置上应用的可训练变换。Transformer 不只是 Attention；前馈网络、位置信息、残差连接和归一化同样是架构的重要组成部分。

## 位置信息为什么必要？

同一组词换个顺序，含义可能不同：

```text
猫追狗
狗追猫
```

Attention 本身需要配合某种位置信息，模型才能区分顺序。原始论文使用位置编码；后来的 Transformer 变体还采用其他位置表示方法。

## Encoder 和 Decoder 是什么？

原始 Transformer 是 Encoder–Decoder 结构：

```text
输入 → Encoder 表示输入 → Decoder 生成输出
```

后来常见变体包括：

- Encoder-only：侧重理解和表示输入；
- Decoder-only：根据已有序列继续生成，许多自回归 LLM 使用这一类；
- Encoder–Decoder：读取一种输入并生成另一种序列。

这些名称描述结构用法，不代表所有模型内部细节完全相同。

## Transformer 和 LLM 的关系

```text
Transformer：一种模型架构
       ↓ 可按不同规模和目标训练
语言模型：对语言序列建模
       ↓ 大规模数据与参数
LLM：大型语言模型
```

现代 LLM 常采用 Transformer 或其变体，但 Transformer 也能用于图像、音频等任务。不能把两者当同义词。

## 最容易搞混的东西

### Transformer ≠ Attention

Attention 是核心组件之一；Transformer 还包含前馈网络、位置处理、残差与归一化等。

### Transformer ≠ 框架

Transformer 是架构；框架负责用代码实现、训练和运行它。

### Transformer ≠ GPT

GPT 是采用 Transformer 路线的一类具体模型家族。Transformer 不是某家公司独有的产品名。

### Transformer ≠ 所有神经网络

卷积网络、循环网络等也是神经网络架构。不同架构仍在不同任务和系统中使用。

## 常见误区

### 误区 1：Attention 会像人一样主动关注

“关注”只是类比。实际过程是根据当前表示计算权重并组合信息，不表示模型具有人类注意力体验。

### 误区 2：Transformer 可以无限处理长文本

不对。模型仍有上下文窗口和计算、内存限制；不同 Attention 与位置方法有不同边界。

### 误区 3：用了 Transformer 就一定是 LLM

不对。是否是语言模型、规模多大、怎样训练，都取决于具体模型与任务。

## 你只需要记住

1. Transformer 是神经网络架构，不是框架或单一模型。
2. 它通过 Attention 连接序列位置，并结合前馈网络、位置信息等组件。
3. 原始架构是 Encoder–Decoder，现代模型有多种结构变体。
4. 许多 LLM 使用 Transformer，但 Transformer 不等于 LLM。

## 继续学习

- [上一篇：模型架构是什么](./02-architecture.md)
- [下一篇：Attention 是什么](./05-attention.md)
- [相关：什么是大语言模型 LLM](../01-ai-and-llm/04-what-is-llm.md)

## 资料与核验

- [Vaswani et al.: Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Harvard NLP: The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)
- [Jurafsky & Martin: Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/)
