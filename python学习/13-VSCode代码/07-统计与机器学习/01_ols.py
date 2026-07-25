# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import numpy as np
import pandas as pd
import statsmodels.api as sm

rng = np.random.default_rng(42)
x1 = rng.uniform(0, 10, 120)
x2 = rng.normal(5, 2, 120)
y = 3 + 2 * x1 - 0.8 * x2 + rng.normal(0, 2, 120)
X = sm.add_constant(pd.DataFrame({"投入": x1, "规模": x2}))
model = sm.OLS(y, X).fit(cov_type="HC3")
print(model.params)
print(model.conf_int())
print(model.rsquared_adj)
