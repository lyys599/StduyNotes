---
课程: 数学建模国赛
模块: 03-统计与预测
文件类型: 方法笔记
来源范围: PDF原有+扩展
优先级: 必须掌握
预计学习时间: 2小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - t检验
  - 均值比较
  - 统计推断
aliases:
  - Student t-test
---

# t 检验

## 1. 三种 t 检验

| 类型 | 问题 | 数据关系 |
|---|---|---|
| 单样本 | 样本均值是否等于基准 $\mu_0$ | 一组 |
| 独立样本 | 两独立组均值是否不同 | 不同对象 |
| 配对样本 | 同一对象前后差值均值是否为 0 | 一一配对 |

两独立组默认优先 Welch t 检验，因为它不要求方差相等。

## 2. Python 案例

```python
import numpy as np
from scipy import stats

group_a = np.array([10, 12, 9, 11, 13])
group_b = np.array([15, 14, 13, 16, 17])

# Welch独立样本t检验
t_stat, p = stats.ttest_ind(
    group_a,
    group_b,
    equal_var=False
)
print(t_stat, p)

# 单样本
print(stats.ttest_1samp(group_a, popmean=10))

# 配对
before = np.array([60, 65, 70, 75])
after = np.array([63, 68, 72, 80])
print(stats.ttest_rel(after, before))
```

## 3. 假设

- 观测独立；配对设计中是“配对之间独立”；
- 数据或配对差值近似正态，尤其小样本；
- 独立样本 Student t 还要求方差齐，Welch 不要求。

样本量中等且无严重重尾/极端值时，t 检验对轻微非正态常较稳健。

## 4. Cohen's d

独立组效应量可报告标准化均值差。Welch 检验时也可更直接报告原始均值差与 Bootstrap 区间，避免只盯标准化值。

```python
diff = group_b.mean() - group_a.mean()
print("均值差:", diff)
```

## 5. 论文表达

> B 组均值比 A 组高……。Welch t 检验得到 $t=...$、自由度……、$p=...$，均值差的 95% 置信区间为……。该差异在统计上显著/不显著，实际大小为……。

## 6. 易错点

- 同一批对象前后数据却用独立样本检验。
- 方差不齐仍机械使用 pooled t。
- 多组两两做 t 检验却不校正。
- 把“未显著”解释为等价；等价需专门等效检验。

关联：[[非参数检验]]、[[Bootstrap重抽样与置信区间]]。

