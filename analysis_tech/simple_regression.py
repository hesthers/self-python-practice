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

### Model learning - simple regression
x = us_county_info[['IncomePerCap']]   
y = us_county_info['Income']        

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.4, random_state=100) 
print('train data 개수:', len(x_train))
print('test data 개수:', len(x_test))

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)

r_square = lr.score(x_test, y_test) 
print(r_square)      

print("기울기 a", lr.coef_)
print("y 절편 b", lr.intercept_)
