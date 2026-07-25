# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
print("MAE：", mean_absolute_error(y_test, prediction))
print("R2：", r2_score(y_test, prediction))
