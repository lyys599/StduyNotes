# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
from pathlib import Path
import pandas as pd

output = Path("建模结果.xlsx")
summary = pd.DataFrame({"模型": ["基准"], "MAE": [2.314]})
predictions = pd.DataFrame({"真实值": [10, 12], "预测值": [10.5, 11.8]})
with pd.ExcelWriter(output, engine="openpyxl") as writer:
    summary.to_excel(writer, sheet_name="模型汇总", index=False)
    predictions.to_excel(writer, sheet_name="预测明细", index=False)
print(output.resolve())
