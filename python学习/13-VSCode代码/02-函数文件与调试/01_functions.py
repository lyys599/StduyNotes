# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
def missing_rate(values: list[object], missing_mark=None) -> float:
    missing = sum(value is missing_mark for value in values)
    return missing / len(values) if values else 0.0

data = [12.0, None, 18.5, None, 20.0]
rate = missing_rate(data)
print(f"缺失率：{rate:.1%}")
