# Retrieval 是什么？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> RAG 是怎么从几万份资料里找到相关段落的？
>
> Retrieval 找到的内容，就是最终答案吗？

## 先说人话

Retrieval（检索）是根据查询，从候选资料中找出可能相关内容的过程。

它负责“找证据候选”，不负责保证候选正确，也不负责生成最终回答。

## 举个例子

用户问：“中国区员工出差住宿上限是多少？”检索系统可能：

```text
理解查询中的地区、主题和时间
        ↓
搜索知识库
        ↓
过滤到中国区与有效版本
        ↓
返回最相关的若干政策片段
```

生成模型再阅读这些片段并组织答案。如果检索阶段拿错了地区或旧版本，后面的回答很可能也会错。

## 严格来说

Retrieval 接收 Query（查询），在 Corpus（候选集合）中计算匹配或相关性，并返回排序后的候选结果。

```text
Query
  +
可搜索的文档 / 片段 / 记录
  ↓
匹配、过滤与排序
  ↓
Top-k 候选
```

Top-k 表示返回得分较高的前 k 个候选；它是数量设置，不是正确性保证。

## 常见检索方式

### 关键词 / 稀疏检索

根据词语出现、稀有程度等信号匹配。它擅长精确名称、编号和专有词，但可能漏掉用不同措辞表达的内容。

### Dense Retrieval（稠密检索）

用 Embedding Model 把查询和文档映射成向量，再比较相似度。它更容易匹配近义表达，但可能忽略精确数字、否定或细粒度条件。

### Hybrid Retrieval（混合检索）

组合关键词、向量和其他业务信号。混合不自动更好，仍需要针对真实查询评估和调权重。

## Chunk 为什么会影响 Retrieval？

文档通常会被切成 Chunk（片段）后建立索引。片段太大，可能混入许多无关信息；太小，又可能丢失标题、条件和上下文。

切分方式、重叠、标题保留和表格处理都会影响检索。Chunk 会在后续 Optional 文章展开。

## Recall 和 Precision 是什么？

可以先用两句话理解：

- Recall（召回率）：需要的证据有没有被找回来；
- Precision（精确率）：找回来的候选里，有多少真的相关。

返回更多候选可能提高 Recall，也可能带来更多噪声。RAG 还受 Context 容量限制，不能无限增加 top-k。

## 为什么还需要 Rerank？

第一阶段检索常追求快速找回候选；Rerank（重排）再用更精细的方法重新排序，把更相关内容放在前面。

```text
快速召回较多候选
        ↓
Rerank 精细比较
        ↓
选择少量内容进入 Context
```

重排可以改善排序，但不会补回第一阶段完全漏掉的资料。

## 权限应该在哪检查？

检索前或检索过程中就应根据用户身份过滤不可访问资料，并在返回和生成阶段继续防护。

如果先把机密内容取回并放进 Context，再要求模型“不要说”，敏感数据已经越过了不该越过的边界。

## 最容易搞混的东西

### Retrieval ≠ Generation

Retrieval 返回候选证据；Generation 根据 Context 生成内容。两步需要分别评估。

### Retrieval ≠ Search UI

搜索框是界面；检索是背后的查询、匹配、过滤和排序过程，也可以被程序或 Agent 调用。

### Retrieval ≠ Vector Search

向量搜索是一种检索方法。关键词、SQL、图查询和混合方法也可以参与 Retrieval。

### 相关 ≠ 足以回答

一段资料可能与主题相关，却没有包含问题需要的数字、条件或结论。

## 常见误区

### 误区 1：相似度最高就一定最有用

相似度只是一种信号。时效、权限、来源质量和业务条件同样重要。

### 误区 2：top-k 越大越好

更多候选会增加延迟和 Context 噪声，还可能把冲突资料一起送入模型。

### 误区 3：最终答案错了，就一定是模型幻觉

也可能是知识库缺失、查询错误、权限过滤、切分、召回或排序出了问题。

## 为什么我要知道它？

Retrieval 决定模型在本次回答中能看到哪些证据。理解它后，你能把“没找到”“找错了”和“找到却没用好”分开排查。

## 你只需要记住

1. Retrieval 根据查询从候选集合中召回并排序相关内容。
2. 关键词、Dense 和 Hybrid 都是检索方式，向量搜索不是唯一方案。
3. top-k 是候选数量，不是正确性保证；Recall 与 Precision 需要平衡。
4. 检索、权限、重排和生成是不同阶段，应分别验证。

## 继续学习

- [上一篇：Vector Database 是什么](./05-vector-database.md)
- 下一篇（待完成）：RAG 和 Fine-tuning 有什么区别？
- [相关：RAG 是什么](./01-what-is-rag.md)

## 资料与核验

- [Karpukhin et al.: Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906)
- [Lewis et al.: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Reimers & Gurevych: Sentence-BERT](https://arxiv.org/abs/1908.10084)
