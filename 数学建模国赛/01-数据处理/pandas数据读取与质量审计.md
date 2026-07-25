---
课程: 数学建模国赛
模块: 01-数据处理
文件类型: 方法笔记
来源范围: 扩展
优先级: 必须掌握
预计学习时间: 2小时
复习状态: 未开始
创建时间: 2026-07-25
tags:
  - pandas
  - 数据审计
  - 数据质量
aliases:
  - 数据质量报告
---

# pandas 数据读取与质量审计

## 1. 宏观定位

数据审计是在“修改数据”之前回答：数据有多少、各列是什么、哪里可能错。没有审计记录就直接填补或删行，论文中很难解释处理依据。

## 2. 读取时先控制什么

```python
import pandas as pd

df = pd.read_excel(
    "附件1.xlsx",
    sheet_name="数据",
    na_values=["-", "--", "缺失", "无", ""]
)

print(df.shape)
print(df.head())
print(df.dtypes)
```

- `sheet_name` 明确工作表，避免读错默认页。
- `na_values` 把题目中特殊缺失标记统一成 `NaN`。
- 不要看到数字就默认单位一致；“万元”和“元”必须先统一。

CSV 中文乱码时尝试 `encoding="utf-8-sig"` 或先确认文件实际编码，不要盲目轮换。

## 3. 一份最小质量报告

```python
def quality_report(df: pd.DataFrame) -> pd.DataFrame:
    n = len(df)
    report = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing_n": df.isna().sum(),
        "missing_rate": df.isna().mean(),
        "unique_n": df.nunique(dropna=True),
        "duplicate_rate": [
            df[col].duplicated(keep=False).mean()
            for col in df.columns
        ]
    })
    report["constant"] = report["unique_n"] <= 1
    report["missing_rate"] = report["missing_rate"].round(4)
    return report.sort_values("missing_rate", ascending=False)

print(quality_report(df))
print("整行重复数:", df.duplicated().sum())
```

`unique_n <= 1` 提醒常量列，但常量列也可能是题目分组后的合法结果，不能自动删除。

## 4. 数值与类别摘要

```python
print(df.describe().T)
print(df.describe(include=["object", "category"]).T)
```

重点看：

- 最小/最大值是否违反业务边界；
- 均值与中位数差异是否提示偏态；
- 类别拼写是否混乱，如“广东”“广东省”“ 广东”；
- 时间列是否被读取为字符串；
- 身份编号是否被错误读成浮点数。

```python
df["日期"] = pd.to_datetime(df["日期"], errors="coerce")
df["金额"] = pd.to_numeric(df["金额"], errors="coerce")
df["地区"] = df["地区"].astype("string").str.strip()
```

## 5. 逻辑约束检查

```python
checks = pd.DataFrame(index=df.index)
checks["年龄非法"] = ~df["年龄"].between(0, 120)
checks["结束早于开始"] = df["结束日期"] < df["开始日期"]
checks["金额为负"] = df["金额"] < 0

bad_rows = df.loc[checks.any(axis=1)].copy()
bad_rows["违反规则"] = checks.apply(
    lambda row: "；".join(row.index[row]),
    axis=1
)
print(bad_rows)
```

保留“问题行清单”，比直接 `drop` 更适合竞赛复核。

## 6. 论文中怎么写

> 本文首先对原始数据进行质量审计，统计各字段的数据类型、缺失率、唯一值数和取值范围，并依据题意建立年龄范围、日期先后和金额非负等逻辑校验规则。对于被标记的记录，结合原始附件逐项核查，再决定修正、保留或剔除，以避免将真实极端事件误判为错误数据。

## 7. 易错点

> [!warning]
> - `errors="coerce"` 会把非法文本变成缺失值，转换后必须比较缺失数是否增加。
> - 编号列不要做均值或标准化。
> - `df.info()` 显示非空数量，不等于数据完全有效。
> - 不要覆盖原始文件；保留 `raw` 与 `processed` 两份。

## 8. 练习

构造 10 行数据，故意加入一个负金额、一个非法日期、一个重复主键和一个字符串数字。输出质量报告和问题行清单。

关联：[[数据筛选与逻辑校验]]、[[多表合并与主键验证]]。

