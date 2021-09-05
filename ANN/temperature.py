# Practice for ANN (Artificial Neural Network) python code

# preprocessing
import pandas as pd
temperature = pd.read_csv('기온데이터_서울.csv', index_col=None, header=None)
temperature.drop(labels=1, axis=1, inplace=True)
temperature.rename(columns={0:'date', 2:'avg_temp', 3:'low_temp', 4:'high_temp'}, inplace=True)

# variables - independent & dependent
test = temperature['avg_temp']
test = test.values
train = temperature[['low_temp', 'high_temp']]
train = train.values

# split - test, train, validation data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(train, test, test_size = 0.3, random_state = 1000)

import numpy as np
mean = np.mean(x_train, axis = 0)
std = np.std(x_train, axis = 0)
x_train = (x_train - mean) / std
x_test = (x_test - mean) / std

x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size = 0.2, random_state = 1000)

# data training

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(64, activation = 'relu', input_shape = (2,)),
    Dense(32, activation = 'relu'),
    Dense(10,activation = 'relu'),
    Dense(1)])

model.compile(optimizer = 'adam', loss ='mse', metrics = 'acc')
history = model.fit(x_train, y_train, epochs = 200, verbose = 0, validation_data = (x_val, y_val))

# model evaluation
model.evaluate(x_test, y_test)
