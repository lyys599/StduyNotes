---
课程: 数学建模国赛
模块: 05-机器学习
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 建议掌握
预计学习时间: 3小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - DBSCAN
  - 密度聚类
  - 异常检测
aliases:
  - Density-Based Clustering
---

# DBSCAN 聚类

## 1. 三类点

- 核心点：$\varepsilon$ 邻域内至少有 `min_samples` 个点；
- 边界点：自身不是核心点，但落在某核心点邻域；
- 噪声点：不属于任何簇，标签为 -1。

它可发现任意形状簇，不需预先指定簇数，但对密度不均和高维距离退化敏感。

## 2. Python 案例

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

X_scaled = StandardScaler().fit_transform(X)

model = DBSCAN(
    eps=0.5,
    min_samples=5
)
labels = model.fit_predict(X_scaled)

mask = labels != -1
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print("簇数:", n_clusters)
print("噪声比例:", (labels == -1).mean())

if n_clusters >= 2 and mask.sum() > n_clusters:
    print("非噪声轮廓系数:",
          silhouette_score(X_scaled[mask], labels[mask]))
```

排除噪声计算轮廓系数会使结果变乐观，应同时报告噪声比例。

## 3. 参数选择

- `min_samples`：越大，核心点要求越严格；
- `eps`：邻域半径，过小噪声多，过大簇合并。

可画第 $k$ 近邻距离曲线找拐点：

```python
import numpy as np
from sklearn.neighbors import NearestNeighbors

k = 5
nn = NearestNeighbors(n_neighbors=k).fit(X_scaled)
distances, _ = nn.kneighbors(X_scaled)
kdist = np.sort(distances[:, -1])
```

拐点只是候选，还要结合稳定性和解释。

## 4. 与 K-Means

| 特性 | K-Means | DBSCAN |
|---|---|---|
| 簇形状 | 近似球状 | 任意形状 |
| 簇数 | 预先给 K | 自动产生 |
| 噪声 | 敏感 | 可标记 |
| 密度不均 | 有时可用 | 容易失败 |
| 高维 | 同样困难 | 距离退化明显 |

## 5. 论文表达

> 数据散点显示簇形状非球状并含噪声，故采用 DBSCAN。连续特征标准化后，通过 k-distance 曲线与稳定性分析选择 $\varepsilon$ 和 `min_samples`。得到……个簇，噪声比例为……。

## 6. 易错点

- 未标准化。
- 把 -1 全部删除而不解释。
- 只为得到理想簇数调 eps。
- 高维直接使用欧氏距离。
- 用固定样本量阈值判断能否使用。

参考：Ester et al. (1996)；[scikit-learn DBSCAN](https://scikit-learn.org/stable/modules/clustering.html#dbscan)。

