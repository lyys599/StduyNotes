---
课程: 数学建模国赛
模块: 02-探索性分析
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 3小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - PCA
  - 降维
  - 主成分分析
aliases:
  - 主成分分析
---

# PCA 主成分分析

## 1. 核心思想

PCA 寻找一组互相正交的新坐标轴，使第一主成分解释最大方差，第二主成分在与第一正交的条件下解释剩余最大方差，依次类推。

$$
Z=XW
$$

$W$ 的列是协方差/相关矩阵的特征向量。PCA 是无监督方法，不使用目标 $y$。

## 2. 适用场景

- 连续变量多且强相关；
- 需要压缩维度、去噪或二维可视化；
- 预测比原变量解释更重要；
- 希望缓解共线性。

不适合直接声称“主成分就是某个真实因素”；载荷解释需要谨慎。

## 3. 为什么通常先标准化

若变量单位差异大，方差大的变量会主导 PCA。除非量纲本身有明确意义，一般先 [[Z-score标准化]]。

## 4. Python 完整案例

```python
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X = df[["经济", "教育", "医疗", "环境"]].dropna()

pipe = make_pipeline(
    StandardScaler(),
    PCA(n_components=0.90)
)
Z = pipe.fit_transform(X)

pca = pipe.named_steps["pca"]
print("各主成分解释方差比:", pca.explained_variance_ratio_)
print("累计解释方差:", pca.explained_variance_ratio_.cumsum())
print("保留维数:", pca.n_components_)

loadings = pd.DataFrame(
    pca.components_.T,
    index=X.columns,
    columns=[f"PC{i+1}" for i in range(pca.n_components_)]
)
print(loadings)
```

`n_components=0.90` 表示保留达到 90% 累计解释方差所需的最少主成分，不是固定保留 2 或 3 个。

## 5. 载荷与得分

- 载荷：原变量在主成分方向上的权重。
- 得分：每个样本投影到主成分后的坐标。
- 特征向量符号整体翻转不影响 PCA 结果。

若用于预测，PCA 必须在交叉验证训练折内拟合：

```python
model = make_pipeline(
    StandardScaler(),
    PCA(n_components=0.90),
    estimator
)
```

## 6. 选择主成分数

结合：

- 累计解释方差；
- 碎石图；
- 下游交叉验证性能；
- 计算与可视化需求；
- 解释性。

“95% 信息”只是常见经验，不是永远正确。

## 7. 论文表达

> 为缓解指标间共线性，先对连续变量标准化，再基于训练数据实施 PCA。累计解释方差达到 90% 时保留……个主成分。第一主成分在……变量上载荷较高，可谨慎解释为……；同时通过交叉验证比较 PCA 前后预测性能。

## 8. 易错点

- 在全数据上 PCA 后再划分。
- 把二维图好看当作模型有效。
- 主成分得分没有原单位，却被当作原指标解释。
- 自动认为前 2/3 个主成分保留 95% 方差。
- 类别编码后未经考虑直接 PCA。

练习：构造 `x2≈2*x1` 的数据，比较原变量 VIF、PCA 解释方差和回归性能。

参考：[scikit-learn PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca)。
