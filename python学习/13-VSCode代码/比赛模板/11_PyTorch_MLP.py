
import torch
from torch import nn


def main() -> None:
    torch.manual_seed(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    X = torch.randn(128, 4, device=device)
    y = (2 * X[:, :1] - X[:, 1:2] + 0.1 * torch.randn(128, 1, device=device))
    model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1)).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.02)
    loss_fn = nn.MSELoss()
    for _ in range(100):
        optimizer.zero_grad()
        loss = loss_fn(model(X), y)
        loss.backward()
        optimizer.step()
    print("device:", device, "loss:", loss.item())


if __name__ == "__main__":
    main()
