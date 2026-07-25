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
  - Spearman
  - 秩相关
  - 单调关系
aliases:
  - 斯皮尔曼秩相关系数
---

# Spearman 秩相关系数

## 1. 核心思想

把 $x,y$ 各自转为秩（排名），再计算秩的 Pearson 相关：

$$
\rho_s=\operatorname{corr}(\operatorname{rank}(X),\operatorname{rank}(Y))
$$

没有并列秩时可写为：

$$
\rho_s=1-\frac{6\sum d_i^2}{n(n^2-1)}
$$

有并列值时应使用平均秩和软件计算，不能直接套简化公式。

## 2. 它衡量什么

Spearman 衡量**单调关系**：$X$ 增大时，$Y$ 总体倾向于持续增大或减小，但不要求直线。

先升后降的 U 型或倒 U 型关系是非单调的，即使关系很强，Spearman 也可能接近 0。

## 3. Python

```python
import numpy as np
from scipy.stats import spearmanr

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

rho, p = spearmanr(x, y)
print("rho:", rho)
print("p:", p)
```

这里 Pearson 也很高，但 Spearman 恰为 1，因为排名完全一致。

## 4. 适用场景

- 等级数据；
- 偏态、离群值较多；
- 关系单调但非线性；
- 比较两种排序的稳定性；
- 综合评价新旧排名一致性。

## 5. 稳健性比较

```python
pearson = df[["x", "y"]].corr(method="pearson").iloc[0, 1]
spearman = df[["x", "y"]].corr(method="spearman").iloc[0, 1]
print(pearson, spearman)
```

差异很大时检查极端值、非线性和等级尺度。

## 6. 论文表达

> 由于指标分布明显偏态且关系呈单调非线性，采用 Spearman 秩相关。结果显示……。在稳健性检验中，以 Spearman 系数比较两种赋权方法得到的方案排序，$\rho_s=...$，说明核心排序具有较高一致性。

## 7. 易错点

- 把 Spearman 解释为“变化形状相似”。
- 忽略非单调关系。
- 把排名相关性当作绝对得分一致。
- 用它证明因果。

练习：令 $x=-3,-2,\ldots,3$，$y=x^2$，计算 Pearson 和 Spearman 并画散点图。

