import yfinance as yf  
import pandas as pd   
import matplotlib.pyplot as plt  
from prophet import Prophet            
from prophet.diagnostics import cross_validation, performance_metrics
ticker  = 'HINDUNILVR.NS'
data = yf.download(ticker, start = '2021-01-01',end = '2024-12-31')
df = data.reset_index()[['Date','Close']]
df.columns = [ 'ds','y']
df['ds'] = pd.to_datetime(df['ds'])
plt.figure(figsize=(13,6))
plt.plot(df['ds'],df['y'],color = "#afef0b",marker = 'o',markersize = 4,linewidth = 2,label = ' HINDUNILVR  close')
plt.title('HINDUNILVR (2021 - 2024)',fontsize = 16,color = '#afef0b')
plt.xlabel('Date',fontsize = 12)
plt.ylabel('Price (INR)',fontsize = 12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(rotation = 30,fontsize = 10)
plt.yticks(fontsize = 10)
plt.legend()
plt.tight_layout()
# plt.show()
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality = True,
    daily_seasonality=True,
    changepoint_prior_scale=.02,
    seasonality_mode='multiplicative'
)
model.add_country_holidays(country_name = 'India')
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
plt.show()
df_cv = cross_validation(model, initial = '730 days',period = '90 days',horizon = '90 days') 
df_p =performance_metrics(df_cv)
print(df_p[['horizon','mae','rmse']]) 