# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import json
from pathlib import Path

config = {
    "random_seed": 42,
    "test_size": 0.2,
    "target": "产量",
}
path = Path("config.json")
path.write_text(
    json.dumps(config, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
loaded = json.loads(path.read_text(encoding="utf-8"))
print(loaded["target"], loaded["test_size"])
