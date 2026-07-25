
import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp
from common import DATA_DIR, OUTPUT_DIR, ensure_directories


def solve(budget: float = 1800.0, benefit_scale: float = 1.0) -> pd.DataFrame:
    projects = pd.read_csv(DATA_DIR / "附件3_应急项目.csv")
    scores = pd.read_csv(OUTPUT_DIR / "city_scores.csv")
    forecast = pd.read_csv(OUTPUT_DIR / "next_quarter_forecast.csv")
    risk = forecast.groupby("城市ID", as_index=False)["预测灾害损失率"].mean()
    projects = projects.merge(scores[["城市ID", "韧性得分"]], on="城市ID",
                              validate="many_to_one")
    projects = projects.merge(risk, on="城市ID", validate="many_to_one")
    projects["综合收益"] = benefit_scale * (
        projects["预测风险下降"] * (1 + projects["预测灾害损失率"] / 10)
        + projects["韧性提升"] * (1 + (1 - projects["韧性得分"]))
    )
    n = len(projects)
    constraints = [LinearConstraint(projects["成本"].to_numpy()[None, :], -np.inf, budget)]
    for _, index in projects.groupby("城市ID").groups.items():
        row = np.zeros(n)
        row[list(index)] = 1
        constraints.append(LinearConstraint(row[None, :], -np.inf, 2))
    result = milp(
        c=-projects["综合收益"].to_numpy(),
        integrality=np.ones(n),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=constraints,
        options={"time_limit": 30},
    )
    if not result.success:
        raise RuntimeError(result.message)
    projects["是否选择"] = (result.x > 0.5).astype(int)
    chosen = projects.loc[projects["是否选择"] == 1].copy()
    if chosen["成本"].sum() > budget + 1e-6:
        raise AssertionError("预算约束未满足")
    return chosen


def main() -> None:
    ensure_directories()
    all_scenarios = []
    for budget in (1620, 1800, 1980):
        for scale in (0.9, 1.0, 1.1):
            chosen = solve(budget, scale)
            chosen["预算情景"] = budget
            chosen["收益系数"] = scale
            all_scenarios.append(chosen)
    result = pd.concat(all_scenarios, ignore_index=True)
    result.to_csv(OUTPUT_DIR / "allocation_scenarios.csv", index=False, encoding="utf-8-sig")
    base = result.loc[(result["预算情景"] == 1800) & (result["收益系数"] == 1.0)]
    print("base cost:", base["成本"].sum(), "projects:", len(base))


if __name__ == "__main__":
    main()
