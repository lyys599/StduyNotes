---
课程: Python学习
类型: 主题笔记
难度: 必修
预计学习时间: 130分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - 统计与机器学习
---

# scikit-learn统一建模流程

> [!abstract] 学完本篇，你要能够
- 完成 `fit/predict/score`流程
- 划分训练集与测试集
- 固定随机种子并保留基准模型

## 核心概念

- 特征X通常二维，目标y通常一维
- 训练集用于学习，测试集只做最终评估
- 估计器接口在多数模型中一致

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
print("MAE：", mean_absolute_error(y_test, prediction))
print("R2：", r2_score(y_test, prediction))
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/07-统计与机器学习/03_sklearn_workflow.py|打开对应 `.py` 文件]]。

## 代码拆解

1. 划分发生在训练前。
2. `fit`只看训练数据。
3. 测试指标衡量未参与训练的数据表现。

## 数学建模中的用途

统一接口让你能快速比较线性模型、树模型和支持向量机。

## 常见报错与易错点

- 测试集参与调参。
- 随机划分时间序列。
- 没有简单基准就直接上复杂模型。

## 独立练习

使用内置数据比较线性回归与决策树，记录训练和测试指标并解释过拟合。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- [[数学建模国赛/05-机器学习/机器学习建模总流程|机器学习建模总流程]]
- [[数学建模国赛/01-数据处理/数据集划分与交叉验证|数据集划分与交叉验证]]

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
