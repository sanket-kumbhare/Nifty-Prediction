import numpy as np

from nsepy import get_history
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

from keras.callbacks import EarlyStopping
import datetime as dt

print("getting data")
ds = get_history(
    symbol='WIPRO',
    start=dt.date(2011, 1, 17),
    end=dt.date.today()
)


sc = MinMaxScaler()
train_set = sc.fit_transform(ds['Close'][:2459].values.reshape(-1, 1))

# create the training dataset
# create the scaled training dataset

past_days = 30


def prepare_data(timeseries_data, n_features):
    X, y = [], []
    for i in range(len(timeseries_data)):
        # find the end of this pattern
        end_ix = i + n_features
        # check if we are beyond the sequence
        if end_ix > len(timeseries_data)-1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = timeseries_data[i:end_ix], timeseries_data[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)


# define input sequence
timeseries_data = ds['Close'][:6100].tolist()
# choose a number of time steps
n_steps = past_days
# split into samples
X, y = prepare_data(timeseries_data, n_steps)

n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))


# Build the LSTM model
print("buliding model")
callback = [EarlyStopping(monitor='loss', mode='auto',)]
model = Sequential()
model.add(LSTM(64, activation='relu', return_sequences=True,
               input_shape=(n_steps, n_features)))
model.add(LSTM(64, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse',)
# fit model
model.fit(X, y, epochs=30, verbose=1)

print("saving data...   ")
model_json = model.to_json()
with open("lstmModel_final.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("weights_final.h5")
print("Saved model to disk")
