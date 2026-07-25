# 本文件对应同名主题笔记。建议先自己手敲，再运行本文件核对。
from dataclasses import dataclass
import random
import numpy as np

@dataclass(frozen=True)
class Settings:
    random_seed: int = 42
    threshold: float = 0.10

settings = Settings()
random.seed(settings.random_seed)
rng = np.random.default_rng(settings.random_seed)
print(rng.normal(size=3))
