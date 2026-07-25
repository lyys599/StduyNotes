
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "12-示例数据"
OUTPUT_DIR = ROOT / "tmp" / "比赛模板输出"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    measurements = pd.read_csv(DATA / "环境监测数据.csv", parse_dates=["日期"])
    stations = pd.read_csv(DATA / "站点信息.csv")
    measurements = measurements.drop_duplicates("记录ID").copy()
    measurements["温度"] = measurements["温度"].fillna(
        measurements.groupby("站点")["温度"].transform("median")
    )
    merged = measurements.merge(
        stations, on="站点", how="left", validate="many_to_one", indicator=True
    )
    if (merged["_merge"] != "both").any():
        raise ValueError("存在未匹配站点")
    merged.drop(columns="_merge").to_csv(
        OUTPUT_DIR / "clean_merged.csv", index=False, encoding="utf-8-sig"
    )
    print("clean shape:", merged.shape)


if __name__ == "__main__":
    main()
