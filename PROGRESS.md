# LLM-101 项目进度

> 当前版本：v0.1
>
> 最后更新：2026-08-18

## 当前阶段

Phase 1 第一批 Core 已完成。持续执行模式已经启用：每批最多三篇，Review 通过后提交并推送，再自动进入下一批。

## Pre-Batch Architecture Review Fix

完成：

- README 主路线补入 Model 和 Language Model。
- 将错误的一棵总览树拆成技术路线、现代 AI 应用组成和 RAG 流程三张图。
- 删除前三篇正文中的内部编辑说明。
- 明确正文中的“模型”默认指机器学习模型，尤其是神经网络模型。
- 修正模型落盘可能由权重、架构配置、Tokenizer 配置等一个或多个文件共同表示。
- 删除已有正式内容目录中的无意义 `.gitkeep`。
- CONTENT_MAP 增加独立的 `Path: Main / Optional` 维度，并为 v0.1 Main Path 记录 Article Path。

Review：

- Architecture: PASS
- Beginner: PASS
- Terminology: PASS
- Link: PASS

Review 中修复：

- README 的 Core 定义与新 Path 维度职责重叠，已改为 `Level` 表示内容深度、`Path` 表示阅读优先级。
- Main 路线最初用同一行箭头压缩多个章节，可能被误读成概念父子关系，已改成逐步学习顺序。

## Phase 0 仓库检查

### 检查时已有文件

- `README.md`
- `CONTENT_MAP.md`
- `ARTICLE_TEMPLATE.md`
- `DIRECTORY_TREE.md`
- `docs/`、`history/`、`ecosystem/`、`appendix/`、`faq/`、`assets/` 的目录骨架

### 检查时缺少文件

- `PROGRESS.md`
- `GLOSSARY.md`
- `faq/beginner-questions.md`
- Phase 1 正文文章

### 发现并修复的问题

1. 项目展示名称的大小写不统一：已统一为 `LLM-101`。
2. `DIRECTORY_TREE.md` 未包含 Master Prompt 要求的 `PROGRESS.md` 和 `GLOSSARY.md`：已补充。
3. `CONTENT_MAP.md` 缺少 Phase 1 第三篇“模型”的独立内容项：已补充。
4. 第一批文章完成前没有可用的课程入口：已在 `README.md` 增加前三篇链接。
5. 仓库中没有正式正文，因此原有链接只有根目录设计文档链接；已在正文落地后重新检查相对链接。
6. Research Notes 使用 `.tmp/research/`，并通过 `.gitignore` 排除，避免临时核验材料进入正式内容。

### 保留不改的事项

- `CONTRIBUTING.md` 和 `LICENSE` 在目录设计中明确标记为“后续补 / 后续确定”，本批不擅自决定。
- 没有为未来文章批量创建空文件。
- 没有改动现有章节结构，只做了与本批执行直接相关的最小修复。

## 已完成文章

| # | 文章 | 等级 | 状态 |
|---|---|---|---|
| 01 | [AI 是什么](./docs/01-ai-and-llm/01-what-is-ai.md) | Core | Done |
| 02 | [AI、ML、DL 到底什么关系](./docs/01-ai-and-llm/02-ai-ml-dl.md) | Core | Done |
| 03 | [什么是模型](./docs/01-ai-and-llm/03-what-is-model.md) | Core | Done |
| 04 | [什么是大语言模型 LLM](./docs/01-ai-and-llm/04-what-is-llm.md) | Core | Done |
| 05 | [GPT 和 ChatGPT 有什么区别](./docs/01-ai-and-llm/05-gpt-vs-chatgpt.md) | Core | Done |
| 06 | [参数到底是什么](./docs/03-how-models-work/06-parameter.md) | Core | Done |
| 07 | [参数量和训练数据有什么区别](./docs/03-how-models-work/07-parameter-vs-training-data.md) | Core | Done |
| 08 | [Token 是什么](./docs/02-chat-and-context/04-token.md) | Core | Done |
| 09 | [Context / Context Window 是什么](./docs/02-chat-and-context/07-context.md) | Core | Done |
| 10 | [一个大模型到底是怎么诞生的](./docs/03-how-models-work/01-model-lifecycle.md) | Core | Done |
| 11 | [为什么预测下一个 Token 还能学到能力](./docs/03-how-models-work/10-next-token-prediction.md) | Core | Done |
| 12 | [Training 和 Inference 有什么区别](./docs/03-how-models-work/18-training-vs-inference.md) | Core | Done |
| 13 | [Prompt 是什么](./docs/02-chat-and-context/01-prompt.md) | Core | Done |
| 14 | [模型架构是什么](./docs/03-how-models-work/02-architecture.md) | Core | Done |
| 15 | [Transformer 是什么](./docs/03-how-models-work/03-transformer.md) | Core | Done |

## 本批 Research

- 每篇均先记录教学目标、真实问题、关键定义、来源和风险表述。
- 正式事实优先采用 NIST、OECD、权威教材和原始综述论文。
- 《大模型入门手册》和微信聊天记录只用于发现小白问题，没有把其中的历史回答直接当作事实来源。
- 三篇均为稳定概念，不包含模型排名、价格、参数规模或产品能力等易变事实。

## Batch 1 Review

### Accuracy Review

- 通过。明确 AI 没有唯一公认的一句话定义，并采用 NIST / OECD 的共同核心表述。
- 通过。明确 `Deep Learning ⊂ Machine Learning ⊂ AI` 是概念范围关系，不代表所有 AI 都靠学习，也不代表所有机器学习都是深度学习。
- 通过。模型被定义为训练得到的输入到输出的计算关系；没有把模型简化成“参数”“训练数据”或“模型文件”。

### Beginner Review

