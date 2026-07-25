---
课程: Python学习
类型: 主题笔记
难度: 进阶
预计学习时间: 85分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - 数据可视化
---

# Seaborn与相关性热力图

> [!abstract] 学完本篇，你要能够
- 使用Seaborn快速展示统计关系
- 绘制相关性热力图
- 避免把相关性图当因果证据

## 核心概念

- Seaborn建立在Matplotlib之上
- `corr`默认计算数值列相关
- 热力图适合变量数量适中时总览

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "温度": [20, 22, 25, 27, 30],
    "能耗": [50, 53, 58, 65, 76],
    "湿度": [70, 68, 65, 61, 58],
})
corr = df.corr(numeric_only=True)
fig, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(corr, annot=True, cmap="RdBu_r", center=0, ax=ax)
fig.tight_layout()
fig.savefig("correlation.png", dpi=300)
plt.close(fig)
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/05-数据可视化/04_seaborn_heatmap.py|打开对应 `.py` 文件]]。

## 代码拆解

1. 先明确参与相关计算的列。
2. 中心设为0，颜色区分正负。
3. 相关矩阵对称，变量太多时应筛选。

## 数学建模中的用途

热力图可用于初步发现共线性、变量组和后续特征选择方向。

## 常见报错与易错点

- 类别编码后直接解释Pearson相关。
- 只看相关系数不看散点。
- 把共同趋势造成的相关解释成因果。

## 独立练习

读取环境数据，画数值列相关热力图，再选择绝对相关最高的一对画散点图。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- [[数学建模国赛/02-探索性分析/Pearson相关系数|Pearson相关系数]]
- [[数学建模国赛/02-探索性分析/Spearman秩相关系数|Spearman秩相关系数]]

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
