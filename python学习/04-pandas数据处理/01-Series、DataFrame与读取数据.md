---
课程: Python学习
类型: 主题笔记
难度: 必修
预计学习时间: 100分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - pandas数据处理
---

# Series、DataFrame与读取数据

> [!abstract] 学完本篇，你要能够
- 理解行索引、列名和数据类型
- 读取CSV与Excel
- 用 `head/info/describe`快速审计

## 核心概念

- Series是一维带标签数据
- DataFrame是二维异质表
- 读取后先检查形状、列名、类型和样例

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[2]
path = root / "12-示例数据" / "环境监测数据.csv"
df = pd.read_csv(path)
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe(include="all"))
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/04-pandas数据处理/01_read_audit.py|打开对应 `.py` 文件]]。

## 代码拆解

1. 基于项目根目录定位数据。
2. `shape`给行列数。
3. `include='all'`同时摘要数值与类别列。

## 数学建模中的用途

C题第一步通常是附件读取和数据质量审计，不能读完立即建模。

## 常见报错与易错点

- Excel工作表读错。
- 中文编码不一致。
- 把编号误读为数值或日期误读为文本。

## 独立练习

分别读取同一份CSV和Excel，比较形状、列名和数据类型是否一致。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- [[数学建模国赛/01-数据处理/pandas数据读取与质量审计|pandas数据读取与质量审计]]

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
