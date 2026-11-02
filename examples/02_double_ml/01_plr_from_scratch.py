"""Learning exercise: see nuisance estimation, cross-fitting, and DML result.

Run from the repository root:
    python examples/02_double_ml/01_plr_from_scratch.py
"""

import numpy as np
from causal_methods_lab import estimate_plr_crossfit, simulate_partially_linear


def main():
    data = simulate_partially_linear(n=2000, theta=2.0, seed=2026)
    naive = np.linalg.lstsq(
        np.column_stack((np.ones(len(data)), data["d"])),
        data["y"],
        rcond=None,
    )[0][1]
    result = estimate_plr_crossfit(
        data, covariates=["x1", "x2", "x3"], n_folds=5, seed=2026
    )
    print("=== Educational PLR simulation ===")
    print("True effect:        2.000")
    print(f"Naive OLS effect:   {naive:.3f}")
    print(f"DML PLR estimate:   {result.theta:.3f}")
    print(f"Score-based SE:     {result.standard_error:.3f}")
    print(f"Approximate 95% CI: [{result.ci_lower:.3f}, {result.ci_upper:.3f}]")
    print(f"Cross-fitting:      {result.n_folds} folds")
    print("\nTry setting n_folds=2 or changing the random seed.")


if __name__ == "__main__":
    main()
