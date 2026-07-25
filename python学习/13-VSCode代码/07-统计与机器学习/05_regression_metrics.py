# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_true = np.array([10, 12, 15, 20], dtype=float)
y_pred = np.array([11, 11, 14, 24], dtype=float)
mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
r2 = r2_score(y_true, y_pred)
print(f"MAE={mae:.3f}, RMSE={rmse:.3f}, R2={r2:.3f}")
