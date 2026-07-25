# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np

rng = np.random.default_rng(42)
sample = np.array([12, 15, 14, 18, 20, 17, 16], dtype=float)
bootstrap_means = np.empty(5000)
for i in range(len(bootstrap_means)):
    resample = rng.choice(sample, size=len(sample), replace=True)
    bootstrap_means[i] = resample.mean()
interval = np.quantile(bootstrap_means, [0.025, 0.975])
print("均值：", sample.mean())
print("Bootstrap 95%区间：", interval)
