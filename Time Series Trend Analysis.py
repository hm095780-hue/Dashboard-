import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("stock_data.xlsx")

print(df.head())
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
print(df.isnull().sum())
print(df.isnull().sum())
df = df.dropna()
plt.figure(figsize=(12, 6))

plt.plot(df['Date'], df['Price'])

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Stock Price Trend Over Time")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
df['MA_7'] = df['Price'].rolling(window=7).mean()
plt.figure(figsize=(12, 6))

plt.plot(df['Date'], df['Price'], label='Actual Price')
plt.plot(df['Date'], df['MA_7'], label='7-Day Moving Average')

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Stock Price with 7-Day Moving Average")

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
df['Month'] = df['Date'].dt.month

monthly_avg = df.groupby('Month')['Price'].mean()

print(monthly_avg)
monthly_avg.plot(kind='bar', figsize=(10, 5))

plt.title("Monthly Average Price")
plt.xlabel("Month")
plt.ylabel("Average Price")

plt.show()
df['Difference'] = abs(df['Price'] - df['MA_7'])

threshold = df['Difference'].mean() * 2

anomalies = df[df['Difference'] > threshold]

print(anomalies)
plt.figure(figsize=(12, 6))

plt.plot(df['Date'], df['Price'], label='Price')

plt.scatter(
    anomalies['Date'],
    anomalies['Price'],
    label='Anomaly'
)

plt.title("Stock Price Anomalies")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
df['MA_30'] = df['Price'].rolling(window=30).mean()
plt.figure(figsize=(12, 6))

plt.plot(df['Date'], df['Price'], label='Actual Price')
plt.plot(df['Date'], df['MA_7'], label='7-Day MA')
plt.plot(df['Date'], df['MA_30'], label='30-Day MA')

plt.title("Stock Price Trend with Moving Averages")

plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
from prophet import Prophet
forecast_data = df[['Date', 'Price']].copy()

forecast_data.columns = ['ds', 'y']
model = Prophet()

model.fit(forecast_data)
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
model.plot(forecast)

plt.title("30-Day Stock Price Forecast")

plt.show()