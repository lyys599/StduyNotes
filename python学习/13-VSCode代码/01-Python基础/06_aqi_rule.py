# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
score = 78
if not 0 <= score <= 100:
    label = "非法"
elif score >= 85:
    label = "优秀"
elif score >= 60:
    label = "合格"
else:
    label = "不合格"
print(label)
