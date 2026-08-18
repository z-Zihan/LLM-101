# Agent 和 Skill 有什么区别？

> Level: `Core` · Path: `Main`
>
> 最后核验：2026-08-18

## 先说人话

Agent 是围绕目标运行、会观察结果并继续行动的系统；Skill 是 Agent 可按需加载的一套任务方法和材料。

```text
Agent：谁在推进任务
Skill：推进某类任务时采用什么方法
```

## 举个例子

一个 Coding Agent 要制作发布说明。它可以加载“发布说明” Skill，按照其中规范读取提交、分类变化、套用模板并检查链接。

Agent 负责决定何时加载、调用哪些 Tools 和何时完成；Skill 只提供方法、脚本和参考。

## 核心区别

| 维度 | Agent | Skill |
|---|---|---|
| 类型 | 运行系统 | 文件形式的能力包 |
| 是否有目标与状态 | 通常有 | 不独立运行 |
| 是否有 Agent Loop | 可以有 | 不提供运行循环 |
| 是否执行 Tool | 由 Host 授权后可执行 | 只能指导或提供脚本 |
| 数量关系 | 一个 Agent 可加载多个 Skills | 一个 Skill 可被多个 Agent 使用 |

## Skill 会不会自己运行？

不会。Skill 文件需要被 Agent 或其他 Runtime 发现、读取，并在权限允许时执行脚本。仅把目录放在磁盘上不会自动推进任务。

## Agent 没有 Skill 能工作吗？

可以。简单任务可以直接依赖 Prompt 和 Tools。Skill 的价值是把反复使用的专业方法从临时 Prompt 中抽出，便于复用和维护。

## 安全边界

Agent 的权限、预算和停止条件由 Host 管理；Skill 内容与脚本需要来源审查。Agent 选中了 Skill，也不表示其中每个操作都已授权。

## 常见误区

### 误区 1：Skill 是一个小 Agent

Skill 没有独立目标、状态和循环，更像可加载的任务知识包。

### 误区 2：装更多 Skills 会自动让 Agent 更可靠

过时、重叠或恶意 Skill 会增加错误和风险，仍需评测与治理。

### 误区 3：Agent 会永久学会 Skill

Skill 通常在运行时进入 Context，不等于更新模型参数。

## 你只需要记住

1. Agent 是运行系统，Skill 是可加载的任务能力包。
2. Agent 负责目标、状态、循环和 Tool 使用；Skill 提供方法与材料。
3. 二者可以多对多复用，但 Skill 不会独立运行。
4. 选择 Skill 不等于获得额外权限或完成训练。

## 继续学习

- [上一篇：MCP 和 Skill 有什么区别](./04-MCP和Skill有什么区别.md)
- [下一篇：AI Coding 是什么](../11-Coding-Agent/01-AI-Coding是什么.md)

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
