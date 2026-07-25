---
课程: Python学习
类型: 主题笔记
难度: 赛时查阅
预计学习时间: 180分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - 数学建模算法实现
---

# PyTorch全连接网络训练

> [!abstract] 学完本篇，你要能够
- 使用Dataset和DataLoader
- 搭建回归全连接网络
- 完成训练、验证、早停与保存

## 核心概念

- 训练循环包含前向、损失、清梯度、反向和更新
- 标准化只在训练集拟合
- 验证损失用于早停

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
import torch
from torch import nn

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = nn.Sequential(
    nn.Linear(4, 16), nn.ReLU(),
    nn.Linear(16, 8), nn.ReLU(),
    nn.Linear(8, 1),
).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_function = nn.MSELoss()
X = torch.randn(32, 4, device=device)
y = torch.randn(32, 1, device=device)
optimizer.zero_grad()
prediction = model(X)
loss = loss_function(prediction, y)
loss.backward()
optimizer.step()
print(loss.item())
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/08-数学建模算法实现/08_torch_mlp.py|打开对应 `.py` 文件]]。

## 代码拆解

1. 输出维度与目标一致。
2. 每批训练前清空旧梯度。
3. 优化器根据梯度更新参数。

## 数学建模中的用途

基础MLP可做表格回归或分类对比模型；必须与线性和树模型公平比较。

## 常见报错与易错点

- 全数据标准化后才划分。
- 训练损失下降就认为泛化良好。
- 不固定随机种子或不保存最佳验证模型。

## 独立练习

完成一个回归和一个二分类网络，加入验证集、早停、学习曲线和最佳权重保存。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- [[数学建模国赛/05-机器学习/机器学习建模总流程|机器学习建模总流程]]
- [[数学建模国赛/07-模型检验/模型对比与消融实验|模型对比与消融实验]]

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
