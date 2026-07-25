# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
from pathlib import Path
import pandas as pd

def audit_table(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "类型": df.dtypes.astype(str),
        "缺失数": df.isna().sum(),
        "缺失率": df.isna().mean(),
        "唯一值数": df.nunique(dropna=False),
    })

data = pd.DataFrame({"A": [1, 2, None], "B": ["x", "x", "y"]})
report = audit_table(data)
Path("outputs").mkdir(exist_ok=True)
report.to_csv("outputs/数据审计.csv", encoding="utf-8-sig")
print(report)
