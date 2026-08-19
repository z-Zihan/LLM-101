# MCP 和 Skill 有什么区别？

> 所属专题：Skill · 前置：[Tool 和 Skill 有什么区别](./03-Tool和Skill有什么区别.md) · 后续：[Agent 和 Skill 有什么区别](./05-Agent和Skill有什么区别.md)
>
> 最后核验：2026-08-19

MCP 是 Host 连接外部能力的协议；Skill 是保存任务方法、脚本与资料的能力包。MCP 解决“怎样发现并连上”，Skill 解决“怎样把能力用好并完成这类任务”。

## 项目管理场景怎样组合

MCP Server 可以提供查询项目、创建任务和修改状态的 Tools。项目管理 Skill 则规定怎样拆分目标、使用哪些字段、何时先查重、创建后怎样验证。

```text
Skill：任务方法与验收
  ↓ 指导 Agent
MCP Client ↔ MCP Server：发现并调用外部能力
  ↓
后端项目管理系统
```

这张图想说明 Skill 不负责建立协议连接，MCP 也不自动提供组织工作法。读图时注意两者可以独立存在：Skill 可使用内置 Tool，MCP 应用也可不加载 Skill。

## MCP Prompt 为什么仍不是 Skill

MCP Prompt 是 Server 暴露的可复用消息模板；Skill 是带 metadata 和完整说明的目录包，还可能包含脚本、参考与素材。Skill 可以引用 MCP Prompt，平台也能编写转换层，但格式、发现方式和生命周期不同。

MCP Client/Server 需要处理协议版本和能力协商；Skill 维护者要更新业务规则、脚本和资料。协议兼容不保证 Skill 内容仍正确，Skill 更新也不会自动升级 Server。

## 组合时要审查两套边界

检查 Skill 是否要求危险操作、脚本会访问什么；同时检查 Server 来源、凭证权限、Tool 参数和用户确认。标准格式提高互操作性，不建立信任。

有 Skill 不会自动安装 MCP Server，Server 的 Tool 描述也不等于完整 Skill。两者不是父子关系，只是可以在 Agent 运行时协作的不同层。

## 回答关键问题

**MCP 和 Skill 哪个负责连接？** MCP。

**哪个负责多步任务方法？** Skill。

**MCP Prompt 是 Skill 吗？** 不是，它只是协议暴露的一类提示模板。

**能只用一个吗？** 可以；是否组合取决于任务和现有工具。

## 继续学习

- [Agent 和 Skill 有什么区别](./05-Agent和Skill有什么区别.md)
- [MCP 到底是什么](../09-MCP/01-MCP到底是什么.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/2026-07-28)
