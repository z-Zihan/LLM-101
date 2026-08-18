# Skill 是什么？

> Level: `Core` · Path: `Main`
>
> 最后核验：2026-08-18

## 一个小白真的会怎么问？

> Skill 是一个很长的 Prompt，还是一个工具？

## 先说人话

在本章中，Skill 指 Agent Skills 风格的可移植能力包：它把完成一类任务的方法写进 `SKILL.md`，还可以带脚本、参考资料和模板，让 Agent 在需要时加载使用。

不同产品也可能把其他功能叫 Skill，因此看到这个词时要确认具体平台定义。

## 一个 Skill 目录里有什么？

```text
my-skill/
├── SKILL.md       # 必需：metadata 与任务说明
├── scripts/       # 可选：可执行脚本
├── references/    # 可选：参考资料
└── assets/        # 可选：模板或素材
```

`SKILL.md` 顶部 metadata 至少描述名称和用途；正文告诉 Agent 何时使用、如何执行、怎样验证结果。

## 为什么不把所有说明一次塞进 Prompt？

Agent 可能拥有许多 Skills。如果每次都加载全部内容，会浪费 Context 并增加干扰。

Agent Skills 使用 Progressive Disclosure（渐进披露）的思路：

```text
先读取简短 metadata
   ↓ 判断当前任务是否相关
相关时再加载 SKILL.md 正文
   ↓
需要时继续读取脚本、参考或素材
```

这样把长期可复用知识保存在文件中，按任务逐步进入 Context。

## Skill 能做什么？

Skill 可以封装：

- 一类任务的标准步骤；
- 组织或项目特有规范；
- 文档模板与示例；
- 质量检查清单；
- 调用现有 Tool 的方法；
- 可重复执行的辅助脚本。

Skill 本身不必提供新的系统权限。它通常教 Agent 怎样使用已有能力。

## Skill 和 Prompt 的区别

Prompt 是提供给模型的输入内容；Skill 是可被发现、按需加载的任务能力包，其中会包含提示说明，但还可能包含脚本、资料和素材。

因此 Skill 不是“任何长 Prompt”的同义词。

## Skill 和 Tool 的区别

Tool 提供可执行能力，例如读文件或调用 API；Skill 说明怎样组合步骤、工具和材料完成一类任务。

```text
Tool：能做什么
Skill：怎样把能力用好并完成任务
```

## Skill 和 MCP 的区别

MCP 是 Host 连接 Server 能力的协议；Skill 是任务知识的打包格式。Skill 可以指导 Agent 使用 MCP Tool，也可以完全不依赖 MCP。

## 安全边界

Skill 可能包含脚本和外部操作说明，因此安装与使用前要检查：

- 来源是否可信；
- 脚本会读写哪些文件或系统；
- 是否要求凭证或网络权限；
- 是否包含隐蔽的破坏性指令；
- 输出是否需要人工确认。

“只是 Markdown 文件”不代表整个 Skill 没有执行风险。

## 常见误区

### 误区 1：安装 Skill 会训练模型参数

不会。Skill 内容在运行时进入 Context 或被工具执行，不等于 Fine-tuning。

### 误区 2：Skill 越多越好

重叠、过时或描述不清的 Skills 会增加选择错误和维护成本。

### 误区 3：Skill 可以绕过 Tool 权限

不能。Skill 中的说明不应突破 Host、沙箱或操作系统授权。

## 你只需要记住

1. 本章的 Skill 是带 `SKILL.md` 的可移植任务能力包。
2. 它通过渐进披露按需加载说明、脚本、资料和素材。
3. Skill 不等于 Prompt、Tool、MCP 或 Agent，但可以组织它们协作。
4. Skill 可能包含可执行脚本，必须审查来源、权限和副作用。

## 继续学习

- [上一篇：MCP 和 Agent 有什么区别](../09-mcp/06-mcp-vs-agent.md)
- [下一篇：Prompt 和 Skill 有什么区别](./02-skill-vs-prompt.md)

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [Agent Skills Overview](https://agentskills.io/home)
- [Anthropic: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
