# Prompt 和 Skill 有什么区别？

> Level: `Core` · Path: `Main`
>
> 最后核验：2026-08-18

## 先说人话

Prompt 是当前提供给模型、用于影响输出的输入内容；Skill 是可被发现并按需加载的任务能力包。

Skill 会包含提示说明，但还可以携带脚本、参考资料和模板，所以它不只是“更长的 Prompt”。

## 举个例子

```text
Prompt：请把这份报告改写成简洁的周报。

Skill：
- 什么时候使用周报流程
- 周报固定结构与语气
- 数据核验步骤
- 模板文件
- 渲染和检查脚本
```

Prompt 表达当前请求；Skill 保存可跨任务复用的方法和材料。

## 生命周期有什么不同？

Prompt 通常直接进入当前 Context。Skill 先通过名称和描述被发现，只有与任务相关时才加载正文或其他资源。

```text
当前请求 → Prompt 进入 Context

可用 Skills → 先看 metadata → 选中后加载正文 / 资源
```

Skill 文件长期存在，不代表内容一直占用模型 Context。

## Prompt 能不能复用？

可以。Prompt 模板本身也能保存和复用。但 Agent Skills 风格的 Skill 还规定目录与 `SKILL.md` metadata，并允许组织脚本、参考和素材。

因此“可复用”不是两者的唯一分界，包装结构和加载机制同样重要。

## Skill 里面为什么仍然需要 Prompt？

Agent 最终仍要把相关说明放进模型 Context。Skill 负责在合适时机提供这些说明，并补充完成任务需要的文件和流程。

## 最容易搞混的东西

### Skill ≠ System Prompt

System Prompt 是系统提供给模型的高优先级指令；Skill 是可选择的任务能力包，不能覆盖 Host 的安全与系统规则。

### Prompt 写得长 ≠ Skill

没有可发现 metadata、目录结构和按需加载机制时，它仍可能只是一段 Prompt。

### 安装 Skill ≠ 训练模型

Skill 内容在运行时进入 Context，不会因此更新参数。

## 什么时候只用 Prompt？

一次性、简单、上下文明确的任务通常直接 Prompt 就够了。任务方法需要反复使用、包含参考资料或脚本、并希望跨项目分发时，Skill 更适合。

## 你只需要记住

1. Prompt 是当前模型输入；Skill 是可发现、按需加载的任务能力包。
2. Skill 包含提示说明，也可带脚本、参考资料和素材。
3. 可复用 Prompt 不自动等于 Skill，长 Prompt 也不自动等于 Skill。
4. Skill 不能覆盖 System Prompt、权限或安全规则。

## 继续学习

- [上一篇：Skill 是什么](./01-Skill到底是什么.md)
- [下一篇：Tool 和 Skill 有什么区别](./03-Tool和Skill有什么区别.md)

## 资料与核验

- [Agent Skills Specification](https://agentskills.io/specification)
- [Agent Skills Overview](https://agentskills.io/home)
- [Microsoft Learn: Prompt engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)
