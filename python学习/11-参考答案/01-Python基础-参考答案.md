---
课程: Python学习
类型: 参考答案
模块: 01-Python基础
tags: [Python, 参考答案, 数学建模]
---

# Python基础三级练习参考答案

> [!important] 正确使用答案
> 先比较思路，不要逐字复制。找出自己代码与参考实现的三个差异；关闭本页后，从空白文件重写一次。

## 思路拆解

1. 先验证输入形状、字段或取值范围。
2. 把核心计算封装成函数，打印只放在调用处。
3. 先用极小数据人工核对，再运行完整数据。
4. 保存可复查结果，不能只依赖屏幕输出。

## 参考实现

```python
def clean_values(values):
    valid = [value for value in values if 0 <= value <= 100]
    if not valid:
        raise ValueError("没有有效值")
    return {
        "有效值": valid,
        "均值": sum(valid) / len(valid),
        "最大值": max(valid),
        "最小值": min(valid),
    }

records = [
    ("A", 20.0), ("A", -1.0), ("B", 31.0),
    ("B", 999.0), ("B", 28.0), ("C", 26.0),
]
summary = {}
for station, value in records:
    item = summary.setdefault(station, {"总数": 0, "异常数": 0})
    item["总数"] += 1
    if not 0 <= value <= 100:
        item["异常数"] += 1
for station, item in summary.items():
    item["异常率"] = item["异常数"] / item["总数"]
ranking = sorted(summary.items(), key=lambda pair: pair[1]["异常率"],
                 reverse=True)
print(ranking)
```

可运行文件：[[python学习/13-VSCode代码/01-Python基础/模块综合参考.py|模块综合参考.py]]

## 预期结果

数值会随题目数据而不同，但必须满足：程序无未捕获异常、输出量纲合理、排序或指标能用人工小例子复核。

## 常见错误

- 输入校验放在计算之后。
- 只为当前数据写死列号或绝对路径。
- 函数内部同时读取、计算、画图、保存，导致难以测试。
- 对随机结果报告过多小数，却没有固定随机种子。

## 另一种写法

数据规模扩大后，可把基础列表循环替换成NumPy向量化或pandas分组；但替换前后必须在小样本上得到一致结果。
