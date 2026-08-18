# Tool 和 Skill 有什么区别？

> Level: `Core` · Path: `Main`
>
> 最后核验：2026-08-18

## 先说人话

Tool 提供可执行的能力；Skill 提供完成一类任务的方法、说明和配套材料。

```text
Tool：可以做什么
Skill：应该怎样做
```

## 举个例子

一个文档 Agent 拥有：

- 文件读取 Tool；
- 文档渲染 Tool；
- “制作正式报告” Skill。

Skill 可以规定先读模板、再生成文档、渲染检查、发现排版问题后修复；Tools 负责真正读取文件和运行渲染。

## 严格来说

Tool 通常由 Host 或 Server 暴露，有名称、描述和输入 Schema，并在获得授权后执行操作。

Skill 通常是包含 `SKILL.md` 的目录，描述任务目标、步骤、检查方法，并可带脚本和资料。Agent 把 Skill 说明加入 Context 后，再选择合适 Tools。

## Skill 里的脚本是不是 Tool？

脚本是可执行文件，但只有运行环境把它作为命令或工具执行时才产生操作。Skill 不能仅凭文字自行获得执行权限。

```text
Skill 提到脚本
   ↓
Agent 请求执行
   ↓
Host / Runtime 检查权限
   ↓
真正运行
```

## Tool 能不能没有 Skill？

可以。简单工具可以直接由模型或用户调用。但当使用步骤复杂、容易出错或有组织规范时，Skill 能提供稳定方法。

## Skill 能不能没有 Tool？

可以。写作风格、检查清单或分析框架可能只需模型按照说明工作，不一定调用外部 Tool。

## 最容易搞混的东西

### Tool Description ≠ Skill

Tool Description 主要帮助模型选择并填写调用；Skill 可以覆盖完整多步任务和验证流程。

### Skill ≠ 权限

Skill 可以建议删除文件，但是否允许删除由 Host、沙箱和操作系统决定。

### Tool Result ≠ Skill 结果

一次 Tool Result 只表示某个步骤返回；Skill 定义的完整任务可能还需要验证和后续步骤。

## 安全边界

Tool 要检查输入、授权和副作用；Skill 要审查来源、说明与脚本。组合后还要防止 Skill 引导 Agent 误用高权限 Tool。

## 你只需要记住

1. Tool 提供外部执行能力；Skill 提供任务方法和配套材料。
2. Skill 可以指导多个 Tools 协作，Tool 本身不等于完整做事流程。
3. Skill 中包含脚本不代表已获执行权限。
4. Tool 与 Skill 都需要独立的来源、权限和副作用审查。

## 继续学习

- [上一篇：Prompt 和 Skill 有什么区别](./02-skill-vs-prompt.md)
- [下一篇：MCP 和 Skill 有什么区别](./04-skill-vs-mcp.md)

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [MCP Specification: Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
