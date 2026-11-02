"""Illustration: association is not causation when X confounds D and Y.

Run from the repository root:
    python examples/01_foundations/01_confounding.py
"""

import numpy as np
from causal_methods_lab import simulate_partially_linear


def ols_coefficient(y, *predictors):
    x = np.column_stack([np.ones(len(y)), *predictors])
    return np.linalg.lstsq(x, y, rcond=None)[0][1]


def main():
    df = simulate_partially_linear(n=5000, theta=2.0, seed=42)
    y, d = df["y"].to_numpy(), df["d"].to_numpy()
    naive = ols_coefficient(y, d)
    adjusted_linear = ols_coefficient(
        y, d, df["x1"], df["x2"], df["x3"]
    )
    print("Known true treatment effect: 2.000")
    print(f"Naive OLS (Y ~ D):        {naive:.3f}")
    print(f"Linear OLS (Y ~ D + X):   {adjusted_linear:.3f}")
    print("\nExercise: Why can linear OLS remain imperfect when confounding is nonlinear?")


if __name__ == "__main__":
    main()
