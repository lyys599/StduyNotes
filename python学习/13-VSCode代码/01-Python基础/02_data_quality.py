# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
sample_count = 120
missing_count = 7
missing_rate = missing_count / sample_count
qualified = missing_rate < 0.1
print(type(sample_count), type(missing_rate))
print(f"缺失率：{missing_rate:.2%}")
print("是否达到数据质量要求：", qualified)
