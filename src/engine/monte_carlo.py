import numpy as np

from src.common import config


def calculate_returns(prices):
    """
    Convert prices → returns
    """
    prices = np.array(prices)

    if len(prices) < 2:
        return []

    returns = (prices[1:] / prices[:-1]) - 1
    return returns


def simulate_price_paths(prices):
    """
    Monte Carlo simulation using GBM (simplified)
    """
    returns = calculate_returns(prices)

    if len(returns) == 0:
        return None

    # Step 1: estimate mean and std
    mu = np.mean(returns)
    sigma = np.std(returns)

    # Step 2: last known price
    S0 = prices[-1]

    simulations = config.SIMULATIONS
    T = config.TIME_HORIZON_DAYS

    simulated_prices = []

    for _ in range(simulations):
        # random shock
        shock = np.random.normal(mu, sigma)

        # GBM formula (simplified 1-step)
        future_price = S0 * (1 + shock)

        simulated_prices.append(future_price)

    return simulated_prices


def monte_carlo_var(prices, confidence_level=0.95):
    """
    Calculate VaR using simulated prices
    """
    simulated_prices = simulate_price_paths(prices)

    if simulated_prices is None:
        return None

    S0 = prices[-1]

    # Convert simulated prices → returns
    simulated_returns = [(p / S0) - 1 for p in simulated_prices]

    percentile = (1 - confidence_level) * 100
    var = np.percentile(simulated_returns, percentile)

    return float(var)