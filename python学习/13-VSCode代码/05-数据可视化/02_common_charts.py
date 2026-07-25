# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
x = rng.normal(size=100)
y = 2 * x + rng.normal(scale=0.8, size=100)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].scatter(x, y, alpha=0.7)
axes[0].set(xlabel="特征X", ylabel="目标Y", title="关系")
axes[1].hist(y, bins=12, edgecolor="white")
axes[1].set(title="目标变量分布")
fig.tight_layout()
fig.savefig("distribution.png", dpi=300)
plt.close(fig)
