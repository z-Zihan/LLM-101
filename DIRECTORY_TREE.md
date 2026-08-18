# LLM-101 Directory Tree

```text
LLM-101/
│
├── .gitignore
├── README.md
├── CONTENT_MAP.md
├── ARTICLE_TEMPLATE.md
├── DIRECTORY_TREE.md
├── PROGRESS.md
├── GLOSSARY.md
├── CONTRIBUTING.md                  # 后续补
├── LICENSE                          # 后续确定
│
├── docs/
│   │
│   ├── 01-ai-and-llm/
│   │   ├── 01-what-is-ai.md
│   │   ├── 02-ai-ml-dl.md
│   │   ├── 03-what-is-model.md
│   │   ├── 04-what-is-llm.md
│   │   ├── 05-gpt-vs-chatgpt.md
│   │   ├── 06-foundation-model.md
│   │   └── 07-model-api-product-company.md
│   │
│   ├── 02-chat-and-context/
│   │   ├── 01-prompt.md
│   │   ├── 02-system-prompt.md
│   │   ├── 03-prompt-engineering.md
│   │   ├── 04-token.md
│   │   ├── 05-k-m-b-t.md
│   │   ├── 06-tokenizer.md
│   │   ├── 07-context.md
│   │   ├── 08-long-context.md
│   │   ├── 09-next-token-generation.md
│   │   ├── 10-temperature-top-p.md
│   │   └── 11-kv-cache.md
│   │
│   ├── 03-how-models-work/
│   │   ├── 01-model-lifecycle.md
│   │   ├── 02-architecture.md
│   │   ├── 03-transformer.md
│   │   ├── 04-layer-width.md
│   │   ├── 05-attention.md
│   │   ├── 06-parameter.md
│   │   ├── 07-parameter-vs-training-data.md
│   │   ├── 08-random-initialization.md
│   │   ├── 09-pretraining.md
│   │   ├── 10-next-token-prediction.md
│   │   ├── 11-loss.md
│   │   ├── 12-gradient-and-backprop.md
│   │   ├── 13-post-training.md
│   │   ├── 14-sft.md
│   │   ├── 15-rlhf-dpo.md
│   │   ├── 16-checkpoint-and-weights.md
│   │   ├── 17-deployment.md
│   │   └── 18-training-vs-inference.md
│   │
│   ├── 04-capabilities/
│   │   ├── 01-generalization.md
│   │   ├── 02-emergence.md
│   │   ├── 03-reasoning.md
│   │   ├── 04-in-context-learning.md
│   │   ├── 05-multimodal.md
│   │   ├── 06-moe.md
│   │   ├── 07-scaling-laws.md
│   │   ├── 08-distillation.md
│   │   ├── 09-quantization.md
│   │   ├── 10-lora.md
│   │   └── 11-reproducibility.md
│   │
│   ├── 05-limitations/
│   │   ├── 01-hallucination.md
│   │   ├── 02-llm-is-not-database.md
│   │   ├── 03-knowledge-in-parameters.md
│   │   ├── 04-verification.md
│   │   ├── 05-prompt-injection.md
│   │   └── 06-jailbreak-red-team.md
│   │
│   ├── 06-tools/
│   │   ├── 01-api.md
│   │   ├── 02-tool.md
│   │   ├── 03-function-calling.md
│   │   ├── 04-tool-calling.md
│   │   ├── 05-web-search.md
│   │   ├── 06-file-tools.md
│   │   ├── 07-code-execution.md
│   │   ├── 08-browser-computer-use.md
│   │   ├── 09-database-tools.md
│   │   └── 10-ocr.md
│   │
│   ├── 07-agent/
│   │   ├── 01-what-is-agent.md
│   │   ├── 02-model-vs-agent.md
│   │   ├── 03-agent-loop.md
│   │   ├── 04-planning.md
│   │   ├── 05-workflow-vs-agent.md
│   │   ├── 06-copilot-vs-agent.md
│   │   ├── 07-ai-embedded-copilot-agent.md
│   │   ├── 08-multi-agent.md
│   │   └── 09-long-running-agent.md
│   │
│   ├── 08-rag/
│   │   ├── 01-what-is-rag.md
│   │   ├── 02-knowledge-base.md
│   │   ├── 03-embedding.md
│   │   ├── 04-vector.md
│   │   ├── 05-vector-database.md
│   │   ├── 06-semantic-search.md
│   │   ├── 07-chunk.md
│   │   ├── 08-retrieval.md
│   │   ├── 09-rerank.md
│   │   ├── 10-knowledge-graph.md
│   │   ├── 11-rag-vs-finetuning.md
│   │   └── 12-rag-limitations.md
│   │
│   ├── 09-mcp/
│   │   ├── 01-what-is-mcp.md
│   │   ├── 02-client-server.md
│   │   ├── 03-tools-resources-prompts.md
│   │   ├── 04-mcp-vs-api.md
│   │   ├── 05-mcp-vs-function-calling.md
│   │   └── 06-mcp-vs-agent.md
│   │
│   ├── 10-skills/
│   │   ├── 01-what-is-skill.md
│   │   ├── 02-skill-vs-prompt.md
│   │   ├── 03-skill-vs-tool.md
│   │   ├── 04-skill-vs-mcp.md
│   │   └── 05-skill-vs-agent.md
│   │
│   ├── 11-coding-agent/
│   │   ├── 01-ai-coding.md
│   │   ├── 02-code-completion.md
│   │   ├── 03-copilot.md
│   │   ├── 04-coding-agent.md
│   │   ├── 05-ide.md
│   │   ├── 06-terminal.md
│   │   ├── 07-git.md
│   │   ├── 08-project-context.md
│   │   └── 09-context-engineering.md
│   │
│   ├── 12-memory/
│   │   ├── 01-conversation-history.md
│   │   ├── 02-context-vs-memory.md
│   │   ├── 03-memory.md
│   │   ├── 04-long-term-memory.md
│   │   ├── 05-rag-vs-memory.md
│   │   └── 06-context-memory-rag-cache.md
│   │
│   └── 13-ai-map/
│       ├── 01-ai-concept-map.md
│       ├── 02-model-lifecycle-map.md
│       ├── 03-training-inference-map.md
│       ├── 04-agent-architecture-map.md
│       ├── 05-ai-application-stack.md
│       └── 06-concept-cheatsheet.md
│
├── history/
│   └── ai-timeline.md
│
├── ecosystem/
│   ├── model-classification.md
│   ├── model-providers.md
│   ├── hardware-vendors.md
│   └── ai-industry-stack.md
│
├── appendix/
│   ├── hardware/
│   │   ├── cpu.md
│   │   ├── gpu.md
│   │   ├── cuda.md
│   │   ├── tensor-core.md
│   │   ├── flops.md
│   │   ├── multiply-accumulate.md
│   │   ├── vram.md
│   │   ├── ram.md
│   │   ├── ssd.md
│   │   ├── hbm.md
│   │   ├── bandwidth.md
│   │   ├── interconnect.md
│   │   ├── server.md
│   │   ├── cluster.md
│   │   └── distributed-training.md
│   │
│   ├── training/
│   │   ├── loss-curve.md
│   │   ├── overfitting-underfitting.md
│   │   ├── optimizer.md
│   │   ├── learning-rate.md
│   │   ├── batch-epoch.md
│   │   ├── mixed-precision.md
│   │   └── parallelism.md
│   │
│   └── advanced/
│       ├── chain-of-thought.md
│       ├── tree-of-thought.md
│       ├── react.md
│       └── pruning.md
│
├── faq/
│   └── beginner-questions.md
│
└── assets/
    ├── diagrams/
    └── images/
```

## 顶层职责

- `README.md`：地图与学习入口
- `CONTENT_MAP.md`：整个项目的内容管理蓝图
- `ARTICLE_TEMPLATE.md`：单篇文章写作标准
- `docs/`：正式课程
- `history/`：AI 关键发展节点
- `ecosystem/`：模型分类、厂商、产业结构
- `appendix/`：硬件、训练、深度技术
- `faq/`：真实小白问题池
- `assets/`：统一管理图和示意图

## 原则

README 是地图，`docs` 是课程，FAQ 是真实问题，Appendix 是深挖。

不要把四者混在一起。
