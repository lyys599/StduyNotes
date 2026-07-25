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
  - 归一化
  - MinMax
  - 预处理
aliases:
  - MinMaxScaler
---

# Min-Max 归一化

## 1. 公式

映射到 $[0,1]$：

$$
x_i'=\frac{x_i-x_{\min}}{x_{\max}-x_{\min}}
$$

它保留线性比例和排序，但对极端最小/最大值敏感。测试集出现超出训练范围的值时，结果可小于 0 或大于 1；这不是程序错误。

## 2. 适用场景

- 神经网络或需要固定输入范围的算法；
- 图像像素等已知边界变量；
- TOPSIS 等评价方法的某些规范化步骤；
- 希望特征处在统一有限范围。

综合评价中的“向量归一化”不等于 Min-Max，详见[[指标正向化与无量纲化]]。

## 3. Python

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Pipeline 用法：

```python
from sklearn.pipeline import make_pipeline

model = make_pipeline(
    MinMaxScaler(),
    estimator
)
```

## 4. 常数列

若 $x_{\max}=x_{\min}$，手算公式分母为 0。scikit-learn 会将其映射到范围下界附近，但常数列通常没有预测信息，应在质量审计中标记。

## 5. 论文表达

> 对需要固定范围的连续指标，以训练集最小值和最大值估计 Min-Max 变换参数，并将相同参数应用于验证和测试数据，避免未来信息泄漏。

## 6. 与 Z-score 选择

| 需求 | 推荐 |
|---|---|
| 均值方差统一、线性/SVM/PCA | [[Z-score标准化]] |
| 固定区间、已知边界 | Min-Max |
| 极端值很多 | 先核查异常，或比较 RobustScaler |
| 树模型 | 通常不需要 |

练习：训练集为 `[0, 10, 20]`，测试值为 30。手算其归一化结果并解释为什么大于 1。

