---
课程: 数学建模国赛
模块: 01-数据处理
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 建议掌握
预计学习时间: 1.5小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - Little检验
  - MCAR
  - 缺失值
aliases:
  - Littles MCAR test
---

# Little MCAR 检验

## 1. 检验问题

- 原假设 $H_0$：数据满足 MCAR。
- 备择假设 $H_1$：数据不满足 MCAR。

Little 检验将样本按缺失模式分组，比较各组在可观测变量上的均值与基于模型估计的总体均值差异，构造近似卡方统计量。

若 $p<\alpha$，拒绝 MCAR；若 $p\ge\alpha$，只能说“没有足够证据拒绝 MCAR”，不能证明 MCAR 为真。

## 2. 使用前提与限制

- 主要面向连续变量，并依赖多元正态等近似。
- 样本很小、缺失模式太多时检验不稳定。
- 大样本中很小的偏离也可能显著。
- 它不能区分 MAR 和 MNAR。
- 检验结果必须结合缺失图和数据生成机制。

## 3. R 实现（推荐）

```r
install.packages("naniar")
library(naniar)

dat <- data.frame(
  age = c(20, 21, 35, 40, 52, 60),
  income = c(4.2, NA, 7.0, 8.1, NA, 6.5),
  score = c(80, 82, NA, 90, 78, 75)
)

result <- mcar_test(dat)
print(result)
```

重点读取统计量、自由度和 p 值。比赛代码中记录包版本。

## 4. Python 可选实现

可使用 `pyampute` 的 Little 检验实现；第三方包接口可能随版本变化，比赛前锁定并测试版本：

```bash
python -m pip install pyampute
```

```python
import pandas as pd
from pyampute.exploration.mcar_statistical_tests import MCARTest

df = pd.DataFrame({
    "age": [20, 21, 35, 40, 52, 60],
    "income": [4.2, None, 7.0, 8.1, None, 6.5],
    "score": [80, 82, None, 90, 78, 75]
})

test = MCARTest(method="little")
p_value = test.little_mcar_test(df)
print("p值:", p_value)
```

若实际安装版本接口不同，以该版本官方示例为准；不要在竞赛当天临时换库。

## 5. 论文表达模板

> Little MCAR 检验得到 $\chi^2=\cdots$、自由度为……、$p=\cdots$。在显著性水平 0.05 下（拒绝/未拒绝）MCAR 假设。结合缺失模式与字段生成过程，本文在……假设下采用……处理，并通过……敏感性分析检查结论。

## 6. 易错点

> [!warning]
> - $p>0.05$ 不等于“证明 MCAR”。
> - 把所有类别编码成数字后直接检验，可能破坏含义。
> - 检验显著后不能直接断言 MNAR。
> - 不要把 Little 检验与一般的卡方独立性检验混为一谈。

关联：[[缺失机制MCAR-MAR-MNAR]]。

