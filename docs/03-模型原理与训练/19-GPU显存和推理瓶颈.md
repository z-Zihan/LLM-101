# GPU、显存和推理瓶颈

> 所属专题：[训练与推理](./18-训练和推理有什么区别.md) · [Attention](./05-Attention到底是什么.md) · [上下文窗口](../02-聊天Token与上下文/07-上下文和上下文窗口是什么.md)
>
> 这是一篇硬件与性能扩展页，不改变 32 篇主路线顺序。

“模型能装进显存”只回答了能否启动，没有回答跑得多快。LLM 运行时间可能花在矩阵计算、从显存搬权重和缓存、GPU 间通信、请求调度或等待小 Batch 上；不同阶段的瓶颈也会变化。

GPU 提供大量并行计算单元和分层存储。HBM 或 GDDR 常被统称为显存，容量大于片上缓存，却离计算单元更远。算子只有同时安排好计算和数据移动，理论 FLOPs 才可能转成实际速度。

## 算力瓶颈与带宽瓶颈

一个操作需要的运算量与搬运字节之比称为算术强度。若每读一批数据就做大量计算，更可能受计算吞吐限制；若反复搬很多权重却只做少量运算，更可能受显存带宽限制。Roofline 模型用这个关系解释性能上限。

LLM 的 Prefill 会一次处理 Prompt 中许多 Token，矩阵乘法形状较大，权重可在多个 Token 间复用，通常更容易提高 GPU 计算利用率。Decode 每步只生成少量 Token，却要读取大量模型权重和 KV Cache，低 Batch 时常更像带宽受限。

这不是永久标签。更大的 Batch、量化、并行策略、投机解码和不同硬件会改变算术强度；超长 Prompt 的 Attention 也可能让 Prefill 受到显存容量或带宽限制。

## VRAM 无限大也不会让 GPU 无限快

显存容量决定权重、KV Cache、激活和运行缓冲区能否同时放下。增加容量可以避免 CPU Offload 或频繁换入换出，却不会自动增加：

- Tensor Core 等计算单元的峰值吞吐；
- HBM/GDDR 每秒可传输的数据量；
- PCIe 或 NVLink 的跨设备带宽；
- 内核、Batch 与调度对硬件的利用率。

一张容量很大但计算和带宽较低的卡，可以装下模型却生成很慢。相反，算力很强但容量不足，也可能因无法放置权重或 KV Cache 而不能服务目标上下文与并发。

## Tokens/s 需要拆开报告

把 Prompt 处理和生成混成一个 Tokens/s 会隐藏实际体验。常见指标包括：

- Time to First Token：从请求到首 Token 的时间，受排队和 Prefill 影响；
- Prefill Throughput：每秒处理多少输入 Token；
- Inter-Token Latency：连续输出 Token 之间的间隔；
- Decode Throughput：单请求或全服务每秒生成多少 Token；
- Request Throughput：给定延迟目标下每秒完成多少请求。

测试时应记录输入长度、输出长度、Batch/并发、精度、采样、硬件、软件版本和是否包含排队。单用户 50 tokens/s 与服务器总吞吐 5000 tokens/s 不能直接比较。

## KV Cache 怎样估算

标准自回归 Transformer 会为每层保存历史 Token 的 Key 和 Value。一个常用近似是：

```text
KV 字节 ≈ 层数 × 2(K和V) × KV Head 数
          × Head Dimension × 已缓存 Token 数
          × 每元素字节 × Batch
```

多头注意力中 KV Head 数可能等于 Query Head 数；Multi-Query 或 Grouped-Query Attention 会减少 KV Head，因此缓存明显变小。实际服务还会有分页、对齐、元数据、临时缓冲和碎片，公式只是下界估算。

例如 32 层、8 个 KV Head、Head Dimension 128、16-bit（2 字节）、8192 Token、Batch 1，近似需要 `32 × 2 × 8 × 128 × 8192 × 2` 字节，约 1 GiB。并发和上下文长度会近似线性放大这部分。

## 为什么两张卡通常不会快两倍

模型并行把一次推理拆到多卡后，设备要交换激活、分片结果或同步信号。PCIe、NVLink 和跨机网络都有有限带宽与启动延迟；算子过小、切分不均或频繁同步时，通信会盖过并行收益。

