# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import math
import numpy as np

rng = np.random.default_rng(42)
current = rng.uniform(-5, 5)
best = current
temperature = 10.0
objective = lambda x: x**2 + 4 * np.sin(3 * x)
while temperature > 1e-3:
    candidate = current + rng.normal(0, temperature / 5)
    delta = objective(candidate) - objective(current)
    if delta < 0 or rng.random() < math.exp(-delta / temperature):
        current = candidate
    if objective(current) < objective(best):
        best = current
    temperature *= 0.98
print(best, objective(best))
