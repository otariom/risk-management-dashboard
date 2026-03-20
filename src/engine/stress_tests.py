import numpy as np


def calculate_returns(prices):
    """
    Convert prices → returns
    """
    prices = np.array(prices)

    if len(prices) < 2:
        return []

    returns = (prices[1:] / prices[:-1]) - 1
    return returns


def apply_market_crash(prices, crash_percent=0.2):
    """
    Simulate a market crash (e.g., -20%)
    """
    stressed_prices = [p * (1 - crash_percent) for p in prices]
    return stressed_prices


def apply_bull_run(prices, growth_percent=0.1):
    """
    Simulate strong market growth (+10%)
    """
    stressed_prices = [p * (1 + growth_percent) for p in prices]
    return stressed_prices


def apply_custom_shock(prices, shock_percent):
    """
    Apply custom shock (+ or -)
    Example:
        -0.15 → 15% drop
        +0.10 → 10% increase
    """
    stressed_prices = [p * (1 + shock_percent) for p in prices]
    return stressed_prices


def stress_test_summary(prices):
    """
    Run all stress scenarios and return summary
    """
    if len(prices) < 2:
        return None

    crash_prices = apply_market_crash(prices)
    bull_prices = apply_bull_run(prices)

    # Compare final values
    original_final = prices[-1]
    crash_final = crash_prices[-1]
    bull_final = bull_prices[-1]

    return {
        "original_price": original_final,
        "crash_price": crash_final,
        "bull_price": bull_final,
        "crash_impact_%": ((crash_final - original_final) / original_final) * 100,
        "bull_impact_%": ((bull_final - original_final) / original_final) * 100,
    }