两张卡也可能只是解决“单卡装不下”，而不是缩短关键路径。流水线并行会有气泡，张量并行每层都有通信，CPU 调度和采样仍可能串行。只有可并行计算足够大、互联足够快且软件能重叠通信与计算时，速度才可能接近线性扩展。

## HBM、片上存储和计算核心怎样配合

HBM 容量大、带宽高，但访问仍比寄存器和片上 SRAM 慢。GPU 会把数据分块搬进更近的层级，让一个线程块重复使用；Warp 是一组以相同指令节奏执行的线程，Tensor Core 则加速特定矩阵运算。

数据不能一直留在 HBM 里“原地计算”，因为算术单元位于芯片内部。每次从 HBM 取数都付出能耗和时间；若数据在片上被重复利用，就能减少外部读写。布局不连续、分块不合适或线程分歧都会降低利用率。

## FlashAttention 主要减少数据搬运

标准 Attention 若把完整分数矩阵写回 HBM，再读取做 Softmax 和乘 V，会产生大量中间读写。FlashAttention 使用分块与在线 Softmax，在片上存储中计算局部块，避免物化完整矩阵。

它计算的是精确 Attention 的数值等价实现（受浮点舍入影响），主要收益来自更少的 HBM I/O 和更好的融合，而不是把理论上的所有 `QKᵀ` 乘加都删掉。序列长度、Head Dimension、硬件和实现版本会影响加速比例。

## 线上变慢怎样定位

先固定可复现负载，分别测 Prefill、Decode、首 Token、单请求和总吞吐，再观察：

1. GPU 利用率、Tensor Core 利用率和内核时间；
2. HBM 使用量、带宽、KV Cache 命中与碎片；
3. Batch 大小、排队、动态批处理和请求长度分布；
4. 多卡链路带宽、Collective 时间与拓扑；
5. CPU Tokenization、采样、网络与日志是否占关键路径；
6. 最近模型、精度、内核、驱动或调度配置变化。

只看到“GPU 100%”不能判断是高效计算还是等待内存；只看到显存满也不能证明容量就是延迟根因。需要 profiler、服务指标和受控 A/B 实验一起定位。

## 回答八个真实追问

**Prefill 与 Decode 为什么瓶颈不同？** Prefill 能在大量 Token 间复用权重，Decode 每步常要重新读取大量权重和缓存，算术强度不同。

**无限 VRAM 能高效跑超大模型吗？** 只能解决容量；计算吞吐、带宽、互联和软件利用率仍会限制速度。

**多 GPU 为什么不直接翻倍？** 切分增加通信、同步、流水线气泡和调度开销，有时多卡只让模型放得下。

**Tokens/s 怎样测？** 分开输入处理、首 Token、逐 Token 延迟、单请求速度和服务器总吞吐，并写清负载条件。

**KV Cache 如何估算？** 按层数、K/V、KV Head、Head Dimension、Token、精度和 Batch 相乘，再给运行开销留余量。

**HBM、SRAM、Tensor Core、Warp 是什么关系？** 它们分别属于外部显存、片上存储、矩阵计算单元和线程执行组织，共同决定数据能否高效喂给计算。

**FlashAttention 省 FLOPs 还是读写？** 核心优势是分块和融合减少 HBM 中间读写，而非取消精确 Attention 的主要乘加。

**线上突然变慢先查什么？** 拆阶段与指标，再用 profiler 区分计算、带宽、缓存、Batch、通信和调度。

## 从这里继续

- [训练和推理有什么区别](./18-训练和推理有什么区别.md)
- [Attention 到底是什么](./05-Attention到底是什么.md)
- [分布式训练是什么](./20-分布式训练是什么.md)
- 返回：[知识网络](../../知识网络.md) · [真实问题矩阵](../../真实问题矩阵.md)

## 资料与核验

- [Williams, Waterman & Patterson: Roofline](https://doi.org/10.1145/1498765.1498785)
- [Dao et al.: FlashAttention](https://arxiv.org/abs/2205.14135)
- [Kwon et al.: Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [NVIDIA CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)
