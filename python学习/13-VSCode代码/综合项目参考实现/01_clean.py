
import json
import pandas as pd
from common import DATA_DIR, OUTPUT_DIR, ensure_directories


def main() -> None:
    ensure_directories()
    monthly = pd.read_csv(DATA_DIR / "附件1_城市月度监测.csv", parse_dates=["日期"])
    cities = pd.read_csv(DATA_DIR / "附件2_城市基础信息.csv")
    before = len(monthly)
    duplicate_count = int(monthly["记录ID"].duplicated().sum())
    monthly = monthly.drop_duplicates("记录ID").copy()
    numeric = ["经济活力", "医疗负荷", "应急响应时间", "基础设施完好率", "灾害损失率", "降雨量"]
    missing_before = monthly[numeric].isna().sum().astype(int).to_dict()
    for column in numeric:
        monthly[column] = monthly[column].fillna(
            monthly.groupby("城市ID")[column].transform("median")
        )
        monthly[column] = monthly[column].fillna(monthly[column].median())
    anomaly_rows = []
    for column in numeric:
        q1, q3 = monthly[column].quantile([0.25, 0.75])
        lower, upper = q1 - 3 * (q3 - q1), q3 + 3 * (q3 - q1)
        mask = ~monthly[column].between(lower, upper)
        if mask.any():
            part = monthly.loc[mask, ["记录ID", "城市ID", "日期", column]].copy()
            part["字段"] = column
            part["原值"] = part[column]
            anomaly_rows.append(part.drop(columns=column))
            monthly.loc[mask, column] = monthly.loc[~mask, column].median()
    merged = monthly.merge(
        cities, on="城市ID", how="left", validate="many_to_one", indicator=True
    )
    if (merged["_merge"] != "both").any():
        raise ValueError("存在无法匹配的城市ID")
    merged = merged.drop(columns="_merge")
    anomalies = pd.concat(anomaly_rows, ignore_index=True) if anomaly_rows else pd.DataFrame()
    log = {
        "清洗前行数": before,
        "重复记录数": duplicate_count,
        "清洗后行数": len(merged),
        "缺失数": missing_before,
        "异常替换数": len(anomalies),
    }
    merged.to_csv(OUTPUT_DIR / "clean_monthly.csv", index=False, encoding="utf-8-sig")
    anomalies.to_csv(OUTPUT_DIR / "anomalies.csv", index=False, encoding="utf-8-sig")
    (OUTPUT_DIR / "cleaning_log.json").write_text(
        json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(log)


if __name__ == "__main__":
    main()
