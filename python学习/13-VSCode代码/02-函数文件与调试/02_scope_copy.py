# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
def add_total(record: dict[str, float]) -> dict[str, float]:
    result = record.copy()
    result["总分"] = result["数学"] + result["英语"]
    return result

original = {"数学": 90, "英语": 82}
updated = add_total(original)
print(original)
print(updated)
