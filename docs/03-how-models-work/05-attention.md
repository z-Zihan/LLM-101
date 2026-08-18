# Attention 是什么？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> Attention 是不是模型像人一样“注意”某些词？
>
> 它到底对 Token 做了什么？

## 先说人话

Attention 可以先理解成：处理一个位置的信息时，模型会计算其他位置和它有多相关，再按不同权重汇总那些信息。

“关注”只是帮助理解的类比。实际发生的是数值计算，不表示模型拥有人的注意力或主观体验。

## 举个例子

看这句话：

```text
小猫没有吃鱼，因为它不饿。
```

模型处理“它”时，需要结合前面的内容判断这个位置和哪些位置更相关。“小猫”通常比“鱼”更有助于理解“它”指什么。

Attention 做的不是在文字上画荧光笔，而是让当前位置能够按计算出的权重组合其他位置携带的信息。

## 严格来说

一组常见的 Attention 计算会为每个位置形成三类表示：

- Query（查询）：当前位置正在寻找什么信息；
- Key（键）：各位置提供什么匹配线索；
- Value（值）：各位置实际可被汇总的信息。

模型比较 Query 与各个 Key，得到相关性分数；这些分数经过处理后成为权重，再用来加权汇总对应的 Value。

```text
当前位置的 Query
       +
各位置的 Key
       ↓
计算相关性与权重
       ↓
按权重汇总各位置的 Value
       ↓
得到结合上下文的新表示
```

“查询、键、值”是对三类数值表示的名称，不是在模型里真的存放搜索框、钥匙和资料卡。

## Self-Attention 是什么？

Self-Attention（自注意力）表示 Query、Key、Value 都来自同一段序列的表示。这样，一段序列中的不同位置可以在同一次计算中交换信息。

“Self”指信息来源于同一序列，不是说模型在“关注自己”。在自回归语言模型中，还会使用遮罩限制当前位置读取未来 Token，避免生成时提前看到尚未产生的内容。

## Multi-Head Attention 又是什么？

Multi-Head Attention（多头注意力）会在多个不同的可训练投影中并行进行 Attention，再合并结果。这让模型有机会用不同的表示方式建立位置之间的关系。

有些分析会观察到某些 Head 呈现特定模式，但不能据此承诺“每个 Head 都固定负责一种可用人话命名的功能”。模型行为来自许多组件和参数共同作用。

## 为什么会有 Attention？

处理序列时，一个位置的含义经常依赖远处的信息。早期序列模型常让信息按时间步逐步传递；路径变长时，建立远距离联系和训练并行都更困难。

Attention 提供了另一种做法：让一个位置直接计算它与其他位置的关系，并汇总有用信息。Transformer 进一步把 Attention 作为核心组件，使训练时许多位置可以并行计算。

## 最容易搞混的东西

### Attention ≠ Transformer

Attention 是一种信息聚合机制。Transformer 还包含前馈网络、位置信息、残差连接和归一化等组件。

### Attention 权重 ≠ 完整解释

权重可以显示一次计算中信息怎样被分配，但不能自动成为模型输出的完整因果解释。其他层、参数和后续计算同样会影响结果。

### Attention ≠ “记住所有 Context”

一个 Token 位于上下文窗口内，只表示它可以被纳入计算，不保证模型一定正确利用它。位置方法、模型能力、输入组织和任务都会影响结果。

## 常见误区

### 误区 1：权重最高的位置就是唯一答案来源

不一定。模型有多层、多头和其他计算组件，最终输出不是由一张 Attention 权重表单独决定的。

### 误区 2：Attention 会把知识永久写进参数

Attention 在一次前向计算中组合当前表示；参数是否改变属于训练过程。把新资料放进 Context 不等于把它训练进模型。

### 误区 3：有 Attention 就能无限处理长文本

不对。模型仍受上下文窗口、计算量、内存和位置处理方法等限制。

## 为什么我要知道它？

Attention 连接了 Token、Context 和 Transformer：Token 先变成数值表示，Attention 让不同位置交换相关信息，Transformer 再通过多层组件继续处理这些表示。

理解它以后，你不会再把 Transformer 当成“神秘地读懂整句话”，也能更准确地理解长上下文为什么既有容量问题，也有信息利用问题。

## 你只需要记住

1. Attention 根据相关性计算权重，并加权汇总各位置的信息。
2. “关注”只是类比；实际过程是 Query、Key、Value 等数值表示之间的计算。
3. Self-Attention 的信息来自同一序列，不是模型在关注自己。
4. Attention 是 Transformer 的组件之一，不等于 Transformer，也不保证所有 Context 都被正确利用。

## 继续学习

- [上一篇：Transformer 是什么](./03-transformer.md)
- [下一篇：为什么预测下一个 Token 还能学到能力](./10-next-token-prediction.md)
- [相关：Context / Context Window 是什么](../02-chat-and-context/07-context.md)

## 资料与核验

- [Bahdanau, Cho & Bengio: Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)
- [Vaswani et al.: Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Harvard NLP: The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)
