import yfinance as yf
import streamlit as st
import pandas as pd
import datetime

stock = st.text_input("Enter the stock name", "AAPL")

# Define the ticker symbol and the period for data retrieval
ticker_symbol = stock  # Example: Apple Inc.
start_date = st.date_input("START DATE", value=datetime.date(2019, 1, 7))
end_date = st.date_input("END DATE", value=datetime.date(2023, 1, 7))

st.header("Stock Analysis App")
st.text("Currently Analyzing " + stock)
# Download the data
data = yf.download(ticker_symbol, start=start_date, end=end_date)


st.write(data)



col1, col2 = st.columns(2)

with col1:
    st.line_chart(data["Close"])

with col2:
    st.bar_chart(data["Volume"])
