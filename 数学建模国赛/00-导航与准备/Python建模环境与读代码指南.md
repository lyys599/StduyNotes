---
课程: 数学建模国赛
模块: 00-导航与准备
文件类型: 工具基础
来源范围: 扩展
优先级: 必须掌握
预计学习时间: 3小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - Python
  - NumPy
  - pandas
  - Matplotlib
  - scikit-learn
aliases:
  - Python建模入门
---

# Python 建模环境与读代码指南

## 1. 先理解四个核心库

| 库 | 主要对象 | 在竞赛中的任务 |
|---|---|---|
| NumPy | `ndarray` 数组 | 数值计算、矩阵、随机模拟 |
| pandas | `Series`、`DataFrame` | 读取、清洗、合并、筛选表格 |
| Matplotlib | `Figure`、`Axes` | 绘图和精细控制 |
| scikit-learn | estimator、transformer、Pipeline | 预处理、机器学习、交叉验证、指标 |

`DataFrame` 可以理解为“带行名和列名的二维表”；`ndarray` 更像只关心数值的矩阵。多数情况下先用 pandas 整理表格，再把特征送给 scikit-learn。

## 2. 推荐环境

建议使用 Miniconda/Anaconda 或普通 Python 虚拟环境，配合 VS Code 或 JupyterLab。竞赛前固定一个环境，不要在比赛当天升级所有库。

```bash
python -m venv .venv
```

Windows PowerShell 激活：

```powershell
.\.venv\Scripts\Activate.ps1
```

安装基础包：

```bash
python -m pip install numpy pandas matplotlib seaborn scipy scikit-learn statsmodels openpyxl jupyterlab
```

按题型再安装：

```bash
python -m pip install xgboost lightgbm pulp pymoo
```

> [!tip] 为什么不一次安装几十个库
> 环境越复杂，依赖冲突越多。先保证基础流程可运行；确定需要某个算法后再安装对应库。

## 3. 一段代码应该怎样读

```python
import pandas as pd

df = pd.read_excel("data.xlsx")
df = df.drop_duplicates()
df["收入"] = pd.to_numeric(df["收入"], errors="coerce")
print(df.describe(include="all"))
```

逐行理解：

1. `import pandas as pd`：导入 pandas，并给它短名 `pd`。
2. `read_excel`：读取 Excel，返回 `DataFrame`。
3. `drop_duplicates`：删除完全重复的行；返回新表，所以重新赋给 `df`。
4. `df["收入"]`：选择名为“收入”的列。
5. `to_numeric(..., errors="coerce")`：尝试转成数值；非法文本变为缺失值 `NaN`。
6. `describe(include="all")`：同时查看数值列与类别列的摘要。

### 常见符号

| 写法 | 意义 |
|---|---|
| `obj.method()` | 对对象调用方法 |
| `func(x, a=1)` | 调用函数，`a` 是有名字的参数 |
| `df["列"]` | 取一列 |
| `df[["列1", "列2"]]` | 取多列，结果仍是表 |
| `df.loc[行条件, 列名]` | 按标签选取 |
| `df.iloc[0:5, 0:3]` | 按位置选取 |
| `X` | 特征矩阵，通常二维 |
| `y` | 目标变量，通常一维 |
| `random_state=42` | 固定随机性，方便复现 |

## 4. NumPy 最小案例

```python
import numpy as np

x = np.array([10, 12, 13, 15, 50], dtype=float)
print("均值:", x.mean())
print("中位数:", np.median(x))
print("标准差:", x.std(ddof=1))

rng = np.random.default_rng(42)
sample = rng.normal(loc=0, scale=1, size=5)
print(sample)
```

`ddof=1` 表示用样本标准差的分母 $n-1$。`default_rng(42)` 创建可复现的随机数生成器。

## 5. pandas 最小案例

```python
import pandas as pd

df = pd.DataFrame({
    "城市": ["A", "B", "C", "D"],
    "人口": [120, 85, 150, 90],
    "污染指数": [62, 48, None, 55]
})

print(df.head())
print(df.dtypes)
print(df.isna().sum())

selected = df.loc[df["人口"] >= 100, ["城市", "人口"]]
print(selected)
```

关键点：布尔条件 `df["人口"] >= 100` 产生一列 `True/False`，`loc` 只留下为真的行。

## 6. Matplotlib 最小案例

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [3, 5, 4, 8]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, marker="o")
ax.set(xlabel="时间", ylabel="指标值", title="指标随时间变化")
ax.grid(alpha=0.3)
fig.tight_layout()
plt.show()
```

推荐始终显式使用 `fig, ax`。`Figure` 是整张画布，`Axes` 是具体坐标区域。

中文乱码时可在程序开头设置：

```python
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False
```

## 7. scikit-learn 的统一接口

```python
from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4]]
y = [2.1, 3.9, 6.2, 7.8]

model = LinearRegression()
model.fit(X, y)
pred = model.predict([[5]])

print("系数:", model.coef_)
print("截距:", model.intercept_)
print("预测:", pred)
```

常见接口：

- `fit(X, y)`：从训练数据学习参数。
- `transform(X)`：按学到的规则转换数据。
- `predict(X)`：预测。
- `fit_transform(X)`：只适合训练阶段的便捷写法。
- `score(X, y)`：返回模型默认分数；正式比较时更建议显式调用指标。

## 8. 最重要的 Pipeline 思维

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0))
])

pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)
```

Pipeline 会保证插补和标准化只在训练集上学习，再把同样规则应用到测试集。详见[[防止数据泄漏与Pipeline]]。

## 9. 报错阅读顺序

1. 看 Traceback 最后一行：错误类型和直接原因。
2. 往上找到第一处属于自己代码的文件与行号。
3. 打印 `shape`、`dtypes`、缺失数和几行数据。
4. 用最小数据复现，不要一次修改五处。

```python
print(df.shape)
print(df.dtypes)
print(df.isna().sum())
print(df.head())
```

## 10. 练习

1. 创建一个包含姓名、成绩、班级的 `DataFrame`。
2. 筛选成绩大于等于 80 的学生。
3. 按班级计算平均成绩。
4. 画出各班平均成绩柱状图。
5. 故意把一个成绩写成 `"缺考"`，观察 `to_numeric(errors="coerce")` 的结果。

## 11. 延伸

- 下一步：[[pandas数据读取与质量审计]]
- 复现规范：[[代码项目结构与复现清单]]
- 官方文档：[pandas User Guide](https://pandas.pydata.org/docs/user_guide/)、[scikit-learn User Guide](https://scikit-learn.org/stable/user_guide)、[Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

