# LLM-101 项目进度

> 当前版本：v0.1
>
> 最后更新：2026-08-18

## 当前阶段

Phase 1 第一批 Core 已完成：本批只处理前三篇，未继续批量生成后续文章。

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

## 正在进行

- 无。按照 Master Prompt，前三篇完成 Review 后在此批停止。

## 待核验

- 后续历史文章中的年份、论文和产品发布时间。
- 后续具体模型的参数、上下文窗口、训练数据、API 与产品能力。
- 原参考手册中的 Kimi K3、硬件成本、Token 固定换算、训练计算量等具体说法，均不得直接复用。

## 下一批任务

下一批最多处理 1～3 篇，建议按顺序：

1. 什么是大语言模型 LLM
2. GPT 和 ChatGPT 有什么区别
3. 参数到底是什么

开始前仍须逐篇执行 Research → Draft → Fact Check → Concept Check → Beginner Check → Dependency Check → Link Check。
