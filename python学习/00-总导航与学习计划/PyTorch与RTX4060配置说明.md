---
课程: Python学习
类型: 环境配置
难度: 赛时查阅
tags: [Python, PyTorch, CUDA, RTX4060]
---

# PyTorch与RTX 4060配置说明

## 当前检测结果

- 显卡：NVIDIA GeForce RTX 4060 Laptop GPU
- 显存：约8GB
- NVIDIA驱动：591.74
- `nvidia-smi`报告的驱动CUDA能力：13.1
- 本课程`.venv`当前安装CPU版PyTorch，用于保证示例已经实际运行验证

> [!important] 驱动显示的CUDA版本不等于必须安装同版本的本地CUDA工具包
> 使用pip安装PyTorch预编译包时，应从官方安装选择器选择Windows、Pip、Python和受支持的CUDA构建。不要仅根据`nvidia-smi`数字手工拼接下载地址。

## 什么时候切换CUDA版

Python基础、NumPy、pandas、传统机器学习和小型MLP都可以先用CPU学习。完成[[python学习/08-数学建模算法实现/07-PyTorch张量、设备与自动求导|PyTorch张量、设备与自动求导]]后，再切换CUDA版。

## 安装步骤

1. 关闭正在使用该环境的Notebook与Python终端。
2. 打开[PyTorch官方安装选择器](https://pytorch.org/get-started/locally/)。
3. 选择Windows、Pip、Python和官方当前支持的CUDA版本。
4. 在VS Code终端中运行选择器给出的命令。
5. 运行：

```powershell
python 13-VSCode代码/00-环境检查.py
```

6. 验收：

```python
import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")
```

只有第二项为`True`且第三项显示RTX 4060，才说明当前`.venv`真正使用GPU。

## 8GB显存建议

- 表格MLP从`batch_size=32`或64开始。
- 先用CPU或小样本验证代码正确，再启动GPU训练。
- 遇到显存不足先减小批量，不要盲目降低所有数据精度。
- 保存验证集表现最好的权重，而不是最后一轮权重。
- 比赛前冻结可运行环境，不在比赛当天更换CUDA或PyTorch版本。

## CPU回退

课程代码统一使用：

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

因此CUDA不可用时仍能在CPU运行，不需要维护两份代码。
