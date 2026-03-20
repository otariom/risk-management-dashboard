import yfinance as yf
from fastapi import FastAPI
import redis
import numpy as np
import pandas as pd

from src.common import config
from src.engine.core_math import compute_risk_metrics
from src.engine.stress_tests import stress_test_summary


app = FastAPI(title="Risk Engine API")


# Redis connection
r = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB,
    decode_responses=True
)


def get_prices_from_redis(ticker):
    key = f"{ticker}_prices"

    try:
        prices = r.lrange(key, 0, -1)

        if not prices:
            return []

        return [float(p) for p in prices]

    except Exception:
        # 🔥 Redis not available (tests/local)
        return []


def fetch_prices_from_yfinance(ticker):
    data = yf.download(ticker, period="1d", interval="1m", progress=False)

    if data.empty:
        return []

    close_data = data["Close"]

    if hasattr(close_data, "columns"):
        close_data = close_data.iloc[:, 0]

    return close_data.dropna().tolist()


@app.get("/")
def home():
    return {"message": "Risk Engine API is running"}


# 🔹 Risk endpoint (single stock)
@app.get("/risk/{ticker}")
def get_risk(ticker: str):
    ticker = ticker.upper()

    prices = get_prices_from_redis(ticker)

    if len(prices) < 2:
        prices = fetch_prices_from_yfinance(ticker)

    if len(prices) < 2:
        return {"error": "Invalid ticker or no data available"}

    metrics = compute_risk_metrics(
        prices,
        confidence_level=config.CONFIDENCE_LEVEL
    )

    stress = stress_test_summary(prices)

    return {
        "ticker": ticker,
        "VaR": metrics["VaR"],
        "CVaR": metrics["CVaR"],
        "data_points": len(prices),
        "prices": prices,
        "stress": stress
    }


# 🔹 Correlation endpoint (multiple stocks)
@app.post("/correlation")
def get_correlation(tickers: list[str]):
    data = {}

    for ticker in tickers:
        ticker = ticker.upper()
        prices = fetch_prices_from_yfinance(ticker)

        if len(prices) < 10:   # 🔥 skip weak data
            continue

        returns = np.diff(prices) / prices[:-1]
        data[ticker] = returns

    if len(data) < 2:
        return {"error": "Need at least 2 valid tickers"}

    # 🔥 FIX: align lengths
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

    df = df.dropna()   # remove mismatched rows

    if df.empty:
        return {"error": "Not enough overlapping data"}

    corr_matrix = df.corr()

    return corr_matrix.to_dict()