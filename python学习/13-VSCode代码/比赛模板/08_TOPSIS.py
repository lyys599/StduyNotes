
import numpy as np


def topsis(X, weights, cost_columns=()):
    X = np.asarray(X, dtype=float).copy()
    weights = np.asarray(weights, dtype=float)
    for column in cost_columns:
        X[:, column] = X[:, column].max() - X[:, column]
    denominator = np.linalg.norm(X, axis=0)
    denominator[denominator == 0] = 1
    V = X / denominator * (weights / weights.sum())
    d_pos = np.linalg.norm(V - V.max(axis=0), axis=1)
    d_neg = np.linalg.norm(V - V.min(axis=0), axis=1)
    score = d_neg / np.where(d_pos + d_neg == 0, 1, d_pos + d_neg)
    return score


def main() -> None:
    X = [[80, 20, 7], [70, 15, 9], [90, 30, 6]]
    score = topsis(X, [0.4, 0.3, 0.3], cost_columns=[1])
    print(score)
    print("ranking:", np.argsort(-score) + 1)


if __name__ == "__main__":
    main()
