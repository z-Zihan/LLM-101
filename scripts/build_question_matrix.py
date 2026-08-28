#!/usr/bin/env python3
"""从真实问题库.yml生成面向读者的真实问题矩阵.md。"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from knowledge_graph_lib import load_graph
from question_lib import load_questions


ROOT = Path(__file__).resolve().parents[1]

DIFFICULTY_ORDER = ["beginner", "intermediate", "advanced"]
DIFFICULTY_LABELS = {"beginner": "入门", "intermediate": "进阶", "advanced": "高阶"}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
PRIORITY_LABELS = {"high": "高", "medium": "中", "low": "低"}
STATUS_LABELS = {"answered": "已回答", "needs_rewrite": "待 V3 重写", "planned": "已规划"}


def page_title(path: str) -> str:
    """从文件名得到标题，如 04-Token到底是什么.md → Token到底是什么。"""
    return re.sub(r"^\d+-", "", Path(path).stem)


def concept_cells(item: dict, by_concept: dict) -> str:
    return "、".join(
        f"[{by_concept[cid]['name']}](./{by_concept[cid]['path']})" for cid in item["concepts"]
    )


def question_table(items: list[dict], by_concept: dict) -> list[str]:
    lines = [
        "| 真实问题 | 涉及概念 | 优先级 | 状态 | 答案页面 |",
        "|---|---|---|---|---|",
    ]
    for item in items:
        answer = "—"
        if item["answer_path"]:
            answer = f"[查看回答](./{item['answer_path']})"
        lines.append(
            f"| {item['question']} | {concept_cells(item, by_concept)} | "
            f"{PRIORITY_LABELS[item['priority']]} | {STATUS_LABELS[item['status']]} | {answer} |"
        )
    return lines


def main() -> None:
    graph = load_graph(ROOT / "知识网络.yml")
    question_data = load_questions(ROOT / "真实问题库.yml")
    by_concept = {item["id"]: item for item in graph["concepts"]}
    questions = question_data["questions"]
    status_counts = Counter(item["status"] for item in questions)

    by_difficulty: dict[str, list[dict]] = {
        level: [q for q in questions if q["difficulty"] == level] for level in DIFFICULTY_ORDER
    }

    lines = [
        "# LLM-101 真实问题矩阵",
        "",
        "> 本页由 [`真实问题库.yml`](./真实问题库.yml) 自动生成，请勿手工编辑。",
        "> 重新生成：`python3 scripts/build_question_matrix.py`",
        "",
        f"当前收录 **{len(questions)}** 个真实问题；已回答 {status_counts['answered']} 个，等待按 V3 重写 {status_counts['needs_rewrite']} 个，规划中 {status_counts['planned']} 个。",
        "",
        "这些问题用来帮助你从自己的困惑直接找到答案。技术结论仍由正文所列论文、官方文档或权威资料支撑。",
        "",
        f"**目录**：[入门问题](#入门问题)（{len(by_difficulty['beginner'])}）· "
        f"[进阶问题](#进阶问题)（{len(by_difficulty['intermediate'])}）· "
        f"[高阶问题](#高阶问题)（{len(by_difficulty['advanced'])}）· "
        "[按答案页面查找](#按答案页面查找)",
        "",
    ]

    section_intro = {
        "beginner": "刚接触 AI 时最常见的困惑；答案页通常只假设很少的前置概念。",
        "intermediate": "已经有基础直觉，想弄清边界、机制和工程取舍时从这里找。",
        "advanced": "贴近面试和实战深水区的问题；建议先读过对应概念主页面再进入。",
    }
    for level in DIFFICULTY_ORDER:
        items = sorted(
            by_difficulty[level],
            key=lambda q: PRIORITY_ORDER.get(q["priority"], 9),
        )
        label = DIFFICULTY_LABELS[level]
        lines.extend(
            [
                f"## {label}问题",
                "",
                f"{label}共 {len(items)} 个。{section_intro[level]}",
                "",
            ]
        )
        lines.extend(question_table(items, by_concept))
        lines.append("")

    grouped: dict[str, list[dict]] = {}
    page_order: list[str] = []
    for item in questions:
        path = item.get("answer_path") or ""
        if not path or not path.startswith("docs/"):
            continue
        if path not in grouped:
            grouped[path] = []
            page_order.append(path)
        grouped[path].append(item)

    lines.extend(
        [
            "## 按答案页面查找",
            "",
            "同一篇文章往往承接多条真实追问。下面按答案页面列出它们各自回答的问题：如果你正打开某篇文章、想知道它还能回答什么，或者读完想确认自己的疑问是否被覆盖，用这一节更快。",
            "",
        ]
    )
    for path in page_order:
        items = grouped[path]
        title = page_title(path)
        lines.extend([f"### {title}", ""])
        for item in items:
            lines.append(f"- [{item['question']}](./{path})")
        lines.append("")

    lines.extend(
        [
            "## 怎样使用这张表",
            "",
            "- 有具体困惑：直接从问题进入答案页面；不确定难度就先扫「入门问题」一节。",
            "- 想系统学习：进入任一概念主页面，再沿文章底部的自然导航继续阅读。",
            "- 打开某篇文章后想看它还回答哪些问题：用上面的「按答案页面查找」。",
            "",
        ]
    )
    (ROOT / "真实问题矩阵.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
