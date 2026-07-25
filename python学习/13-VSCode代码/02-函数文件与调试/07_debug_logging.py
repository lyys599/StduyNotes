# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
values = [2, 4, 8]
logging.info("开始处理，样本量=%d", len(values))
result = sum(values) / len(values)
logging.info("处理完成，均值=%.3f", result)
