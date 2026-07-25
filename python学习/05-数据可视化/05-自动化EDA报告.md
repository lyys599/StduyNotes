---
课程: Python学习
类型: 主题笔记
难度: 必修
预计学习时间: 120分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - 数据可视化
---

# 自动化EDA报告

> [!abstract] 学完本篇，你要能够
- 把数据审计和绘图封装为函数
- 批量生成数值列分布图
- 输出可交付的摘要表与图片目录

## 核心概念

- 自动化减少重复劳动
- 仍需人工判断变量语义
- 文件名必须安全且可追踪

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
from pathlib import Path
import pandas as pd

def audit_table(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "类型": df.dtypes.astype(str),
        "缺失数": df.isna().sum(),
        "缺失率": df.isna().mean(),
        "唯一值数": df.nunique(dropna=False),
    })

data = pd.DataFrame({"A": [1, 2, None], "B": ["x", "x", "y"]})
report = audit_table(data)
Path("outputs").mkdir(exist_ok=True)
report.to_csv("outputs/数据审计.csv", encoding="utf-8-sig")
print(report)
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/05-数据可视化/05_eda_report.py|打开对应 `.py` 文件]]。

## 代码拆解

1. 审计表以原列名为索引。
2. 缺失率是布尔均值。
3. UTF-8带BOM方便Excel直接打开中文。

## 数学建模中的用途

拿到附件后的前1小时可运行EDA模板，快速向建模手反馈数据结构和明显问题。

## 常见报错与易错点

- 自动图很多却没有问题意识。
- 对ID列画分布。
- 输出文件覆盖且不记录版本。

## 独立练习

扩展审计函数：加入均值、标准差、最小最大值和IQR异常数，并生成至少三类图。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- [[数学建模国赛/02-探索性分析/EDA完整工作流|EDA完整工作流]]

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
