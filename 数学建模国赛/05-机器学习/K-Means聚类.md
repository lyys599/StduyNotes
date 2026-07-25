---
课程: 数学建模国赛
模块: 05-机器学习
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 3小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - K-Means
  - 聚类
  - 无监督学习
aliases:
  - K均值聚类
---

# K-Means 聚类

## 1. 目标

将样本分为 $K$ 簇，最小化簇内平方距离：

$$
\min\sum_{k=1}^{K}\sum_{x_i\in C_k}\|x_i-\mu_k\|^2
$$

适合近似球状、尺度相近、没有大量异常点的簇。

## 2. Python 案例

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

model = make_pipeline(
    StandardScaler(),
    KMeans(
        n_clusters=3,
        n_init=20,
        random_state=42
    )
)

labels = model.fit_predict(X)
X_scaled = model.named_steps["standardscaler"].transform(X)
print("轮廓系数:", silhouette_score(X_scaled, labels))
```

必须在与聚类使用相同的空间中计算轮廓系数。

## 3. 如何选择 K

- 肘部法：簇内平方和边际改善；
- 平均轮廓系数；
- Gap statistic；
- 多随机种子/Bootstrap 稳定性；
- 业务可解释性与可执行性。

不要只凭一张肘部图。

## 4. 聚类后的业务解释

```python
profile = (
    X.assign(cluster=labels)
     .groupby("cluster")
     .agg(["mean", "median", "count"])
)
print(profile)
```

根据各簇画像命名，如“高投入高产出”，不要叫“第一类最好”而缺乏依据。

## 5. 重要边界

- 标签 0/1/2 没有大小顺序；
- 聚类是探索结构，不是发现天然真类；
- 初始点、尺度、异常值和特征选择会改变结果；
- 没有固定的最佳样本量范围。

## 6. 论文表达

> 对连续特征标准化后实施 K-Means。综合轮廓系数、肘部曲线、不同随机种子的稳定性和业务可解释性选择 $K=...$。各簇分别表现为……，并通过重抽样匹配检查聚类稳定性。

## 7. 易错点

- 未标准化。
- 把编号和无序类别当欧氏距离。
- 只运行一次 `n_init=1`。
- 先 PCA 到二维只为画图，再误以为二维聚类就是原空间结果。

关联：[[DBSCAN聚类]]、[[聚类评价指标]]。

