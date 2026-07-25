
from pathlib import Path
import subprocess
import sys


def main() -> None:
    folder = Path(__file__).resolve().parent
    scripts = ["01_clean.py", "02_evaluate.py", "03_predict.py",
               "04_optimize.py", "05_export.py"]
    for script in scripts:
        print(f"\n===== RUN {script} =====")
        subprocess.run([sys.executable, str(folder / script)], check=True)


if __name__ == "__main__":
    main()
