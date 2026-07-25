# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, _ = load_iris(return_X_y=True)
cluster_model = make_pipeline(
    StandardScaler(), KMeans(n_clusters=3, n_init=20, random_state=42)
)
labels = cluster_model.fit_predict(X)
X_scaled = StandardScaler().fit_transform(X)
print("轮廓系数：", silhouette_score(X_scaled, labels))
pca = PCA(n_components=2).fit(X_scaled)
print("累计贡献率：", pca.explained_variance_ratio_.sum())
