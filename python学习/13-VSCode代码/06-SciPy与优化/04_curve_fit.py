# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np
from scipy.optimize import curve_fit

def growth(t, capacity, rate):
    return capacity * (1 - np.exp(-rate * t))

t = np.arange(1, 9, dtype=float)
y = np.array([18, 31, 43, 53, 61, 67, 72, 76], dtype=float)
params, covariance = curve_fit(
    growth, t, y, p0=[90, 0.25], bounds=(0, np.inf)
)
standard_errors = np.sqrt(np.diag(covariance))
print(params, standard_errors)
