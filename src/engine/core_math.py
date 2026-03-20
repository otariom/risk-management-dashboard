import numpy as np


def calculate_returns(prices):
    """
    Convert price list → returns
    Formula: (P_t / P_t-1) - 1
    """
    prices = np.array(prices)

    if len(prices) < 2:
        return []

    returns = (prices[1:] / prices[:-1]) - 1
    return returns


def calculate_var(returns, confidence_level=0.95):
    """
    Historical VaR
    Example: 95% VaR = 5th percentile of losses
    """
    if len(returns) == 0:
        return None

    percentile = (1 - confidence_level) * 100
    var = np.percentile(returns, percentile)

    return var


def calculate_cvar(returns, confidence_level=0.95):
    """
    CVaR (Expected Shortfall)
    Average of worst losses beyond VaR
    """
    if len(returns) == 0:
        return None

    # Convert to numpy array (IMPORTANT FIX)
    returns = np.array(returns)

    var = calculate_var(returns, confidence_level)

    # select worst losses
    losses = returns[returns <= var]

    if len(losses) == 0:
        return None

    cvar = losses.mean()
    return cvar


def compute_risk_metrics(prices, confidence_level=0.95):
    """
    Full pipeline:
    prices → returns → VaR + CVaR
    """
    returns = calculate_returns(prices)

    var = calculate_var(returns, confidence_level)
    cvar = calculate_cvar(returns, confidence_level)

    return {
        "VaR": float(var) if var is not None else None,
        "CVaR": float(cvar) if cvar is not None else None,
    }