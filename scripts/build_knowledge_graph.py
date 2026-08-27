#!/usr/bin/env python3
"""从知识网络.yml生成面向读者的知识网络.md。"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from knowledge_graph_lib import load_graph
from question_lib import load_questions


ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "知识网络.yml"
OUTPUT_PATH = ROOT / "知识网络.md"

PART_LABELS = {
    "docs/00": "起点",
    "docs/01-AI与大模型": "AI 与模型",
    "docs/02-聊天Token与上下文": "文字、提示与上下文",
    "docs/03-模型原理与训练": "模型原理与训练",
    "docs/04-模型能力": "模型能力",
    "docs/05-幻觉与模型局限": "幻觉与验证",
    "docs/06-工具与Function-Calling": "工具与 Function Calling",
    "docs/07-Agent": "Agent",
    "docs/08-RAG与知识库": "RAG 与知识库",
    "docs/09-MCP": "MCP",
    "docs/10-Skill": "Skill",
    "docs/11-Coding-Agent": "Coding Agent",
    "docs/12-Memory": "Memory",
}

OVERVIEW_PATH = "docs/00-从一句话开始，带你看懂整个大模型世界.md"


def link(node: dict) -> str:
    return f"[{node['name']}](./{node['path']})"


def mermaid_id(concept_id: str) -> str:
    return "n_" + concept_id.replace("-", "_")


def page_title(path: str) -> str:
    """从文件名得到标题，如 05-Attention到底是什么.md → Attention到底是什么。"""
    return re.sub(r"^\d+-", "", Path(path).stem)


def grouped_outline(paths: list[str]) -> list[str]:
    """把去重后的主路线页面按真实教学顺序编号；每项尾注所属部分，便于定位。"""
    lines: list[str] = []
    seen: set[str] = set()
    number = 0
    for path in paths:
        if path in seen:
            continue
        seen.add(path)
        number += 1
        part_key = next(
            (key for key in PART_LABELS if path.startswith(key)),
            str(Path(path).parent),
        )
        label = PART_LABELS.get(part_key, Path(part_key).name)
        lines.append(f"{number}. [{page_title(path)}](./{path}) · {label}")
    lines.append("")
    return lines


def main() -> None:
    graph = load_graph(GRAPH_PATH)
    question_data = load_questions(ROOT / "真实问题库.yml")
    concepts = graph["concepts"]
    by_id = {item["id"]: item for item in concepts}
    by_question = {item["id"]: item for item in question_data["questions"]}
    incoming = defaultdict(list)
    outgoing = defaultdict(list)
    for relation in graph["relations"]:
        outgoing[relation["from"]].append(relation)
        incoming[relation["to"]].append(relation)

    lines = [
        "# LLM-101 知识网络",
        "",
        "> 本页由 [`知识网络.yml`](./知识网络.yml) 自动生成，请勿手工编辑。",
        "> 重新生成：`python3 scripts/build_knowledge_graph.py`",
        "",
        "这里适合已经知道自己想学什么的读者。第一次接触 AI，请先从 README 的默认学习路线开始。",
        "",
        "## 主学习路线",
        "",
        "适合第一次从头学习。路线只保留会明显影响后续理解的概念。下面先给整条链的速览，再给出按阶段分组的逐篇清单——迷路时回到这里就能恢复位置。",
        "",
        " → ".join(link(by_id[item]) for item in graph["main_path"]),
        "",
        f"0. [从一句话开始，带你看懂整个大模型世界](./{OVERVIEW_PATH})（可选的全局入口）",
        "",
    ]
    lines.extend(grouped_outline([by_id[item]["path"] for item in graph["main_path"]]))
    lines.extend(
        [
            "## 扩展学习路线",
            "",
            "理解主线后，可以按需要深入这些概念。",
            "",
            " → ".join(link(by_id[item]) for item in graph["extended_path"]),
            "",
            "## 按概念找下一步",
            "",
            "| 概念 | 一句话 | 如果没懂先看 | 接下来会遇到 | 你可能会问 | 进入文章 |",
            "|---|---|---|---|---|---|",
        ]
    )
    for node in concepts:
        cid = node["id"]
        prerequisites = "、".join(link(by_id[item]) for item in node.get("prerequisites", [])) or "—"
        relations = []
        for item in outgoing[cid][:3]:
            relations.append(f"{item['relation']} {link(by_id[item['to']])}")
        for item in incoming[cid][:2]:
            relations.append(f"{link(by_id[item['from']])} {item['relation']}它")
        relation_text = "；".join(relations) or "—"
        questions = []
        for question_id in node.get("questions", [])[:3]:
            question = by_question[question_id]
            if question.get("answer_path"):
                questions.append(f"[{question['question']}](./{question['answer_path']})")
            else:
                questions.append(question["question"])
        question_text = "<br>".join(questions) or "—"
        lines.append(
            f"| {link(node)} | {node['summary']} | {prerequisites} | {relation_text} | {question_text} | {link(node)} |"
        )

    groups = defaultdict(list)
    for node in concepts:
        groups[node["group"]].append(node["id"])
    group_order = [
        "AI与模型",
        "模型训练",
        "推理与Token",
        "RAG与知识",
        "Tool与Agent",
        "MCP与Skill",
        "Coding Agent",
        "Memory",
        "硬件",
    ]
    lines.extend(["", "## 按专题探索", ""])
    for index, group in enumerate(group_order, 1):
        member_ids = groups.get(group, [])
        if not member_ids:
            lines.extend(
                [
                    f"### {index:02d} {group}",
                    "",
                    "本专题暂不进入当前 V3 发布范围；新增节点需要真实问题与主页面支撑。",
                    "",
                ]
            )
            continue
        member_set = set(member_ids)
        lines.extend([f"### {index:02d} {group}", "", "```mermaid", "flowchart LR"])
        for cid in member_ids:
            node = by_id[cid]
            lines.append(f'    {mermaid_id(cid)}["{node["name"]}"]')
        for relation in graph["relations"]:
            if relation["from"] in member_set and relation["to"] in member_set:
                lines.append(
                    f'    {mermaid_id(relation["from"])} -->|"{relation["relation"]}"| {mermaid_id(relation["to"])}'
                )
        lines.extend(["```", ""])

    main_set = set(graph["main_path"])
    lines.extend(
        [
            "## 全景图",
            "",
            "全景图展示全部主路线节点及其关系。整张图较大，展开后加载需要一点时间；只想查单个概念的下一步，用上面的「按概念找下一步」表格更快。",
            "",
            "<details>",
            "<summary>展开全景图</summary>",
            "",
            "```mermaid",
            "flowchart LR",
        ]
    )
    for cid in graph["main_path"]:
        lines.append(f'    {mermaid_id(cid)}["{by_id[cid]["name"]}"]')
    for relation in graph["relations"]:
        if relation["from"] in main_set and relation["to"] in main_set:
            lines.append(
                f'    {mermaid_id(relation["from"])} -->|"{relation["relation"]}"| {mermaid_id(relation["to"])}'
            )
    lines.extend(
        [
            "```",
            "",
            "</details>",
            "",
            "## 如何自由探索",
            "",
            "- 从任意概念进入正文。",
            "- 如果前置概念不熟，先沿“如果没懂先看”补一篇。",
            "- 读完正文后，优先选择文章给出的下一步；不必理解图谱的数据结构。",
            "- 迷路时回到本页顶部的「主学习路线」清单恢复位置。",
            "",
        ]
    )

    content = "\n".join(lines)
    OUTPUT_PATH.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
