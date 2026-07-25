# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import pandas as pd

df = pd.DataFrame({
    "地区": ["甲", "乙", "丙", "丁"],
    "产量": [80, 120, 95, 140],
    "成本": [50, 90, 70, 100],
})
df["利润"] = df["产量"] - df["成本"]
selected = df.loc[(df["产量"] >= 100) & (df["利润"] > 25)]
print(selected.sort_values("利润", ascending=False))
