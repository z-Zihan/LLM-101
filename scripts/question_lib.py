#!/usr/bin/env python3
"""读取 LLM-101 真实问题库使用的受限 YAML 子集。"""

from __future__ import annotations

from pathlib import Path

from knowledge_graph_lib import _value


def load_questions(path: Path) -> dict:
    data: dict = {"questions": []}
    section = None
    current = None

    for number, source_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = source_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if not line.startswith(" ") and stripped.endswith(":"):
            section = stripped[:-1]
            current = None
            continue
        if not line.startswith(" ") and ":" in stripped:
            key, raw = stripped.split(":", 1)
            data[key] = _value(raw)
            continue
        if section == "questions":
            if stripped.startswith("- "):
                current = {}
                data[section].append(current)
                item = stripped[2:]
                if item:
                    key, raw = item.split(":", 1)
                    current[key] = _value(raw)
                continue
            if current is not None and ":" in stripped:
                key, raw = stripped.split(":", 1)
                current[key] = _value(raw)
                continue
        raise ValueError(f"{path}:{number}: 无法解析：{source_line}")
    return data
