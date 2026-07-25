---
课程: 数学建模国赛
模块: 02-探索性分析
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 1.5小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - Pearson
  - 相关分析
  - 线性关系
aliases:
  - 皮尔逊相关系数
---

# Pearson 相关系数

## 1. 定义

$$
r=\frac{\sum_{i=1}^{n}(x_i-\bar x)(y_i-\bar y)}
{\sqrt{\sum_{i=1}^{n}(x_i-\bar x)^2}
\sqrt{\sum_{i=1}^{n}(y_i-\bar y)^2}}
$$

上式中分母应理解为两个平方根的**乘积**：

$$
r=\frac{\sum (x_i-\bar x)(y_i-\bar y)}
{\sqrt{\sum (x_i-\bar x)^2\sum (y_i-\bar y)^2}}
$$

$r\in[-1,1]$，衡量线性关联方向与强度。

## 2. 适用边界

- 两个数值变量；
- 关系大致线性；
- 极端值会强烈影响结果；
- 计算 $r$ 本身不要求变量正态；
- 经典显著性检验通常需要独立同分布、二元正态等更强条件。

相关系数接近 0 仍可能存在强非线性关系。

## 3. Python 案例

```python
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 8])

result = pearsonr(x, y)
print("r:", result.statistic)
print("p:", result.pvalue)

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```

先看散点图，再解释 $r$。

## 4. 多变量矩阵

```python
corr = df.select_dtypes("number").corr(method="pearson")
```

多次检验很多变量对会增加假阳性；必要时采用 FDR 校正，并把相关热图视为探索证据。

## 5. 论文表达

> 变量 A 与 B 呈中等强度正线性相关（$r=...$，95% CI ...）。散点图未见明显非线性结构，但存在少量高杠杆点；删除这些点后的相关系数为……，方向保持一致。

不要只写“显著相关”，还要报告方向、大小、区间和图形。

## 6. 易错点

- 把相关解释为因果。
- 忽略共同时间趋势造成的伪相关。
- 对无序类别编码后计算 Pearson。
- 只看 p 值，不看效应大小。
- 用相关矩阵替代 [[VIF多重共线性检测]]。

关联：[[Spearman秩相关系数]]、[[线性回归]]。

