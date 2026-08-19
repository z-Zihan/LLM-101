# Prompt 和 Skill 有什么区别？

> 所属专题：Skill · 前置：[Skill 到底是什么](./01-Skill到底是什么.md) · 后续：[Tool 和 Skill 有什么区别](./03-Tool和Skill有什么区别.md)
>
> 最后核验：2026-08-19

Prompt 是当前交给模型的输入内容；Skill 是可被发现并按需加载的任务能力包。Skill 会包含提示式说明，却还可以组织脚本、参考资料、模板和验证步骤，因此不能用“更长的 Prompt”概括。

## 一次请求和长期方法

用户写“把这份报告改成简洁周报”，这是当前 Prompt。一个周报 Skill 可以保存适用场景、固定结构、数据核验规则、模板文件和渲染检查脚本，供不同任务重复使用。

```text
Prompt：当前请求 → 直接进入 Context

Skill：先发现 metadata → 任务匹配后加载 SKILL.md
                       → 需要时读取脚本与资料
```

这张图想说明 Skill 文件长期存在，不等于一直占用上下文。读图时注意，最终相关说明仍会成为模型输入，但加载时机和配套结构不同。

Prompt 当然也能保存成模板并复用。分界不只在“是否复用”，还在于 Skill 有可发现 metadata、目录约定、渐进披露和任务级工作流。没有这些结构的一段长文本，通常仍只是 Prompt。

## Skill 为什么仍然需要 Prompt

Agent 要执行 Skill，必须把相关说明放入当前上下文。Skill 负责选择并组织这部分说明，还能让确定性脚本完成机械步骤，让参考资料提供准确规范。

Skill 不能覆盖 System Prompt、安全规则或工具权限。安装 Skill 也不会训练参数；它改变的是运行时上下文和可调用材料。

## 什么时候用哪一个

一次性、边界清楚的任务直接 Prompt 往往足够。方法需要反复使用、包含多份参考或脚本、希望跨项目分发并统一验收时，Skill 更适合。

不要为了形式把三行提示包装成复杂 Skill，也不要把几十页规范每次手工粘贴。选择目标是减少遗漏和上下文噪声。

## 回答常见问题

**Skill 只是一个长 Prompt 吗？** 不是，它是带发现和加载机制的任务包，还可包含可执行与参考文件。

**可复用 Prompt 就是 Skill 吗？** 不自动成立，仍要看是否采用 Skill 的目录、metadata 和工作流约定。

**Skill 会更新模型参数吗？** 不会，它在运行时提供上下文与资源。

## 继续学习

- [Tool 和 Skill 有什么区别](./03-Tool和Skill有什么区别.md)
- [MCP 和 Skill 有什么区别](./04-MCP和Skill有什么区别.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [Agent Skills Overview](https://agentskills.io/home)
