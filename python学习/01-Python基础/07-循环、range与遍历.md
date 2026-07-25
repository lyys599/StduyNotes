---
课程: Python学习
类型: 主题笔记
难度: 必修
预计学习时间: 85分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - Python基础
---

# 循环、range与遍历

> [!abstract] 学完本篇，你要能够
- 使用 `for`与`while`
- 掌握 `range/enumerate/zip`
- 使用 `break/continue`控制流程

## 核心概念

- 优先直接遍历对象
- `enumerate`同时给序号和值
- `zip`按位置配对多个序列

## 与 C 语言对照

Python `for`更像遍历容器，不需要手写 `i++`；需要下标时使用 `enumerate`。

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
cities = ["甲市", "乙市", "丙市"]
values = [72.1, 68.4, 91.0]
for index, (city, value) in enumerate(zip(cities, values), start=1):
    if value < 0:
        continue
    print(index, city, value)

total = 0
for value in values:
    total += value
print("平均值：", total / len(values))
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/01-Python基础/07_loop_report.py|打开对应 `.py` 文件]]。

## 代码拆解

1. `zip`把城市与指标值配对。
2. `enumerate(..., start=1)`生成适合报告的序号。
3. 累计变量要在循环前初始化。

## 数学建模中的用途

循环适合批量处理文件、参数组合和情景；大型数值计算优先用向量化。

## 常见报错与易错点

- 修改正在遍历的列表。
- `range(n)`不包含n。
- 循环内重复读取大文件造成性能浪费。

## 独立练习

同时遍历产品名、成本和收益，输出利润并找到利润最高的产品。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- 本主题暂无前置理论链接。

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
