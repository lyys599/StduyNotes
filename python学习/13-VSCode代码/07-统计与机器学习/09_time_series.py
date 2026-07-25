# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error

rng = np.random.default_rng(42)
index = pd.date_range("2023-01-01", periods=36, freq="MS")
values = 100 + np.arange(36) * 1.2 + 8 * np.sin(2 * np.pi * np.arange(36) / 12)
series = pd.Series(values + rng.normal(0, 2, 36), index=index)
train, test = series.iloc[:-6], series.iloc[-6:]
model = ExponentialSmoothing(train, trend="add", seasonal="add",
                             seasonal_periods=12).fit()
prediction = model.forecast(len(test))
print("MAE：", mean_absolute_error(test, prediction))
