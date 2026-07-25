---
课程: 数学建模国赛
模块: 03-统计与预测
文件类型: 方法笔记
来源范围: PDF原有+扩展
优先级: 必须掌握
预计学习时间: 2.5小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - ANOVA
  - 方差分析
  - F检验
aliases:
  - 单因素方差分析
---

# 方差分析 ANOVA

## 1. 回答什么

单因素 ANOVA 检验多个独立组的总体均值是否全部相同：

$$
H_0:\mu_1=\mu_2=\cdots=\mu_k
$$

F 统计量比较组间变异与组内变异。显著只说明至少一组不同，不告诉具体哪组。

## 2. Python 案例

```python
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

df = pd.DataFrame({
    "方案": ["A"] * 5 + ["B"] * 5 + ["C"] * 5,
    "得分": [70, 72, 68, 71, 69,
           75, 78, 74, 76, 77,
           82, 80, 85, 83, 81]
})

model = ols("得分 ~ C(方案)", data=df).fit()
print(sm.stats.anova_lm(model, typ=2))

posthoc = pairwise_tukeyhsd(df["得分"], df["方案"])
print(posthoc)
```

## 3. 假设

- 观测独立；
- 各组误差近似正态；
- 方差齐性。

方差不齐时优先 Welch ANOVA；严重偏态或等级数据可用 [[非参数检验|Kruskal-Wallis]]。

## 4. 双因素与交互

```python
model = ols(
    "得分 ~ C(方案) * C(地区)",
    data=df
).fit()
```

`*` 包含两个主效应和交互项。交互显著时，主效应不能脱离另一个因素简单解释。

## 5. 事后比较

总体 F 显著后，再用 Tukey HSD 等校正方法比较组对。不要未经校正地做大量 t 检验。

## 6. 论文表达

> 单因素 ANOVA 显示三种方案均值不完全相同（$F=...$，$p=...$，效应量 $\eta^2=...$）。Tukey 事后比较表明 C 相比 A、B 显著更高，而 A 与 B 差异不显著。

## 7. 易错点

- 把 ANOVA 与线性回归整体 F 检验混为一谈；二者数学有关联但问题表述不同。
- 总体显著后直接说每组都不同。
- 忽略重复测量设计。
- 有交互却只报告主效应。

