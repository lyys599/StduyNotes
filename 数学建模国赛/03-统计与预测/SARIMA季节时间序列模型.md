---
课程: 数学建模国赛
模块: 03-统计与预测
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 3小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - SARIMA
  - 季节性
  - 时间序列
aliases:
  - 季节ARIMA
---

# SARIMA 季节时间序列模型

## 1. 结构

SARIMA 记作：

$$
ARIMA(p,d,q)(P,D,Q)_s
$$

- 小写部分描述非季节动态；
- $P,D,Q$ 描述季节自回归、季节差分和季节误差；
- $s$ 是季节周期，如月度数据年周期 $s=12$。

## 2. 什么时候使用

- 有稳定、重复的季节周期；
- 单变量预测；
- 季节效应可用线性差分与滞后描述；
- 有至少若干完整周期。

季节周期不能只凭软件自动猜；应由采样频率、业务和图形共同确定。

## 3. Python 案例

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error

rng = np.random.default_rng(42)
n = 96
t = np.arange(n)
y = 20 + 0.05*t + 4*np.sin(2*np.pi*t/12) + rng.normal(0, 1, n)
series = pd.Series(
    y,
    index=pd.date_range("2018-01-01", periods=n, freq="M")
)

train, test = series.iloc[:-12], series.iloc[-12:]

fit = SARIMAX(
    train,
    order=(1, 1, 1),
    seasonal_order=(1, 1, 1, 12),
    enforce_stationarity=False,
    enforce_invertibility=False
).fit(disp=False)

pred = fit.get_forecast(12).predicted_mean
print("MAE:", mean_absolute_error(test, pred))
print(fit.summary())
```

## 4. 选阶

1. 季节图/自相关确定 $s$。
2. 判断是否需要普通差分 $d$ 与季节差分 $D$。
3. 给 $p,q,P,Q$ 设置小范围候选。
4. 比较 AIC/BIC、收敛、参数合理性。
5. 用滚动验证与季节朴素法比较。
6. 检查残差。

不要在小样本上遍历巨大网格。

## 5. 外生变量

`SARIMAX` 可加入外生变量 `exog`。预测未来时必须知道或另行预测未来外生变量，否则会出现隐含信息泄漏。

## 6. 论文表达

> 月度序列呈 12 期季节性，故以季节朴素法为基线并构建 SARIMA。通过滚动验证和 BIC 选择……模型，其测试 MAE 较基线降低……。残差未见显著季节自相关。

## 7. 易错点

- 数据只有一个周期却拟合复杂季节模型。
- 同时使用高阶普通和季节差分，导致过度差分。
- 预测时使用真实未来外生变量。
- 只展示拟合曲线，不做留出预测。

关联：[[ARIMA时间序列模型]]、[[指数平滑ETS]]。

