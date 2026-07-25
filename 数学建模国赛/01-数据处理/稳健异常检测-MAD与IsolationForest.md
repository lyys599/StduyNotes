---
课程: 数学建模国赛
模块: 01-数据处理
文件类型: 方法笔记
来源范围: 扩展
优先级: 建议掌握
预计学习时间: 2小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - 异常检测
  - MAD
  - IsolationForest
aliases:
  - 稳健异常检测
---

# 稳健异常检测：MAD 与 Isolation Forest

## 1. 何时需要

- 分布偏态或极端值污染使均值、标准差不稳定；
- 异常由多个变量组合产生，单变量看不异常；
- 希望用稳健统计或无监督算法辅助筛查。

## 2. MAD

中位数绝对偏差：

$$
MAD=\operatorname{median}(|x_i-\operatorname{median}(x)|)
$$

修正 Z 分数：

$$
M_i=\frac{0.6745(x_i-\tilde x)}{MAD}
$$

经验上常以 $|M_i|>3.5$ 标记候选。

```python
import numpy as np
import pandas as pd

x = pd.Series([10, 11, 10, 9, 12, 10, 50], dtype=float)
median = x.median()
mad = np.median(np.abs(x - median))

if mad == 0:
    modified_z = pd.Series(np.nan, index=x.index)
else:
    modified_z = 0.6745 * (x - median) / mad

print(pd.DataFrame({
    "x": x,
    "modified_z": modified_z,
    "异常候选": modified_z.abs() > 3.5
}))
```

MAD 为 0 时不能直接除，需要换方法或结合业务阈值。

## 3. Isolation Forest

它通过随机切分特征空间隔离样本；异常点通常更容易被少量切分隔离。

```python
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

X = pd.DataFrame({
    "温度": [20, 21, 19, 22, 20, 50],
    "压力": [100, 102, 99, 101, 98, 200]
})

model = make_pipeline(
    StandardScaler(),
    IsolationForest(
        contamination=0.05,
        random_state=42
    )
)

label = model.fit_predict(X)
X["异常候选"] = label == -1
print(X)
```

`contamination` 是预期异常比例，不能为了得到想要的异常数随意调整。

## 4. 如何选择

| 场景 | 推荐 |
|---|---|
| 单个连续变量、偏态 | MAD 或 IQR |
| 多维组合异常 | Isolation Forest |
| 有明确物理边界 | 业务规则优先 |
| 有异常标签 | 监督分类与代价敏感评价 |

## 5. 模型输出不是事实

异常检测的标签只是筛查信号。论文中应报告：

- 参数和异常比例；
- 候选样本的业务特征；
- 处理前后模型结论；
- 是否有人工或规则复核。

## 6. 易错点

- 在包含目标泄漏特征的数据上检测异常。
- 先删除再报告“模型性能大幅提升”，却不检查删除对象。
- 忽略类别变量编码带来的虚假距离。
- 用测试集一起拟合异常检测器。

练习：在二维正常点中加入“温度很高但压力正常”和“两者都略高”的点，比较单变量 MAD 与 Isolation Forest 的标记差异。

