# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np

X = np.array([[80, 20, 7], [70, 15, 9], [90, 30, 6]], dtype=float)
X[:, 1] = X[:, 1].max() - X[:, 1]  # 成本型正向化
Z = X / np.sqrt((X**2).sum(axis=0))
weight = np.array([0.4, 0.3, 0.3])
V = Z * weight
d_pos = np.sqrt(((V - V.max(axis=0)) ** 2).sum(axis=1))
d_neg = np.sqrt(((V - V.min(axis=0)) ** 2).sum(axis=1))
score = d_neg / (d_pos + d_neg)
print(score, np.argsort(-score) + 1)
