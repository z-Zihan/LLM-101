# Token 是什么？

> Level: `Core` · Path: `Main`

## 读完你应该明白

1. Token 是模型处理文本时使用的离散单元。
2. Token 不固定等于一个汉字、单词或字符。
3. Tokenizer 决定文本怎样切分并转换成 Token ID。
4. Token 会影响可处理长度、计算量和 API 计量。

## 一个小白真的会怎么问？

> 1K 是多少 Token？
>
> 一个 Token 是一个字，还是一个英文单词？

## 先说人话

Token 可以先理解成：**模型阅读和生成内容时使用的文本单元。**

它可能是一个字、单词的一部分、标点，或其他常见字符组合。具体怎样切，取决于所用的 Tokenizer。

## 举个例子

同一句话可能被不同 Tokenizer 切成不同结果：

```text
原文：unbelievable!

一种可能：un | believ | able | !
另一种可能：unbelievable | !
```

这只是示意，不代表任何具体模型的真实切分。要得到准确结果，必须使用该模型对应的 Tokenizer 实测。

## 严格来说

Tokenizer（分词器）会把输入内容编码成 Token 序列，再把每个 Token 映射到词表中的整数编号，称为 Token ID。

```text
文本
 ↓ Tokenizer 切分与编码
Token
 ↓ 查词表编号
Token ID
 ↓ 模型继续处理
```

Token 是词表中的离散单元；Token ID 是这个单元对应的数字编号。编号本身没有大小意义，不是“数字越大、词越重要”。

许多现代 Tokenizer 使用子词方法：常见片段可以作为一个 Token，少见词则拆成更小部分。这能在有限词表中处理大量词语和新组合。

## 为什么不直接按字或单词处理？

只按完整单词建词表会遇到新词、拼写变化和词表过大的问题；只按单个字符处理，又可能让序列过长。

子词 Token 在两者之间折中：

```text
有限词表
  +
能组合出少见词
  +
序列长度相对可控
```

## 1K Token 到底是多少字？

`1K Token` 表示 1,000 个 Token，而不是固定数量的汉字或英文单词。

换算会受以下因素影响：

- 具体 Tokenizer；
- 中文、英文或其他语言；
- 空格、标点、数字和代码；
- 生僻词与常见词的比例。

因此，固定写“一个 Token 等于多少汉字”只能作为很粗的经验，不能用于准确预算。准确计数应使用对应模型的 Tokenizer。

## 最容易搞混的东西

### Token ≠ 字符

一个 Token 可能包含多个字符，也可能只是某个字符或字节片段。

### Token ≠ 单词

一个英文单词可能被拆成多个 Token；常见的短词也可能连同空格形成一个 Token。

### Token ≠ Token ID

Token 是单元，Token ID 是词表给它的编号。

### Tokenizer ≠ 模型参数

Tokenizer 负责输入输出的编码与解码；模型参数负责对 Token 序列进行计算。二者配套使用，但不是同一个东西。

## 常见误区

### 误区 1：中文一个字永远等于一个 Token

不对。不同 Tokenizer 对中文、标点、词组和生僻字符的处理可能不同。

### 误区 2：Token 是为了收费才发明的

不对。Token 首先是模型处理离散语言单元的技术表示。API 可以按 Token 计量，是因为它与输入输出规模相关。

### 误区 3：Token 越少，文本信息一定越少

不一定。不同语言和 Tokenizer 的压缩方式不同，Token 数不能直接当作语义信息量。

## 为什么我要知道它？

Token 连接了后续很多概念：

```text
文本 → Tokenizer → Token → Context Window → 模型生成
```

它会影响输入是否超出窗口、生成长度、计算成本以及 API 用量。

## 你只需要记住

1. Token 是模型处理内容时使用的离散单元。
2. Token 不固定等于字、字符或单词。
3. 不同 Tokenizer 会产生不同切分，准确数量必须实测。
4. Token ID 只是词表编号，不表示重要程度。

## 继续学习

- [上一篇：Prompt 是什么](./01-Prompt到底是什么.md)
- [下一篇：Context / Context Window 是什么](./07-上下文和上下文窗口是什么.md)
- [相关：什么是大语言模型 LLM](../01-AI与大模型/04-什么是大语言模型.md)

## 资料与核验

- [OpenAI: tiktoken](https://github.com/openai/tiktoken)
- [Sennrich et al.: Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909)
- [Kudo & Richardson: SentencePiece](https://arxiv.org/abs/1808.06226)
