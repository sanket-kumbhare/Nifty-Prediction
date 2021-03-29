import tensorflow as tf
import numpy as np
from nsepy import get_history
from sklearn.preprocessing import MinMaxScaler
import datetime as dt
from tensorflow.keras import models
from tensorflow.keras.models import model_from_json
import os


class RunModel:
    def __init__(self, company):
        self.symbol = company.symbol

    def __loadModel(self):
        # wipro model
        path = 'lstm/lstmModel.json'
        weights = 'lstm/weights.h5'
        print(weights)
        print(path)
        json_file = open(path, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        model.load_weights(weights)
        print("Loaded model from disk")
        return model

    def __getEndDate(self, today):
        end = str(today).split("-")
        end[-1] = str(int(end[-1])-1)

        end = list(map(int, end))
        return end

    def __inputHandler(self):

        self.model = self.__loadModel()

        start = dt.date(2011, 1, 17)

        end = self.__getEndDate(dt.date.today())
        print("getting data...")
        self.data = get_history(
            symbol=self.symbol,
            start=start,
            end=dt.date(end[0], end[1], end[2]
                        ))
        print(self.data.tail())
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        # Create new data frame
        new_df = self.data.filter(['Close'])
        # get the last 60 days closing price values and convert the dataframe to an array
        last_60_days = new_df[-60:].values
        # scaled the data to be values between 0 and 1
        last_60_days_scaled = self.scaler.fit_transform(last_60_days)
        # create an empty list
        X_test = []
        # append the past 60 days
        X_test.append(last_60_days_scaled)
        # convert the X_test data set to a numpy array
        X_test = np.array(X_test)
        # Reshape the data
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        # get the predicted scaled price
        pred_price = self.model.predict(X_test)
        yhat = pred_price[0]
        # undo the scalling
        self.pred_price = self.scaler.inverse_transform(pred_price)

        return self.pred_price

    def getPrice(self):
        price = self.__inputHandler()
        closePrice = self.data['Close'][-1]
        priceObj = {
            'end': self.data.index[-1],
            'endPrice': closePrice,
            'tommorow': dt.date.today(),
            'prediction': price[0][0]
        }

        return priceObj

    def next30days(self):
        from numpy import array

        lst_output = []
        n_steps = 259
        i = 0
        while(i < 30):

            if(len(temp_input) > 100):
                # print(temp_input)
                x_input = np.array(temp_input[1:])
                print("{} day input {}".format(i, x_input))
                x_input = x_input.reshape(1, -1)
                x_input = x_input.reshape((1, n_steps, 1))
                # print(x_input)
                yhat = self.model.predict(x_input, verbose=0)
                print("{} day output {}".format(i, yhat))
                temp_input.extend(yhat[0].tolist())
                temp_input = temp_input[1:]
                # print(temp_input)
                lst_output.extend(yhat.tolist())
                i = i+1
            else:
                x_input = x_input.reshape((1, n_steps, 1))
                yhat = self.model.predict(x_input, verbose=0)
                print(yhat[0])
                temp_input.extend(yhat[0].tolist())
                print(len(temp_input))
                lst_output.extend(yhat.tolist())
                i = i+1
        output = self.scaler.inverse_transform(lst_output)

        return output
