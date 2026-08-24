#!/usr/bin/env python3
"""检查仓库内 Markdown 相对链接，发现死链时返回非零。"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def repository_paths() -> set[str]:
    """读取 Git 索引中的规范大小写，并补入未跟踪的公开文件。"""
    result = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    paths = {"."}
    for raw in result.stdout.decode("utf-8").split("\0"):
        if not raw:
            continue
        item = Path(raw)
        paths.add(item.as_posix())
        paths.update(parent.as_posix() for parent in item.parents)
    return paths


def has_exact_case(path: Path, known_paths: set[str]) -> bool:
    """在大小写不敏感的文件系统上也校验 GitHub 使用的精确路径。"""
    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        return True
    return relative.as_posix() in known_paths


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
    checked = 0
    known_paths = repository_paths()
    known_paths_by_fold = {item.casefold(): item for item in known_paths}
    files = sorted(ROOT.rglob("*.md"))
    for path in files:
        if any(name in path.parts for name in {".git", ".tmp", ".research"}):
            continue
        if path.name == "文章模板.md":
            continue
        checked += 1
        relative_path = path.relative_to(ROOT).as_posix()
        canonical_path = Path(known_paths_by_fold.get(relative_path.casefold(), relative_path))
        text = markdown_without_fenced_code(path.read_text(encoding="utf-8"))
        for match in LINK.finditer(text):
            target = match.group(1).strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not clean:
                continue
            resolved = Path(os.path.abspath(ROOT / canonical_path.parent / clean))
            if not resolved.exists():
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: {target}")
            elif not has_exact_case(resolved, known_paths):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: 路径大小写不匹配：{target}")
    if errors:
        print("发现 Markdown 死链：")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"链接检查通过：扫描 {checked} 个公开 Markdown 文件。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
