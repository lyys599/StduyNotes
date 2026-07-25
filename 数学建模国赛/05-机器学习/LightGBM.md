---
课程: 数学建模国赛
模块: 05-机器学习
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 了解即可
预计学习时间: 2.5小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - LightGBM
  - Boosting
  - 大规模表格
aliases:
  - LGBM
---

# LightGBM

## 1. 定位

LightGBM 是高效的梯度提升树实现，使用直方图算法与叶子优先生长等设计，在大规模表格数据上速度和内存表现突出。它并非只适合大数据，也不能因为数据小就判定不可用，但小数据上更容易因叶子生长过深而过拟合。

## 2. 安装与案例

```bash
python -m pip install lightgbm
```

```python
from lightgbm import LGBMRegressor
from sklearn.model_selection import cross_validate, KFold

model = LGBMRegressor(
    n_estimators=400,
    learning_rate=0.05,
    num_leaves=15,
    min_child_samples=20,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_lambda=1.0,
    random_state=42,
    n_jobs=-1,
    verbosity=-1
)

cv = KFold(5, shuffle=True, random_state=42)
scores = cross_validate(
    model,
    X,
    y,
    cv=cv,
    scoring="neg_mean_absolute_error"
)
print(-scores["test_score"].mean())
```

## 3. 关键参数

- `num_leaves`：叶子数，决定复杂度；
- `max_depth`：可限制深度；
- `min_child_samples`：叶节点最小样本；
- `learning_rate` 与 `n_estimators`；
- 行/列采样；
- L1/L2 正则。

## 4. 类别特征

LightGBM 可原生处理类别特征，但 pandas 类别类型、类别索引和交叉验证流程必须一致。新手为稳定复现，也可先使用统一的编码 Pipeline。

## 5. 论文表达

> 由于样本量和特征维度较大，使用 LightGBM 作为高效提升树模型。通过限制叶子数和叶节点最小样本控制复杂度，并在相同交叉验证下与 XGBoost、随机森林比较。

## 6. 易错点

- 把 `num_leaves` 设很大而不控制深度。
- 只因为速度快就认为效果一定好。
- 类别编码在训练和测试不一致。
- 不记录版本，导致复现差异。

参考：Ke et al. (2017)；[LightGBM 文档](https://lightgbm.readthedocs.io/en/stable/)。

