---
课程: 数学建模国赛
模块: 01-数据处理
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 1小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - 标准化
  - Z-score
  - 预处理
aliases:
  - StandardScaler
---

# Z-score 标准化

## 1. 公式与含义

$$
z_i=\frac{x_i-\bar x}{s}
$$

转换后训练样本均值约为 0、标准差约为 1。它消除量纲差异，但**不会把任意分布变成正态分布**，排序和分布形状仍基本保留。

## 2. 什么时候需要

通常需要：

- 岭/Lasso/Logistic 等带正则化的线性模型；
- SVM、K-Means、KNN 等基于距离的方法；
- PCA；
- 梯度优化对尺度敏感的模型。

通常不必：

- 决策树、随机森林、XGBoost、LightGBM。

## 3. 正确代码

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

`fit_transform` 只用于训练集；测试集只能 `transform`。

更推荐放进 Pipeline：

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

model = make_pipeline(
    StandardScaler(),
    Ridge(alpha=1.0)
)
model.fit(X_train, y_train)
pred = model.predict(X_test)
```

## 4. 异常值问题

均值和标准差对极端值敏感。异常值真实且不能删除时，可比较：

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
```

它使用中位数和四分位距，但含义不再是标准 Z 分数。

## 5. 论文表达

> 为避免不同量纲影响距离和正则化惩罚，本文在每个训练折内估计均值与标准差，并对训练集和验证/测试集应用同一变换。树模型不进行尺度缩放。

## 6. 易错点

- 在全数据上 `fit_transform`。
- 连目标变量一起标准化后忘记逆变换。
- 对 0/1 哑变量一律标准化，却未考虑模型需求。
- 声称标准化后“服从标准正态分布”。

练习：对 `[1, 2, 3, 100]` 标准化，再删除 100 重新标准化，观察均值和标准差对结果的影响。

