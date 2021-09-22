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
