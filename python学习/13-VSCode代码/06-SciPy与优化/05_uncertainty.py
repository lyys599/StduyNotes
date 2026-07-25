# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np

rng = np.random.default_rng(42)
demand = rng.normal(1000, 80, size=50_000)
unit_cost = rng.triangular(8, 10, 13, size=50_000)
total_cost = np.maximum(demand, 0) * unit_cost
q = np.quantile(total_cost, [0.025, 0.5, 0.975])
print("成本2.5%、50%、97.5%分位数：", q)
print("超过13000概率：", (total_cost > 13000).mean())
