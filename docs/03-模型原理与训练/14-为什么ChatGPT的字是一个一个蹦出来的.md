# 为什么 ChatGPT 的字是一个一个蹦出来的？

> 课程导航：[上一篇：训练和推理有什么区别](./18-训练和推理有什么区别.md) · 第 18 / 32 篇 · [下一篇：泛化是什么](../04-模型能力/01-泛化是什么.md)

聊天界面里的文字像打字一样不断出现，很容易让人以为模型已经在后台写好整段，只是故意做成动画。实际情况更接近：对于主流自回归 LLM，未来内容还不存在，模型每次先为下一个 Token 计算候选分数，选择一项，把它接回当前序列，再继续下一步。

标题里的“字”只是用户看到的效果，严格说生成单位是 Token。一个 Token 可能对应一个汉字、半个词、多个字符、标点或不可直接显示的字节片段；服务也可能把几个 Token 合并后再流式传给界面。因此“一个一个蹦”不保证视觉上每次恰好出现一个字。

## 把“中国的首都是”完整走一遍

用户输入：

```text
中国的首都是
```

一次最小生成流程可以先看成：

```text
Prompt
  ↓ Tokenizer 编码
Token IDs
  ↓ Embedding + Transformer Prefill
最后输入位置的 Hidden Representation + 各层 KV Cache
  ↓ 输出投影
整个 Vocabulary 的 Logits
  ↓ Greedy 或 Sampling
选出 Token：“北京”
  ↓ 追加到当前 Token 序列
再次执行 Decode，选出下一 Token
  ↓
直到 EOS、长度上限或其他停止条件
```

模型不必先把 Token 解码成“中国”再送回神经网络。运行时主要处理 ID、向量和缓存；文字解码是为了把结果交给用户。这里把候选写成“北京”只是方便阅读，真实 Tokenizer 可能把它切成一个或多个 Token。

## Prompt 进入后，Prefill 先把已知输入读完

Prompt 不只可能包含用户这一句。聊天产品还可能把系统指令、历史对话、工具结果或检索资料按既定格式拼入请求。Tokenizer 用模型配套的词表和规则把整段文本编码成 Token ID，Embedding Lookup 再把每个 ID 变成初始向量。

接下来，多层 [Transformer](./03-Transformer到底是什么.md) 处理这些已知输入位置。这一段常叫 Prefill：它为 Prompt 中各位置计算表示，并在每层建立后续生成会用到的 Key / Value 状态。虽然因果遮罩让某个位置不能读取未来位置，但整段输入已经存在，GPU 可以用矩阵运算并行处理许多位置，不需要像生成那样等待某个未知 Token 先被选出来。

Prefill 结束后，第一步生成主要使用最后一个有效输入位置的 Hidden Representation，经过输出投影得到整个词表的 Logits。模型前向计算通常也产生其他输入位置的结果，但生成第一项时关心的是“完整 Prompt 之后应该接什么”。

```text
已知输入 Token 1…N
  ↓ 可以并行完成大量层内计算
Prefill
  ├─ 最后位置表示 → 第一个输出 Token 的 Logits
  └─ 各层历史 K/V → 留给后续 Decode
```

Prefill 是推理，不是训练。它使用已经加载的固定参数，不计算训练 Loss，也不通过反向传播修改模型。

## Logits 只是候选分数，接下来还要决定“怎么选”

假设词表只有几个候选，模型给出以下简化 Logits：

```text
北京   8.2
上海   6.7
中国   5.4
。     3.1
```

Logit 可以为负，也不要求加起来等于 1。Softmax 能把整组相对分数转成概率分布；不过运行时可以把温度缩放、过滤和 Softmax 融合实现，不一定真的在内存里保存一张完整概率表。

得到候选分数后，常见选择方式有两大类：

- Greedy Decoding（贪心解码）：每一步直接选分数最高的候选；
- Sampling（采样）：按处理后的概率随机抽取，给较低概率但仍合理的候选机会。

贪心不是“模型更理性”，采样也不是“模型在自由思考”。它们只是把同一组候选分数变成下一个 Token 的不同策略。Beam Search 等方法还会同时维护多条候选序列，但开放式聊天常见的是贪心或采样及其变体。

## Temperature、Top-k、Top-p 各自在改什么

Temperature 常在 Softmax 前缩放 Logits。温度较低时，分布通常更集中在高分候选；温度较高时，候选之间的概率更平。它不重新训练参数，不向模型写入新知识，也不会自动纠正事实错误。

```text
Probability(token_i) = softmax(logit_i / T)
```

这个公式只适用于 `T > 0`。产品写 `temperature = 0` 时，常把它解释为贪心或接近贪心的特殊分支，而不是实际执行除以 0；精确行为要看 API 或推理引擎文档。

