# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np
from scipy import stats

a = np.array([72, 75, 71, 78, 74, 77], dtype=float)
b = np.array([68, 70, 72, 69, 71, 70], dtype=float)
result = stats.ttest_ind(a, b, equal_var=False)
pooled = np.sqrt((a.var(ddof=1) + b.var(ddof=1)) / 2)
effect = (a.mean() - b.mean()) / pooled
print("t与p：", result.statistic, result.pvalue)
print("标准化效应量：", effect)
