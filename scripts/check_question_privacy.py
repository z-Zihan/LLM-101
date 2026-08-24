#!/usr/bin/env python3
"""阻止真实问题的来源与身份信息进入公开文件。"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".tmp", ".research"}
PUBLIC_SUFFIXES = {".md", ".yml", ".yaml"}

FORBIDDEN_FIELDS = re.compile(
    r"^\s*(source_url|source_platform|source_title|source_kind|source_type)\s*:",
    re.IGNORECASE,
)
SOURCE_TAGGED_ID = re.compile(
    r"^\s*-\s+id:\s+.*-(?:web|reddit|v2ex|zhihu|github|hn|so|ai-se|stats|su)-\d+\s*$",
    re.IGNORECASE,
)
SOURCE_IDENTITIES = r"微信|牛客|Reddit|知乎|V2EX|Stack Overflow|Hacker News|GitHub Issue"
ATTRIBUTION_PATTERNS = [
    re.compile(rf"真实(?:问题|讨论)来源[^\n]*(?:{SOURCE_IDENTITIES})", re.IGNORECASE),
    re.compile(rf"(?:问题|提问|讨论).{{0,24}}来自.{{0,24}}(?:{SOURCE_IDENTITIES})", re.IGNORECASE),
    re.compile(rf"(?:{SOURCE_IDENTITIES}).{{0,24}}(?:有人问|用户问|提问|问题写在标题|讨论直接)", re.IGNORECASE),
    re.compile(r"用户提供的原始聊天记录", re.IGNORECASE),
]


def public_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in PUBLIC_SUFFIXES
        and not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )


def main() -> int:
    errors: list[str] = []
    for path in public_files():
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if FORBIDDEN_FIELDS.search(line):
                errors.append(f"{path.relative_to(ROOT)}:{number}: 公开文件含来源字段")
            if SOURCE_TAGGED_ID.search(line):
                errors.append(f"{path.relative_to(ROOT)}:{number}: 问题 ID 暴露来源平台")
            for pattern in ATTRIBUTION_PATTERNS:
                if pattern.search(line):
                    errors.append(f"{path.relative_to(ROOT)}:{number}: 公开内容暴露问题来源身份")
                    break

    if errors:
        print("真实问题隐私检查失败：")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"真实问题隐私检查通过：已检查 {len(public_files())} 个公开 Markdown/YAML 文件。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
