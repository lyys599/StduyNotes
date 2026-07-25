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
  - 遗传算法
  - GA
  - 启发式优化
aliases:
  - Genetic Algorithm
---

# 遗传算法 GA

## 1. 核心结构

遗传算法维护一群候选解，通过：

1. 适应度评价；
2. 选择；
3. 交叉；
4. 变异；
5. 精英保留；

逐代寻找较优解。它对不可导、非凸、离散或黑箱目标有用，但通常**不保证全局最优**。

## 2. 最小连续案例

最大化：

$$
f(x)=10-(x-3)^2,\quad -5\le x\le10
$$

```python
import numpy as np

rng = np.random.default_rng(42)
pop_size = 40
generations = 80
mutation_sd = 0.3

pop = rng.uniform(-5, 10, pop_size)

def fitness(x):
    return 10 - (x - 3) ** 2

for _ in range(generations):
    score = fitness(pop)

    # 精英：保留最好两个
    elite = pop[np.argsort(score)[-2:]]

    # 锦标赛选择
    parents = []
    for _ in range(pop_size - 2):
        idx = rng.choice(pop_size, 3, replace=False)
        parents.append(pop[idx[np.argmax(score[idx])]])
    parents = np.array(parents)

    # 算术交叉
    rng.shuffle(parents)
    children = []
    for i in range(0, len(parents) - 1, 2):
        a = rng.random()
        children += [
            a * parents[i] + (1-a) * parents[i+1],
            a * parents[i+1] + (1-a) * parents[i]
        ]
    children = np.array(children[:pop_size-2])

    # 变异并修复边界
    children += rng.normal(0, mutation_sd, len(children))
    children = np.clip(children, -5, 10)
    pop = np.r_[elite, children]

best = pop[np.argmax(fitness(pop))]
print("best x:", best, "fitness:", fitness(best))
```

## 3. 约束处理

- 修复：把不可行解投影/调整回可行域；
- 罚函数：违反约束就降低适应度；
- 可行优先规则；
- 专门编码保证天然可行。

罚系数过小会保留不可行解，过大会妨碍搜索。

## 4. 参数

- 种群规模；
- 代数；
- 交叉率；
- 变异率；
- 选择压力；
- 停止条件。

至少运行多个随机种子，报告最好值、中位数和波动，而不是只展示一次幸运结果。

## 5. 论文表达

> 由于目标函数非凸且含离散决策，采用遗传算法搜索可行解。使用……编码、……约束修复策略，种群规模……，迭代……代。对 30 个随机种子重复运行，目标值中位数为……，最优值为……，并与简单基线/精确小规模解比较。

## 6. 易错点

- 说“获得全局最优”却无证明。
- 只调一次参数和随机种子。
- 不说明编码、约束和停止条件。
- 能用线性/整数规划精确求解却直接上 GA。

关联：[[模拟退火SA]]、[[NSGA-II多目标优化]]。