Top-k 只保留分数最高的 k 个候选，再在其中归一化和采样。Top-p（Nucleus Sampling）则先按概率从高到低排序，保留累计概率达到阈值 p 的最小候选集合：分布很集中时集合可能很小，分布平坦时会纳入更多项。

```text
Logits
  ↓ Temperature 调整分布尖锐程度
候选概率
  ↓ Top-k：固定保留 k 个候选
  或 Top-p：保留累计概率达到 p 的动态集合
  ↓
从保留集合采样一个 Token
```

不同运行时可能改变处理顺序、同时启用多种过滤、设置最小概率，或加入重复惩罚和禁止词规则。因此不能只看一个 Temperature 数字就断言输出必然“更有创造力”；要连同完整生成配置、模型版本和随机种子一起看。

相同 Prompt 有时得到不同答案，最直接的原因是采样抽中了不同 Token。一旦早期一步不同，后面所有条件概率都基于不同前缀，文本会逐渐分叉。即使采用贪心，不同硬件、精度、并行归约或非确定性算子也可能在候选分数极接近时造成差异，所以跨平台不应承诺永久逐 Token 一致。

## 选出一个 Token 后，Decode 循环才真正开始

假设第一步选出“北京”。运行时把这个 Token ID 追加到当前序列，计算它在各层的新表示，再从最新位置产生下一组 Logits。第二步必须知道第一步究竟选了什么；第三步又依赖前两步，因此输出时间轴上存在无法消除的串行依赖。

```text
当前序列：“中国的首都是”
  ↓ 选择
Token 1：“北京”
  ↓ 追加到序列并更新缓存
当前序列：“中国的首都是北京”
  ↓ 选择
Token 2：“。”
  ↓ 追加，再继续……
```

这段逐 Token 生成阶段叫 Decode。这里的 Decode 不只是“把 ID 翻译回文字”，而是服务领域里从已有前缀反复计算和选择新 Token 的阶段；Tokenizer 的文本解码只是其中一个输出步骤。

训练时整条正确序列已知，配合 Causal Mask 可以并行计算许多位置的 Loss；推理时正确未来不存在，不能把尚未选择的 Token 提前当输入。这就是“训练能并行算很多目标，但生成仍需逐步进行”的根本差别。

## KV Cache 避免每一步重算整个历史

如果生成第 100 个 Token 时每一层都重新计算前 99 个位置的全部 Key 和 Value，会浪费大量重复工作。KV Cache 把历史位置在各 Transformer 层中已经得到的 K/V 状态保存下来。新一步只需为新 Token 计算新的 Q/K/V：新 Query 读取历史 K/V，再把新 K/V 追加进缓存。

```text
历史 Token 的各层 K/V ──保存在 KV Cache──┐
                                           ├─ 新 Query 做 Attention
新 Token ──计算本步 Q/K/V──────────────────┘
                       ↓
                  追加新的 K/V
```

标准因果 Attention 下一步需要用新位置的 Query 去匹配所有历史 Key，并汇总历史 Value；过去位置的 Query 已经完成过自己的读取任务，通常不需要为未来位置保存。这就是常见问题“为什么缓存 K/V，却不缓存所有 Q”的第一层答案。

KV Cache 不保存整句自然语言，也不是跨会话 Memory，更不会修改模型参数。它是当前推理请求的中间状态。缓存通常随层数、KV Head 数、Head Dimension、已缓存 Token 数、数据精度和 Batch 近似线性增长；使用 MQA / GQA、量化或分页管理会改变实际占用。不能脱离架构给出“每个 Token 固定占多少显存”的通用数字。

缓存让历史 K/V 不必重复计算，却不能突破自回归依赖：下一 Token 仍要等当前 Token 被选出。它也不是免费加速；长上下文和高并发会让 KV Cache 吃掉大量显存，还会增加每步需要读取的历史状态。

## 模型什么时候停下来

常见停止条件不只一个：

- 模型选出 EOS（End of Sequence）等结束 Token；
- 已生成数量达到 `max_output_tokens` 一类服务上限；
- 输入加输出触及模型或服务允许的 Context Window；
- 命中调用方配置的 Stop Sequence；
- 请求被用户取消、超时，或服务因安全和资源策略中止。

EOS 也是词表中的特殊 Token，模型可以像预测其他 Token 一样给它分数。它出现表示模型选择结束，但服务不一定只靠 EOS：如果模型迟迟不选 EOS，硬长度上限仍会截停；Stop Sequence 也可能由服务在文本层检测，而不是模型生成单一 EOS ID。

输出上限与上下文窗口不是同一个概念。输出上限规定这次最多新生成多少 Token；上下文窗口约束一次计算能够容纳的输入与生成历史总量。某些服务还会分别设置输入上限、输出上限和总量规则，所以判断“还能生成多少”必须查看具体模型与 API 的计数口径。

