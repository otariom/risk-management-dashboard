from src.engine.core_math import (
    calculate_returns,
    calculate_var,
    calculate_cvar,
    compute_risk_metrics
)


def test_calculate_returns():
    prices = [100, 105, 110]

    returns = calculate_returns(prices)

    assert len(returns) == 2
    assert round(returns[0], 4) == 0.05
    assert round(returns[1], 4) == 0.0476


def test_calculate_var():
    returns = [-0.01, -0.02, 0.01, 0.02, -0.03]

    var = calculate_var(returns, confidence_level=0.95)

    assert var <= 0  # VaR should be a loss (negative)


def test_calculate_cvar():
    returns = [-0.01, -0.02, 0.01, 0.02, -0.05]

    cvar = calculate_cvar(returns, confidence_level=0.95)

    assert cvar <= 0  # CVaR should also be negative


def test_compute_risk_metrics():
    prices = [100, 102, 101, 98, 97]

    result = compute_risk_metrics(prices)

    assert "VaR" in result
    assert "CVaR" in result
    assert isinstance(result["VaR"], float)
    assert isinstance(result["CVaR"], float)