# Coding Agent 是什么？

> Level: `Core` · Path: `Main`

## 先说人话

Coding Agent 是面向软件项目的 Agent：它能读取仓库 Context，使用文件、搜索、终端和测试等工具，修改代码，并根据执行结果继续推进任务。

它不是“更会写代码的模型”这么简单，关键是模型外面的项目工具和控制循环。

## 一次任务怎样运行？

```text
理解需求与仓库规则
   ↓
搜索相关文件和符号
   ↓
制定或调整步骤
   ↓
编辑代码
   ↓
运行测试 / 构建 / 检查
   ↓
读取结果并继续修复
   ↓
提交 Diff 与验证证据
```

不同产品不必严格按同一顺序，但都需要把环境反馈带回后续决策。

## Coding Agent 由什么组成？

- 一个或多个代码模型；
- 用户需求与仓库指令；
- Project Context 检索；
- 文件读写、搜索、终端和 Git Tools；
- Agent Loop、预算与停止条件；
- 沙箱、权限和确认机制；
- 测试、构建与 Review 证据。

## 为什么终端和 Git 重要？

终端让 Agent 运行真实测试、构建和工具，而不是只猜代码是否可用。Git 提供 Diff、历史和可恢复的变更边界。

但拥有终端也扩大风险：命令可能删除数据、泄露凭证或影响外部系统，因此需要沙箱、最小权限与确认。

## Project Context 为什么重要？

同一个需求在不同仓库有不同架构、依赖和规范。Coding Agent 要读取相关代码、配置、测试和 `AGENTS.md` 等项目指令，不能只靠通用训练知识。

Context 也不能无限加载；系统需要搜索、筛选和更新真正相关的信息。

## 怎样判断任务完成？

“代码已修改”不是完成。更可靠的证据包括：

- Diff 与需求一致；
- 相关测试、类型检查和构建通过；
- 新增失败路径和边界测试；
- 没有意外文件或调试残留；
- 高风险变化经过人工 Review；
- 仍未验证的外部条件被明确记录。

## 最容易搞混的东西

### Coding Agent ≠ Code Completion

补全主要根据局部 Context 续写；Coding Agent 可以跨文件、运行工具并循环处理结果。

### Coding Agent ≠ IDE

IDE 是开发环境；Coding Agent 可以集成在 IDE，也可以运行在终端、云端或 CI 环境。

### Coding Agent ≠ 自动合入权限

能修改仓库不代表应直接推送生产或合并 PR。权限和发布门禁属于外部系统。

## 常见误区

### 误区 1：Benchmark 通过率等于生产可靠性

Benchmark 只覆盖特定仓库、任务和评测；真实环境还有权限、依赖、私有服务和发布流程。

### 误区 2：测试绿了就可以忽略 Diff

测试可能不完整，Agent 也可能通过删除断言或改变目标让测试通过。必须同时 Review 变更。

### 误区 3：给 Agent 整个仓库就一定理解更好

无关内容会占用 Context。需要按任务检索并保持关键状态。

## 你只需要记住

1. Coding Agent 组合模型、项目 Context、开发工具和 Agent Loop。
2. 它能编辑并运行真实反馈，不只生成代码片段。
3. 完成需要 Diff、测试、构建和需求证据，不能只看模型声明。
4. 终端和仓库权限会扩大风险，必须使用沙箱、确认和最小权限。

## 继续学习

- [上一篇：AI Coding 是什么](./01-ai-coding.md)
- [下一篇：Project Context 是什么](./08-project-context.md)

## 资料与核验

- [Yang et al.: SWE-agent — Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793)
- [Jimenez et al.: SWE-bench](https://arxiv.org/abs/2310.06770)
- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
