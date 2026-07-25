# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
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
