# Knowledge Base 是什么？

> Level: `Core` · Path: `Main`

## 一个小白真的会怎么问？

> 知识库就是把一堆 PDF 放进文件夹吗？
>
> 知识库、数据库和向量数据库是一回事吗？

## 先说人话

Knowledge Base（知识库）是为了查询、回答或完成任务而组织和管理的一组资料。

它可以包含文档、网页、表格、产品记录、问答和元数据；“知识库”描述的是资料集合及其管理边界，不限定必须使用某一种数据库。

## 举个例子

公司客服知识库可能包含：

- 产品说明书；
- 退换货政策；
- 常见问题与标准答案；
- 故障处理步骤；
- 每份资料的版本、适用地区和更新时间。

只有把 PDF 丢进文件夹，还没有解决哪些内容有效、谁能访问、怎样更新和怎样检索等问题。

## 严格来说

在不同领域，Knowledge Base 可能有不同结构：

- 文档型：文章、手册、网页和文件；
- 结构化：表格、实体、属性与关系；
- 混合型：同时包含原文、数据库记录、标签和索引。

用于 RAG 时，知识库通常是系统允许检索的权威资料范围，并配合切分、索引、权限和更新流程。

```text
原始资料
  + 元数据
  + 权限与版本
  + 可检索索引
        ↓
可供应用查询的 Knowledge Base
```

## 元数据有什么用？

Metadata（元数据）是描述资料的数据，例如：

- 标题、作者和来源；
- 创建与更新时间；
- 产品、地区、语言和版本；
- 保密等级与访问权限；
- 原文位置和有效期。

元数据能帮助系统过滤和追踪来源。例如查询中国区政策时，可以排除其他地区的旧版本。

## Knowledge Base 和 Database 有什么区别？

Database 强调按数据结构保存、查询和更新记录；Knowledge Base 强调“哪些资料被组织为可供回答和推理使用的知识范围”。

知识库可以建立在数据库、文件系统、搜索引擎或多种存储之上。数据库也可以保存交易数据，而不被产品称为知识库。

## Knowledge Base 和 Vector Database 的区别

Vector Database（向量数据库）主要负责保存向量并支持相似性检索。它可以存放知识库切片的向量索引，但通常不是完整知识库本身。

```text
Knowledge Base
├── 原始文档或记录
├── 元数据、权限和版本
└── 一个或多个检索索引
     ├── 关键词索引
     └── 向量索引（可由 Vector DB 承载）
```

有些产品会把“知识库”作为整个 RAG 数据服务的名称，具体范围要看产品文档。

## 建好知识库就等于完成 RAG 吗？

不等于。RAG 还需要：

- 把用户问题转换成检索请求；
- 找到并排序相关资料；
- 把资料放入模型 Context；
- 生成并验证回答；
- 记录引用与失败情况。

知识库是 RAG 的信息来源之一，不是完整问答流程。

## 知识库为什么会失效？

常见原因包括：

- 资料长期不更新；
- 新旧版本同时存在且没有标记；
- 扫描件或表格解析错误；
- 权限过滤错误导致泄露或漏检；
- 重复、冲突和低质量内容过多；
- 缺少来源和更新时间，无法验证。

知识库质量不只看文件数量，还要看准确性、覆盖率、可检索性、时效性和权限治理。

## 最容易搞混的东西

### Knowledge Base ≠ 模型参数

知识库是外部资料系统；模型参数来自训练。更新知识库不会自动更新模型参数。

### Knowledge Base ≠ Context

知识库可以很大；Context 只包含当前请求实际提供给模型的有限信息。

### Knowledge Base ≠ 文件夹

文件夹可以存放原始资料，但完整知识库还需要组织、权限、版本、索引和维护。

### Knowledge Base ≠ 正确保证

知识库也可能错误、过时或互相冲突，仍需治理和验证。

## 常见误区

### 误区 1：文档越多，回答越好

低质量和重复资料会增加检索噪声。覆盖率与质量都重要。

### 误区 2：做了向量化，就不需要原文

向量用于检索，不应替代可审查的原始内容、来源和权限信息。

### 误区 3：所有用户都应该搜索同一套资料

不同用户可能有不同权限。检索前后都需要落实访问控制，不能只靠 Prompt 要求模型保密。

## 为什么我要知道它？

知识库是 RAG 的“资料从哪里来”这一层。理解它后，才能继续学习 Embedding、Vector Database、Chunk 和 Retrieval，而不会把整个系统误认为一个向量数据库。

## 你只需要记住

1. Knowledge Base 是为查询和任务组织、管理的一组资料，不限定一种存储技术。
2. 元数据、版本、权限和更新时间与原文同样重要。
3. Vector Database 可以承载向量索引，但不等于完整知识库。
4. 知识库是 RAG 的信息来源之一，建立知识库不等于 RAG 已完成。

## 继续学习

- [上一篇：RAG 是什么](./01-what-is-rag.md)
- [下一篇：Embedding 是什么](./03-embedding.md)
- [相关：为什么 LLM 不是数据库](../05-limitations/02-llm-is-not-database.md)

## 资料与核验

- [Lewis et al.: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [Karpukhin et al.: Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906)
- [Microsoft Learn: RAG solution design and evaluation guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide)
