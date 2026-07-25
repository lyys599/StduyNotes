# 完成独立尝试后再阅读本文件。
import numpy as np

def topsis(X, weights, cost_columns=()):
    X = np.asarray(X, dtype=float).copy()
    weights = np.asarray(weights, dtype=float)
    if X.ndim != 2 or len(weights) != X.shape[1]:
        raise ValueError("矩阵和权重形状不匹配")
    if np.any(weights < 0) or weights.sum() <= 0:
        raise ValueError("权重必须非负且总和大于0")
    for column in cost_columns:
        X[:, column] = X[:, column].max() - X[:, column]
    denominator = np.sqrt((X**2).sum(axis=0))
    denominator[denominator == 0] = 1
    V = X / denominator * (weights / weights.sum())
    d_pos = np.linalg.norm(V - V.max(axis=0), axis=1)
    d_neg = np.linalg.norm(V - V.min(axis=0), axis=1)
    score = d_neg / np.where(d_pos + d_neg == 0, 1, d_pos + d_neg)
    return score, np.argsort(-score)

X = [[80, 20, 7, 50], [70, 15, 9, 60],
     [90, 30, 6, 55], [82, 18, 8, 58]]
score, order = topsis(X, [0.3, 0.2, 0.25, 0.25], cost_columns=[1])
print(score, order + 1)
