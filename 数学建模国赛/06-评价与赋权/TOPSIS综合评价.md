---
课程: 数学建模国赛
模块: 06-评价与赋权
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 3小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - TOPSIS
  - 综合评价
  - 排序
aliases:
  - 优劣解距离法
---

# TOPSIS 综合评价

## 1. 核心思想

方案越接近正理想解、越远离负理想解越好。

对正向化、规范化并加权后的矩阵 $V=(v_{ij})$：

$$
v_j^+=\max_i v_{ij},\quad v_j^-=\min_i v_{ij}
$$

$$
D_i^+=\sqrt{\sum_j(v_{ij}-v_j^+)^2}
$$

$$
D_i^-=\sqrt{\sum_j(v_{ij}-v_j^-)^2}
$$

贴近度：

$$
C_i=\frac{D_i^-}{D_i^++D_i^-}
$$

$C_i$ 越大，方案相对越优。

## 2. Python 完整案例

```python
import numpy as np
import pandas as pd

X = pd.DataFrame({
    "收益": [80, 70, 90],
    "成本": [40, 30, 60],
    "满意度": [85, 88, 82]
}, index=["方案A", "方案B", "方案C"])

# 正向化：成本越小越好
Y = X.copy().astype(float)
Y["成本"] = Y["成本"].max() - Y["成本"]

# 向量规范化
Z = Y / np.sqrt((Y ** 2).sum(axis=0))

weights = pd.Series(
    [0.4, 0.3, 0.3],
    index=Z.columns
)
V = Z * weights

best = V.max(axis=0)
worst = V.min(axis=0)
d_best = np.sqrt(((V - best) ** 2).sum(axis=1))
d_worst = np.sqrt(((V - worst) ** 2).sum(axis=1))
score = d_worst / (d_best + d_worst)

result = pd.DataFrame({
    "贴近度": score,
    "排名": score.rank(ascending=False, method="min")
}).sort_values("排名")
print(result)
```

## 3. 权重来源

可来自 AHP、熵权、CRITIC 或组合赋权。TOPSIS 是综合排序方法，不负责证明权重正确。

## 4. 相对性与排序反转

理想解取决于当前方案集合。加入或删除方案可能改变理想点与排序，因此贴近度不是绝对质量。应检查：

- 权重扰动；
- 规范化方法；
- 增删方案；
- 异常值；
- 替代赋权方法。

## 5. 论文表达

> 指标正向化并向量规范化后，采用……权重构造加权矩阵。计算各方案到正、负理想解的欧氏距离及贴近度。方案 A 的贴近度最高。对权重 ±10% 扰动和替代赋权后，其排名保持……。

## 6. 易错点

- 写成“TOPISIS”。
- 成本指标未正向化。
- 权重与列顺序错位。
- 分子误用 $D_i^+$。
- 把相对排名说成绝对优劣。

关联：[[熵权法]]、[[CRITIC赋权法]]、[[敏感性分析]]。

