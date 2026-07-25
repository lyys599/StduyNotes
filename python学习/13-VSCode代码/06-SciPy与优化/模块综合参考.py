# 完成独立尝试后再阅读本文件。
import numpy as np
from scipy.optimize import linprog

profit = np.array([5, 7, 4], dtype=float)
resources = np.array([[2, 3, 1], [1, 2, 2]], dtype=float)
limits = np.array([180, 120], dtype=float)
result = linprog(
    -profit, A_ub=resources, b_ub=limits,
    bounds=[(0, None)] * 3, method="highs"
)
if not result.success:
    raise RuntimeError(result.message)
print("方案：", result.x)
print("利润：", -result.fun)
print("资源消耗：", resources @ result.x)
print("剩余资源：", limits - resources @ result.x)
