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
  - SVM
  - 支持向量机
  - 核方法
aliases:
  - Support Vector Machine
---

# 支持向量机 SVM

## 1. 核心思想

线性 SVM 寻找最大间隔分类超平面；核技巧把非线性关系隐式映射到高维。支持向量是决定边界的关键样本。

没有通用“只适合 3000 以下样本”的硬阈值。核 SVM 的时间/内存随样本增长较快，大数据可用线性 SVM 或其他模型。

## 2. Pipeline 分类案例

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

pipe = make_pipeline(
    StandardScaler(),
    SVC(
        kernel="rbf",
        probability=True,
        class_weight="balanced",
        random_state=42
    )
)

search = GridSearchCV(
    pipe,
    {
        "svc__C": [0.1, 1, 10],
        "svc__gamma": ["scale", 0.01, 0.1]
    },
    cv=5,
    scoring="f1"
)
search.fit(X_train, y_train)
print(search.best_params_)
```

SVM 基于距离/内积，对尺度敏感，通常必须标准化。

## 3. 参数直觉

- $C$ 大：更重视训练误差，边界复杂；
- $C$ 小：更强正则、更宽容；
- RBF 的 $\gamma$ 大：每个样本影响范围小，边界更弯曲；
- $\gamma$ 小：边界更平滑。

## 4. 回归与异常检测

- `SVR`：支持向量回归；
- `OneClassSVM`：新颖点/异常检测。

不要把同一参数解释直接照搬到所有变体。

## 5. 概率与阈值

`probability=True` 会增加训练开销，概率还应检查校准。若只需决策分数，可使用 `decision_function`。

## 6. 论文表达

> 特征维度适中且关系可能非线性，故比较 RBF-SVM。所有连续变量在训练折内标准化，通过交叉验证选择 $C$ 和 $\gamma$。最终模型 F1 为……，并与 Logistic 基线比较。

## 7. 易错点

- 未标准化。
- 参数搜索范围太窄或直接用默认值。
- 样本极大仍使用核 SVM。
- 把支持向量当“最重要业务样本”作因果解释。

关联：[[Logistic回归]]、[[超参数搜索与模型选择]]。
