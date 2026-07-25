---
课程: Python学习
类型: 主题笔记
难度: 必修
预计学习时间: 90分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - 数据可视化
---

# Matplotlib的Figure与Axes

> [!abstract] 学完本篇，你要能够
- 使用面向对象接口绘图
- 理解Figure、Axes与Artist
- 保存而不是只显示图像

## 核心概念

- Figure是整张画布
- Axes是一个坐标区域
- `fig.savefig`输出可复现图片

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
from pathlib import Path
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2.1, 3.4, 3.0, 4.8]
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, marker="o", label="观测值")
ax.set(xlabel="时间", ylabel="指标", title="指标变化趋势")
ax.legend()
fig.tight_layout()
fig.savefig(Path("trend.png"), dpi=300, bbox_inches="tight")
plt.close(fig)
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/05-数据可视化/01_figure_axes.py|打开对应 `.py` 文件]]。

## 代码拆解

1. 面向对象接口便于多图和精细控制。
2. `tight_layout`减少遮挡。
3. 保存后关闭图，批量绘图时避免内存堆积。

## 数学建模中的用途

论文中的每一张图都应由脚本生成并保留数据来源和参数。

## 常见报错与易错点

- 用 `plt.show()`阻塞批处理。
- 保存图后忘记关闭。
- 坐标轴没有单位。

## 独立练习

画一张带标题、单位、图例和数据点标记的折线图，保存为300 DPI PNG。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- [[数学建模国赛/02-探索性分析/建模可视化选择指南|建模可视化选择指南]]
- [[数学建模国赛/08-竞赛实战/图表规范与结果叙事|图表规范与结果叙事]]

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
