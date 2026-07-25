# 完成独立尝试后再阅读本文件。
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[2]
df = pd.read_csv(root / "12-示例数据" / "环境监测数据.csv")
df["日期"] = pd.to_datetime(df["日期"])
df = df.drop_duplicates("记录ID").copy()
df["温度"] = df["温度"].fillna(df.groupby("站点")["温度"].transform("median"))
q1, q3 = df["PM2.5"].quantile([0.25, 0.75])
lower, upper = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
df["PM2.5异常"] = ~df["PM2.5"].between(lower, upper) & df["PM2.5"].notna()
df["月份"] = df["日期"].dt.to_period("M").astype(str)
summary = df.groupby(["地区", "月份"], as_index=False).agg(
    平均PM25=("PM2.5", "mean"), 样本量=("记录ID", "size")
)
output = root / "tmp" / "pandas练习结果.xlsx"
output.parent.mkdir(exist_ok=True)
with pd.ExcelWriter(output, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="清洗数据", index=False)
    df.loc[df["PM2.5异常"]].to_excel(writer, sheet_name="异常记录", index=False)
    summary.to_excel(writer, sheet_name="统计汇总", index=False)
print(output)
