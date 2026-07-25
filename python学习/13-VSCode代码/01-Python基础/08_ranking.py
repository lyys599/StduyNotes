# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
scores = {"甲": 82, "乙": 91, "丙": 76}
passed = {name: score for name, score in scores.items() if score >= 80}
ranking = sorted(scores.items(), key=lambda item: item[1], reverse=True)
print(passed)
print(ranking)
