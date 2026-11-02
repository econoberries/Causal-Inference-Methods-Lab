"""Educational cross-fitted Double Machine Learning for the PLR model.

Reference: Chernozhukov et al. (2018), Econometrics Journal 21: C1-C68.
Teaching implementation, not a replacement for the DoubleML package.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.model_selection import KFold
from sklearn.ensemble import HistGradientBoostingRegressor


@dataclass(frozen=True)
class PLRResult:
    theta: float
    standard_error: float
    ci_lower: float
    ci_upper: float
    n_obs: int
    n_folds: int


def _default_learner():
    return HistGradientBoostingRegressor(
        max_iter=120, max_leaf_nodes=15, min_samples_leaf=20, random_state=42
    )


def estimate_plr_crossfit(
    data: pd.DataFrame,
    covariates: list[str],
    n_folds: int = 5,
    seed: int = 42,
    learner_factory: Callable | None = None,
) -> PLRResult:
    """Estimate constant-effect PLR theta with cross-fitting and orthogonal score.

    On each held-out fold:
      lhat(X) ~ E[Y|X] and mhat(X) ~ E[D|X]
    Then solve
      mean[(D-mhat)*(Y-lhat-theta*(D-mhat))] = 0.

    The returned standard error is the heteroskedasticity-robust
    orthogonal-score plug-in estimate for this iid DGP (one split), not
    cluster-robust or repeated-crossfit inference.

    A causal reading additionally assumes conditional exogeneity,
    residualized treatment variation, and adequate nuisance fits.
    """
    if n_folds < 2 or n_folds > len(data):
        raise ValueError("n_folds must be between 2 and number of rows")
    required = ["y", "d", *covariates]
    if not covariates or any(c not in data.columns for c in required):
        raise ValueError("Provide nonempty covariates and y, d columns")
    if data[required].isna().any().any():
        raise ValueError("Missing values are not handled in this tutorial")

    x = data[covariates].to_numpy()
    y = data["y"].to_numpy(dtype=float)
    d = data["d"].to_numpy(dtype=float)
    if not np.isfinite(x).all() or not np.isfinite(y).all() or not np.isfinite(d).all():
        raise ValueError("All values must be finite")

    make_learner = learner_factory or _default_learner
    lhat = np.empty(len(data))
    mhat = np.empty(len(data))

    for train_idx, test_idx in KFold(
        n_splits=n_folds, shuffle=True, random_state=seed
    ).split(x):
        learner_y = clone(make_learner())
        learner_d = clone(make_learner())
        learner_y.fit(x[train_idx], y[train_idx])
        learner_d.fit(x[train_idx], d[train_idx])
        lhat[test_idx] = learner_y.predict(x[test_idx])
        mhat[test_idx] = learner_d.predict(x[test_idx])

    y_resid = y - lhat
    d_resid = d - mhat
    denominator = np.mean(d_resid**2)
    if denominator <= 1e-12:
        raise ValueError("Insufficient residualized treatment variation")
    theta = float(np.mean(d_resid * y_resid) / denominator)

    # Orthogonal score at fitted theta; iid plug-in SE.
    psi = d_resid * (y_resid - theta * d_resid)
    standard_error = float(
        np.sqrt(np.mean(psi**2) / (denominator**2 * len(data)))
    )
    return PLRResult(
        theta=theta,
        standard_error=standard_error,
        ci_lower=theta - 1.96 * standard_error,
        ci_upper=theta + 1.96 * standard_error,
        n_obs=len(data),
        n_folds=n_folds,
    )
