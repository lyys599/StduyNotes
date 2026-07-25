# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
values = [18.2, 20.1, 19.7, 50.0, 21.3]
normal = [x for x in values if x < 40]
normal.append(22.0)
print("前三项：", normal[:3])
print("均值：", sum(normal) / len(normal))
station = ("A01", 31.2, 121.5)
print("站点编号：", station[0])
