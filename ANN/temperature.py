# Practice for ANN (Artificial Neural Network) python code

import pandas as pd
temperature = pd.read_csv('기온데이터_서울.csv', index_col=None, header=None)
temperature.drop(labels=1, axis=1, inplace=True)
temperature.rename(columns={0:'date', 2:'avg_temp', 3:'low_temp', 4:'high_temp'}, inplace=True)

