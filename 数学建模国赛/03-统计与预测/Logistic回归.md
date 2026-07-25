---
课程: 数学建模国赛
模块: 03-统计与预测
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 3小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - Logistic回归
  - 分类
  - 概率模型
aliases:
  - 逻辑回归
---

# Logistic 回归

## 1. 模型

二分类概率：

$$
p(y=1|x)=\sigma(\beta_0+x^T\beta)
=\frac{1}{1+\exp[-(\beta_0+x^T\beta)]}
$$

等价的对数优势：

$$
\log\frac{p}{1-p}=\beta_0+x^T\beta
$$

系数 $\beta_j$ 表示 $x_j$ 增加 1 单位时 log-odds 的变化，优势比为 $e^{\beta_j}$。

## 2. 为什么叫回归却用于分类

它回归的是条件概率的对数优势，再按阈值转为类别。阈值不必固定为 0.5，应结合漏判/误判代价与验证数据选择。

## 3. Pipeline 案例

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(
        max_iter=2000,
        class_weight="balanced"
    )
)

model.fit(X_train, y_train)
prob = model.predict_proba(X_test)[:, 1]
pred = (prob >= 0.5).astype(int)

print(classification_report(y_test, pred))
print("ROC-AUC:", roc_auc_score(y_test, prob))
```

标准化不是数学硬条件，但在正则化和尺度差异大时很有帮助。

## 4. 主要检查

- 连续变量与 logit 是否近似线性；
- 是否存在完全分离；
- 类别是否严重不平衡；
- 概率是否校准；
- 多重共线性；
- 阈值是否符合任务代价。

## 5. 多分类

scikit-learn 可拟合多项 Logistic。多分类不是简单把类别数字当连续值；应使用多项或 one-vs-rest 结构并报告宏/微平均指标。

## 6. 论文表达

> 目标为二分类变量，故建立 Logistic 回归作为可解释基线。连续变量在训练折内标准化，并根据验证集上的 F1/业务代价选择分类阈值。变量 A 的优势比为……，表示控制其余变量后，A 每增加 1 单位，事件优势乘以……。

## 7. 易错点

- 把概率 0.6 说成“一定属于正类”。
- 用准确率评价严重不平衡数据。
- 在测试集选择阈值。
- 将优势比误写为概率增加百分比。
- 把关联系数解释为因果。

关联：[[极大似然估计]]、[[分类评价指标]]。

