---
课程: Python学习
类型: 主题笔记
难度: 必修
预计学习时间: 105分钟
掌握状态: 未开始
tags:
  - Python
  - 数学建模
  - pandas数据处理
---

# Excel多工作表与结果导出

> [!abstract] 学完本篇，你要能够
- 读取指定或全部工作表
- 用上下文管理器写多表Excel
- 控制索引、列顺序和浮点格式

## 核心概念

- `sheet_name=None`返回工作表字典
- `ExcelWriter`一次写多个表
- 导出前先建立结果数据字典

## 手敲示例

先预测输出，再逐行输入；运行成功后至少修改三个值。

```python
from pathlib import Path
import pandas as pd

output = Path("建模结果.xlsx")
summary = pd.DataFrame({"模型": ["基准"], "MAE": [2.314]})
predictions = pd.DataFrame({"真实值": [10, 12], "预测值": [10.5, 11.8]})
with pd.ExcelWriter(output, engine="openpyxl") as writer:
    summary.to_excel(writer, sheet_name="模型汇总", index=False)
    predictions.to_excel(writer, sheet_name="预测明细", index=False)
print(output.resolve())
```

> [!example] 可运行代码
> [[python学习/13-VSCode代码/04-pandas数据处理/07_excel_io.py|打开对应 `.py` 文件]]。

## 代码拆解

1. 一个Writer管理整个工作簿。
2. 每张结果表命名清楚。
3. 不导出无意义的DataFrame索引。

## 数学建模中的用途

论文手通常直接使用Excel结果；规范导出能减少复制错误。

## 常见报错与易错点

- 覆盖原始附件。
- 工作表名超过31字符。
- 数值被保存为字符串。

## 独立练习

把清洗数据、描述统计、异常记录分别写入同一个Excel的三张工作表。

完成后去本模块的练习题笔记做“基础模仿题”；不要提前打开参考答案。

## 验收清单

- [ ] 不看示例，从空白文件写出同类程序。
- [ ] 能解释示例中每个变量的类型、形状或业务含义。
- [ ] 主动制造一次错误，并能根据报错定位问题。
- [ ] 修改输入数据后，能判断输出是否合理。
- [ ] 能用两三句话向队友解释这段代码解决了什么问题。

## 理论关联

- 本主题暂无前置理论链接。

## 下一步

返回 [[python学习/00-总导航与学习计划/Python数学建模学习总导航|Python数学建模学习总导航]]，按推荐顺序继续。
