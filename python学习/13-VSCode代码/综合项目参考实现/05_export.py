
import pandas as pd
from common import OUTPUT_DIR, ensure_directories


def main() -> None:
    ensure_directories()
    sheets = {
        "城市评价": pd.read_csv(OUTPUT_DIR / "city_scores.csv"),
        "模型评价": pd.read_csv(OUTPUT_DIR / "forecast_metrics.csv"),
        "下季预测": pd.read_csv(OUTPUT_DIR / "next_quarter_forecast.csv"),
        "资源配置": pd.read_csv(OUTPUT_DIR / "allocation_scenarios.csv"),
    }
    with pd.ExcelWriter(OUTPUT_DIR / "模拟C题结果.xlsx", engine="openpyxl") as writer:
        for sheet_name, frame in sheets.items():
            frame.to_excel(writer, sheet_name=sheet_name, index=False)
    print(OUTPUT_DIR / "模拟C题结果.xlsx")


if __name__ == "__main__":
    main()
