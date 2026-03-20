# Redis Configuration
REDIS_HOST = "redis"
REDIS_PORT = 6379
REDIS_DB = 0


# Market Configuration
TICKERS = ["AAPL", "MSFT", "GOOG"]
WINDOW_SIZE = 100  # number of recent prices to store


# Risk Configuration
CONFIDENCE_LEVEL = 0.95


# Monte Carlo Configuration
SIMULATIONS = 10000
TIME_HORIZON_DAYS = 1