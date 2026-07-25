# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import pandas as pd

city = pd.DataFrame({"城市ID": [1, 2], "城市": ["甲", "乙"]})
yearly = pd.DataFrame({
    "城市ID": [1, 1, 2, 2],
    "年份": [2025, 2026, 2025, 2026],
    "指标": [10, 12, 8, 11],
})
merged = yearly.merge(
    city, on="城市ID", how="left", validate="many_to_one",
    indicator=True,
)
print(merged)
print(merged["_merge"].value_counts())
