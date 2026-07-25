# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np

X = np.array([[10, 2], [15, 8], [20, 4], [25, 9]])
print("第一列：", X[:, 0])
mask = (X[:, 0] >= 15) & (X[:, 1] < 9)
selected = X[mask]
print(selected)
