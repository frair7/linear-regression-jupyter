#!/usr/bin/env python3
"""Fit a simple linear regression and save a scatter plot with regression line."""

import os
import sys
from pathlib import Path

cache_dir = Path(__file__).parent / ".matplotlib_cache"
cache_dir.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(cache_dir))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def usage() -> None:
    print("Usage: python regression_plot.py <filename> <x_column> <y_column>")


def main() -> None:
    if len(sys.argv) != 4:
        usage()
        sys.exit(1)

    filename = sys.argv[1]
    x_column = sys.argv[2]
    y_column = sys.argv[3]

    data_path = Path(filename)
    if not data_path.exists():
        print(f"Error: file not found: {filename}")
        sys.exit(1)

    data = pd.read_csv(data_path)
    if x_column not in data.columns or y_column not in data.columns:
        print(f"Error: columns must exist in {filename}")
        print(f"Available columns: {', '.join(data.columns)}")
        sys.exit(1)

    x = data[[x_column]].values
    y = data[y_column].values

    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)

    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))

    x_line = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
    y_line = model.predict(x_line)

    plt.figure(figsize=(8, 6))
    plt.scatter(data[x_column], data[y_column], alpha=0.7, edgecolors="k", linewidths=0.5)
    plt.plot(x_line, y_line, color="red", linewidth=2, label="Regression line")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"Linear Regression: {y_column} vs {x_column}")
    plt.text(
        0.05,
        0.95,
        f"R² = {r2:.4f}\nRMSE = {rmse:.4f}",
        transform=plt.gca().transAxes,
        verticalalignment="top",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.8},
    )
    plt.legend()
    plt.tight_layout()

    output_name = f"{data_path.stem}_regression_plot_python.png"
    plt.savefig(output_name, dpi=150)
    plt.close()

    print(f"Saved regression plot to {output_name}")
    print(f"R-squared: {r2:.4f}")
    print(f"RMSE: {rmse:.4f}")


if __name__ == "__main__":
    main()
