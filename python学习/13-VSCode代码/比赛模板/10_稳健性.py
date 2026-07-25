
import numpy as np


def bootstrap_mean(values, n_bootstrap=5000, seed=42):
    values = np.asarray(values, dtype=float)
    rng = np.random.default_rng(seed)
    samples = rng.choice(values, size=(n_bootstrap, len(values)), replace=True)
    means = samples.mean(axis=1)
    return np.quantile(means, [0.025, 0.5, 0.975])


def main() -> None:
    values = [12, 15, 14, 18, 20, 17, 16]
    print(bootstrap_mean(values))


if __name__ == "__main__":
    main()
