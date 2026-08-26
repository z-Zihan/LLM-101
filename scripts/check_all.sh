#!/usr/bin/env bash
# 依次运行 LLM-101 全部自动门禁；任一步失败立即停止并返回非零。

set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/build_knowledge_graph.py
python3 scripts/build_question_matrix.py
python3 scripts/check_links.py
python3 scripts/check_concepts.py
python3 scripts/check_questions.py --strict
python3 scripts/check_question_privacy.py
python3 scripts/check_reader_experience.py
python3 scripts/check_orphans.py
python3 -m py_compile scripts/*.py
git diff --check

echo "全部自动检查通过。"
