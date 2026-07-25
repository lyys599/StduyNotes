# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import pandas as pd

df = pd.DataFrame({
    "日期": ["2026-01-01", "2026-01-03", "2026-01-02"],
    "值": [10, 14, 12],
})
df["日期"] = pd.to_datetime(df["日期"])
df = df.sort_values("日期").set_index("日期")
daily = df.resample("D").mean().interpolate()
daily["星期"] = daily.index.dayofweek
print(daily)
