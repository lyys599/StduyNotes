
from __future__ import annotations

import importlib
import os
import platform
import sys
from pathlib import Path

matplotlib_cache = Path(__file__).resolve().parents[1] / "tmp" / ".matplotlib"
matplotlib_cache.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(matplotlib_cache))


PACKAGES = [
    "numpy", "pandas", "matplotlib", "seaborn", "scipy",
    "statsmodels", "sklearn", "openpyxl", "torch",
]


def main() -> None:
    print("Python:", sys.version.replace("\n", " "))
    print("解释器:", sys.executable)
    print("系统:", platform.platform())
    for name in PACKAGES:
        try:
            module = importlib.import_module(name)
            version = getattr(module, "__version__", "未知")
            print(f"[OK] {name:<12} {version}")
        except Exception as error:
            print(f"[--] {name:<12} {type(error).__name__}: {error}")
    try:
        import torch
        print("CUDA可用:", torch.cuda.is_available())
        if torch.cuda.is_available():
            print("GPU:", torch.cuda.get_device_name(0))
    except ImportError:
        pass


if __name__ == "__main__":
    main()
