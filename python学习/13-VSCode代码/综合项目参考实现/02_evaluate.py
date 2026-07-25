
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from common import FIGURE_DIR, OUTPUT_DIR, RANDOM_SEED, ensure_directories


def entropy_weights(X: np.ndarray) -> np.ndarray:
    minimum, span = X.min(axis=0), X.max(axis=0) - X.min(axis=0)
    Z = (X - minimum) / np.where(span == 0, 1, span)
    P = (Z + 1e-12) / (Z + 1e-12).sum(axis=0)
    entropy = -(P * np.log(P)).sum(axis=0) / np.log(len(X))
    difference = 1 - entropy
    return difference / difference.sum()


def topsis(X: np.ndarray, weights: np.ndarray) -> np.ndarray:
    denominator = np.linalg.norm(X, axis=0)
    V = X / np.where(denominator == 0, 1, denominator) * weights
    d_pos = np.linalg.norm(V - V.max(axis=0), axis=1)
    d_neg = np.linalg.norm(V - V.min(axis=0), axis=1)
    return d_neg / np.where(d_pos + d_neg == 0, 1, d_pos + d_neg)


def main() -> None:
    ensure_directories()
    df = pd.read_csv(OUTPUT_DIR / "clean_monthly.csv", parse_dates=["日期"])
    latest_year = df["日期"].dt.year.max()
    current = df.loc[df["日期"].dt.year == latest_year]
    city = current.groupby(["城市ID", "城市名称", "地区"], as_index=False).agg(
        经济活力=("经济活力", "mean"),
        医疗负荷=("医疗负荷", "mean"),
        应急响应时间=("应急响应时间", "mean"),
        基础设施完好率=("基础设施完好率", "mean"),
        灾害损失率=("灾害损失率", "mean"),
    )
    columns = ["经济活力", "医疗负荷", "应急响应时间", "基础设施完好率", "灾害损失率"]
    X = city[columns].to_numpy(float)
    X[:, [1, 2, 4]] *= -1
    weights = entropy_weights(X)
    city["韧性得分"] = topsis(X, weights)
    city["韧性排名"] = city["韧性得分"].rank(ascending=False, method="min").astype(int)
    X_scaled = StandardScaler().fit_transform(city[columns])
    labels = KMeans(n_clusters=3, n_init=30, random_state=RANDOM_SEED).fit_predict(X_scaled)
    city["城市类型"] = labels + 1
    print("silhouette:", silhouette_score(X_scaled, labels))
    city.sort_values("韧性排名").to_csv(
        OUTPUT_DIR / "city_scores.csv", index=False, encoding="utf-8-sig"
    )
    pd.DataFrame({"指标": columns, "熵权": weights}).to_csv(
        OUTPUT_DIR / "weights.csv", index=False, encoding="utf-8-sig"
    )
    fig, ax = plt.subplots(figsize=(8, 4))
    ordered = city.sort_values("韧性得分")
    ax.barh(ordered["城市名称"], ordered["韧性得分"], color="#4C78A8")
    ax.set(xlabel="Resilience score", title="City resilience ranking")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "city_ranking.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
