# 完成独立尝试后再阅读本文件。
import json
from pathlib import Path
import pandas as pd

def audit_csv(input_path: Path, key: str) -> dict:
    df = pd.read_csv(input_path)
    if key not in df.columns:
        raise ValueError(f"缺少主键列：{key}")
    return {
        "行数": len(df),
        "列数": df.shape[1],
        "主键重复数": int(df[key].duplicated().sum()),
        "各列缺失数": df.isna().sum().astype(int).to_dict(),
    }

def main():
    root = Path(__file__).resolve().parents[2]
    result = audit_csv(root / "12-示例数据" / "环境监测数据.csv", "记录ID")
    output = root / "tmp" / "审计摘要.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2),
                      encoding="utf-8")
    print(result)

if __name__ == "__main__":
    main()
