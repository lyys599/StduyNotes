# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
records = ["A", "B", "A", "C", "B", "A"]
counts = {}
for name in records:
    counts[name] = counts.get(name, 0) + 1
print("频数：", counts)
print("站点集合：", sorted(set(records)))
required = {"A", "B", "C", "D"}
print("缺失站点：", required - set(records))
