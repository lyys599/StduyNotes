# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
from pathlib import Path
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2.1, 3.4, 3.0, 4.8]
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, marker="o", label="观测值")
ax.set(xlabel="时间", ylabel="指标", title="指标变化趋势")
ax.legend()
fig.tight_layout()
fig.savefig(Path("trend.png"), dpi=300, bbox_inches="tight")
plt.close(fig)
