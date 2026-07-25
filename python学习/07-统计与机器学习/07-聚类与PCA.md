---
课程: Python学习
类型: 主题笔记
难度: 必修
预计学习时间: 145分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - 统计与机器学习
---

# 聚类与PCA

> [!abstract] 学完本篇，你要能够
- 标准化后进行K-Means
- 用轮廓系数比较聚类数
- 使用PCA降维并解释方差贡献

## 核心概念

- 距离模型对尺度敏感
- 聚类标签本身没有大小意义
- PCA是线性组合而非变量筛选

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, _ = load_iris(return_X_y=True)
cluster_model = make_pipeline(
    StandardScaler(), KMeans(n_clusters=3, n_init=20, random_state=42)
)
labels = cluster_model.fit_predict(X)
X_scaled = StandardScaler().fit_transform(X)
print("轮廓系数：", silhouette_score(X_scaled, labels))
pca = PCA(n_components=2).fit(X_scaled)
print("累计贡献率：", pca.explained_variance_ratio_.sum())
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/07-统计与机器学习/07_cluster_pca.py|打开对应 `.py` 文件]]。

## 代码拆解

1. 聚类Pipeline内部完成标准化。
2. 轮廓系数在同一标准化空间计算。
3. PCA贡献率说明二维保留的信息比例。

## 数学建模中的用途

城市分型、对象画像、指标降维和综合评价前的数据结构探索常用。

## 常见报错与易错点

- 未标准化就按欧氏距离聚类。
- 看二维图主观命名类别。
- 用真实标签选择无监督模型后声称纯无监督。

## 独立练习

比较K=2至6的轮廓系数，选择K并用PCA二维图展示，描述而非过度解释簇。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- [[数学建模国赛/05-机器学习/K-Means聚类|K-Means聚类]]
- [[数学建模国赛/02-探索性分析/PCA主成分分析|PCA主成分分析]]
- [[数学建模国赛/07-模型检验/聚类评价指标|聚类评价指标]]

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
