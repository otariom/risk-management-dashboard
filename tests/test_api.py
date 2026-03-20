from fastapi.testclient import TestClient

from src.api.server import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Risk Engine API is running"}


def test_risk_endpoint_no_data():
    """
    Since Redis may not have data,
    API should return an error message
    """
    response = client.get("/risk/AAPL")

    assert response.status_code == 200
    data = response.json()

    assert "error" in data


def test_risk_endpoint_no_data(monkeypatch):
    """
    Simulate invalid ticker scenario
    """

    def mock_fetch_prices(ticker):
        return []  # simulate no data from yfinance

    monkeypatch.setattr(
        "src.api.server.fetch_prices_from_yfinance",
        mock_fetch_prices
    )

    response = client.get("/risk/INVALID")

    assert response.status_code == 200
    data = response.json()

    assert "error" in data