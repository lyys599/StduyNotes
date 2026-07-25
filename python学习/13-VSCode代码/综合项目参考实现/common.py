
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "12-示例数据" / "模拟C题"
OUTPUT_DIR = ROOT / "tmp" / "模拟C题输出"
FIGURE_DIR = OUTPUT_DIR / "figures"
RANDOM_SEED = 42


def ensure_directories() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
