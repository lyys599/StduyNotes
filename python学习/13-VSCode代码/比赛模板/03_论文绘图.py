
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "12-示例数据" / "环境监测数据.csv"
OUTPUT_DIR = ROOT / "tmp" / "比赛模板输出"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA, parse_dates=["日期"])
    daily = df.groupby("日期", as_index=False)["PM2.5"].mean()
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(daily["日期"], daily["PM2.5"], color="#4C78A8")
    ax.set(xlabel="Date", ylabel="PM2.5 (ug/m3)", title="Daily PM2.5")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "paper_figure.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
