import time
import yfinance as yf
import redis

from src.common import config


# Connect to Redis
r = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB,
    decode_responses=True
)


def fetch_latest_price(ticker):
    data = yf.download(ticker, period="1d", interval="1m", progress=False)
    if data.empty:
        return None

    latest_price = data["Close"].iloc[-1]

    # Ensure it's a scalar value
    if hasattr(latest_price, "item"):
        latest_price = latest_price.item()

    return float(latest_price)


def store_price(ticker, price):
    """
    Store latest price in Redis list
    Keeps only last N prices
    """
    key = f"{ticker}_prices"

    # push new price
    r.rpush(key, price)

    # keep only last WINDOW_SIZE values
    r.ltrim(key, -config.WINDOW_SIZE, -1)


def run_collector():
    """
    Main loop: fetch and store prices continuously
    """
    print("Starting data collector...")

    while True:
        for ticker in config.TICKERS:
            try:
                price = fetch_latest_price(ticker)

                if price is not None:
                    store_price(ticker, price)
                    print(f"{ticker}: {price}")

            except Exception as e:
                print(f"Error fetching {ticker}: {e}")

        time.sleep(10)


if __name__ == "__main__":
    run_collector()