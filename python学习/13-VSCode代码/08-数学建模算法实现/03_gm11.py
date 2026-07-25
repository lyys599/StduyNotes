# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np

x0 = np.array([12, 15, 19, 24, 30], dtype=float)
x1 = np.cumsum(x0)
z1 = -0.5 * (x1[1:] + x1[:-1])
B = np.column_stack([z1, np.ones(len(z1))])
a, b = np.linalg.lstsq(B, x0[1:], rcond=None)[0]
x1_hat = (x0[0] - b / a) * np.exp(-a * np.arange(len(x0) + 2)) + b / a
x0_hat = np.r_[x1_hat[0], np.diff(x1_hat)]
print("参数：", a, b)
print("拟合与未来：", x0_hat)
