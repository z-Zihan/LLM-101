#!/usr/bin/env python3
"""从真实问题库.yml生成面向读者的真实问题矩阵.md。"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from knowledge_graph_lib import load_graph
from question_lib import load_questions


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    graph = load_graph(ROOT / "知识网络.yml")
    question_data = load_questions(ROOT / "真实问题库.yml")
    by_concept = {item["id"]: item for item in graph["concepts"]}
    questions = question_data["questions"]
    status_counts = Counter(item["status"] for item in questions)

    lines = [
        "# LLM-101 真实问题矩阵",
        "",
        "> 本页由 [`真实问题库.yml`](./真实问题库.yml) 自动生成，请勿手工编辑。",
        "> 重新生成：`python3 scripts/build_question_matrix.py`",
        "",
        f"当前收录 **{len(questions)}** 个真实问题；已回答 {status_counts['answered']} 个，等待按 V3 重写 {status_counts['needs_rewrite']} 个，规划中 {status_counts['planned']} 个。",
        "",
        "公开问题只证明困惑真实存在，技术答案仍需用论文、官方文档或权威资料核验。英文来源的问题会转述成自然中文，并明确标记。",
        "",
        "## 问题总表",
        "",
        "| 真实问题 | 来源 | 涉及概念 | 难度 | 优先级 | 状态 | 答案页面 |",
        "|---|---|---|---|---|---|---|",
    ]
    labels = {
        "beginner": "入门",
        "intermediate": "进阶",
        "high": "高",
        "medium": "中",
        "low": "低",
        "answered": "已回答",
        "needs_rewrite": "待 V3 重写",
        "planned": "已规划",
    }
    for item in questions:
        if item["source_url"]:
            source = f"[{item['source_title']}]({item['source_url']})"
            if item["paraphrased"]:
                source += "（转述）"
        else:
            source = item["source_title"]
        concepts = "、".join(
            f"[{by_concept[cid]['name']}](./{by_concept[cid]['path']})" for cid in item["concepts"]
        )
        answer = "—"
        if item["answer_path"]:
            answer = f"[查看回答](./{item['answer_path']})"
        lines.append(
            f"| {item['question']} | {source} | {concepts} | {labels[item['difficulty']]} | "
            f"{labels[item['priority']]} | {labels[item['status']]} | {answer} |"
        )

    lines.extend(
        [
            "",
            "## 怎样使用这张表",
            "",
            "- 有具体困惑：直接从问题进入答案页面。",
            "- 想系统学习：进入任一概念主页面，再沿知识网络继续阅读。",
            "- 想核对来源：打开公开链接；原始聊天问题来自用户提供的聊天记录，不公开身份信息。",
            "",
        ]
    )
    (ROOT / "真实问题矩阵.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
