# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
years = [2022, 2023, 2024, 2025]
values = [62, 68, 74, 71]
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(years, values, color="#4C78A8")
ax.axhline(70, color="#E45756", linestyle="--", label="目标线")
ax.annotate("最高", xy=(2024, 74), xytext=(2023.4, 80),
            arrowprops={"arrowstyle": "->"})
ax.set_ylabel("综合得分")
ax.legend()
fig.tight_layout()
fig.savefig("styled_chart.png", dpi=300)
plt.close(fig)
