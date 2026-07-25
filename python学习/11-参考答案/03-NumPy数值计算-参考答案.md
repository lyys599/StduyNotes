---
课程: Python学习
类型: 参考答案
模块: 03-NumPy数值计算
tags: [Python, 参考答案, 数学建模]
---

# NumPy三级练习参考答案

> [!important] 正确使用答案
> 先比较思路，不要逐字复制。找出自己代码与参考实现的三个差异；关闭本页后，从空白文件重写一次。

## 思路拆解

1. 先验证输入形状、字段或取值范围。
2. 把核心计算封装成函数，打印只放在调用处。
3. 先用极小数据人工核对，再运行完整数据。
4. 保存可复查结果，不能只依赖屏幕输出。

## 参考实现

```python
import numpy as np

def minmax(X):
    X = np.asarray(X, dtype=float)
    minimum = X.min(axis=0)
    span = X.max(axis=0) - minimum
    safe_span = np.where(span == 0, 1, span)
    return (X - minimum) / safe_span

def simulate_profit(n=100_000, seed=42):
    rng = np.random.default_rng(seed)
    price = rng.normal(20, 1.5, n)
    demand = np.maximum(rng.normal(1000, 120, n), 0)
    unit_cost = rng.triangular(12, 14, 17, n)
    fixed_cost = 4200
    profit = (price - unit_cost) * demand - fixed_cost
    return {
        "盈利概率": float((profit > 0).mean()),
        "平均利润": float(profit.mean()),
        "95%区间": np.quantile(profit, [0.025, 0.975]).tolist(),
    }

print(simulate_profit())
```

可运行文件：[[python学习/13-VSCode代码/03-NumPy数值计算/模块综合参考.py|模块综合参考.py]]

## 预期结果

数值会随题目数据而不同，但必须满足：程序无未捕获异常、输出量纲合理、排序或指标能用人工小例子复核。

## 常见错误

- 输入校验放在计算之后。
- 只为当前数据写死列号或绝对路径。
- 函数内部同时读取、计算、画图、保存，导致难以测试。
- 对随机结果报告过多小数，却没有固定随机种子。

## 另一种写法

数据规模扩大后，可把基础列表循环替换成NumPy向量化或pandas分组；但替换前后必须在小样本上得到一致结果。
