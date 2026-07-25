# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import pandas as pd

df = pd.DataFrame({"值": [10, 11, None, 12, 80, 12]})
q1, q3 = df["值"].quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
df["异常"] = ~df["值"].between(lower, upper) & df["值"].notna()
df["值_填补"] = df["值"].fillna(df["值"].median())
print(df)
