import numpy as np
from nsepy import get_history
import datetime as dt
from tensorflow.keras.models import model_from_json


class RunModel:
    def __init__(self, company):
        self.symbol = company.symbol

    def __loadModel(self):
        # wipro model
        path = 'lstm/lstmModel_final.json'
        weights = 'lstm/weights_final.h5'
        # print(weights)
        # print(path)
        json_file = open(path, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        model.load_weights(weights)
        print("Loaded model from disk")
        return model

    # getting data for selected company
    def __inputHandler(self):

        self.model = self.__loadModel()

        start = dt.date(2011, 1, 17)
        try:
            #end = self.__getEndDate(dt.date.today())
            print("getting data...")
            self.data = get_history(
                symbol=self.symbol,
                start=start,
                end=dt.date.today() - dt.timedelta(days=1)
            )
            print(self.data.tail())
        except ConnectionError as e:
            print(e)

    # prediction for next 30 days

    def getNext30Days(self):
        self.__inputHandler()
        dataset = self.data
        dataset = dataset['Close'].values
        dataset = dataset[len(dataset)-30:]
        n_features = 1
        n_steps = 30
        past_days = 30
        # demonstrate prediction for next 10 days
        x_input = np.array(dataset.tolist())
        temp_input = list(x_input)
        lst_output = []
        i = 0
        while(i < 30):

            if(len(temp_input) > past_days):
                x_input = np.array(temp_input[1:])
                #print("{} day input {}".format(i, x_input))
                # print(x_input)
                x_input = x_input.reshape((1, n_steps, n_features))
                # print(x_input)
                yhat = self.model.predict(x_input, verbose=0)
                #print("{} day output {}".format(i, yhat))
                temp_input.append(yhat[0][0])
                temp_input = temp_input[1:]
                # print(temp_input)
                lst_output.append(yhat[0][0])
                i = i+1
            else:
                x_input = x_input.reshape((1, n_steps, n_features))
                yhat = self.model.predict(x_input, verbose=0)
                # print(yhat[0])
                temp_input.append(yhat[0][0])
                lst_output.append(yhat[0][0])
                i = i+1
        print(lst_output)
        predictions = lst_output
        return predictions