- 通过。每篇先给 20 秒人话解释，再补严格说法。
- 通过。首次出现的机器学习、深度学习、神经网络、参数、训练等术语都在当前语境中给出最小解释或指向后续文章。
- 通过。没有使用数学公式；流程图可直接在 GitHub 阅读。

### Architecture Review

- 通过。三篇都位于 `docs/01-ai-and-llm/`，与 `DIRECTORY_TREE.md` 一致。
- 通过。顺序形成 `AI → ML / DL → Model → LLM`，第三篇没有提前展开参数与训练细节。
- 通过。没有新增重复章节或改变后续目录规划。

### Terminology Review

- 通过。统一使用“人工智能（Artificial Intelligence, AI）”“机器学习（Machine Learning, ML）”“深度学习（Deep Learning, DL）”。
- 通过。区分模型、算法、训练数据、程序、API 和产品。
- 通过。类比均标明边界，没有把“学习”“看见”“会做”等拟人化说法当作严格定义。

### Duplication Review

- 通过。AI 的主定义只在第一篇展开；第二、三篇只做必要回链。
- 通过。模型的完整解释集中在第三篇；参数、训练、LLM 只预告，不抢先展开。

### Link Review

- 通过。前三篇上一页 / 下一页链接、Glossary、README 和 Progress 链接均指向现有文件。
- 模板中的 `XXX` 示例链接属于占位示例，不计为项目死链。

## Batch 2：LLM、GPT / ChatGPT、参数

完成：

- 什么是大语言模型 LLM
- GPT 和 ChatGPT 有什么区别
- 参数到底是什么

Review：

- Accuracy: PASS
- Beginner: PASS
- Architecture: PASS
- Terminology: PASS
- Duplication: PASS
- Source: PASS
- Link: PASS

Review 中修复：

- Parameter 初稿首次出现 Checkpoint 和 Tokenizer 时解释不足，已补充最小定义。
- Glossary 新增词条后字母分组顺序混乱，已按 A–P 重排。
- 上一批“模型”文章的待完成文本已替换为可用的 LLM 正文链接；Parameter 的下一篇尚未完成，保留为非链接文本，避免死链。
- OpenAI 官方网页对命令行请求返回访问限制；历史 GPT 事实同时使用可访问的 OpenAI 官方论文，产品页仅支持 ChatGPT 首发事实，不扩写当前套餐和功能。

## 正在进行

- 无。Batch 5 Review 已完成，等待提交后自动进入 Batch 6。

## Batch 3：参数量与数据、Token、Context

完成：

- 参数量和训练数据有什么区别
- Token 是什么
- Context / Context Window 是什么

Review：

- Accuracy: PASS
- Beginner: PASS
- Architecture: PASS
- Terminology: PASS
- Duplication: PASS
- Source: PASS
- Link: PASS

Review 中修复：

- 原目录同时规划 `context.md` 与 `context-window.md`，会和 Phase 1 合并文章产生重复；已将后者调整为未来 Optional 的 `long-context.md`。
- 新增正式内容后删除 `docs/02-chat-and-context/` 与 `docs/03-how-models-work/` 中失去作用的 `.gitkeep`。
- Glossary 的 C 分组重新按 ChatGPT、Context、Context Window 排序。
- Token 文章明确拒绝固定中英文 Token 换算；Context 文章区分容量上限和信息利用质量。

## 待核验

- 后续历史文章中的年份、论文和产品发布时间。
- 后续具体模型的参数、上下文窗口、训练数据、API 与产品能力。
- 原参考手册中的 Kimi K3、硬件成本、Token 固定换算、训练计算量等具体说法，均不得直接复用。

## Batch 4：模型生命周期、下一个 Token、训练与推理

完成：

- 一个大模型到底是怎么诞生的
- 为什么预测下一个 Token 还能学到能力
- Training 和 Inference 有什么区别

Review：

- Accuracy: PASS
- Beginner: PASS
- Architecture: PASS
- Terminology: PASS
- Duplication: PASS
- Source: PASS
- Link: PASS

Review 中修复：

- 生命周期明确为可回退、可并行的迭代过程，不写成所有组织必须照搬的固定流水线。
- 下一 Token 文章区分自监督目标、可观察能力与有争议的“理解”，没有把预测目标写成能力的唯一来源。
- Training / Inference 文章限定“普通推理通常不更新模型训练参数”，同时保留缓存、日志和 Memory 等系统状态可能变化的边界。
- Glossary 新增 Inference / Training 后重新校正字母与词条顺序。

## Batch 5：Prompt、Architecture、Transformer

完成：

- Prompt 是什么
- 模型架构是什么
- Transformer 是什么

Review：

- Accuracy: PASS
- Beginner: PASS
- Architecture: PASS
- Terminology: PASS
- Duplication: PASS
- Source: PASS
- Link: PASS

Review 中修复：

- Prompt 正文明确用户 Prompt 只是完整 Context 的一部分，不把具体平台消息角色写成永久标准。
- Architecture 区分架构、框架、参数、训练方法和产品，并避免把参数量完全归因于架构名称。
- Transformer 明确原始论文为 Encoder–Decoder，现代 LLM 可使用 Decoder-only 等变体；同时说明生成阶段仍通常逐 Token 进行。
- Prompt 的两个外部辅助来源在本机持续超时，已替换为可访问的 Microsoft Learn 官方文档；OpenAI 官方文档保留为 P0 来源。
- 重新连接 Main Path 上的前后文章，避免 Prompt、Architecture 和 Transformer 成为导航孤岛。

## 下一批任务

下一批最多处理 1～3 篇，建议按顺序：

1. Attention 是什么
2. Generalization 是什么
3. Reasoning 是什么

开始前仍须逐篇执行 Research → Draft → Fact Check → Concept Check → Beginner Check → Dependency Check → Link Check。
