# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[2]
path = root / "12-示例数据" / "环境监测数据.csv"
df = pd.read_csv(path)
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe(include="all"))
