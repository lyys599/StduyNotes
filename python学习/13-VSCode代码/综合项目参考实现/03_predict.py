
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from common import FIGURE_DIR, OUTPUT_DIR, ensure_directories


def main() -> None:
    ensure_directories()
    df = pd.read_csv(OUTPUT_DIR / "clean_monthly.csv", parse_dates=["日期"])
    rows, forecasts = [], []
    for (city_id, city_name), group in df.groupby(["城市ID", "城市名称"]):
        series = group.sort_values("日期").set_index("日期")["灾害损失率"]
        train, test = series.iloc[:-3], series.iloc[-3:]
        naive = np.repeat(train.iloc[-1], len(test))
        model = ExponentialSmoothing(
            train, trend="add", seasonal="add", seasonal_periods=12
        ).fit(optimized=True)
        pred = model.forecast(len(test))
        rows.append({
            "城市ID": city_id, "城市名称": city_name,
            "朴素MAE": mean_absolute_error(test, naive),
            "ETS_MAE": mean_absolute_error(test, pred),
            "ETS_RMSE": np.sqrt(mean_squared_error(test, pred)),
        })
        final_model = ExponentialSmoothing(
            series, trend="add", seasonal="add", seasonal_periods=12
        ).fit(optimized=True)
        future = final_model.forecast(3)
        for day, value in future.items():
            forecasts.append({
                "城市ID": city_id, "城市名称": city_name,
                "日期": day, "预测灾害损失率": max(float(value), 0.0),
            })
    metrics = pd.DataFrame(rows)
    forecast_df = pd.DataFrame(forecasts)
    metrics.to_csv(OUTPUT_DIR / "forecast_metrics.csv", index=False, encoding="utf-8-sig")
    forecast_df.to_csv(OUTPUT_DIR / "next_quarter_forecast.csv", index=False, encoding="utf-8-sig")
    first_city = df["城市名称"].iloc[0]
    history = df.loc[df["城市名称"] == first_city].sort_values("日期")
    future = forecast_df.loc[forecast_df["城市名称"] == first_city]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(history["日期"], history["灾害损失率"], label="history")
    ax.plot(pd.to_datetime(future["日期"]), future["预测灾害损失率"],
            marker="o", label="forecast")
    ax.legend()
    ax.set(title=f"Risk forecast: {first_city}", ylabel="Loss rate")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "risk_forecast.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(metrics.mean(numeric_only=True).to_dict())


if __name__ == "__main__":
    main()
