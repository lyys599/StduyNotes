---
课程: Python学习
类型: 参考答案
模块: 06-SciPy与优化
tags: [Python, 参考答案, 数学建模]
---

# SciPy与优化三级练习参考答案

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
from scipy.optimize import linprog

profit = np.array([5, 7, 4], dtype=float)
resources = np.array([[2, 3, 1], [1, 2, 2]], dtype=float)
limits = np.array([180, 120], dtype=float)
result = linprog(
    -profit, A_ub=resources, b_ub=limits,
    bounds=[(0, None)] * 3, method="highs"
)
if not result.success:
    raise RuntimeError(result.message)
print("方案：", result.x)
print("利润：", -result.fun)
print("资源消耗：", resources @ result.x)
print("剩余资源：", limits - resources @ result.x)
```

可运行文件：[[python学习/13-VSCode代码/06-SciPy与优化/模块综合参考.py|模块综合参考.py]]

## 预期结果

数值会随题目数据而不同，但必须满足：程序无未捕获异常、输出量纲合理、排序或指标能用人工小例子复核。

## 常见错误

- 输入校验放在计算之后。
- 只为当前数据写死列号或绝对路径。
- 函数内部同时读取、计算、画图、保存，导致难以测试。
- 对随机结果报告过多小数，却没有固定随机种子。

## 另一种写法

数据规模扩大后，可把基础列表循环替换成NumPy向量化或pandas分组；但替换前后必须在小样本上得到一致结果。
