# MCP 和 API 有什么区别？

> 所属专题：MCP · 前置：[MCP 工具、资源和提示是什么](./03-MCP工具资源和提示是什么.md) · 后续：[MCP 和 Function Calling 有什么区别](./05-MCP和Function-Calling有什么区别.md)
>
> 最后核验：2026-08-19

API 是软件接口的广泛概念；MCP 是面向 AI Host 连接外部能力的一套具体开放协议。MCP Server 常在内部调用既有 API，所以两者更多是上下层组合，不是互相淘汰。

## 项目管理 API 怎样被包装成 MCP

项目平台已有 REST API，负责创建任务、查询项目和修改状态。一个 MCP Server 可以把其中少量操作包装成 Tools，并把项目说明暴露为 Resources。

```text
AI Host
  ↓ MCP：发现与请求能力
MCP Server
  ↓ 业务 API：认证并执行操作
项目管理系统
```

这张图想说明 MCP 没有接管真实业务。读图时注意，平台 API 仍决定资源、权限和操作语义；MCP 层负责让 AI Host 以统一方式发现和使用包装后的能力。

## API、OpenAPI 与 MCP 各自描述什么

API 可以是网络接口、代码库函数或操作系统接口。OpenAPI 以机器可读形式描述 HTTP API 的路径、参数和响应。MCP 则约定 Host、Client、Server 角色，以及初始化、能力协商、Tools、Resources、Prompts 和消息交互。

| 维度 | 一般 API | MCP |
|---|---|---|
| 范围 | 软件接口的上位概念 | AI 连接场景的具体协议 |
| 调用方 | 任意软件组件 | Host 内 Client 与 MCP Server |
| 能力发现 | 取决于接口与文档 | 协议定义发现方式 |
| 生命周期 | 各自设计 | 定义初始化与能力协商 |
| 传输 | 可采用多种机制 | 当前规范提供标准传输 |

表格比较的是抽象层次，不表示所有 API 都缺少发现或生命周期。成熟 API 可以自行实现类似能力，只是没有采用 MCP 的统一形状。

## 什么时候直接 API 已经够用

系统只连接一个稳定服务，调用方和接口都由同一团队控制，直接使用 SDK 或 API 往往更简单。增加 MCP 层会带来 Server 实现、生命周期、权限映射和运维成本。

当同一能力要被多个 AI Host 发现使用，或一个 Host 要连接许多来源时，统一协议的复用价值更明显。是否使用 MCP，应从集成数量、生态兼容、权限和维护成本判断。

## 版本演进：谁为兼容负责

长期运行时，两层的兼容责任同样分开。

REST API 靠版本号和废弃公告约束调用方：平台升级接口，得等每个调用方自己跟进，改不动就一直维护旧版本。MCP 把一部分兼容问题前移到了握手时刻——Host 和 Server 在连接时协商协议版本、交换能力清单，不匹配就在建立连接时失败，而不是运行到一半才炸。这让“两端版本不一致”变成启动期可见的错误，代价是升级时任何一端单方面变更都可能让原本正常的连接直接建立不起来。

底下业务 API 变更时的传导路径也值得注意：接口路径改了、字段改名了，MCP Server 必须先适配，再把包装后的能力原样提供给 Host——理想情况下 Host 与模型毫无感知；适配漏了，错误则表现为 Tool 结果异常。这就是上一节说“API 层负责真实语义”的另一半：连接层再统一，也代替不了下游接口自己的版本纪律。

## 两层安全都不能省

Host/MCP 层决定是否向模型提供工具、用户是否同意当前操作；后端 API 仍要验证身份、资源权限、业务规则和幂等。Host 已确认不能成为后端跳过授权的理由。

反过来，API 有鉴权也不等于模型操作获得用户意图授权。模型可能选错工具或参数，破坏性动作仍需在 Host 侧确认和限制。

## 回答真实问题

**MCP 是一种 API 吗？** 广义上它定义程序接口；教学上更清楚的说法是 API 是上位概念，MCP 是具体协议。

**OpenAPI 已能描述接口，MCP 多了什么？** 它额外约定 AI Host 的连接角色、生命周期、能力协商，以及 Tools、Resources、Prompts 的发现和交互。

**有 MCP 以后还需要业务 API 吗？** 很多 MCP Server 正是建立在 API 上，后端接口仍负责真实业务。

**任何 API 都能自动成为 MCP Server 吗？** 不能，必须实现 MCP 消息、生命周期和能力接口，并重新设计合适的权限边界。

## 从这里继续

- [MCP 和 Function Calling 有什么区别](./05-MCP和Function-Calling有什么区别.md)
- [MCP 和 Agent 有什么区别](./06-MCP和Agent有什么区别.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Model Context Protocol Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28)
- [MCP Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
