#!/usr/bin/env python3
"""读取 LLM-101 使用的受限 YAML 子集，不依赖第三方包。"""

from __future__ import annotations

import ast
from pathlib import Path


def _value(raw: str):
    raw = raw.strip()
    if not raw:
        return ""
    if raw.startswith("["):
        return ast.literal_eval(raw)
    if raw.startswith(('"', "'")):
        return ast.literal_eval(raw)
    if raw in {"true", "false"}:
        return raw == "true"
    try:
        return int(raw)
    except ValueError:
        return raw


def load_graph(path: Path) -> dict:
    data: dict = {"main_path": [], "extended_path": [], "concepts": [], "relations": []}
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
        if section in {"main_path", "extended_path"} and stripped.startswith("- "):
            data[section].append(_value(stripped[2:]))
            continue
        if section in {"concepts", "relations"}:
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
