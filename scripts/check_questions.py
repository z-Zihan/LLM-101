#!/usr/bin/env python3
"""检查真实问题的来源、映射、答案路径和知识节点双向连接。"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

from knowledge_graph_lib import load_graph
from question_lib import load_questions


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    graph = load_graph(ROOT / "知识网络.yml")
    questions = load_questions(ROOT / "真实问题库.yml")["questions"]
    by_concept = {item["id"]: item for item in graph["concepts"]}
    by_question = {item.get("id"): item for item in questions}
    errors = []
    warnings = []

    required = {
        "id", "question", "source_type", "source_url", "source_title", "language",
        "paraphrased", "concepts", "difficulty", "priority", "status", "answer_path", "cluster",
    }
    for question_id, count in Counter(item.get("id") for item in questions).items():
        if count > 1:
            errors.append(f"问题 ID 重复：{question_id}")

    for item in questions:
        qid = item.get("id")
        missing = required - item.keys()
        if missing:
            errors.append(f"问题 {qid} 缺少字段：{', '.join(sorted(missing))}")
            continue
        if item["source_type"] not in {"original_chat", "public_web"}:
            errors.append(f"问题 {qid} 的 source_type 无效：{item['source_type']}")
        if item["source_type"] == "public_web" and not str(item["source_url"]).startswith("https://"):
            errors.append(f"公开问题 {qid} 缺少 HTTPS 来源")
        if item.get("interview_question") is True:
            if item["source_type"] != "public_web":
                errors.append(f"真实面试题 {qid} 必须来自公开问题记录")
            if not str(item["source_url"]).startswith("https://"):
                errors.append(f"真实面试题 {qid} 缺少公开 HTTPS 来源")
            if not item.get("source_kind"):
                errors.append(f"真实面试题 {qid} 缺少 source_kind")
        if item["language"] == "en" and not item["paraphrased"]:
            errors.append(f"英文来源问题 {qid} 的中文问法必须标记 paraphrased")
        if item["difficulty"] not in {"beginner", "intermediate", "advanced"}:
            errors.append(f"问题 {qid} 的 difficulty 无效：{item['difficulty']}")
        if item["priority"] not in {"high", "medium", "low"}:
            errors.append(f"问题 {qid} 的 priority 无效：{item['priority']}")
        if item["status"] not in {"answered", "needs_rewrite", "planned"}:
            errors.append(f"问题 {qid} 的 status 无效：{item['status']}")
        if not item["concepts"]:
            errors.append(f"问题 {qid} 没有映射概念")
        for concept_id in item["concepts"]:
            if concept_id not in by_concept:
                errors.append(f"问题 {qid} 引用了不存在的概念：{concept_id}")
                continue
            if qid not in by_concept[concept_id].get("questions", []):
                errors.append(f"问题 {qid} 没有反向写入节点 {concept_id}")
        if item["answer_path"]:
            answer = ROOT / item["answer_path"]
            if not answer.is_file():
                errors.append(f"问题 {qid} 的答案页面不存在：{item['answer_path']}")
        elif item["status"] != "planned":
            errors.append(f"问题 {qid} 状态为 {item['status']}，但没有 answer_path")
        if item["priority"] == "high" and item["status"] != "answered":
            warnings.append(f"高优先级问题仍待完成：{qid}")

    for concept_id, concept in by_concept.items():
        node_questions = concept.get("questions", [])
        if concept.get("level") == "Core" and not node_questions:
            errors.append(f"核心节点没有真实问题：{concept_id}")
        for question_id in node_questions:
            if question_id not in by_question:
                errors.append(f"节点 {concept_id} 引用了不存在的问题：{question_id}")
            elif concept_id not in by_question[question_id]["concepts"]:
                errors.append(f"节点 {concept_id} 与问题 {question_id} 的映射不是双向的")

    strict = "--strict" in sys.argv
    if strict and warnings:
        errors.extend(warnings)
    if errors:
        print("真实问题检查失败：")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"真实问题检查通过：{len(questions)} 个问题，覆盖 {len(by_concept)} 个概念节点。")
    if warnings:
        print(f"进度提示：仍有 {len(warnings)} 个高优先级问题等待 V3 重写；最终审查请使用 --strict。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
