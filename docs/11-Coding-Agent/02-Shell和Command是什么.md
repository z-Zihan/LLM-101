# Shell 和 Command 是什么？

> 你现在的位置：[代码执行](../06-工具与Function-Calling/05-代码执行和Computer-Use有什么风险.md) → **Shell 与 Command** → [Coding Agent](./04-Coding-Agent是什么.md)
>
> 所属专题：Coding Agent 基础 · 本文是 Optional 扩展阅读

有位 Linux 新手说，Shell、Terminal、Console 和 Command Line 几个词一直让他困惑。Coding Agent 又经常显示“正在运行 Shell 命令”，于是很多人会进一步误解：终端是不是一个黑色窗口？模型输出一行命令以后，事情是否已经发生？

可以先把角色拆开：终端负责人与文本程序交互，Shell 负责读取并解释命令语言，Command 是要执行的具体指令，操作系统则创建真实进程。它们常一起出现，不代表是同一个东西。

## 输入 `python test.py` 后发生了什么

你在终端里输入：

```sh
python test.py
```

终端把按键交给当前 Shell。Shell 按自己的语法把这一行解析成命令名 `python` 和参数 `test.py`，根据环境变量 `PATH` 查找可执行程序，然后请求操作系统启动进程。Python 再读取脚本并运行，最后返回退出状态；Shell 把程序输出显示回终端。

```text
终端：收集输入、显示输出
  ↓
Shell：解析语法、展开变量、连接管道、查找命令
  ↓
操作系统：启动进程并分配权限与资源
  ↓
程序：执行工作，写出标准输出 / 错误，返回退出码
```

这张图要拆开“文字”和“执行”。命令字符串只是输入；Shell 解析后，操作系统中的进程才产生真实副作用。

## Terminal、Console、CLI 分别指什么

历史上的终端是连接大型计算机的实体设备。今天常说的 Terminal 多指终端模拟器，例如 macOS Terminal、Windows Terminal 或 IDE 内置终端：它们提供窗口、字符显示、键盘输入和会话连接。

Console 原本更强调直接连接设备的系统控制台，现代用法也可能指应用的日志或开发者控制台。Command-line Interface（CLI）是“通过文本命令交互”的界面类型；它可以运行在终端中，也可以由脚本、CI 或另一个程序非交互调用。

Shell 是命令解释器和脚本语言运行环境。Bash、Zsh、Fish、PowerShell 都是 Shell，但语法和行为不完全相同。`ls`、`git`、`python` 通常是外部程序；`cd` 往往是 Shell 内建命令，因为改变工作目录必须影响当前 Shell 进程。

## Command 不只是“程序名”

一行 Shell 文字可以包含变量展开、通配符、重定向、管道、条件和子命令：

```sh
rg "error" logs/ | head -20 > summary.txt
```

Shell 会先理解引号和通配规则，启动 `rg` 与 `head` 两个进程，把前者的标准输出连接到后者的标准输入，再把结果重定向到文件。这里既有两个程序，也有 Shell 提供的连接语法。

这解释了为什么“把参数列表直接交给程序”和“把一整段字符串交给 Shell”风险不同。后者可能把用户内容中的 `;`、`|`、`$()` 等解释成额外语法，形成命令注入。能不用 Shell 时，程序应使用参数数组调用明确的可执行文件；必须使用时，严格限制输入、目录和环境，而不是自己拼接字符串。

## 同一个命令为什么在 Agent 里结果不同

命令依赖当前工作目录、环境变量、Shell 类型、用户身份、文件状态、网络和已安装程序。你在自己的终端运行成功，不代表 Agent 的沙箱里也成功；Agent 可能位于另一个目录、使用非交互 Shell、没有加载个人配置，或没有访问相同密钥。

因此，任务日志应该记录工作目录、关键环境、实际参数、退出码和必要输出。不要只保存模型原本想运行的那行字，因为宿主可能拒绝、修改或超时终止了它。

标准输出是程序正常写出的文本，标准错误用于诊断；两者都不等于成败。许多 CLI 用退出码 `0` 表示按约定成功，非零表示某类失败，但具体含义由程序定义。即使测试命令退出 `0`，也只能证明被选中的测试通过，不能证明所有业务行为正确。

## 权限在哪里生效

Shell 本身不会让 Agent 自动变成管理员。进程继承执行身份及其文件、网络和系统权限；`sudo`、容器挂载、云凭证和远程 SSH 会改变边界。模型能写出 `sudo rm ...`，不代表宿主应允许执行。

安全的 Coding Agent 会区分读取、编辑、运行测试、安装依赖、访问网络、提交 Git 和发布外部系统。破坏性或外部副作用命令需要明确范围与确认；密钥不应出现在命令行、Prompt 或长期日志中。超时、进程数、CPU、内存和输出量也要限制，避免命令失控拖垮环境。

管道还会造成隐藏的数据流。读取私有文件的命令与网络上传命令各自可能合法，组合后却能外泄。策略不能只检查命令名，还要关注参数、输入来源、输出目标和前后步骤。

## Agent 为什么离不开 Shell，又不能只靠 Shell

软件项目已有大量成熟 CLI：编译器、测试框架、包管理器、Git、搜索和格式化工具。Shell 能把这些能力接入 Agent，不需要为每个项目重新设计图形接口。命令输出又会成为下一轮判断的证据。

但自由 Shell 是宽而危险的接口。结构化工具能更清楚地限制参数和返回状态，例如专用的“运行测试文件”工具比任意命令更容易授权。成熟系统常组合两者：高频操作提供窄工具，确实需要开放命令时在沙箱内运行并加强确认与审计。

失败恢复要面对真实进程状态。超时不一定代表进程没有写文件，取消也不保证所有子进程结束。Agent 应在重试前检查 Git Diff、文件和业务状态；不能因为没有看到输出就重复执行带副作用的命令。

## 把概念重新对齐

**Terminal 和 Shell 是一个东西吗？** 不是。终端提供输入输出界面，Shell 解释命令语言；一个终端可运行不同 Shell，一个 Shell 也可被脚本或远程会话调用。

**Command 就是一段文字吗？** 文字是命令输入。Shell 解析后可能启动一个或多个真实进程，重定向文件并连接数据流。

**模型生成命令就等于执行了吗？** 不等于。宿主仍要校验、授权、确认和启动进程，并把真实结果返回。

**为什么脚本里和手动终端里结果不一样？** 常见原因是 Shell、交互模式、工作目录、环境变量、权限和文件状态不同。

## 下一步

- 看运行环境风险：[代码执行和 Computer Use 有什么风险](../06-工具与Function-Calling/05-代码执行和Computer-Use有什么风险.md)
- 看项目级工具循环：[Coding Agent 是什么](./04-Coding-Agent是什么.md)
- 看当前仓库信息：[项目上下文是什么](./08-项目上下文是什么.md)
- 返回全局：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [POSIX：Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)
- [GNU Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)
- [The Open Group：Shell and Utilities](https://pubs.opengroup.org/onlinepubs/9799919799/idx/shell.html)
- [OWASP：OS Command Injection Defense Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- 真实问题来源：[Super User：Shell、Terminal、Console 和 Command Line 有什么区别](https://superuser.com/questions/795950/what-is-the-differences-of-these-conceptsshell-terminal-console-and-command-l)
