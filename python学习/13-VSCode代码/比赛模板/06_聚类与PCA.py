
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def main() -> None:
    X, _ = load_iris(return_X_y=True)
    X_scaled = StandardScaler().fit_transform(X)
    labels = KMeans(n_clusters=3, n_init=20, random_state=42).fit_predict(X_scaled)
    points = PCA(n_components=2).fit_transform(X_scaled)
    print("silhouette:", silhouette_score(X_scaled, labels))
    print("PCA shape:", points.shape)


if __name__ == "__main__":
    main()