## Prefill Latency 和 Decode Tokens/s 为什么必须分开看

Prefill 处理已知 Prompt，较长输入会增加首 Token 出现前的工作；常见观察指标包括 Time to First Token 和输入 Token 吞吐。Decode 每一步只新增少量位置，却要反复读取权重和 KV Cache；常见指标包括 Inter-Token Latency、单请求输出 Tokens/s 和服务总输出吞吐。

```text
请求到达 ── 排队 + Prefill ──> 首 Token
                               │
                               └─ Decode 1 → Decode 2 → … → 完成
```

Prompt 很长但回答很短，体验可能主要被 Prefill 与排队控制；Prompt 短而回答很长，逐 Token Decode 速度更显眼。低 Batch Decode 经常更受显存带宽影响，Prefill 更容易利用大矩阵计算，但这不是永久定律：Batch、并发、量化、Attention 实现、硬件和调度都会改变瓶颈。

因此，“模型每秒 100 Token”若不说明是输入还是输出、单请求还是全服务器、什么 Batch 与上下文长度，几乎无法比较。硬件细节与 KV 显存估算在 [GPU、显存和推理瓶颈](./19-GPU显存和推理瓶颈.md)继续展开。

## 把整条推理链收回来

现在可以把用户按下发送后的动作压成一条不丢环节的链：

```text
Prompt → Tokenizer → Token IDs → Embedding
       → Transformer Prefill → KV Cache + Logits
       → Temperature / Top-k / Top-p / Greedy / Sampling
       → New Token → 追加到 Context
       → Decode + 更新 KV Cache
       → 重复，直到停止条件 → Final Answer
```

这条链中，参数负责把当前 Token 序列映射成候选分数；生成策略负责怎样选下一项；Context 和 KV Cache 保存当前请求不断增长的状态。普通推理不会因为某次回答好坏执行 NLL、Backpropagation 和 Optimizer 更新，那是[训练 Loss 闭环](./12-没人给大模型批作业它怎么知道预测错了.md)的工作。

## 把真实追问逐个回答

**模型最终怎样生成一个 Token？** Prompt 编码成 ID 并经过 Prefill，最后位置产生词表 Logits；系统按贪心或采样策略选出一个 Token ID，再追加到当前序列。

**为什么必须逐 Token 生成？** 后一步的条件分布依赖前一步实际选出的结果；未知未来无法像已知 Prompt 一样预先并行计算。

**Temperature 改变模型知识吗？** 不改变。它缩放当前候选分数的相对差异，影响选择分布，不修改参数。

**Top-k 和 Top-p 有什么区别？** Top-k 固定保留 k 个高分候选；Top-p 按累计概率动态决定集合大小。

**KV Cache 缓存什么，为什么通常不缓存 Q？** 它缓存各层历史位置的 K/V，供每个新 Query 读取；过去 Query 的读取任务已完成，未来步骤通常不再需要它们。

**Prefill 和 Decode 有什么区别？** Prefill 并行处理已知输入并建立缓存；Decode 依赖前一步结果，逐 Token 生成和追加缓存。

**模型输出超过限制会怎样？** 服务在 EOS、输出上限、上下文总量、Stop Sequence 或运行中止条件之一满足时停止；截断不代表模型已经自然说完。

**为什么 Prefill 和 Decode 速度不能混成一个 Tokens/s？** 一个衡量输入处理，另一个衡量串行输出；负载形状、并行度与常见瓶颈不同，混合数字会掩盖真实等待发生在哪里。

## 从这里继续

- 回看输入单位：[模型不认识文字，那“你好”到底是怎么变成数字的](../02-聊天Token与上下文/04-Token到底是什么.md)
- 回看候选分数来源：[ChatGPT 看起来什么都会，底层只是在预测下一个 Token 吗](./10-为什么预测下一个Token能学到能力.md)
- 区分参数是否更新：[训练和推理有什么区别](./18-训练和推理有什么区别.md)
- 深挖运行成本：[GPU、显存和推理瓶颈](./19-GPU显存和推理瓶颈.md)
- 返回全局：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Vaswani et al.: Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Hugging Face Transformers: Generation strategies](https://github.com/huggingface/transformers/blob/main/docs/source/en/generation_strategies.md)
- [Hugging Face Transformers: Cache strategies](https://github.com/huggingface/transformers/blob/main/docs/source/en/kv_cache.md)
- [Holtzman et al.: The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751)
- [Kwon et al.: Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [NVIDIA TensorRT-LLM: Performance Tuning Guide](https://nvidia.github.io/TensorRT-LLM/performance/performance-tuning-guide/index.html)
- [PyTorch: Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html)
