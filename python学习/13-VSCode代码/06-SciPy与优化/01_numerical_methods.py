# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import root_scalar
from scipy.integrate import quad

x = np.array([0, 1, 2, 3], dtype=float)
y = np.array([0, 1, 4, 9], dtype=float)
f = interp1d(x, y, kind="linear")
print("插值：", float(f(1.5)))
root = root_scalar(lambda z: z**2 - 2, bracket=[1, 2])
area, error = quad(lambda z: np.exp(-z**2), 0, 1)
print(root.root, area, error)
