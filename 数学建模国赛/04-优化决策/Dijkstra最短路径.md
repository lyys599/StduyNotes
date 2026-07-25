---
课程: 数学建模国赛
模块: 04-优化决策
文件类型: 方法笔记
来源范围: PDF提及+扩展
优先级: 建议掌握
预计学习时间: 2小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - Dijkstra
  - 图论
  - 最短路径
aliases:
  - 迪杰斯特拉算法
---

# Dijkstra 最短路径

## 1. 解决什么

在边权非负的图中，求一个源点到其他节点的最短距离。交通时间、成本、风险都可作为边权，但必须是可加且非负。

若存在负权边，Dijkstra 不适用；可考虑 Bellman-Ford。若要经过多个点、容量或时间窗约束，则可能变成车辆路径等更复杂问题。

## 2. Python 手写案例

```python
import heapq
import math

graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 1), ("D", 5)],
    "C": [("B", 1), ("D", 8), ("E", 10)],
    "D": [("E", 2)],
    "E": []
}

def dijkstra(graph, source):
    dist = {node: math.inf for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist != dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, prev

def build_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return path[::-1]

dist, prev = dijkstra(graph, "A")
print(dist["E"], build_path(prev, "E"))
```

## 3. 建图比算法更重要

需要说明：

- 节点代表什么；
- 边何时存在；
- 有向还是无向；
- 权重单位和来源；
- 交通拥堵等动态因素如何处理；
- 不可达节点怎样报告。

## 4. 多指标路径

时间、成本、风险无法简单相加时，可：

- 先规范化再加权；
- 设置一个目标，其他作为约束；
- 做多目标最短路径并输出 Pareto 方案。

权重选择必须有依据。

## 5. 论文表达

> 将站点建模为节点、可通行路段建模为有向边，以预计通行时间作为非负边权。采用 Dijkstra 求源点到各节点最短时间，并回溯前驱节点得到路径。对高峰时段重新估计边权进行敏感性分析。

## 6. 易错点

- 有负边仍使用 Dijkstra。
- 把地理直线距离当实际通行成本。
- 节点/边构造不解释。
- 只给最短距离，不输出路径与可行性。
