# 完成独立尝试后再阅读本文件。
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
pipeline = make_pipeline(SimpleImputer(), StandardScaler(), Ridge())
search = GridSearchCV(
    pipeline, {"ridge__alpha": [0.01, 0.1, 1, 10, 100]},
    scoring="neg_mean_absolute_error", cv=5
)
search.fit(X_train, y_train)
prediction = search.predict(X_test)
print(search.best_params_)
print("MAE", mean_absolute_error(y_test, prediction))
print("RMSE", np.sqrt(mean_squared_error(y_test, prediction)))
print("R2", r2_score(y_test, prediction))
