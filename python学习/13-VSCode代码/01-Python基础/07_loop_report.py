# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
cities = ["甲市", "乙市", "丙市"]
values = [72.1, 68.4, 91.0]
for index, (city, value) in enumerate(zip(cities, values), start=1):
    if value < 0:
        continue
    print(index, city, value)

total = 0
for value in values:
    total += value
print("平均值：", total / len(values))
