import streamlit as st
import requests
import pandas as pd

from src.common import config


API_URL = "http://localhost:8000"


st.set_page_config(page_title="Risk Dashboard", layout="wide")

st.title("📊 Real-Time Risk Dashboard")


# 🔹 Single ticker input
ticker = st.text_input("Enter Ticker", "AAPL")


if st.button("Get Risk Metrics"):

    try:
        response = requests.get(f"{API_URL}/risk/{ticker}")
        data = response.json()

        if "error" in data:
            st.error(data["error"])

        else:
            st.success(f"Data for {ticker}")

            col1, col2, col3 = st.columns(3)

            col1.metric("VaR (95%)", f"{data['VaR']:.4f}")
            col2.metric("CVaR (95%)", f"{data['CVaR']:.4f}")
            col3.metric("Data Points", data["data_points"])

            prices = data["prices"]
            df = pd.DataFrame(prices, columns=["Price"])

            st.subheader("📈 Price Trend")
            st.line_chart(df)

            df["Returns"] = df["Price"].pct_change()

            st.subheader("📊 Returns")
            st.line_chart(df["Returns"])

            st.subheader("📉 Returns Distribution")
            st.bar_chart(df["Returns"].value_counts().sort_index())

            # 🔥 Stress Test Section
            stress = data.get("stress")

            if stress and isinstance(stress, dict):
                st.subheader("⚡ Stress Test")

                col1, col2 = st.columns(2)

                col1.metric("Crash Price", f"{stress['crash_price']:.2f}")
                col2.metric("Bull Price", f"{stress['bull_price']:.2f}")

                st.write("Crash Impact (%)", round(stress["crash_impact_%"], 2))
                st.write("Bull Impact (%)", round(stress["bull_impact_%"], 2))

    except Exception as e:
        st.error(f"API connection failed: {e}")


# 🔹 Correlation Section
st.subheader("📊 Correlation Analysis")

tickers_input = st.text_input(
    "Enter multiple tickers (comma separated)",
    "AAPL,MSFT,TSLA"
)

tickers_list = [t.strip().upper() for t in tickers_input.split(",")]


if st.button("Show Correlation Matrix"):

    try:
        response = requests.post(
        f"{API_URL}/correlation",
        json=tickers_list
)

        corr_data = response.json()

        if "error" in corr_data:
            st.error(corr_data["error"])
        else:
            df_corr = pd.DataFrame(corr_data)

            st.dataframe(df_corr)

    except Exception as e:
        st.error(f"API connection failed: {e}")