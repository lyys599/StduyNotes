# 完成独立尝试后再阅读本文件。
def clean_values(values):
    valid = [value for value in values if 0 <= value <= 100]
    if not valid:
        raise ValueError("没有有效值")
    return {
        "有效值": valid,
        "均值": sum(valid) / len(valid),
        "最大值": max(valid),
        "最小值": min(valid),
    }

records = [
    ("A", 20.0), ("A", -1.0), ("B", 31.0),
    ("B", 999.0), ("B", 28.0), ("C", 26.0),
]
summary = {}
for station, value in records:
    item = summary.setdefault(station, {"总数": 0, "异常数": 0})
    item["总数"] += 1
    if not 0 <= value <= 100:
        item["异常数"] += 1
for station, item in summary.items():
    item["异常率"] = item["异常数"] / item["总数"]
ranking = sorted(summary.items(), key=lambda pair: pair[1]["异常率"],
                 reverse=True)
print(ranking)
