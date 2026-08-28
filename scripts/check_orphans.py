#!/usr/bin/env python3
"""检查读者可达性：每个内容页面至少被另一个公开文件引用。"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", ".tmp", ".research"}
CONTENT_DIRS = ("docs", "history")
REFERRER_SUFFIXES = (".md", ".yml")


def markdown_without_fenced_code(text: str) -> str:
    kept = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            kept.append(line)
    return "\n".join(kept)


def referrer_texts() -> dict[str, str]:
    texts = {}
    for path in sorted(ROOT.rglob("*")):
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        if path.suffix not in REFERRER_SUFFIXES or path.name == "文章模板.md":
            continue
        text = path.read_text(encoding="utf-8")
        texts[path.relative_to(ROOT).as_posix()] = (
            markdown_without_fenced_code(text) if path.suffix == ".md" else text
        )
    return texts


def main() -> int:
    texts = referrer_texts()
    content_files = [
        ROOT / name
        for name in sorted(texts)
        if name.split("/", 1)[0] in CONTENT_DIRS
    ]
    errors = []
    for path in content_files:
        relative = path.relative_to(ROOT).as_posix()
        inbound = [
            referrer
            for referrer, text in texts.items()
            if referrer != relative and path.name in text
        ]
        if not inbound:
            errors.append(f"{relative} 没有任何入口链接指向它")
    if errors:
        print("内容可达性检查失败：")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"内容可达性检查通过：{len(content_files)} 个内容页面都有入口引用。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
