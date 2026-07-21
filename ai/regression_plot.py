#!/usr/bin/env python3
"""Linear regression analysis of salary versus years of experience."""

import os
from pathlib import Path

cache_dir = Path(__file__).parent / ".matplotlib_cache"
cache_dir.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(cache_dir))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

SCRIPT_DIR = Path(__file__).parent
DATA_FILE = SCRIPT_DIR / "regression_data.csv"
OUTPUT_FILE = SCRIPT_DIR / "linear_regression_python_output.png"

X_COLUMN = "YearsExperience"
Y_COLUMN = "Salary"
PREDICT_YEARS = 6.0


def format_currency(value: float) -> str:
    return f"${value:,.0f}"


def create_regression_plot(
    data: pd.DataFrame,
    model: LinearRegression,
    intercept: float,
    slope: float,
    r2: float,
    predict_years: float,
    predicted_salary: float,
    output_file: Path,
) -> None:
    x_values = data[X_COLUMN].values
    y_values = data[Y_COLUMN].values
    x_line = np.linspace(x_values.min(), x_values.max(), 100).reshape(-1, 1)
    y_line = model.predict(x_line)

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor("#fafafa")
    ax.set_facecolor("#ffffff")

    ax.scatter(
        x_values,
        y_values,
        s=90,
        alpha=0.85,
        color="#2E86AB",
        edgecolors="white",
        linewidths=1.2,
        label="Observed data",
        zorder=3,
    )
    ax.plot(
        x_line,
        y_line,
        color="#C0392B",
        linewidth=2.5,
        label="Fitted regression line",
        zorder=2,
    )
    ax.scatter(
        [predict_years],
        [predicted_salary],
        s=180,
        color="#F39C12",
        edgecolors="#2C3E50",
        linewidths=1.5,
        label=f"Prediction at {predict_years:g} years",
        zorder=4,
    )

    ax.annotate(
        f"Predicted salary: {format_currency(predicted_salary)}",
        xy=(predict_years, predicted_salary),
        xytext=(predict_years + 0.35, predicted_salary + 3500),
        fontsize=11,
        fontweight="bold",
        color="#2C3E50",
        arrowprops={"arrowstyle": "->", "color": "#2C3E50", "lw": 1.2},
        bbox={"boxstyle": "round,pad=0.4", "facecolor": "#FFF3CD", "edgecolor": "#F39C12"},
    )

    equation = f"Salary = {intercept:,.2f} + {slope:,.2f} × YearsExperience"
    stats_text = f"{equation}\nR² = {r2:.4f}"
    ax.text(
        0.02,
        0.98,
        stats_text,
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontsize=11,
        bbox={"boxstyle": "round,pad=0.5", "facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.95},
    )

    ax.set_title(
        "Linear Regression: Salary vs Years of Experience",
        fontsize=15,
        fontweight="bold",
        pad=14,
    )
    ax.set_xlabel("Years of Experience", fontsize=12)
    ax.set_ylabel("Salary ($)", fontsize=12)
    ax.grid(True, linestyle="--", alpha=0.35)
    ax.legend(loc="lower right", frameon=True, framealpha=0.95)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(output_file, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    if not DATA_FILE.exists():
        print(f"Error: file not found: {DATA_FILE}")
        raise SystemExit(1)

    data = pd.read_csv(DATA_FILE)
    if X_COLUMN not in data.columns or Y_COLUMN not in data.columns:
        print(f"Error: required columns not found in {DATA_FILE.name}")
        print(f"Available columns: {', '.join(data.columns)}")
        raise SystemExit(1)

    x = data[[X_COLUMN]].values
    y = data[Y_COLUMN].values

    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)

    intercept = float(model.intercept_)
    slope = float(model.coef_[0])
    r2 = float(r2_score(y, y_pred))
    predicted_salary = float(model.predict([[PREDICT_YEARS]])[0])

    equation = f"Salary = {intercept:.4f} + {slope:.4f} * YearsExperience"

    print("Linear Regression Results")
    print("-" * 40)
    print(f"Slope: {slope:.4f}")
    print(f"Intercept: {intercept:.4f}")
    print(f"Regression equation: {equation}")
    print(f"R-squared: {r2:.4f}")
    print(
        f"Predicted salary at {PREDICT_YEARS:g} years of experience: "
        f"{predicted_salary:.2f}"
    )

    create_regression_plot(
        data=data,
        model=model,
        intercept=intercept,
        slope=slope,
        r2=r2,
        predict_years=PREDICT_YEARS,
        predicted_salary=predicted_salary,
        output_file=OUTPUT_FILE,
    )

    print(f"Saved regression plot to {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
