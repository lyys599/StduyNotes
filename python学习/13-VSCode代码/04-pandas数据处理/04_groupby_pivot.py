# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import pandas as pd

df = pd.DataFrame({
    "地区": ["甲", "甲", "乙", "乙"],
    "季度": [1, 2, 1, 2],
    "销量": [30, 45, 28, 50],
})
summary = df.groupby("地区", as_index=False).agg(
    平均销量=("销量", "mean"),
    总销量=("销量", "sum"),
    样本量=("销量", "size"),
)
table = df.pivot_table(index="地区", columns="季度", values="销量")
print(summary)
print(table)
