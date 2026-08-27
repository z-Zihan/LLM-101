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

“把 Skills 作为 MCP Tools 与 Prompts 暴露”这类需求，正说明它需要显式转换，不是三个概念天然等价。

## 两层安全要分别审查

Tool 要审查输入、权限和现实副作用；Skill 要审查来源、说明与脚本。组合后还要防止恶意或过时 Skill 诱导 Agent 误用高权限 Tool。

**Tool 能做什么，Skill 教怎样做。** 两者都不能绕过 Host、沙箱和操作系统授权。

## 需求到底缺的是哪一层

动手补齐之前，可以先问三个问题，判断缺的是能力还是方法。

第一问：要用的能力已经存在吗？如果把需求拆到最后一步，发现只是“没有工具能写这个文件”，那是 Tool 层的缺口，任何说明书都填不上。第二问：步骤能一句话说清吗？“把这十个文件合并成一个”虽然体量不小，流程却单一，写一段仔细的 Prompt 就够；要说清得画流程图，就该考虑 Skill 了。第三问：出错之后谁负责兜底？如果失败模式只有一种且一眼可见，普通调用即可；如果每种失败各有处理方式，比如格式不合就先转换、权限不足就换路径，这就是方法知识，适合沉淀进说明。

拿每天备份笔记举例。写文件的工具通常早就有（第一问通过）；备份这个动作一句话说得清吗？未必——要先去重、按日期命名、校验副本可读（第二问不通过）；坏了怎么办也有讲究：目标盘满、源文件被占用、上次没备份完（第三问也不通过）。三问下来缺口在方法层：为一个备份 Tool 配上步骤与异常处理的说明，正好是一个最小但完整的 Skill。

## 方法层补不了能力层的坑

另一个方向的反向错觉值得单独说清：写一份再详细的说明，也不能让不存在的工具出现。

如果 Skill 的流程规定“导出为 PDF 后核对页码”，而环境里根本没有 PDF 渲染工具，Agent 读到这一步只会失败得更流畅——它清楚自己卡在哪，却依然卡着。同理，当一个 Tool 自身的描述含混（名称叫 process_data 却不说处理什么），试图用 Skill 逐处提醒“注意这个工具容易误解”，往往是在给脆弱性打补丁：说明越叠越多，跨环境的兼容面越来越窄。正确的修法是把模糊的定义修回 Tool 侧，让一次调用自然可理解，而不是让说明书替工具道歉。

所以看到一套臃肿的 Skill 时，可以先问一句：这些防御性段落里，有多少其实在控诉底层能力的缺陷？把属于 Tool 的问题还给 Tool，说明才能瘦回真正的“方法”。

## 继续学习

- [MCP 和 Skill 有什么区别](./04-MCP和Skill有什么区别.md)
- [Agent 和 Skill 有什么区别](./05-Agent和Skill有什么区别.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [MCP Specification: Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- [PatternFly MCP issue: Allow MCP skills as tools and prompts](https://github.com/patternfly/patternfly-mcp/issues/186)
