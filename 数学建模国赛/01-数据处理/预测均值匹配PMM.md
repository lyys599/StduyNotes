---
课程: 数学建模国赛
模块: 01-数据处理
文件类型: 方法笔记
来源范围: PDF原有+扩展
优先级: 建议掌握
预计学习时间: 2小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - PMM
  - 缺失值
  - MICE
aliases:
  - 预测均值匹配
---

# 预测均值匹配 PMM

## 1. 核心思想

PMM 不直接把回归预测值填入缺口。它先预测每个观测和缺失样本的条件均值，再从“预测值最接近”的若干已观测样本中随机选择一个真实值作为供体。

```mermaid
flowchart LR
    A["拟合目标变量回归"] --> B["预测观测与缺失样本"]
    B --> C["为缺失样本找k个近邻供体"]
    C --> D["随机抽一个真实观测值"]
    D --> E["填入缺口"]
```

这样插补值来自真实观测范围，常比直接线性回归插补更能保持偏态、边界和离散形态。

## 2. 简化 Python 演示

下面只演示单变量的一次 PMM，不等同于完整 MICE：

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def pmm_once(df, target, predictors, k=5, seed=42):
    out = df.copy()
    obs = out[target].notna()
    mis = ~obs

    if out.loc[:, predictors].isna().any().any():
        raise ValueError("演示函数要求预测变量无缺失")

    model = LinearRegression().fit(
        out.loc[obs, predictors],
        out.loc[obs, target]
    )

    pred_obs = model.predict(out.loc[obs, predictors])
    pred_mis = model.predict(out.loc[mis, predictors])
    y_obs = out.loc[obs, target].to_numpy()
    rng = np.random.default_rng(seed)

    for row_index, predicted in zip(out.index[mis], pred_mis):
        donor_pos = np.argsort(np.abs(pred_obs - predicted))[:k]
        out.loc[row_index, target] = rng.choice(y_obs[donor_pos])

    return out
```

完整多重插补应在链式迭代中重复、加入参数不确定性并生成多份数据，详见[[MICE多重插补]]。

## 3. R 中用于 MICE

```r
library(mice)

imp <- mice(
  data,
  m = 10,
  maxit = 20,
  method = "pmm",
  seed = 42
)
```

实际数据中不同变量类型应设置不同方法，而不是整张表全部强制 PMM。

## 4. 参数与条件

- 供体数 $k$ 常取 3～10，要做敏感性检查；
- 预测变量应包含与缺失机制和目标相关的信息；
- 样本太小或局部无相似供体时不稳定；
- PMM 不要求残差严格正态，但回归预测结构仍可能设错；
- 它不能自动解决 MNAR。

## 5. 论文表达

> 对右偏连续变量采用 MICE-PMM。每个缺失位置从预测均值最接近的 5 个已观测供体中随机抽取真实值，从而避免回归插补产生超出观测范围或过度平滑的数值。供体数改为 3 和 10 时核心结论保持稳定。

## 6. 易错点

- 把 PMM 说成“无需任何假设”。
- 只做一次 PMM，却称为多重插补。
- 供体数无说明。
- 预测变量自身缺失却不纳入链式处理。
- 将插补值当作真实观测，不传播不确定性。

