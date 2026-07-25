from __future__ import annotations

from pathlib import Path
import json
import os
import re
import subprocess
import sys


VAULT = Path(r"E:\LXZ\Documents\obsidian笔记！\StudyNote")
ROOT = VAULT / "python学习"
CODE = ROOT / "13-VSCode代码"
RUNTIME = ROOT / "tmp" / "verification_runtime"


def check_markdown_links() -> list[str]:
    failures: list[str] = []
    pattern = re.compile(r"\[\[([^\]|#]+)")
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        text_without_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for target in pattern.findall(text_without_code):
            target = target.strip()
            if target.startswith(("http://", "https://")):
                continue
            candidates = [
                VAULT / target,
                VAULT / f"{target}.md",
                VAULT / f"{target}.py",
            ]
            if not any(path.exists() for path in candidates):
                failures.append(f"{markdown.relative_to(ROOT)} -> {target}")
    return failures


def check_notebook() -> list[str]:
    failures: list[str] = []
    for notebook in ROOT.rglob("*.ipynb"):
        try:
            data = json.loads(notebook.read_text(encoding="utf-8"))
            assert data["nbformat"] == 4
            assert isinstance(data["cells"], list)
        except Exception as error:
            failures.append(f"{notebook.relative_to(ROOT)}: {error}")
    return failures


def compile_scripts() -> list[str]:
    failures: list[str] = []
    for script in ROOT.rglob("*.py"):
        if ".venv" in script.parts:
            continue
        try:
            compile(script.read_text(encoding="utf-8"), str(script), "exec")
        except Exception as error:
            failures.append(f"{script.relative_to(ROOT)}: {error}")
    return failures


def run_scripts() -> tuple[list[str], list[str]]:
    failures: list[str] = []
    passed: list[str] = []
    RUNTIME.mkdir(parents=True, exist_ok=True)
    scripts = sorted(CODE.rglob("*.py"))
    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"
    env["PYTHONUTF8"] = "1"
    for script in scripts:
        relative = script.relative_to(ROOT).as_posix()
        if "综合项目参考实现" in relative and script.name != "run_all.py":
            continue
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=RUNTIME,
            env=env,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120,
        )
        if result.returncode:
            failures.append(
                f"{relative}\nSTDOUT:\n{result.stdout[-1000:]}\nSTDERR:\n{result.stderr[-2000:]}"
            )
        else:
            passed.append(relative)
    return failures, passed


def main() -> None:
    report = {
        "markdown_link_failures": check_markdown_links(),
        "notebook_failures": check_notebook(),
        "compile_failures": compile_scripts(),
    }
    run_failures, passed = run_scripts()
    report["run_failures"] = run_failures
    report["passed_scripts"] = passed
    report_path = ROOT / "tmp" / "课程验证报告.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({
        "链接失败": len(report["markdown_link_failures"]),
        "Notebook失败": len(report["notebook_failures"]),
        "编译失败": len(report["compile_failures"]),
        "运行通过": len(passed),
        "运行失败": len(run_failures),
        "报告": str(report_path),
    }, ensure_ascii=False, indent=2))
    if any(report[key] for key in (
        "markdown_link_failures", "notebook_failures",
        "compile_failures", "run_failures",
    )):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
