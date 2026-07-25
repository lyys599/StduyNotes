# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
def safe_ratio(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ValueError("分母不能为0")
    return numerator / denominator

try:
    print(safe_ratio(7, 0))
except ValueError as error:
    print("输入检查失败：", error)
