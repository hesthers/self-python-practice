# Analyzing the US census data

import pandas as pd
us_county = pd.read_csv('./acs2017_county_data.csv', encoding = 'utf8')
us_county.info()

us_county_info = us_county[['State', 'County', 'TotalPop', 'Income', 'IncomePerCap', 'Unemployment', 'Employed']]

us_county_info.head()
us_county_info.info()
