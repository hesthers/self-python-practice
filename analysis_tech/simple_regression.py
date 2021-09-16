# Analyzing the US census data

import pandas as pd
us_county = pd.read_csv('./acs2017_county_data.csv', encoding = 'utf8')
us_county.info()

us_county_info = us_county[['State', 'County', 'TotalPop', 'Income', 'IncomePerCap', 'Unemployment', 'Employed']]

us_county_info.head()
us_county_info.info()

### Graph (Plots)
import seaborn as sns
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.regplot(data = us_county_info, x= 'TotalPop', y = 'Unemployment', ax=ax1)
sns.regplot(data = us_county_info, x= 'Income', y = 'Employed', ax=ax2)
plt.show()

sns.pairplot(us_county_info[['TotalPop', 'Income', 'IncomePerCap', 'Unemployment', 'Employed']])

### 2nd data preprocessing 
us_county_info['Unemployment'] = round(us_county['Unemployment'] * us_county['TotalPop']/100,0).astype('int')

sns.pairplot(us_county_info[['TotalPop', 'Income', 'IncomePerCap', 'Unemployment', 'Employed']])

### new regplots
fig = plt.figure(figsize=(21,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

sns.regplot(data = us_county_info, x= 'TotalPop', y = 'Employed', ax=ax1)
sns.regplot(data = us_county_info, x= 'IncomePerCap', y = 'Income', ax=ax2)
sns.regplot(data = us_county_info, x= 'TotalPop', y = 'Unemployment', ax=ax3)
plt.show()

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.regplot(data = us_county_info, x= 'Unemployment', y = 'Income', ax=ax1)
sns.regplot(data = us_county_info, x= 'Unemployment', y = 'IncomePerCap', ax=ax2)
plt.xlim(range(0, 350000))
plt.show()
