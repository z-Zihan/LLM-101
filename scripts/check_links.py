#!/usr/bin/env python3
"""检查仓库内 Markdown 相对链接，发现死链时返回非零。"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


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


def main() -> int:
    errors = []
    files = sorted(ROOT.rglob("*.md"))
    for path in files:
        if ".git" in path.parts or ".tmp" in path.parts:
            continue
        if path.name == "文章模板.md":
            continue
        text = markdown_without_fenced_code(path.read_text(encoding="utf-8"))
        for match in LINK.finditer(text):
            target = match.group(1).strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: {target}")
    if errors:
        print("发现 Markdown 死链：")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"链接检查通过：扫描 {len(files)} 个 Markdown 文件。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
