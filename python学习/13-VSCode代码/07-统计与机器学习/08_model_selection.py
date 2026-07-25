# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_diabetes(return_X_y=True)
pipeline = make_pipeline(StandardScaler(), Ridge())
search = GridSearchCV(
    pipeline,
    {"ridge__alpha": [0.01, 0.1, 1, 10, 100]},
    scoring="neg_mean_absolute_error",
    cv=KFold(5, shuffle=True, random_state=42),
)
search.fit(X, y)
print(search.best_params_, -search.best_score_)
