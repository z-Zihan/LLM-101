# Tool 和 Skill 有什么区别？

> 所属专题：Skill · 前置：[Prompt 和 Skill 有什么区别](./02-Prompt和Skill有什么区别.md) · 后续：[MCP 和 Skill 有什么区别](./04-MCP和Skill有什么区别.md)
>
> 最后核验：2026-08-19

Tool 提供可执行能力，Skill 提供完成一类任务的方法与配套材料。一个让程序读取文件，另一个告诉 Agent 应该读哪些文件、按什么顺序处理、怎样检查完成质量。

## 做正式报告需要两层能力

文档 Agent 可能拥有文件读取和文档渲染 Tool，同时加载“制作正式报告” Skill。Skill 规定先读模板、核对数据、生成文档、渲染检查并修复排版；Tools 负责真实读写与渲染。

```text
Skill：目标、步骤、规范、验证
  ↓ 指导选择
Tool：读取、转换、执行、返回结果
  ↓
Agent 检查是否满足完整任务
```

这张图想区分一次动作和完整方法。读图时注意，Tool 返回成功只表示某一步执行完成，不代表 Skill 定义的任务已经验收通过。

Tool 通常由 Host 或 Server 暴露，具有名称、描述和输入 Schema。Skill 通常是包含 `SKILL.md` 的目录，还可以携带脚本与参考资料。Tool Description 帮助模型选择一次调用，无法替代多步工作流。

## Skill 里的脚本是不是 Tool

脚本是可执行文件，但只有 Runtime 通过命令或工具运行时才产生操作。Skill 文本不能自行获得文件、网络和凭证权限。

Agent 请求执行脚本后，Host 仍要检查来源、参数和副作用。一个 Skill 可以指导多个 Tool 协作，也可以只提供写作规范而完全不用外部 Tool；Tool 也能被直接调用，不要求配套 Skill。

## Skill 能否直接暴露成 MCP Tool 或 Prompt

平台可以编写适配层，把某个 Skill 的入口包装成 MCP Tool，或把部分模板暴露为 MCP Prompt。但职责不会因此相同：MCP Tool 是可调用操作，MCP Prompt 是消息模板，完整 Skill 还包含触发条件、流程、材料和验证。

公开项目里出现“把 Skills 作为 MCP Tools 与 Prompts 暴露”的需求，正说明这需要显式转换，不是三个概念天然等价。

## 两层安全要分别审查

Tool 要审查输入、权限和现实副作用；Skill 要审查来源、说明与脚本。组合后还要防止恶意或过时 Skill 诱导 Agent 误用高权限 Tool。

**Tool 能做什么，Skill 教怎样做。** 两者都不能绕过 Host、沙箱和操作系统授权。

## 继续学习

- [MCP 和 Skill 有什么区别](./04-MCP和Skill有什么区别.md)
- [Agent 和 Skill 有什么区别](./05-Agent和Skill有什么区别.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [MCP Specification: Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- [PatternFly MCP issue: Allow MCP skills as tools and prompts](https://github.com/patternfly/patternfly-mcp/issues/186)
