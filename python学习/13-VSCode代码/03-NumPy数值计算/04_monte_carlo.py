# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np

rng = np.random.default_rng(42)
points = rng.uniform(-1, 1, size=(100_000, 2))
inside = (points[:, 0] ** 2 + points[:, 1] ** 2) <= 1
pi_estimate = 4 * inside.mean()
print(f"圆周率估计：{pi_estimate:.5f}")
