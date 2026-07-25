# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
output = project_root / "tmp" / "学习记录.txt"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text("今天完成了文件读写。\n", encoding="utf-8")
print(output.read_text(encoding="utf-8"))
