# 完成独立尝试后再阅读本文件。
import numpy as np

def minmax(X):
    X = np.asarray(X, dtype=float)
    minimum = X.min(axis=0)
    span = X.max(axis=0) - minimum
    safe_span = np.where(span == 0, 1, span)
    return (X - minimum) / safe_span

def simulate_profit(n=100_000, seed=42):
    rng = np.random.default_rng(seed)
    price = rng.normal(20, 1.5, n)
    demand = np.maximum(rng.normal(1000, 120, n), 0)
    unit_cost = rng.triangular(12, 14, 17, n)
    fixed_cost = 4200
    profit = (price - unit_cost) * demand - fixed_cost
    return {
        "盈利概率": float((profit > 0).mean()),
        "平均利润": float(profit.mean()),
        "95%区间": np.quantile(profit, [0.025, 0.975]).tolist(),
    }

print(simulate_profit())
