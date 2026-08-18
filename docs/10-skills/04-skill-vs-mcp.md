# MCP 和 Skill 有什么区别？

> Level: `Core` · Path: `Main`
>
> 最后核验：2026-08-18

## 先说人话

MCP 是 AI 应用连接外部能力的协议；Skill 是保存任务方法、脚本和资料的能力包。

MCP 解决“怎样连上”，Skill 解决“怎样完成这类任务”。

## 举个例子

```text
MCP Server：提供查询项目、创建任务的 Tools

项目管理 Skill：
- 怎样把用户目标拆成任务
- 使用哪些字段和命名规范
- 何时先查询避免重复
- 创建后怎样验证
```

Skill 可以指导 Agent 使用 MCP Tools；MCP 不会自动提供这套工作方法。

## 核心区别

| 维度 | MCP | Skill |
|---|---|---|
| 类型 | Client / Server 通信协议 | 文件形式的任务能力包 |
| 主要内容 | 消息、能力、生命周期、Transport | 说明、脚本、参考、素材 |
| 主要用途 | 发现和调用外部能力 | 按需提供任务知识与流程 |
| 是否需要 Server | 是，MCP 连接需要 Server | 不一定 |
| 是否自动执行 | Server 可执行 Tool | 由 Agent / Runtime 读取或执行内容 |

## 能不能只用其中一个？

可以：

- Skill 可指导 Agent 使用内置 Tool，不需要 MCP；
- MCP 应用可直接调用 Tool，不需要 Skill；
- 二者组合时，Skill 提供方法，MCP 提供连接。

## MCP Prompt 是不是 Skill？

不是。MCP Prompt 是 Server 暴露的可复用提示模板；Agent Skill 是包含 metadata、说明和可选资源的目录包。

一个 Skill 可以引用 MCP Prompt，但二者格式、发现方式与生命周期不同。

## 谁负责版本？

MCP Client / Server 要处理协议版本和能力协商；Skill 维护者要管理任务说明、脚本与资料版本。协议兼容不保证 Skill 仍符合业务规则，Skill 更新也不自动升级 Server。

## 安全边界

组合时要同时审查：

- Skill 是否要求危险或越权操作；
- MCP Server 来源与权限；
- Tool 调用参数和用户确认；
- 脚本、返回内容和凭证处理。

标准格式只能提高互操作性，不能自动建立信任。

## 常见误区

### 误区 1：有 Skill 就会自动安装 MCP Server

除非具体平台明确实现这项行为，否则 Skill 只是文件包，不能自行建立协议连接。

### 误区 2：MCP Server 会告诉 Agent 完整业务流程

Server 的 Tool 描述帮助调用能力，不等于完整组织规范和多步方法。

### 误区 3：MCP 和 Skill 是父子关系

不是。它们位于不同层，可以独立存在或组合。

## 你只需要记住

1. MCP 是连接协议，Skill 是任务能力包。
2. MCP 负责发现和调用外部能力，Skill 负责提供做事方法与材料。
3. MCP Prompt 不是 Skill，Tool Description 也不是完整 Skill。
4. 二者组合不自动可信，Server、脚本、权限和调用都要审查。

## 继续学习

- [上一篇：Tool 和 Skill 有什么区别](./03-skill-vs-tool.md)
- 下一篇（待完成）：Agent 和 Skill 有什么区别？

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/2026-07-28)
