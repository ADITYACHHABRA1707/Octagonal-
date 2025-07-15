import streamlit as st
import yfinance as yf
import pandas as pd
import datetime


nifty_fifty_stocks = [
    "ADANIENT.NS",
    "ADANIPORTS.NS",
    "APOLLOHOSP.NS",
    "ASIANPAINT.NS",
    "AXISBANK.NS",
    "BAJAJ-AUTO.NS",
    "BAJFINANCE.NS",
    "BAJAJFINSV.NS",
    "BHARTIARTL.NS",
    "BPCL.NS",
    "BRITANNIA.NS",
    "CIPLA.NS",
    "COALINDIA.NS",
    "DIVISLAB.NS",
    "DRREDDY.NS",
    "EICHERMOT.NS",
    "GRASIM.NS",
    "HCLTECH.NS",
    "HDFCBANK.NS",
    "HDFCLIFE.NS",
    "HEROMOTOCO.NS",
    "HINDALCO.NS",
    "HINDUNILVR.NS",
    "ICICIBANK.NS",
    "INDUSINDBK.NS",
    "INFY.NS",
    "ITC.NS",
    "JSWSTEEL.NS",
    "KOTAKBANK.NS",
    "LT.NS",
    "LTIM.NS",
    "M&M.NS",
    "MARUTI.NS",
    "NESTLEIND.NS",
    "NTPC.NS",
    "ONGC.NS",
    "POWERGRID.NS",
    "RELIANCE.NS",
    "SBILIFE.NS",
    "SBIN.NS",
    "SUNPHARMA.NS",
    "TATACONSUM.NS",
    "TATAMOTORS.NS",
    "TATASTEEL.NS",
    "TCS.NS",
    "TECHM.NS",
    "TITAN.NS",
    "ULTRACEMCO.NS",
    "UPL.NS",
    "WIPRO.NS"
]
us_top_50_stocks = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA", "BRK-B", "UNH", "JNJ",
    "V", "PG", "XOM", "MA", "JPM", "HD", "LLY", "MRK", "ABBV", "PEP",
    "AVGO", "KO", "COST", "PFE", "TMO", "WMT", "CSCO", "ACN", "ABT", "CVX",
    "DHR", "MCD", "AMD", "CRM", "NKE", "DIS", "INTC", "TXN", "LIN", "UNP",
    "PM", "BMY", "NEE", "HON", "ORCL", "MDT", "ADBE", "QCOM", "IBM", "AMGN"
]
st.set_page_config(page_icon="♾️",page_title="Octagonal Stock Chase & Co.", layout="wide")
st.title("                                             Welcome to Octagonal Chase & Co.")
st.header("                                            Chose Your Stock and make your own way of Investing 📊📊 ")
stock_name = st.selectbox("Select Stock", list(nifty_fifty_stocks))
ticker = stock_name 
if st.button("Select Stock"):
    st.balloons()
data = yf.Ticker(ticker)
df = data.history(period = "max")
cp = df['Close'][-1]
mp = df['Close'][-21]
yp = df['Close'][-252]
previous = df['Close'][-2]
change = ((cp - previous)/previous)*100
m = ((cp - mp )/mp )*100
y = ((cp - yp )/yp )*100
st.subheader(f"Current price of {ticker} is ₹{cp:.2f}")
a,b,c = st.columns(3)
x1 =cp - previous
y1 = cp - mp
z1 = cp - yp
a.metric(
    label="Daily Change",
    
    value=f"₹{x1:.2f}",
    delta=f"{change:.2f}%",
    delta_color="normal",  
    help="Change from previous close",
    border=True
)
b.metric(
    label="Month Change",
    value=f"₹{y1:.2f}",
    delta=f"{m:.2f}%",
    delta_color="normal",
    help="Change from previous month",
    border=True
)
c.metric(
    label="Yearly Change",
    value=f"₹{z1:.2f}",
    delta=f"{y:.2f}%",
    delta_color="normal",
    help="Change from previous year",
    border=True
)
st.line_chart(df['Close'], use_container_width=True)

stock_name2 = st.selectbox("Select US Stock", list(us_top_50_stocks))
ticker2 = stock_name2

if st.button("Select US Stock"):
    st.balloons()

data2 = yf.Ticker(ticker2)
df2 = data2.history(period="max")

cp1 = df2['Close'][-1]
mp1 = df2['Close'][-21]
yp1 = df2['Close'][-252]
previous1 = df2['Close'][-2]

c1 = ((cp1 - previous1) / previous1) * 100
m1 = ((cp1 - mp1) /mp1) * 100
y1 = ((cp1 - yp1) / yp1) * 100

st.subheader(f"Current price of {ticker2} is ${cp1:.2f}")
x2 =cp1 - previous1
y2 = cp1 - mp1
z2 = cp1 - yp1
a2, b2, c2 = st.columns(3)

a2.metric(
    label="Daily Change",
    value=f"${x2:.2f}",
    delta=f"{c1:.2f}%",
    delta_color="normal",
    help="Change from previous close",
    border=True
)

b2.metric(
    label="Month Change",
    value=f"${y2:.2f}",
    delta=f"{m1:.2f}%",
    delta_color="normal",
    help="Change from previous month",
    border=True
)

c2.metric(
    label="Yearly Change",
    value=f"${z2:.2f}",
    delta=f"{y1:.2f}%",
    delta_color="normal",
    help="Change from previous year",
    border=True
)

st.line_chart(df2['Close'], use_container_width=True)
