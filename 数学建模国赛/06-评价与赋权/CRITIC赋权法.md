---
课程: 数学建模国赛
模块: 06-评价与赋权
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 2.5小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - CRITIC
  - 客观赋权
  - 相关性
aliases:
  - CRITIC法
---

# CRITIC 赋权法

## 1. 核心思想

CRITIC 同时考虑：

- 对比强度：指标标准差 $s_j$；
- 冲突性：与其他指标相关越低，提供的新信息越多。

$$
C_j=s_j\sum_{k=1}^{m}(1-r_{jk})
$$

$$
w_j=\frac{C_j}{\sum_jC_j}
$$

## 2. Python

```python
import numpy as np
import pandas as pd

def critic_weights(Z: pd.DataFrame) -> pd.Series:
    X = Z.astype(float)
    std = X.std(axis=0, ddof=1)
    corr = X.corr(method="pearson")
    conflict = (1 - corr).sum(axis=1)
    info = std * conflict

    if np.isclose(info.sum(), 0):
        raise ValueError("指标无区分信息或存在退化")

    return info / info.sum()

print(critic_weights(Z))
```

输入必须先正向化和同尺度化，否则标准差无法公平比较。

## 3. 如何解释

一个指标权重高，可能因为：

- 在方案间变化大；
- 与其他指标不重复；
- 二者同时存在。

它不代表业务上“更重要”或有因果影响。

## 4. 相关系数选择

经典 CRITIC 使用 Pearson。若指标严重偏态或关系单调非线性，可将 Spearman 作为稳健性变体，但要明确说明这不是经典原式。

## 5. 极端值与相关性

PDF 中“极端值提高标准差但降低 $1-r$，可相互缓解”不是可靠保证。极端值可能同时扭曲标准差和相关系数，仍需异常核查与敏感性分析。

## 6. 论文表达

> CRITIC 权重同时考虑指标变异和信息冲突。输入矩阵经正向化与 Min-Max 处理。指标 A 因差异较大且与其余指标相关较低获得较高权重。对极端值截尾并用 Spearman 冲突项重算后，排序……。

## 7. 易错点

- 未无量纲化。
- 常数列造成标准差为 0/相关为 NaN。
- 把相关高等同于指标无用。
- 不说明 Pearson/Spearman 选择。
- 把数据权重当政策偏好。

参考：Diakoulaki et al. (1995)。

