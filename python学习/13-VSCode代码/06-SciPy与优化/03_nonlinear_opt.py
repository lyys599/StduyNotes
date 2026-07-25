# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np
from scipy.optimize import minimize

def objective(x):
    return (x[0] - 2) ** 2 + (x[1] - 1) ** 2

constraints = [{"type": "ineq", "fun": lambda x: x[0] + x[1] - 2}]
result = minimize(
    objective, x0=np.array([0.5, 1.5]),
    bounds=[(0, 4), (0, 4)],
    constraints=constraints, method="SLSQP",
)
if not result.success:
    raise RuntimeError(result.message)
print(result.x, result.fun)
