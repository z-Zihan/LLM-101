#!/usr/bin/env python3
"""检查知识网络节点、路径、关系、孤立节点和学习路线。"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

from knowledge_graph_lib import load_graph


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    graph = load_graph(ROOT / "知识网络.yml")
    concepts = graph["concepts"]
    ids = [item.get("id") for item in concepts]
    by_id = {item.get("id"): item for item in concepts}
    errors = []

    for concept_id, count in Counter(ids).items():
        if count > 1:
            errors.append(f"概念 ID 重复：{concept_id}")
    required = {
        "id", "name", "path", "aliases", "level", "path_type", "summary",
        "prerequisites", "related", "questions",
    }
    for item in concepts:
        missing = required - item.keys()
        if missing:
            errors.append(f"节点 {item.get('id')} 缺少字段：{', '.join(sorted(missing))}")
        if item.get("level") not in {"Core", "Advanced", "Appendix"}:
            errors.append(f"节点 {item.get('id')} 的 level 无效：{item.get('level')}")
        if item.get("path_type") not in {"Main", "Extended", "Optional"}:
            errors.append(f"节点 {item.get('id')} 的 path_type 无效：{item.get('path_type')}")
        article = ROOT / item.get("path", "")
        if not article.is_file():
            errors.append(f"节点 {item.get('id')} 的文章不存在：{item.get('path')}")
        for related in item.get("prerequisites", []) + item.get("related", []):
            if related not in by_id:
                errors.append(f"节点 {item.get('id')} 引用了不存在的概念：{related}")

    degree = defaultdict(int)
    relation_keys = set()
    for relation in graph["relations"]:
        source, target = relation.get("from"), relation.get("to")
        if source not in by_id:
            errors.append(f"Relation from 不存在：{source}")
        if target not in by_id:
            errors.append(f"Relation to 不存在：{target}")
        if source in by_id and target in by_id:
            degree[source] += 1
            degree[target] += 1
        key = (source, relation.get("relation"), target)
        if key in relation_keys:
            errors.append(f"重复 Relation：{source} --{relation.get('relation')}--> {target}")
        relation_keys.add(key)
        if relation.get("relation") in {"相关", "related"}:
            errors.append(f"Relation 语义过弱：{source} --{relation.get('relation')}--> {target}")

    for concept_id in ids:
        if degree[concept_id] == 0:
            errors.append(f"孤立节点：{concept_id}")
    for route_name in ("main_path", "extended_path"):
        route = graph[route_name]
        for concept_id in route:
            if concept_id not in by_id:
                errors.append(f"{route_name} 引用了不存在的概念：{concept_id}")
        duplicates = [key for key, count in Counter(route).items() if count > 1]
        if duplicates:
            errors.append(f"{route_name} 有重复概念：{', '.join(duplicates)}")

    main_position = {concept_id: index for index, concept_id in enumerate(graph["main_path"])}
    for concept_id in graph["main_path"]:
        if concept_id not in by_id:
            continue
        for prerequisite in by_id[concept_id].get("prerequisites", []):
            if prerequisite in main_position and main_position[prerequisite] > main_position[concept_id]:
                errors.append(f"Main Path 前置顺序错误：{concept_id} 早于前置概念 {prerequisite}")

    if errors:
        print("知识网络检查失败：")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"概念检查通过：{len(concepts)} 个节点，{len(graph['relations'])} 条关系。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
