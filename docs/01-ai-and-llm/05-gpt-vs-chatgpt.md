# GPT 和 ChatGPT 有什么区别？

> Level: `Core` · Path: `Main`

## 读完你应该明白

1. GPT 是模型家族与技术名称，ChatGPT 是产品服务。
2. OpenAI 是公司，API 是程序调用能力的接口。
3. 一个产品可以组合不同模型、工具和规则。
4. 产品当前使用哪些模型属于易变事实。

## 一个小白真的会怎么问？

> GPT、ChatGPT、OpenAI 是一个东西的三个名字吗？
>
> 我在 ChatGPT 里聊天，是不是就在直接使用一个叫 ChatGPT 的模型？

## 先说人话

最简单的区分是：

```text
OpenAI  = 公司
GPT     = 模型家族 / 技术名称
ChatGPT = 面向用户的聊天产品
API     = 程序调用模型或服务的接口
```

可以把 GPT 类比成“发动机家族”，把 ChatGPT 类比成“装有发动机、方向盘和其他系统的整车”。这只是帮助理解的类比：软件模型和汽车的结构并不相同。

## GPT 是什么？

GPT 来自 Generative Pre-trained Transformer：

- **Generative（生成式）**：能够生成新的内容；
- **Pre-trained（预训练）**：先在广泛数据上训练，再适配具体使用方式；
- **Transformer**：所采用的核心模型架构类型。

OpenAI 在 2018 年的论文中用“生成式预训练”展示了先进行语言模型预训练、再适配具体任务的路线。后来 GPT 成为一系列模型的家族名称。

GPT 不是一个永远固定的单一模型文件。不同代际或不同用途的 GPT 模型可以有不同能力、训练方式和使用边界。

## ChatGPT 是什么？

ChatGPT 是 OpenAI 面向用户提供的 AI 产品。用户通过聊天界面输入内容，产品再组织模型和其他系统能力生成回复。

OpenAI 于 2022 年 11 月 30 日公开发布 ChatGPT。首发说明将它描述为以对话方式交互的模型，并说明当时的模型经过人类反馈强化学习等方法训练。

产品层通常还包含：

```text
用户界面
  +
对话历史与 Context 管理
  +
一个或多个模型
  +
安全与产品规则
  +
搜索、文件、代码等工具
```

具体组成会随产品更新而变化，因此不能把某个时期的模型列表写成 ChatGPT 的永久定义。

## 为什么模型和产品要分开？

因为同一个模型可以通过不同方式被使用：

```text
模型
├── 被聊天产品调用
├── 通过 API 被开发者的程序调用
└── 被其他工作流或 Agent 调用
```

反过来，一个产品也可以根据任务、设置或版本使用不同模型，并在模型之外增加搜索、记忆和工具。

如果把模型和产品混为一谈，就容易产生错误问题，例如“ChatGPT 有多少参数”。更准确的问法是：

> 某个时间、某个 ChatGPT 模式具体使用哪个模型？该模型公开了哪些规格？

## API 又是什么？

应用程序编程接口（Application Programming Interface，API）是一套让程序按约定发出请求、接收结果的接口。

开发者可以在自己的应用中通过 API 使用模型能力，而不必让最终用户打开 ChatGPT 网页或 App。

```text
用户 → ChatGPT 产品 → 产品内部调用能力

用户 → 开发者应用 → API → 模型服务
```

这两条路径可能使用相关模型，但产品体验、数据处理方式、功能和计费不能因此直接画等号。

## 最容易搞混的东西

| 名称 | 类型 | 主要回答的问题 |
|---|---|---|
| OpenAI | 公司 / 组织 | 谁开发和提供相关模型与产品？ |
| GPT | 模型家族 | 哪一类模型在进行计算和生成？ |
| ChatGPT | 产品服务 | 普通用户通过什么界面和功能使用 AI？ |
| API | 程序接口 | 其他软件怎样请求模型或服务？ |

### GPT ≠ ChatGPT 的简称

ChatGPT 的名字包含 GPT，但 ChatGPT 不是 GPT 的另一个缩写。一个是模型家族名称，一个是产品名称。

### ChatGPT ≠ 单一固定模型

产品可以升级、切换或组合模型。询问产品能力时要注明时间；询问模型能力时要明确具体模型。

### GPT ≠ 所有 LLM

GPT 是 OpenAI 的模型家族。其他机构也可以开发大语言模型，它们不因此叫 GPT。

## 常见误区

### 误区 1：OpenAI、GPT、ChatGPT 可以互换使用

不对。公司开发模型，产品使用模型，API 提供程序化入口。它们处在不同层。

### 误区 2：ChatGPT 的所有表现都只由模型决定

不对。系统提示、工具、Context 管理、安全策略和产品界面也会影响体验。

### 误区 3：知道产品名，就知道参数量和上下文窗口

不对。这些规格属于具体模型或具体服务配置，而且可能不公开或随时间变化。

## 为什么我要知道它？

以后看新闻、产品说明或 API 文档时，你需要先判断讨论的是哪一层：

```text
Company
  ↓ 开发 / 提供
Model
  ↓ 被调用
API / Product
  ↓ 服务
User / Application
```

这能避免把产品功能当成模型固有能力，也能避免把某个模型规格套到整个产品上。

## 你只需要记住

1. GPT 是模型家族，ChatGPT 是产品，OpenAI 是公司。
2. API 是程序调用能力的接口，不等于 ChatGPT 产品。
3. 一个产品可以组合不同模型、工具和规则。
4. 当前模型列表和产品功能会变化，讨论时必须注明时间与对象。

## 继续学习

- [上一篇：什么是大语言模型 LLM](./04-what-is-llm.md)
- [下一篇：参数到底是什么](../03-how-models-work/06-parameter.md)
- [相关：什么是模型](./03-what-is-model.md)

## 资料与核验

最后核验：2026-08-18。

本篇只保留稳定的公司、模型、产品与 API 边界，不列当前套餐、价格、模型清单或排行榜。

- [OpenAI: Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
- [OpenAI: Introducing ChatGPT](https://openai.com/index/chatgpt/)
- [OpenAI Developer Docs: Models](https://developers.openai.com/api/docs/models)
