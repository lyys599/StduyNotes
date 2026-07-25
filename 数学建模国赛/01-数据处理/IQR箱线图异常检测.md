---
课程: 数学建模国赛
模块: 01-数据处理
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 1.5小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - 异常检测
  - IQR
  - 箱线图
aliases:
  - 四分位距异常检测
---

# IQR 箱线图异常检测

## 1. 原理

设下四分位数为 $Q_1$，上四分位数为 $Q_3$：

$$
IQR=Q_3-Q_1
$$

常用外围栏：

$$
[Q_1-1.5IQR,\ Q_3+1.5IQR]
$$

超出外围栏的是异常候选。$3IQR$ 常用于标记更极端的点，但不是统一法律。

## 2. 为什么比 3Sigma 稳健

四分位数受极端值影响较小，也不要求正态分布。但它仍是单变量规则；对强偏态分布可能把大量合法大值标记为异常。

## 3. Python 案例

```python
import pandas as pd
import matplotlib.pyplot as plt

x = pd.Series([10, 11, 9, 12, 10, 13, 8, 40], name="指标")

q1 = x.quantile(0.25)
q3 = x.quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

flag = ~x.between(lower, upper)
print(pd.DataFrame({"x": x, "异常候选": flag}))

fig, ax = plt.subplots(figsize=(6, 2.5))
ax.boxplot(x.dropna(), vert=False)
ax.set_title("指标箱线图")
fig.tight_layout()
plt.show()
```

## 4. 分组 IQR

```python
def iqr_flag(s):
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    return (s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)

df["异常候选"] = df.groupby("地区")["指标"].transform(iqr_flag)
```

分组必须来自业务结构，不能为了让异常消失而随意分组。

## 5. 可选处理

- 保留并使用稳健模型；
- 对数/Box-Cox/Yeo-Johnson 变换；
- Winsorize 截尾，但必须报告阈值；
- 确认错误后修正或剔除；
- 分别建模并比较敏感性。

## 6. 论文表达

> 变量呈右偏分布，故采用不依赖正态假设的 IQR 规则标记异常候选，并结合箱线图和原始记录核查。主分析保留具有合理业务含义的极端值，同时在稳健性检验中对其进行截尾处理，比较核心结论。

## 7. 易错点

- 把箱线图须全部“清干净”当成目标。
- 类别编码 0/1/2 上使用 IQR。
- 样本太少导致四分位数不稳定。
- 忽略不同组的基线差异。

关联：[[3Sigma异常检测]]、[[稳健异常检测-MAD与IsolationForest]]。

