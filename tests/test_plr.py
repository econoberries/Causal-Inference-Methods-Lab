"""Lightweight checks for synthetic DGP and educational PLR estimator."""

import pytest
from causal_methods_lab import estimate_plr_crossfit, simulate_partially_linear


def test_simulation_reproducible():
    a = simulate_partially_linear(50, seed=111)
    b = simulate_partially_linear(50, seed=111)
    assert a.equals(b)


def test_crossfit_approximately_recovers_known_effect():
    data = simulate_partially_linear(n=1600, theta=2.0, seed=2026)
    result = estimate_plr_crossfit(data, ["x1", "x2", "x3"], n_folds=3)
    assert result.theta == pytest.approx(2.0, abs=0.30)
    assert result.ci_lower < result.ci_upper
    assert result.standard_error > 0


def test_raises_for_bad_folds():
    data = simulate_partially_linear(30)
    with pytest.raises(ValueError):
        estimate_plr_crossfit(data, ["x1"], n_folds=1)
