# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np
from scipy.optimize import linprog

c = np.array([-3.0, -5.0])
A_ub = np.array([[2, 1], [1, 3]], dtype=float)
b_ub = np.array([100, 90], dtype=float)
result = linprog(c, A_ub=A_ub, b_ub=b_ub,
                 bounds=[(0, None), (0, None)], method="highs")
if not result.success:
    raise RuntimeError(result.message)
print("方案：", result.x)
print("最大利润：", -result.fun)
print("剩余资源：", result.ineqlin.residual)
