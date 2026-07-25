# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np

x = np.array([12, 15, 18, 21], dtype=float)
X = np.array([[1.2, 3.4], [2.0, 4.1], [3.2, 5.0]])
print(x.shape, x.ndim, x.dtype)
print(X.shape)
print("每列均值：", X.mean(axis=0))
