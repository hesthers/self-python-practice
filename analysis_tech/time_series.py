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

test_file_path = './기온데이터_서울.csv'
temp_df = pd.read_csv(test_file_path, index_col=None, header=None)

temp_df.drop(labels=1, axis=1, inplace=True)
temp_df.rename(columns={0:'date', 2:'avg_temp', 3:'low_temp', 4:'high_temp'}, inplace=True)

tmp_df = temp_df[['date', 'avg_temp']]
tmp_df.rename(columns = {'date':'ds', 'avg_temp': 'y'}, inplace=True)

tmp_df = tmp_df[tmp_df.ds >= '2010-01-01']

y = tmp_df.y.values[-15:]
y_pred = forecast_data.yhat.values[-30:-15]
date = tmp_df.ds.values[-15:]

sns.lineplot(data = forecast_data[-30:-15], x= date, y= y_pred, label = 'predicted')
sns.lineplot(data = tmp_df[-15:], x= date, y = y, label = 'real')
plt.xticks(rotation = 75)
plt.ylim((10, 40))
plt.legend()
plt.show()

y_df = pd.DataFrame(y)
y_df.set_index(date, inplace=True)
y_df.rename(columns={0:'real'}, inplace=True)
y_df['pred'] = y_pred
y_df['diff'] = np.abs(y_df['pred']-y_df['real'])
y_df['diff']
