---
课程: 数学建模国赛
模块: 03-统计与预测
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 必须掌握
预计学习时间: 2小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - Lasso
  - L1正则化
  - 特征选择
aliases:
  - Lasso回归
---

# Lasso 回归

## 1. 目标函数

$$
\min_\beta\left[
\frac{1}{2n}\sum_{i=1}^{n}(y_i-\beta_0-x_i^T\beta)^2
+\lambda\sum_{j=1}^{p}|\beta_j|
\right]
$$

L1 惩罚可把一部分系数压到 0，因而兼具预测与变量筛选。

## 2. 适用边界

适合：

- 特征很多，真正有用的可能较少；
- 希望得到较简洁模型；
- 连续特征已标准化。

注意：

- 强相关变量中可能任意保留一个，选择不稳定；
- 真正信号密集时岭回归可能更好；
- 数据驱动选择后的普通 p 值不再可靠。

## 3. Python 案例

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoCV
from sklearn.model_selection import KFold

cv = KFold(5, shuffle=True, random_state=42)

model = make_pipeline(
    StandardScaler(),
    LassoCV(
        cv=cv,
        random_state=42,
        max_iter=20000
    )
)
model.fit(X_train, y_train)

lasso = model.named_steps["lassocv"]
print("最佳alpha:", lasso.alpha_)
print("系数:", lasso.coef_)
```

查看入选特征：

```python
selected = X_train.columns[lasso.coef_ != 0]
print(selected.tolist())
```

## 4. 稳定性选择

对数据多次 Bootstrap，记录每个变量被选中的比例。若一个变量只在少数抽样中入选，不应被强解释。

## 5. 论文表达

> 为获得稀疏模型，在训练折内标准化后采用 Lasso，并通过交叉验证选择惩罚参数。最终保留……个非零特征。考虑到相关特征间选择可能不稳定，进一步通过 Bootstrap 计算入选频率，仅对高频且方向稳定的变量作解释。

## 6. 易错点

- 把“系数为 0”解释成现实中绝对没有作用。
- 在全数据上先 Lasso 筛选，再交叉验证普通模型。
- 未检查相关变量导致的随机选择。
- 把 Lasso 当作唯一的因果筛选工具。

可比较 Elastic Net：同时包含 L1 与 L2，在相关特征成组存在时更稳定。

