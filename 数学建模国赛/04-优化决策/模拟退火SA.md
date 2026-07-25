---
课程: 数学建模国赛
模块: 04-优化决策
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 建议掌握
预计学习时间: 3小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - 模拟退火
  - SA
  - 启发式优化
aliases:
  - Simulated Annealing
---

# 模拟退火 SA

## 1. 接受机制

最小化目标 $f(x)$。新解更好就接受；更差时以概率：

$$
P(\text{accept})=\exp\left(-\frac{\Delta f}{T}\right)
$$

接受，从而有机会跳出局部最优。温度 $T$ 逐渐降低，搜索从探索转向收敛。

## 2. 最小案例

```python
import numpy as np

rng = np.random.default_rng(42)

def f(x):
    return (x - 2) ** 2 + 3 * np.sin(5 * x)

x = 0.0
best_x = x
best_f = f(x)
T = 10.0

for step in range(5000):
    candidate = x + rng.normal(0, 0.5)
    candidate = np.clip(candidate, -5, 5)
    delta = f(candidate) - f(x)

    if delta <= 0 or rng.random() < np.exp(-delta / T):
        x = candidate

    if f(x) < best_f:
        best_x, best_f = x, f(x)

    T *= 0.998
    if T < 1e-4:
        break

print(best_x, best_f)
```

## 3. 关键设计

- 初始温度：应使早期有较高概率接受差解；
- 邻域：决定一步能走多远；
- 降温率：太快易困局部，太慢耗时；
- 每个温度的迭代数；
- 停止条件；
- 约束修复。

## 4. 适用场景

- 组合优化；
- 非光滑或黑箱目标；
- 只有一个当前解，内存要求低；
- 可以快速计算邻域解。

与 GA 相比，SA 维护单个解；GA 维护种群，更易并行和保持多样性。

## 5. 结果验证

- 多随机种子重复；
- 与贪心、局部搜索或小规模精确解比较；
- 画最佳目标随迭代变化；
- 报告可行率、运行时间和分布。

## 6. 易错点

- 温度公式与目标尺度不匹配。
- 邻域无法覆盖可行空间。
- 只运行一次就宣称最优。
- 约束通过巨额罚函数处理却不检查最终可行性。

关联：[[遗传算法GA]]。

