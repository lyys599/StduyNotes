---
课程: 数学建模国赛
模块: 04-优化决策
文件类型: 方法笔记
来源范围: PDF原有+纠错
优先级: 建议掌握
预计学习时间: 4小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - NSGA-II
  - 多目标优化
  - Pareto前沿
aliases:
  - 非支配排序遗传算法二代
---

# NSGA-II 多目标优化

## 1. 为什么没有唯一最优

多个目标冲突时，一个解若无法在不恶化其他目标的情况下改进任一目标，称为 Pareto 最优。所有非支配解组成 Pareto 前沿。

NSGA-II 使用：

- 快速非支配排序；
- 拥挤距离保持多样性；
- 精英保留；

近似前沿。它常用但不是所有多目标问题的唯一首选。

## 2. pymoo 案例

最小化 $f_1=x^2$ 与 $f_2=(x-2)^2$：

```bash
python -m pip install pymoo
```

```python
import numpy as np
import matplotlib.pyplot as plt
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize

class TradeoffProblem(ElementwiseProblem):
    def __init__(self):
        super().__init__(
            n_var=1,
            n_obj=2,
            n_ieq_constr=0,
            xl=np.array([-1.0]),
            xu=np.array([3.0])
        )

    def _evaluate(self, x, out, *args, **kwargs):
        out["F"] = [x[0] ** 2, (x[0] - 2) ** 2]

algorithm = NSGA2(pop_size=100)
result = minimize(
    TradeoffProblem(),
    algorithm,
    termination=("n_gen", 200),
    seed=42,
    verbose=False
)

plt.scatter(result.F[:, 0], result.F[:, 1], s=15)
plt.xlabel("目标1")
plt.ylabel("目标2")
plt.title("Pareto前沿近似")
plt.show()
```

## 3. 建模重点

- 目标方向统一为最小化或明确转换；
- 目标尺度差异过大时进行合理规范化；
- 约束处理必须说明；
- 种群和代数影响收敛与多样性；
- 决策者最终如何从前沿选折中解必须交代。

可用膝点、偏好权重、阈值或情景选择折中解，但不能把算法输出的一堆点直接当结论。

## 4. 评价

- 收敛性：与参考前沿距离；
- 多样性：解是否覆盖均匀；
- 稳定性：不同随机种子；
- 可行性；
- 运行成本。

## 5. 论文表达

> 成本与服务水平相互冲突，故不预先以单一权重强行合并，而采用 NSGA-II 近似 Pareto 前沿。算法重复运行……次，前沿形态稳定。根据……偏好从膝点区域选择折中方案，并报告其相对两端方案的代价与收益。

## 6. 易错点

- 把所有非支配解都叫“全局最优解”。
- 不解释如何选最终方案。
- 目标单位差异导致搜索偏斜。
- 只画一张漂亮前沿，不验证稳定性。

参考：Deb et al. (2002)；[pymoo NSGA-II](https://pymoo.org/algorithms/moo/nsga2.html)。

