# 从 AI Embedded、Copilot 到 Agent

> 你现在的位置：[AI 工具](../06-工具与Function-Calling/02-AI工具到底是什么.md) → **AI Embedded / Copilot / Agent** → [Agent 到底是什么](./01-Agent到底是什么.md)
>
> 所属专题：Agent 产品形态 · 本文是 Optional 扩展阅读

有开发者看到 Visual Studio 的 Agent Mode 默认绑定 GitHub Copilot，于是问：能不能换成另一个模型或 Agent？这个问题把产品名、交互模式、模型和 Agent 运行时叠在了一起。它们经常出现在同一个界面，却不是同一层东西。

AI Embedded、Copilot 和 Agent 更适合看成一条“系统能主动完成多少工作”的连续谱，而不是三个有统一认证标准的产品类别。真正要比较的是上下文、工具、循环、权限、验证和用户控制，而不是按钮上写了什么营销名称。

## 用写邮件看三种协作方式

一个邮箱产品可以把 AI 放在不同位置。

AI Embedded 是嵌入式 AI：用户选中一句话，点击“改得更礼貌”，系统就处理这段明确输入并返回结果。任务范围小，开始和结束都由用户直接控制。

Copilot 常译作“副驾驶”或“助手”。用户写邮件时，它根据当前草稿补全后文，或者在侧边栏回答“这封信有没有遗漏时间”；用户仍然持续掌舵，逐步接受、修改或拒绝建议。

Agent 则接收“找出本周尚未回复的重要客户，并为每人准备一封草稿”这样的目标。它需要搜索邮件、读取多个线程、维护已处理列表、调用草稿工具，并根据结果决定下一步。系统开始出现多轮状态和行动循环。

```text
嵌入式 AI        Copilot                    Agent
一次局部功能  →  持续给建议、由人逐步采纳  →  围绕目标多步观察与行动

上下文范围、工具数量、自主持续时间和副作用通常逐步增加
```

这张图表达的是产品控制方式，不是能力排名。简单补全在边界清楚的任务上可能比 Agent 更快、更可靠；一个名为“Copilot”的产品也可能在某个模式里运行完整 Agent Loop。

## Copilot 不是一种模型

Copilot 通常是产品或功能定位。它背后可能调用不同模型，组合搜索、文件、代码补全和聊天工具，并在不同界面提供不同权限。同一个模型既可以被放进只给建议的补全功能，也可以被 Agent 运行时反复调用。

“换一个模型”只替换生成与判断的一层。Agent Mode 还需要把编辑器上下文、文件工具、终端、计划、确认界面、工具结果和停止条件接到模型上。因此，Visual Studio 或 VS Code 里能否切换提供方，是具体产品和扩展的能力问题，不能从“模型支持 API”直接推出。

同样，“用了 Copilot”不能说明它只是自动补全。判断当前模式时，可以依次问：

- 它只处理我明确选中的内容，还是会自己寻找上下文？
- 它只给建议，还是可以修改文件、运行命令和提交表单？
- 一次响应就结束，还是根据工具结果继续多轮行动？
- 谁判断任务完成，谁检查结果，谁承担最终副作用？

答案比产品名更能预测体验与风险。

## 从建议到行动，中间不是一道开关

现实产品可以停在连续谱的任意位置。代码补全会自动读取光标附近上下文，但不自行运行测试；聊天助手可能读取整个仓库，却只输出 Patch 建议；编辑模式能修改多个文件，但每一组变化等待用户接受；Agent Mode 可以编辑、运行测试并根据失败继续修复。

因此“Copilot 和 Agent 有什么区别”没有脱离模式的唯一答案。教学上可把 Copilot 理解为强调人持续掌舵的协作定位，把 Agent 理解为具有目标、状态、工具和循环的系统结构。当某个 Copilot 模式具备后者，它在结构上就是 Agent，只是产品仍保留 Copilot 名称。

自主性也不等于一次授权所有操作。一个 Agent 可以自动完成低风险搜索和草稿，在发送、付款、删除、发布前停下来确认；另一个产品可能只有一次点击，却会立即产生不可逆副作用。风险取决于真实权限和行动，不取决于对话轮数。

## Coding Copilot 为什么容易跨过边界

编程场景里，局部补全到 Coding Agent 的变化很直观：

```text
续写当前行
  ↓
根据当前文件回答
  ↓
跨文件提出修改
  ↓
直接编辑文件
  ↓
运行 Shell、测试和 Git
  ↓
根据失败继续修改并验证
```

前几步更像建议，后几步已经形成 [Coding Agent](../11-Coding-Agent/04-Coding-Agent是什么.md) 的工具循环。IDE 还是终端只是交互表面；核心差异在于系统能取得什么项目上下文、执行哪些工具、怎样验证和恢复。

公开 Issue 中有人要求 Copilot 永远不要读写 `.env` 文件。这不是“模型是否聪明”的问题，而是项目上下文和工具权限的边界。`.env` 可能包含密钥；只靠 Prompt 提醒模型不要访问，并不能阻止路径误选或恶意内容诱导。宿主应支持忽略规则、敏感文件策略、最小读取范围和写入拦截。

## 选择产品形态时从责任出发

高频、边界稳定、结果容易当场看懂的任务，适合嵌入式 AI：翻译选中文本、生成标题、解释一个错误。用户需要边做边判断的任务，适合 Copilot 式协作：写代码、编辑文章、分析表格。步骤会因环境结果变化、又能通过工具验证的任务，才值得使用 Agent。

Agent 不是默认终点。它会增加工具选择错误、上下文成本、等待时间和副作用。若固定工作流已经能可靠完成，就不必为了“更自主”改成开放循环。

产品评估可以记录四类证据：模型生成了什么、宿主允许了什么、工具实际做了什么、最终结果怎样验证。出现失败时，用户应能查看 Diff、撤销变更、取消后续步骤并接管任务。只有一句“完成了”不构成交付证明。

## 回答真实问题

**Copilot 是模型、产品还是 Agent？** 通常是产品或协作定位。它可以调用不同模型；其中某些模式只给建议，某些模式具备完整 Agent 结构。

**Agent Mode 能不能换另一个模型？** 取决于具体 IDE、扩展和版本是否开放模型提供方与运行时接口。模型 API 可用不代表产品已接好上下文、工具和权限。

**AI Embedded、Copilot、Agent 谁更强？** 不能只按名称排序。应比较任务适配度、上下文、工具、验证成本和用户控制；局部功能常常更稳定。

**为什么 Agent 不该读写 `.env`？** 因为其中可能有密钥和环境配置。边界应由文件访问策略强制执行，不能只依赖模型自觉。

## 接着看系统结构

- Agent 的严格结构：[Agent 到底是什么](./01-Agent到底是什么.md)
- 循环怎样持续：[Agent Loop 是什么](./03-Agent-Loop是什么.md)
- 编程场景：[AI Coding 是什么](../11-Coding-Agent/01-AI-Coding是什么.md) · [Coding Agent 是什么](../11-Coding-Agent/04-Coding-Agent是什么.md)
- 工具权限：[代码执行和 Computer Use 有什么风险](../06-工具与Function-Calling/05-代码执行和Computer-Use有什么风险.md)
- 返回全局：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

> 最后核验：2026-08-21。Copilot 与 Agent Mode 是易变产品术语，支持的模型、工具和确认方式必须以所用版本的官方文档为准。

- [Anthropic：Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [OpenAI：A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [GitHub Docs：Asking GitHub Copilot questions in your IDE](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)
- [GitHub Docs：About GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
