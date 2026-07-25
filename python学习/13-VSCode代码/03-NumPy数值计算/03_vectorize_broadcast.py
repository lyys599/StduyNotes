# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np

X = np.array([[10, 100], [20, 120], [30, 160]], dtype=float)
minimum = X.min(axis=0)
span = X.max(axis=0) - minimum
X_scaled = (X - minimum) / span
print(X_scaled)
