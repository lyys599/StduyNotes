# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train, y_train)
importance = permutation_importance(
    model, X_test, y_test, n_repeats=10, random_state=42
)
print(importance.importances_mean)
