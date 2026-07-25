# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np

A = np.array([[2.0, 1.0], [1.0, 3.0]])
b = np.array([8.0, 13.0])
x = np.linalg.solve(A, b)
print("方程解：", x)
print("验证：", A @ x)
eigenvalues = np.linalg.eigvalsh(A)
print("特征值：", eigenvalues)
