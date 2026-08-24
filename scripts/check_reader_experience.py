#!/usr/bin/env python3
"""检查读者入口、主线导航与最小原理闭环没有退化。"""

from __future__ import annotations

import sys
from pathlib import Path

from knowledge_graph_lib import load_graph


ROOT = Path(__file__).resolve().parents[1]
OVERVIEW = ROOT / "docs/00-从一句话开始，带你看懂整个大模型世界.md"
CORE = [
    "docs/02-聊天Token与上下文/04-Token到底是什么.md",
    "docs/03-模型原理与训练/10-为什么预测下一个Token能学到能力.md",
    "docs/03-模型原理与训练/05-Attention到底是什么.md",
    "docs/03-模型原理与训练/12-没人给大模型批作业它怎么知道预测错了.md",
    "docs/03-模型原理与训练/14-为什么ChatGPT的字是一个一个蹦出来的.md",
]


def main() -> int:
    errors: list[str] = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    first_screen = "\n".join(readme.splitlines()[:18])
    for label in ["从一句话开始", "主学习路线第一篇", "LLM 最小原理闭环"]:
        if label not in first_screen:
            errors.append(f"README 第一屏缺少入口：{label}")

    overview = OVERVIEW.read_text(encoding="utf-8")
    if sum(line.startswith("# ") for line in overview.splitlines()) != 1:
        errors.append("总览文章必须只有一个一级标题")
    for part in "ABCDEFGH":
        if f"### {part}." not in overview:
            errors.append(f"总览文章缺少路线 {part}")

    for index, relative in enumerate(CORE, 1):
        text = (ROOT / relative).read_text(encoding="utf-8")
        marker = f"第 {index} 章 / 共 5 章"
        if marker not in text:
            errors.append(f"{relative} 缺少闭环章节标记：{marker}")
        if "中国的首都是" not in text:
            errors.append(f"{relative} 没有延续贯穿例子")

    graph = load_graph(ROOT / "知识网络.yml")
    by_id = {item["id"]: item for item in graph["concepts"]}
    for concept_id in graph["main_path"]:
        path = ROOT / by_id[concept_id]["path"]
        text = path.read_text(encoding="utf-8")
        if "课程导航" not in text:
            errors.append(f"主路线文章缺少课程导航：{path.relative_to(ROOT)}")

    if errors:
        print("读者体验检查失败：")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print("读者体验检查通过：第一屏、8 条分流路线、5 章闭环与主路线导航均完整。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
