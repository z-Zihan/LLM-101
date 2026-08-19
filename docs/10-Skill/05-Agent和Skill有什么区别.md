# Agent 和 Skill 有什么区别？

> 所属专题：Skill · 前置：[MCP 和 Skill 有什么区别](./04-MCP和Skill有什么区别.md) · 后续：[AI Coding 是什么](../11-Coding-Agent/01-AI-Coding是什么.md)
>
> 最后核验：2026-08-19

Agent 是围绕目标持续推进任务的运行系统；Skill 是 Agent 可以按需加载的一套任务方法和材料。可以把区别压缩成一句话：Agent 负责“谁在做并继续做”，Skill 负责“做这类任务时采用什么方法”。

## 发布说明怎样由两者协作

Coding Agent 接到制作发布说明的目标后，可以加载发布说明 Skill。Skill 规定读取哪些提交、怎样分类变化、使用什么模板、如何检查链接；Agent 决定何时加载、调用哪些 Tools、失败后怎样调整以及何时完成。

```text
Agent：目标、状态、循环、工具与停止条件
  ↓ 按需加载
Skill：步骤、规范、脚本、参考与验收
```

这张图想说明 Skill 不独立运行。读图时注意，磁盘上存在 Skill 目录不会自动推进任务，必须由 Agent 或 Runtime 发现、读取并在权限范围内执行。

一个 Agent 可以加载多个 Skills，同一个 Skill 也能被不同 Agent 使用。简单任务没有 Skill 也能完成；Skill 的价值是把反复使用的专业方法从临时 Prompt 中抽出，便于维护和验证。

Skill 不是“小 Agent”：它没有自己的持续目标、环境状态和 Agent Loop。Skill 中的脚本也不自带权限，Agent 请求执行时仍受 Host、沙箱和操作系统控制。

## 可靠性来自治理，不是数量

更多 Skills 不自动让 Agent 更强。过时、重叠或恶意 Skill 会让触发选择冲突，甚至诱导高权限 Tool。安装前要检查来源和脚本，运行时要限制权限，并用结果证据验证任务。

Skill 内容通常进入运行时 Context，不会因此永久写入模型参数。下一次是否使用，仍取决于发现与触发机制。

## 回答关键问题

**Skill 会自己运行吗？** 不会，需要 Agent 或 Runtime 加载和执行。

**Agent 没有 Skill 能工作吗？** 可以，简单任务可直接使用 Prompt 和 Tools。

**Skill 是一个小 Agent 吗？** 不是，它没有独立目标、状态和循环。

**加载 Skill 就获得新权限吗？** 不会，权限仍由执行环境控制。

## 继续学习

- [AI Coding 是什么](../11-Coding-Agent/01-AI-Coding是什么.md)
- [Coding Agent 是什么](../11-Coding-Agent/04-Coding-Agent是什么.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
