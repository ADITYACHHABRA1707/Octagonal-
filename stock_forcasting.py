import yfinance as yf  
import pandas as pd   
import matplotlib.pyplot as plt  
from prophet import Prophet            
ticker  = 'HINDUNILVR.NS'
data = yf.download(ticker, start = '2021-01-01',end = '2024-12-31')
df = data.reset_index()[['Date','Close']]
df.columns = [ 'ds','y']
df['ds'] = pd.to_datetime(df['ds'])
plt.figure(figsize=(13,6))
plt.plot(df['ds'],df['y'],color = "#afef0b",marker = 'o',markersize = 4,linewidth = 2,label='HINDUNILVR Close')
plt.title('HINDUNILVR (2021 - 2024)',fontsize = 16,color = '#afef0b')
plt.xlabel('Date',fontsize = 12)
plt.ylabel('Price (INR)',fontsize = 12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(rotation = 30,fontsize = 10)
plt.yticks(fontsize = 10)
plt.legend()
plt.tight_layout()
# plt.show()
model = Prophet()
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
# plt.show()
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
test_data = yf.download(ticker, start = '2025-01-01', end = '2025-03-31')
test_df = test_data.reset_index()[['Date','Close']]
test_df.columns = ['ds','y']
test_df['ds'] = pd.to_datetime(test_df['ds'])
forecast_jan_mar = forecast[(forecast['ds'] >= '2025-01-01') & (forecast['ds']<= '2025-03-31')][['ds', 'yhat']]
comparison = pd.merge(test_df,forecast_jan_mar,on='ds')
mae = mean_absolute_error(comparison['y'], comparison['yhat'])
rmse = np.sqrt(mean_squared_error(comparison['y'], comparison['yhat']))
print(f"Mean Absolute Error (mae): {mae:.2f}")
print(f"Root mean Squared error (rmse): {rmse:.2f}")
mape = np.mean(np.abs((comparison['y'] - comparison['yhat']) / comparison['y']))* 100
print(f"mean absolute percentage error (mape): {mape:.2f}%")
plt.figure(figsize = (13,6))
plt.plot(comparison['ds'], comparison['y'],label = 'Actual',color = 'blue',marker = 'o')
plt.plot(comparison['ds'],comparison['yhat'],label = 'Predicted',color = 'red',marker = 'x')
plt.title('HINDUNILVR ACTUAL VS PREDICTED(JAN-MAR 2025)',fontsize = 16)
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
mape = np.mean(np.abs((comparison['y'] - comparison['yhat']) / comparison['y']))* 100
print(f"mean absolute percentage error (mape): {mape:.2f}%")





