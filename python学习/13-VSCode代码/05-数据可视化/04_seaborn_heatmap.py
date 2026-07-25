# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "温度": [20, 22, 25, 27, 30],
    "能耗": [50, 53, 58, 65, 76],
    "湿度": [70, 68, 65, 61, 58],
})
corr = df.corr(numeric_only=True)
fig, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(corr, annot=True, cmap="RdBu_r", center=0, ax=ax)
fig.tight_layout()
fig.savefig("correlation.png", dpi=300)
plt.close(fig)
