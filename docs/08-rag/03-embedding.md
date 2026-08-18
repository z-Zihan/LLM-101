# Embedding 是什么？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> 文字为什么能变成一串数字？
>
> 两段文字的向量靠近，就代表意思完全一样吗？

## 先说人话

Embedding（嵌入表示）是模型把一个对象转换成一串数字，让相关对象在这个数值空间中呈现可比较的关系。

在 RAG 中，常把问题和资料片段分别转换成向量，再寻找距离较近的候选内容。

## 举个例子

下面三句话使用的字不同：

```text
怎么申请退款？
退货以后多久能收到钱？
今天北京天气怎样？
```

为检索训练的 Embedding Model 可能把前两句映射到较接近的向量，把天气问题放得更远，因为前两句都与退款有关。

“空间中的位置”只是类比。实际结果是一组由模型计算出的数值，不是屏幕上天然存在的地图。

## 严格来说

Embedding 是对象的稠密向量表示。Vector（向量）可以先理解成按顺序排列的一组数字：

```text
[0.12, -0.37, 0.81, ...]
```

模型根据训练目标，把输入映射到固定维数的向量空间。系统再用余弦相似度、点积或距离等方法比较向量。

每一维通常不能稳定翻译成“退款”“天气”这样的单个人类概念。关系来自许多维度的共同作用。

## 什么东西可以做 Embedding？

根据模型和任务，可以表示：

- Token 或词；
- 句子、段落和整篇文档；
- 图片、音频或其他对象；
- 用户、商品等业务实体。

不同对象需要合适的模型与训练目标。用于文本检索的模型，不一定适合图片搜索或商品推荐。

## Embedding Model 是 LLM 吗？

不一定。Embedding Model 的主要输出是向量；生成式 LLM 的主要输出通常是后续 Token。

有些架构或基础模型可以经过不同训练用于 Embedding，但“能生成文本”和“适合做检索向量”是不同任务，不能只看模型大小判断。

## 相似度是怎么用的？

```text
资料片段 → Embedding Model → 文档向量
用户问题 → Embedding Model → 查询向量
                         ↓
                  比较向量相似度
                         ↓
                   返回较近候选
```

“较近”只表示符合当前模型与相似度规则。它可能捕捉主题相近，也可能漏掉否定、数字、时间或细微约束。

## 不同 Embedding 能混用吗？

通常不能直接混用。不同模型的维数、训练目标和坐标空间可能不同。更换 Embedding Model 后，已有资料通常需要重新生成向量。

即使维数相同，也不代表两个向量空间兼容。维数只是数字个数，不是统一语义标准。

## 最容易搞混的东西

### Embedding ≠ Token ID

Token ID 是词表中的离散编号；Embedding 是供模型计算的连续数值表示。编号相近不表示语义相近。

### Embedding ≠ 原文

向量用于表示和比较，不应替代需要展示、引用和审计的原始资料。

### Embedding ≠ Vector Database

Embedding Model 负责产生向量；Vector Database 负责保存、索引和检索向量。

### 相似 ≠ 正确

向量相似不能证明两句话事实一致，也不能替代权限、时间和来源核验。

## 常见误区

### 误区 1：向量里的每个数字都对应一个词义

通常不是。可用信息往往分布在多个维度和它们的组合中。

### 误区 2：维数越高，效果一定越好

效果还受模型、数据、训练目标、任务和检索配置影响；更高维也会增加存储与计算成本。

### 误区 3：Embedding 可以无损还原原文

Embedding 是为任务学习的表示，不是通用压缩包。原文仍应单独保存。

## 为什么我要知道它？

Embedding 是语义检索、推荐和聚类等系统的基础。理解它以后，才能明白 RAG 为什么可以用不同措辞找到相关资料，也能理解这种“相似”为什么仍有边界。

## 你只需要记住

1. Embedding 把对象转换成可比较的数值向量表示。
2. 向量接近只在特定模型、训练目标和相似度规则下有意义。
3. 不同 Embedding Model 的向量空间通常不能直接混用。
4. Embedding 不是原文、Token ID 或 Vector Database。

## 继续学习

- [上一篇：Knowledge Base 是什么](./02-knowledge-base.md)
- [下一篇：Vector Database 是什么](./05-vector-database.md)
- [相关：Token 是什么](../02-chat-and-context/04-token.md)

## 资料与核验

- [Mikolov et al.: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- [Reimers & Gurevych: Sentence-BERT](https://arxiv.org/abs/1908.10084)
- [Karpukhin et al.: Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906)
