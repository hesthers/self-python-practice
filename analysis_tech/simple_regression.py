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


