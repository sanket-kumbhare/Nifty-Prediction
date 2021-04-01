import numpy as np
import pandas as pd
from nsepy import get_history
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import math
import datetime as dt

print("getting data")
data = get_history(
    symbol='WIPRO',
    start=dt.date(2011, 1, 17),
    end=dt.date.today()
)

data = data.filter(['Close'])
dataset = data.values  # convert the data frame to a numpy array
# number of rows to train the model on
training_data_len = math.ceil(len(dataset)*.8)

# scale the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)
scaled_data

# create the training dataset
# create the scaled training dataset

train_data = scaled_data[0:training_data_len, :]
# Split the data into x_train, y_train datasets
x_train = []
y_train = []
for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
# reshape the data
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_train.shape

# Build the LSTM model
print("buliding model")
model = Sequential()
model.add(LSTM(64, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(32))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, batch_size=1, epochs=10)

model.summary()

print("saving data...   ")
model_json = model.to_json()
with open("lstmModel.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("weights.h5")
print("Saved model to disk")
