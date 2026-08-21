# Cursor 产品案例：AI 编辑器和 Coding Agent 怎样叠在一起？

> 最后核验：2026-08-21 · 易变产品案例
>
> 本页依据 Cursor 官方文档与官方社区核验，只保留稳定职责。模型列表、价格、上下文长度、按钮位置和版本号可能变化，不作为长期知识。

Cursor 把代码编辑器与 Coding Agent 放在同一产品里。用户可以一边浏览、选择和编辑代码，一边让 Agent 搜索仓库、修改文件、运行终端命令、查网页或调用 MCP。编辑器提供可见上下文，但并不意味着 Agent 只会访问当前屏幕上的文件。

官方社区有用户报告：即使项目规则要求留在仓库内，Agent 仍尝试搜索用户目录或其他仓库。这个案例不能单独证明所有版本都存在同一行为，却能说明一个长期边界：自然语言 Rule 是指导，文件权限、忽略规则、沙箱和操作系统授权才是执行约束。

## 编辑器表面下的六层

| 观察角度 | Cursor 中的职责 | 常见误解 |
|---|---|---|
| 交互入口 | 编辑器 Agent、Agents Window、CLI 或托管任务等表面 | “在编辑器里”就一定只做局部补全 |
| 项目上下文 | 打开的工作区、代码搜索、Rules、忽略文件、对话与工具结果 | 当前标签页等于全部上下文 |
| 工具 | 读写文件、搜索、终端、网页、MCP 与 Review | 编辑建议天然没有副作用 |
| Agent Loop | 理解代码、计划、修改、运行检查、审查差异 | Agent 模式只比补全多写几行代码 |
| 权限 | Run Mode、审批、沙箱、MCP allowlist 和系统权限 | Rule 可以充当强制访问控制 |
| 验证 | Source Control、Agent Review、测试和 Worktree 差异 | 自动 Review 能证明没有缺陷 |

## 编辑器上下文不等于权限边界

当前文件、选区和打开标签页可以帮助 Agent 定位任务；仓库搜索与索引让它发现未打开的定义和调用；Rules 则持续提供项目约定。这三类信息都属于上下文选择，不直接决定进程能读取哪个路径。

`.cursorignore` 可用于阻止 Agent 访问特定文件，操作系统权限和沙箱限制命令的真实范围。项目 Rule 里写“不要离开仓库”仍然有价值，因为它能影响决策；但 Prompt 可能被忽略、误解或被其他内容干扰，不能用它保护密钥或私人目录。

真正敏感的文件还应通过最小账户权限、独立工作区、系统隐私控制和不把密钥写入仓库来保护。对不受信任的仓库，要先审查其中的 Rules、脚本、依赖和文档，避免间接 Prompt Injection 诱导 Agent 读取或发送数据。

## Agent 怎样产生实际改动

官方文档列出的 Agent 工具包括文件、终端、搜索、网页和 MCP。文件修改会写入工作区，终端命令则启动真实进程；如果开发服务器自动重载，尚未审查的文件改动甚至可能立即触发代码运行。

因此，版本控制是恢复机制的一部分，不只是最后提交。复杂或并行任务可以在 Git Worktree 中隔离，让每项任务拥有独立检出和依赖状态；完成后再审查 diff、提交或合并。Worktree 隔离文件冲突，却不会自动隔离共享数据库、云账户或外部服务。

Agent Review 可以对本地差异做额外检查，但它仍是模型和规则驱动的审查层。关键逻辑、迁移、权限和安全改动还需要测试、人工检查和必要的专业 Review。

## Run Mode、审批和沙箱各管什么

Cursor 的 Run Mode 决定哪些工具请求自动运行、哪些需要批准；沙箱限制受支持的终端进程能访问的路径和网络；MCP 连接与工具可有单独批准和 allowlist；操作系统与团队策略继续施加外层限制。

官方安全文档明确把自动分类器称为 best-effort guardrail，而不是硬安全边界。分类器可能误放或误拦。完全自动运行模式减少了打断，也同时取消了重要人工门禁，只适合已经有可靠外部隔离和恢复手段的环境。

默认行为也可能随版本变化。维护这类产品页时，应该写“截至核验日官方文档怎样描述”，而不是把某个菜单或默认开关当作永久概念。

## 越界搜索报告应该怎样处理

先不要只问 Agent “你是不是看了别处”，因为自然语言自述不是可靠审计。检查操作系统隐私提示、工具调用记录、终端命令、实际文件访问日志和工作区配置，确认是否真的越界。

若证据成立，先停止相关任务，收紧系统权限与忽略范围，检查是否有数据离开本机，再用最小示例复现并向产品方报告。项目 Rule 可以继续保留为意图说明，但修复不能只靠增加一句更强硬的 Prompt。

## 回答真实问题

**我写了“只能访问当前仓库”的 Rule，为什么还不能当安全边界？** Rule 进入模型上下文，影响选择；它不是操作系统访问控制。必须同时使用忽略规则、沙箱、账户权限和审计证据。

**Cursor 是补全工具还是 Agent？** 产品同时包含编辑辅助与多步 Agent 工作流。判断当前风险要看它是否能写文件、运行命令和连接外部工具，而不是只看产品名称。

**Worktree 能解决所有隔离问题吗？** 不能。它隔离 Git 检出与文件改动，不自动隔离网络、凭据、数据库和部署环境。

## 从这里继续

- 理解共同底座：[Coding Agent 是什么](./04-Coding-Agent是什么.md)
- 区分辅助与自主执行：[从 AI Embedded、Copilot 到 Agent](../07-Agent/07-从AI-Embedded和Copilot到Agent.md)
- 理解工具风险：[代码执行和 Computer Use 有什么风险](../06-工具与Function-Calling/05-代码执行和Computer-Use有什么风险.md)
- 对照其他产品：[Codex 产品案例](./10-Codex产品案例.md) · [Claude Code 产品案例](./11-Claude-Code产品案例.md)
- 返回全局：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 官方资料与问题来源

- [Cursor 官方文档](https://cursor.com/docs)
- [Cursor Agent Overview](https://cursor.com/docs/agent/overview)
- [Cursor Agent Security](https://cursor.com/docs/agent/security)
- [Cursor Run Modes](https://cursor.com/docs/agent/security/run-modes)
- [Cursor Worktrees](https://cursor.com/docs/configuration/worktrees)
- [真实问题来源：Cursor breaks boundaries such as searching the disk or a different repository](https://forum.cursor.com/t/cursor-breaks-boundaries-such-as-searching-the-disk-or-a-different-repository/167851)
