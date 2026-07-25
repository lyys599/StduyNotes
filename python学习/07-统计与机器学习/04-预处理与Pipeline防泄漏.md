---
课程: Python学习
类型: 主题笔记
难度: 必修
预计学习时间: 140分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - 统计与机器学习
---

# 预处理与Pipeline防泄漏

> [!abstract] 学完本篇，你要能够
- 组合缺失填补、标准化和模型
- 在交叉验证内部拟合预处理
- 处理数值与类别特征

## 核心概念

- Pipeline按顺序变换
- ColumnTransformer按列类型处理
- 任何从数据估计的步骤都应只在训练折拟合

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

numeric = ["温度", "湿度"]
categorical = ["地区"]
preprocess = ColumnTransformer([
    ("num", make_pipeline(SimpleImputer(strategy="median"),
                          StandardScaler()), numeric),
    ("cat", make_pipeline(SimpleImputer(strategy="most_frequent"),
                          OneHotEncoder(handle_unknown="ignore")), categorical),
])
model = make_pipeline(preprocess, Ridge(alpha=1.0))
print(model)
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/07-统计与机器学习/04_pipeline.py|打开对应 `.py` 文件]]。

## 代码拆解

1. 数值列填补后标准化。
2. 类别列填补后独热编码。
3. 未知类别不会让预测直接失败。

## 数学建模中的用途

比赛数据常同时含数值、类别和缺失；Pipeline是稳定复现的核心。

## 常见报错与易错点

- 先用全数据标准化。
- 手工分别处理训练测试导致列不一致。
- 把目标列放进特征。

## 独立练习

在示例分类数据上建立数值+类别Pipeline，完成划分、训练、预测和评价。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- [[数学建模国赛/01-数据处理/防止数据泄漏与Pipeline|防止数据泄漏与Pipeline]]
- [[数学建模国赛/01-数据处理/类别编码与特征工程|类别编码与特征工程]]

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
