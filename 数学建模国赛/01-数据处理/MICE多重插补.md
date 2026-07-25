---
课程: 数学建模国赛
模块: 01-数据处理
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 3小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - MICE
  - 多重插补
  - 缺失值
aliases:
  - 链式方程多重插补
---

# MICE 多重插补

## 1. 核心思想

MICE（Multivariate Imputation by Chained Equations）为每个含缺失的变量建立条件模型，轮流更新缺失位置，得到多份完整数据。多份数据之间的差异用于表达“如果缺失值取其他合理值，结论会怎样”。

```mermaid
flowchart LR
    A["初始化缺失值"] --> B["用其余变量预测 X1"]
    B --> C["更新 X1 缺失位置"]
    C --> D["用其余变量预测 X2"]
    D --> E["更新 X2 缺失位置"]
    E --> F{"完成一轮？"}
    F -->|继续| B
    F -->|收敛后抽样| G["得到一份插补数据"]
    G --> H["重复得到 m 份"]
```

## 2. 适用与不适用

适合：

- 缺失机制可合理近似 MAR；
- 多个变量之间有关联；
- 希望保留参数不确定性；
- 后续模型有清晰的估计量和标准误。

谨慎：

- MNAR 且无敏感性分析；
- 样本极少、缺失率极高；
- 插补模型遗漏强预测变量；
- 时间或层级结构被忽略；
- 类别、边界和逻辑约束没有正确建模。

## 3. 为什么不能只填一次

单次插补把估计值当成确定事实，会低估方差。多重插补在第 $k$ 份数据上得到估计 $\hat Q_k$ 和方差 $U_k$：

$$
\bar Q=\frac{1}{m}\sum_{k=1}^{m}\hat Q_k
$$

组内方差：

$$
\bar U=\frac{1}{m}\sum_{k=1}^{m}U_k
$$

组间方差：

$$
B=\frac{1}{m-1}\sum_{k=1}^{m}(\hat Q_k-\bar Q)^2
$$

总方差：

$$
T=\bar U+\left(1+\frac{1}{m}\right)B
$$

这就是 Rubin 合并规则的核心。它不限于“只能合并线性或逻辑回归”，但待合并统计量必须有合适的估计与方差。

## 4. Python：statsmodels MICE

```python
import numpy as np
import pandas as pd
from statsmodels.imputation.mice import MICEData

rng = np.random.default_rng(42)
n = 100
df = pd.DataFrame({
    "age": rng.normal(40, 10, n),
    "education": rng.normal(14, 2, n)
})
df["income"] = 1000 + 80 * df["age"] + 300 * df["education"] \
               + rng.normal(0, 1000, n)

df.loc[rng.choice(n, 15, replace=False), "income"] = np.nan
df.loc[rng.choice(n, 10, replace=False), "education"] = np.nan

imp = MICEData(df)

# 预热若干轮，让链摆脱初始值
for _ in range(10):
    imp.update_all()

datasets = []
for _ in range(5):
    for _ in range(5):
        imp.update_all()
    datasets.append(imp.data.copy())

print(datasets[0].isna().sum())
```

这段代码演示生成多份数据。正式统计推断可继续使用 statsmodels 的 `MICE` 类拟合并汇总模型，或采用 R 的 `mice` 包完成诊断与 pooling。

## 5. R：更成熟的诊断与合并

```r
install.packages("mice")
library(mice)

imp <- mice(
  data,
  m = 10,
  maxit = 20,
  method = "pmm",
  seed = 42,
  printFlag = FALSE
)

plot(imp)                  # 轨迹图
densityplot(imp)           # 分布比较

fit <- with(imp, lm(y ~ x1 + x2 + x3))
summary(pool(fit))
```

连续变量常用 PMM；二分类可用 logistic，多分类可用多项 logistic。方法要和变量类型一致。

## 6. 诊断清单

- 轨迹图是否稳定并充分混合；
- 插补值是否在合理范围；
- 观测值与插补值分布是否荒谬地不同；
- 不同插补数据的结论是否稳定；
- 增加 $m$ 后标准误是否稳定；
- 插补模型是否包含目标变量、缺失预测变量和重要辅助变量；
- 是否按训练/测试边界避免泄漏。

## 7. 论文表达

> 在 MAR 假设下，对含缺失的协变量采用 MICE。连续变量使用预测均值匹配，分类变量采用相应的逻辑模型，设置 20 次迭代并生成 10 份完整数据。轨迹图显示插补链稳定混合。各数据集分别拟合模型后按 Rubin 规则合并参数和标准误，并将完整案例分析作为敏感性对照。

## 8. 易错点与练习

> [!warning]
> - MICE 不是按缺失率大于 5% 才能使用的硬规则。
> - 不能只输出第一份插补数据然后忘记多重性。
> - 不要让测试集信息参与训练阶段插补器。
> - 类别编码、边界约束和派生变量必须保持一致。

练习：把案例中的 `income` 缺失率改为 30%，比较 5 份与 20 份插补数据中收入均值的变化。

参考：van Buuren & Groothuis-Oudshoorn (2011)；[statsmodels MICE](https://www.statsmodels.org/stable/imputation.html)。
