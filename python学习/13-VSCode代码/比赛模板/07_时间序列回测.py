
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def main() -> None:
    rng = np.random.default_rng(42)
    t = np.arange(48)
    y = 100 + 0.8 * t + 10 * np.sin(2 * np.pi * t / 12) + rng.normal(0, 2, len(t))
    series = pd.Series(y, index=pd.date_range("2022-01-01", periods=48, freq="MS"))
    train, test = series.iloc[:-6], series.iloc[-6:]
    naive = np.repeat(train.iloc[-1], len(test))
    model = ExponentialSmoothing(
        train, trend="add", seasonal="add", seasonal_periods=12
    ).fit()
    pred = model.forecast(len(test))
    print("naive MAE:", mean_absolute_error(test, naive))
    print("ETS MAE:", mean_absolute_error(test, pred))


if __name__ == "__main__":
    main()
