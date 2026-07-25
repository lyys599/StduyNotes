# 完成独立尝试后再阅读本文件。
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

root = Path(__file__).resolve().parents[2]
df = pd.read_csv(root / "12-示例数据" / "环境监测数据.csv",
                 parse_dates=["日期"])
output = root / "tmp" / "eda_panel.png"
output.parent.mkdir(exist_ok=True)
fig, axes = plt.subplots(2, 2, figsize=(11, 8))
daily = df.groupby("日期", as_index=False)["PM2.5"].mean()
axes[0, 0].plot(daily["日期"], daily["PM2.5"])
axes[0, 0].set(title="日均PM2.5趋势", ylabel="μg/m³")
axes[0, 1].hist(df["PM2.5"].dropna(), bins=15)
axes[0, 1].set(title="PM2.5分布")
sns.boxplot(data=df, x="地区", y="PM2.5", ax=axes[1, 0])
corr = df.select_dtypes("number").corr()
sns.heatmap(corr, cmap="RdBu_r", center=0, ax=axes[1, 1])
fig.tight_layout()
fig.savefig(output, dpi=300, bbox_inches="tight")
plt.close(fig)
print(output)
