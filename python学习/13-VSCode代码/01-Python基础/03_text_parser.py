# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
raw = "  A区,2026-07-26,PM2.5=43.7  "
clean = raw.strip()
region, day, value_text = clean.split(",")
value = float(value_text.split("=")[1])
report = f"{day} {region} 的PM2.5为 {value:.1f}"
print(report)
