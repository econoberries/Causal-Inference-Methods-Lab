"""Reproducible synthetic data with known causal effects.

The partially linear regression (PLR) DGP is
    D = m0(X) + V,
    Y = theta * D + h0(X) + epsilon.

X, V, and epsilon are mutually independent. Given X, the treatment has
no unmeasured confounder. The outcome and treatment both depend on X.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def simulate_partially_linear(
    n: int = 2000, theta: float = 2.0, seed: int = 42
) -> pd.DataFrame:
    """Generate observations with confounding through observed nonlinear X."""
    if n < 10:
        raise ValueError("n must be at least 10")
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(n, 3))
    x1, x2, x3 = x.T

    # Treatment depends on observed pre-treatment confounders.
    m0 = 0.9 * x1 - 0.8 * x2 + 0.7 * np.sin(x3) + 0.4 * x1 * x2
    d = m0 + rng.normal(size=n)

    # Nonlinear baseline outcome plus the homogeneous causal effect of D.
    h0 = 1.2 * x1 - 0.5 * x2**2 + 0.8 * np.sin(x3) + 0.4 * x1 * x2
    y = theta * d + h0 + rng.normal(size=n)

    return pd.DataFrame({"y": y, "d": d, "x1": x1, "x2": x2, "x3": x3})
