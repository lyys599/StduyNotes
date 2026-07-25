
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "12-示例数据" / "环境监测数据.csv"
OUTPUT_DIR = ROOT / "tmp" / "比赛模板输出"


def audit(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing_count": df.isna().sum(),
        "missing_rate": df.isna().mean(),
        "unique_count": df.nunique(dropna=False),
    })


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA_PATH)
    print("shape:", df.shape)
    print("columns:", df.columns.tolist())
    audit(df).to_csv(OUTPUT_DIR / "audit.csv", encoding="utf-8-sig")
    df.describe(include="all").to_csv(
        OUTPUT_DIR / "describe.csv", encoding="utf-8-sig"
    )


if __name__ == "__main__":
    main()
