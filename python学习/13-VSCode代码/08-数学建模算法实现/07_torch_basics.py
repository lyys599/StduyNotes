# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.tensor([1.0, 2.0, 3.0], device=device, requires_grad=True)
loss = ((x - 2.0) ** 2).mean()
loss.backward()
print("设备：", device)
print("损失：", loss.item())
print("梯度：", x.grad.cpu().numpy())
