# Skill 到底是什么？

> 你现在的位置：[MCP](../09-MCP/01-MCP到底是什么.md) → **Skill** → [Coding Agent](../11-Coding-Agent/04-Coding-Agent是什么.md)
>
> 课程导航：[上一篇：MCP 到底是什么](../09-MCP/01-MCP到底是什么.md) · 第 26 / 28 篇 · [下一篇：Coding Agent 是什么](../11-Coding-Agent/04-Coding-Agent是什么.md)
>
> 最后核验：2026-08-19

“Skill”在不同产品里可能指不同功能。本章使用 Agent Skills 语境：Skill 是可移植的任务能力包，以 `SKILL.md` 描述何时使用、怎样完成和如何验证，还可以附带脚本、参考资料、模板与素材。

它不训练模型参数，也不自动授予新权限。Skill 更像按需加载的做事方法，让 Agent 不必在每次任务里重新摸索流程。

## 一个 Skill 目录里有什么

```text
my-skill/
├── SKILL.md       # 名称、用途、步骤与验证
├── scripts/       # 可选：辅助脚本
├── references/    # 可选：规范和参考资料
└── assets/        # 可选：模板或素材
```

这张图想说明 Skill 不只是长 Prompt。读图时注意，`SKILL.md` 是入口，其他文件按任务需要读取或执行；一个只有说明的 Skill 也可以有效。

名称和描述用于发现与匹配，正文给出完整工作流。脚本适合重复、确定的机械操作，参考资料提供事实与规范，模板保证输出结构。Skill 是否可移植，还取决于它有没有假设不存在的工具、路径或权限。

## 为什么要渐进披露

Agent 可能安装许多 Skill。每次把全部说明、脚本和资料塞入上下文，会浪费 Token 并产生冲突。渐进披露先暴露简短 metadata，匹配任务后读取 `SKILL.md`，只有需要时再加载相关文件。

```text
发现名称与描述
  ↓ 当前任务相关
读取完整 SKILL.md
  ↓ 某一步需要
加载指定脚本、资料或模板
```

这张图想说明“安装”不等于“每次全部加载”。读图时注意，何时触发、读哪些文件应由清晰说明决定，不能靠猜测隐藏依赖。

## Skill 与 Prompt、Tool、MCP、Agent

Prompt 是一次模型输入；Skill 是可发现、按需加载的任务包，其中会包含提示说明，但还可包含脚本和材料。Tool 提供可执行能力，Skill 说明怎样组合能力完成任务。

MCP 是 Host 连接 Server 的协议，Skill 可以指导 Agent 使用 MCP Tool，也可以完全不依赖 MCP。Agent 是运行系统，Skill 为它提供方法；没有 Agent 执行与工具权限，Skill 文件不会自己行动。

Skill 也可以描述如何把能力暴露为 MCP Tool 或 Prompt，但“说明怎样做”和“协议上已经提供能力”仍是两件事。

## 如何判断一个 Skill 是否可靠

先检查来源、适用范围和依赖，再阅读脚本会访问哪些文件、网络和凭证。破坏性动作、外部发布和权限变更必须保留确认；Markdown 中的指令也可能诱导 Agent 执行危险操作。

好的 Skill 给出输入、步骤、失败处理和可验证结果，而不是只写“生成高质量内容”。安装数量越多并不越强，重叠、过时或触发描述含糊会增加选择错误。

## 回答真实问题

**Skill 是一个很长的 Prompt 吗？** 不只是。它是可发现的任务包，可包含 Prompt 风格说明、脚本、资料和模板。

**Skill 是 Tool 吗？** 不是。Tool 提供执行能力，Skill 提供使用这些能力的方法。

**安装 Skill 会训练模型吗？** 不会，它在运行时进入上下文或调用已有工具。

**Skill 能绕过权限吗？** 不能，Host、沙箱和操作系统权限仍然生效。

## 从这里继续

- [Prompt 和 Skill 有什么区别](./02-Prompt和Skill有什么区别.md)
- [Tool 和 Skill 有什么区别](./03-Tool和Skill有什么区别.md)
- [MCP 和 Skill 有什么区别](./04-MCP和Skill有什么区别.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [Agent Skills Overview](https://agentskills.io/home)
- [Anthropic: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
