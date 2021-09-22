import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fbprophet import Prophet

temperature = pd.read_csv('기온데이터_서울.csv', index_col=None, header=None)

temperature.drop(labels=1, axis=1, inplace=True)
temperature.rename(columns={0:'date', 2:'avg_temp', 3:'low_temp', 4:'high_temp'}, inplace=True)

tmp = temperature[['date', 'avg_temp']]
tmp.rename(columns = {'date':'ds', 'avg_temp': 'y'}, inplace=True)

tmp = tmp[tmp.ds >= '2010-01-01']
tmp.info()

prophet = Prophet(growth = 'linear', seasonality_mode='multiplicative', yearly_seasonality=True,
                  weekly_seasonality=True, daily_seasonality=True,
                  changepoint_prior_scale=0.5)

prophet.fit(tmp)

future_data = prophet.make_future_dataframe(periods=15, freq='d')
forecast_data = prophet.predict(future_data)
forecast_data

forecast_data[['ds', 'yhat_lower', 'yhat_upper', 'yhat']].tail(15)

fig1 = prophet.plot(forecast_data)
fig2 = prophet.plot_components(forecast_data)

y = tmp.y.values
y_pred = forecast_data.yhat.values[:-15]
print(y)
print(y_pred)

from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

r2 = r2_score(y, y_pred)
r2
rmse = sqrt(mean_squared_error(y, y_pred))
rmse
