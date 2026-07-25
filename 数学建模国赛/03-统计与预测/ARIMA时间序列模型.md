---
课程: 数学建模国赛
模块: 03-统计与预测
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 4小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - ARIMA
  - 时间序列
  - 预测
aliases:
  - ARIMA模型
---

# ARIMA 时间序列模型

## 1. 结构

ARIMA$(p,d,q)$：

- $p$：自回归阶数，使用过去观测；
- $d$：差分次数，使序列近似平稳；
- $q$：移动平均阶数，使用过去预测误差。

差分后的序列满足 ARMA：

$$
\phi(B)(1-B)^d y_t=c+\theta(B)\varepsilon_t
$$

## 2. 适用场景

- 单变量时间序列；
- 等间隔观测；
- 线性自相关结构；
- 无强季节性，或季节性已处理；
- 短中期预测。

先建立朴素基线：上一期值、移动平均或漂移法。ARIMA 必须在滚动验证中优于基线才有意义。

## 3. 建模 SOP

1. 画时序图，确认频率、缺口、异常和结构突变。
2. 划分最后一段为测试期，禁止随机划分。
3. 用 ADF/KPSS、图形和领域知识判断平稳性。
4. 尽量使用低阶差分，避免过度差分。
5. ACF/PACF 提供 $p,q$ 候选，不机械套截尾口诀。
6. 结合 AIC/BIC 与滚动验证选阶。
7. 做残差白噪声诊断。
8. 输出预测区间。

## 4. Python 案例

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox
from sklearn.metrics import mean_absolute_error

rng = np.random.default_rng(42)
n = 80
e = rng.normal(0, 1, n)
y = np.zeros(n)
for t in range(1, n):
    y[t] = 0.7 * y[t-1] + e[t]

series = pd.Series(
    y,
    index=pd.date_range("2020-01-01", periods=n, freq="M")
)

train, test = series.iloc[:-12], series.iloc[-12:]
fit = ARIMA(train, order=(1, 0, 0), trend="c").fit()

forecast = fit.get_forecast(steps=len(test))
pred = forecast.predicted_mean
ci = forecast.conf_int()

print(fit.summary())
print("MAE:", mean_absolute_error(test, pred))
print(acorr_ljungbox(fit.resid, lags=[10], return_df=True))
```

Ljung-Box 若显著，说明残差仍有自相关，模型未吸收完时间结构。

## 5. ADF 与 KPSS

- ADF 原假设：存在单位根，即不平稳。
- KPSS 原假设：平稳。

两者结合比单独用一个更稳妥。检验对结构突变和样本量敏感。

## 6. 正态性与白噪声不同

白噪声重点是无系统自相关。残差非正态主要影响高斯预测区间，不一定破坏点预测。可使用 Bootstrap 区间或稳健模型，但不能把“Q-Q 图正常”当成白噪声证明。

## 7. 论文表达

> 序列经一阶差分后趋势消失，ADF 与 KPSS 结果共同支持近似平稳。依据 ACF/PACF 构造候选阶数，并通过滚动验证 MAE 与 BIC 选择 ARIMA(……)。Ljung-Box 检验未发现显著残差自相关，预测区间随步长增加而变宽。

## 8. 易错点

- 随机划分时间序列。
- 只以 AIC 最小选模型，不看预测验证。
- 不断差分直到 p 值满意。
- 用预测期真实值参与变换或选阶。
- 把预测区间写成确定范围。

关联：[[SARIMA季节时间序列模型]]、[[指数平滑ETS]]、[[回归评价指标]]。

