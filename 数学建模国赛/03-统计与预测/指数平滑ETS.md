---
课程: 数学建模国赛
模块: 03-统计与预测
文件类型: 方法笔记
来源范围: 扩展
优先级: 建议掌握
预计学习时间: 2.5小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - 指数平滑
  - ETS
  - 时间序列
aliases:
  - Holt-Winters
---

# 指数平滑 ETS

## 1. 核心思想

指数平滑让近期观测权重更大。ETS 将序列拆为：

- Error：误差；
- Trend：趋势；
- Seasonal：季节。

常见模型包括简单指数平滑、Holt 趋势、阻尼趋势、Holt-Winters 季节模型。

## 2. 为什么值得作为基线

它不需要显式解释 ACF/PACF，对稳定的水平、趋势和季节结构效果常很好，参数少、速度快、容易解释。

## 3. Python 案例

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error

rng = np.random.default_rng(42)
n = 72
t = np.arange(n)
y = 30 + 0.2*t + 5*np.sin(2*np.pi*t/12) + rng.normal(0, 1, n)
series = pd.Series(
    y,
    index=pd.date_range("2020-01-01", periods=n, freq="M")
)

train, test = series.iloc[:-12], series.iloc[-12:]

fit = ExponentialSmoothing(
    train,
    trend="add",
    damped_trend=True,
    seasonal="add",
    seasonal_periods=12,
    initialization_method="estimated"
).fit(optimized=True)

pred = fit.forecast(12)
print("MAE:", mean_absolute_error(test, pred))
```

## 4. 加法还是乘法

- 加法季节：季节波动幅度大致固定。
- 乘法季节：水平越高，季节波动幅度越大；序列需为正。

可通过图形、残差和滚动验证选择。

## 5. 与 ARIMA 的区别

- ETS 直接描述水平、趋势和季节状态；
- ARIMA 描述差分和自相关；
- 两者都可做优秀基线，没有绝对高低；
- 以滚动验证和残差诊断决定。

## 6. 论文表达

> 序列的季节波动幅度近似恒定，因此采用加法 Holt-Winters，并使用阻尼趋势避免长期趋势无限外推。模型在滚动验证上的 MAE 为……，优于季节朴素法/与 SARIMA 相当。

## 7. 易错点

- 季节周期设置错误。
- 没有足够完整周期。
- 长期外推不加阻尼。
- 只比较样本内拟合。

关联：[[SARIMA季节时间序列模型]]。

