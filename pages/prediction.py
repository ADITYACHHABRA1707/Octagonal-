import streamlit as st
import yfinance as yf  
import pandas as pd   
import matplotlib.pyplot as plt  
from prophet import Prophet            
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from datetime import datetime, timedelta
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
st.set_page_config(page_icon="♾️",page_title="Octagonal Stock Chase & Co.", layout="wide")
st.title("                                             Welcome to Octagonal Chase & Co.")
st.header("                                            Chose Your Stock For the Prediction  and make your own way of Investing 📊📊 ")
stock_name = st.selectbox("Select Stock", list(nifty_fifty_stocks))
ticker = stock_name           
end_date = datetime.today().strftime('%Y-%m-%d')
data = yf.download(ticker, start = '2021-01-01',end=end_date)
df = data.reset_index()[['Date','Close']]
df.columns = [ 'ds','y']
df['ds'] = pd.to_datetime(df['ds'])

plt.figure(figsize=(13,6))
plt.plot(df['ds'],df['y'],color = "#cdda15",marker = 'o',markersize = 4,linewidth = 2,label=f'{ticker} Close')
plt.title('{ticker} (2021 - today)',fontsize = 16,color = "#0baeef")
plt.xlabel('Date',fontsize = 12)
plt.ylabel('Price (INR)',fontsize = 12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(rotation = 30,fontsize = 10)
plt.yticks(fontsize = 10)
plt.legend()
plt.tight_layout()
st.subheader("📈 Historical Stock Price (2021–2025)")  
st.pyplot(plt)  
plt.clf()  
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False,
    changepoint_prior_scale=0.05,
    seasonality_prior_scale=10,
    holidays_prior_scale=10,
    seasonality_mode='multiplicative'
)
model.add_country_holidays(country_name='IN')
model.add_seasonality(name='monthly', period=30.5, fourier_order=8)
model.add_seasonality(name='quarterly', period=91.5, fourier_order=8)
df = df.dropna()  
model.fit(df)  

future = model.make_future_dataframe(periods = 90)
forecast = model.predict(future)
fig = model.plot(forecast)
ax = fig.gca()
ax.set_title("HINDUNILVR Forecast (NEXT 90 days)",fontsize = 16) 
ax.set_xlabel("Date",fontsize = 12)
ax.set_ylabel("Price(INR)",fontsize = 12)
ax.grid(True)
plt.tight_layout()
st.subheader("🔮 Forecast Plot")   
st.pyplot(fig)
end_date = datetime.today()
start_date = end_date - timedelta(days=90)

# Download actual stock data for last 90 days
test_data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
test_df = test_data.reset_index()[['Date','Close']]
test_df.columns = ['ds','y']
test_df['ds'] = pd.to_datetime(test_df['ds'])

# Get forecasted values for same dates
forecast_recent = forecast[(forecast['ds'] >= start_date) & (forecast['ds'] <= end_date)][['ds', 'yhat']]
comparison = pd.merge(test_df, forecast_recent, on='ds')
comparison = comparison.sort_values('ds')

comparison = comparison.sort_values('ds')
mae = mean_absolute_error(comparison['y'], comparison['yhat'])
rmse = np.sqrt(mean_squared_error(comparison['y'], comparison['yhat']))
mape = np.mean(np.abs((comparison['y'] - comparison['yhat']) / comparison['y']))* 100
st.subheader("📏 Model Performance Metrics (Jan–Mar 2025)")  
col1, col2, col3 = st.columns(3)                             
col1.metric("MAE", f"{mae:.2f}")                            
col2.metric("RMSE", f"{rmse:.2f}")                           
col3.metric("MAPE", f"{mape:.2f}%")                         

plt.figure(figsize = (13,6))
plt.plot(comparison['ds'], comparison['y'],label = 'Actual',color = 'blue',marker = 'o')
plt.plot(comparison['ds'],comparison['yhat'],label = 'Predicted',color = 'red',marker = 'x')
plt.title(f'{ticker} ACTUAL VS PREDICTED (Last 90 Days)', fontsize=16)

plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.tight_layout()
st.subheader("📏 Model Performance Metrics (Last 90 Days)")
st.pyplot(plt)   
plt.clf()