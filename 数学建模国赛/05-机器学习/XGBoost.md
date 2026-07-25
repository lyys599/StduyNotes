---
课程: 数学建模国赛
模块: 05-机器学习
文件类型: 方法笔记
来源范围: PDF原有+扩展
优先级: 建议掌握
预计学习时间: 3小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - XGBoost
  - Boosting
  - 表格数据
aliases:
  - 梯度提升树
---

# XGBoost

## 1. 原理

XGBoost 逐轮添加新树去拟合当前损失的梯度，每棵新树修正已有模型。目标函数包含训练损失和树复杂度正则项。

与随机森林并行平均多棵树不同，Boosting 是顺序纠错，精度常高但更易因调参不当过拟合。

## 2. 安装与案例

```bash
python -m pip install xgboost
```

```python
from xgboost import XGBRegressor
from sklearn.model_selection import cross_validate, KFold

model = XGBRegressor(
    n_estimators=400,
    max_depth=3,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_lambda=1.0,
    objective="reg:squarederror",
    random_state=42,
    n_jobs=-1
)

cv = KFold(5, shuffle=True, random_state=42)
scores = cross_validate(
    model,
    X,
    y,
    cv=cv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1
)
print(-scores["test_score"].mean())
```

## 3. 参数逻辑

- `learning_rate` 小：每棵树贡献小，通常需更多树；
- `max_depth` 大：交互复杂，也更易过拟合；
- `subsample`、`colsample_bytree`：增加随机性；
- `reg_alpha`、`reg_lambda`：L1/L2 正则；
- `min_child_weight`：限制过小节点。

优先调学习率、树数、深度和采样比例，不要一次搜索几十个参数。

## 4. 早停

早停需设置独立验证集，并确保预处理只由训练部分拟合。具体接口随 XGBoost 版本可能变化，比赛前按锁定版本的官方文档测试，不要在测试集上早停。

## 5. 论文表达

> 采用 XGBoost 捕捉非线性和高阶交互。以较小学习率配合更多弱树，并通过交叉验证选择深度和采样比例。相较随机森林，验证 MAE 改善……；同时通过 SHAP/Permutation importance 分析主要特征。

## 6. 易错点

- 使用默认参数就称为“最优 XGBoost”。
- 用测试集早停。
- 高基数编号列被模型记忆。
- 只看 gain importance。
- 小数据上追求复杂模型而不比较线性基线。

参考：Chen & Guestrin (2016)；[XGBoost 文档](https://xgboost.readthedocs.io/en/stable/)。

