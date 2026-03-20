# risk-management-dashboard
# 📊 Real-Time Risk Engine (Quant Finance Project)

A production-style **real-time portfolio risk analysis system** that computes **VaR, CVaR, Monte Carlo simulations, stress testing, and correlation analysis** using live market data.

---

## 🚀 What This Project Does

This system helps you understand:

* 📉 **How much you can lose (VaR)**
* ⚠️ **How bad losses can get (CVaR)**
* 🔮 **Possible future scenarios (Monte Carlo)**
* 💥 **Impact of extreme market events (Stress Testing)**
* 🔗 **How stocks move together (Correlation Matrix)**

👉 It is a **risk analysis tool**, not a stock recommendation system.

---

## 🧠 Core Idea
This system answers:

> “If I invest in this stock, how risky is it?”

---

## 🏗️ System Architecture

```
User Input → FastAPI → Risk Engine → Redis (optional) → UI (Streamlit)
```

* **FastAPI** → backend API
* **Redis** → fast data storage
* **Streamlit** → interactive dashboard
* **NumPy/Pandas** → quant calculations

---

## 📁 Project Structure

```
risk-management-dashboard/
│
├── src/
│   ├── api/                # FastAPI backend
│   ├── engine/             # Quant logic (VaR, CVaR, Monte Carlo, Stress)
│   ├── ingestion/          # Data collection
│   ├── ui/                 # Streamlit dashboard
│   └── common/             # Config
│
├── tests/                  # Unit & API tests
├── docker-compose.yml      # Multi-container setup
├── Dockerfile              # Container config
└── requirements.txt
```

---

## ⚙️ Features

### 📉 Risk Metrics

* Historical VaR
* CVaR (Expected Shortfall)

### 🔮 Simulation

* Monte Carlo simulation (10,000 scenarios)

### 💥 Stress Testing

* Market crash scenario
* Bull run scenario

### 🔗 Correlation Analysis

* Multi-stock correlation matrix
* Understand portfolio diversification

### 📊 Visualization

* Price trends
* Returns
* Returns distribution

---

## 🖥️ UI Preview (What You See)

* Enter any ticker (AAPL, TSLA, RELIANCE.NS, etc.)
* Get:

  * VaR & CVaR
  * Charts
  * Stress test results
* Enter multiple tickers:

  * View correlation matrix

---

## 🧪 Testing

Run tests using:

```bash
python -m pytest tests/
```

✔ Covers:

* VaR / CVaR correctness
* API responses

---

## 🐳 How to Run (Docker - Recommended)

### 1️⃣ Clone the repo

```bash
git clone <your-repo-link>
cd risk-management-dashboard
```

---

### 2️⃣ Start the system

```bash
docker-compose up
```

---

### 3️⃣ Open in browser

* UI → http://localhost:8501
* API Docs → http://localhost:8000/docs

---

## ⚡ How to Use

### 🔹 Single Stock Risk

1. Enter ticker (e.g., `AAPL`)
2. Click **Get Risk Metrics**
3. View:

   * VaR
   * CVaR
   * Charts
   * Stress results

---

### 🔹 Correlation Analysis

1. Enter tickers:

   ```
   AAPL,MSFT,TSLA
   ```
2. Click **Show Correlation Matrix**
3. Understand:

   * Which stocks move together
   * Portfolio diversification

---

## 📊 Example Use Case

If:

| Stock | VaR |
| ----- | --- |
| AAPL  | -2% |
| TSLA  | -5% |

👉 TSLA is riskier than AAPL

---

## ⚠️ Limitations

* Uses **historical data** (past ≠ future)
* Not a trading or recommendation system
* Assumes simple return distributions

---

## 🧠 Tech Stack

* **Python**
* **FastAPI**
* **Streamlit**
* **Redis**
* **NumPy / Pandas**
* **Docker**
* **Pytest**

---

## 🔥 What Makes This Project Strong

* Real-time data pipeline
* Quant finance concepts
* Full-stack system (backend + UI)
* Dockerized (production-ready)
* Tested (unit + API)

---

## 🚀 Future Improvements

* Portfolio VaR (multi-asset risk)
* GARCH volatility modeling
* Real-time streaming (WebSockets)
* Risk-adjusted return metrics
* Deployment to cloud (AWS/GCP)

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
