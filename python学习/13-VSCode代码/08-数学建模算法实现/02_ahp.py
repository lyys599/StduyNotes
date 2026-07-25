# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np

A = np.array([[1, 3, 5], [1/3, 1, 2], [1/5, 1/2, 1]], dtype=float)
eigenvalues, eigenvectors = np.linalg.eig(A)
index = np.argmax(eigenvalues.real)
weight = np.abs(eigenvectors[:, index].real)
weight /= weight.sum()
n = len(A)
ci = (eigenvalues[index].real - n) / (n - 1)
ri = {3: 0.58}[n]
cr = ci / ri
print(weight, cr)
