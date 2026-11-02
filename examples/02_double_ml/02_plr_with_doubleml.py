"""Reproduce the synthetic PLR example using the official Python DoubleML.

Install optional dependencies first:
    python -m pip install -e '.[dml]'

Run from repository root:
    python examples/02_double_ml/02_plr_with_doubleml.py
"""

from sklearn.ensemble import RandomForestRegressor
from causal_methods_lab import simulate_partially_linear


def main():
    try:
        import doubleml as dml
    except ImportError as exc:
        raise SystemExit("Install DoubleML: python -m pip install -e '.[dml]'") from exc

    df = simulate_partially_linear(n=2000, theta=2.0, seed=2026)
    data = dml.DoubleMLData(df, y_col="y", d_cols="d", x_cols=["x1", "x2", "x3"])
    learner = RandomForestRegressor(
        n_estimators=200, min_samples_leaf=5, random_state=42, n_jobs=-1
    )
    model = dml.DoubleMLPLR(
        data, ml_l=learner, ml_m=learner, n_folds=5, n_rep=1
    )
    model.fit()
    print("True effect = 2.000")
    print(model.summary)
    print("\nCompare with 01_plr_from_scratch.py; learners differ, so estimates need not match.")


if __name__ == "__main__":
    main()
