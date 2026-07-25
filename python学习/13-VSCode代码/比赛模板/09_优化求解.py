
import numpy as np
from scipy.optimize import linprog


def main() -> None:
    profit = np.array([5, 7, 4], dtype=float)
    A = np.array([[2, 3, 1], [1, 2, 2]], dtype=float)
    b = np.array([180, 120], dtype=float)
    result = linprog(-profit, A_ub=A, b_ub=b,
                     bounds=[(0, None)] * 3, method="highs")
    if not result.success:
        raise RuntimeError(result.message)
    print("x:", result.x)
    print("objective:", -result.fun)
    print("feasible:", np.all(A @ result.x <= b + 1e-7))


if __name__ == "__main__":
    main()
