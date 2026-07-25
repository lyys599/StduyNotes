---
课程: Python学习
类型: 主题笔记
难度: 必修
预计学习时间: 135分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - 数学建模算法实现
---

# 敏感性、Bootstrap与稳健性实现

> [!abstract] 学完本篇，你要能够
- 进行单因素与情景敏感性分析
- 用Bootstrap估计区间
- 输出结论稳定性表

## 核心概念

- 敏感性看输入变化如何传到输出
- Bootstrap从观测样本有放回抽样
- 稳健性需要替代设定而非重复同一模型

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
import numpy as np

rng = np.random.default_rng(42)
sample = np.array([12, 15, 14, 18, 20, 17, 16], dtype=float)
bootstrap_means = np.empty(5000)
for i in range(len(bootstrap_means)):
    resample = rng.choice(sample, size=len(sample), replace=True)
    bootstrap_means[i] = resample.mean()
interval = np.quantile(bootstrap_means, [0.025, 0.975])
print("均值：", sample.mean())
print("Bootstrap 95%区间：", interval)
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/08-数学建模算法实现/06_bootstrap_sensitivity.py|打开对应 `.py` 文件]]。

## 代码拆解

1. 每次重抽样与原样本同样大小。
2. 统计量可替换为中位数、模型系数或排名。
3. 分位数给经验区间。

## 数学建模中的用途

竞赛论文至少应说明结论是否对权重、阈值、抽样和模型选择敏感。

## 常见报错与易错点

- 时间序列随意独立重抽样。
- 样本偏差被Bootstrap复制。
- 只展示一个参数点。

## 独立练习

对TOPSIS输入进行Bootstrap，统计每个城市成为第一名的概率。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- [[数学建模国赛/03-统计与预测/Bootstrap重抽样与置信区间|Bootstrap]]
- [[数学建模国赛/07-模型检验/敏感性分析|敏感性分析]]
- [[数学建模国赛/07-模型检验/稳健性检验|稳健性检验]]

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
