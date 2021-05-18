# Stock Price Prediction of Nifty 50 Companies
## Group members
- Nihal N. Bhopatrao (Roll No. 5)
- Sanket R. Kumbhare (Roll No. 36)
- Shashank D. Wankhede (Roll No. 59)
---
## Project Guide
- Prof. A. S. Kunte
---
## Content
### Main Directory
```
Nifty-Prediction  
└───Documents
└───Nifty-50-Prediction
└───models
└───Screenshots
```
### 1. Documents Folder
Contains Reports, PPT and Project diaries of 7<sup>th</sup> and 8<sup>th</sup> semester.
> Documents Directory
```
Documents
|
|
|
|
|
|
```
### 2. Nifty-50-Prediction Folder
Contains following Django Project files and folders.
  - #### Stock_Prediction
  > The Django project holds some configurations that apply to the project as a whole, such as project settings, URLs, shared templates and static files. Each application can have its own database and has its own functions to control how the data is displayed to the user in HTML templates.
 ```
 Stock_Prediction Directory
 |   __init__.py
 |   asgi.py
 |   settings.py
 |   urls.py
 |   wsgi.py
 ```
  - #### lstm
  > It is special kind of recurrent neural network that is capable of learning long term dependencies in data. This is achieved because the recurring module of the model has a combination of four layers interacting with each other.\
  > lstm Directory
 ```
 lstm
 |   RunModel.py
 |   TrainModel.py
 |   lstmModel_final.json
 |   weights_final.h5
 ```
**Our LSTM model** \
following code is from [TrainModel.py](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Nifty-50-Prediction/lstm/TrainModel.py)
```python
model = Sequential()
model.add(LSTM(64, activation='relu', return_sequences=True,input_shape=(n_steps, n_features)))
model.add(LSTM(64, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse',)
model.fit(X, y, epochs=30, verbose=1)
```
**Prediction for 30 days** \
following code is from [RunModel.py](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Nifty-50-Prediction/lstm/RunModel.py)
```python
def getNext30Days(self):
        self.__inputHandler()
        dataset = self.data
        dataset = dataset['Close'].values
        dataset = dataset[len(dataset)-30:]
        n_features = 1
        n_steps = 30
        past_days = 30
        # demonstrate prediction for next 30 days
        x_input = np.array(dataset.tolist())
        temp_input = list(x_input)
        lst_output = []
        i = 0
        while(i < 30):

            if(len(temp_input) > past_days):
                x_input = np.array(temp_input[1:])
                x_input = x_input.reshape((1, n_steps, n_features))
                yhat = self.model.predict(x_input, verbose=0)
                temp_input.append(yhat[0][0])
                temp_input = temp_input[1:]
                lst_output.append(yhat[0][0])
                i = i+1
            else:
                x_input = x_input.reshape((1, n_steps, n_features))
                yhat = self.model.predict(x_input, verbose=0)
                temp_input.append(yhat[0][0])
                lst_output.append(yhat[0][0])
                i = i+1
        print(lst_output)
        predictions = lst_output
        return predictions
```
  - #### stock
  > A Django application is a Python package that is specifically intended for use in a Django project. An application may use common Django conventions, such as having models , tests , urls , and views submodules.\
  > stock Directory
```
stock
└───migrations
└───templates
|   |   base.html
|   |   home.html
|   |   signup.html
|   __init__.py
|   admin.py
|   apps.py
|   forms.py
|   models.py
|   tests.py
|   views.py
```
  - #### db.sqlite3
  > SQLite3 is a software library that provides a relational database management system. The lite in SQLite means lightweight in terms of setup, database administration, and required resources. SQLite has the following noticeable features: self-contained, serverless, zero-configuration, transactional.\
  > We are using sqlite3 for manageing User Authentication
  - #### manage.py
  > A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py. The inner mysite/ directory is the actual Python package for your project.
  - #### nifty50Companies
### 3. models Folder
Contains experiments with models 
  > models Directory
  ```
  models
  |   NiftyPrediction.ipynb
  |   NiftyPrediction.ipynb
  ```
### 4. Screenshots Folder
Contains screenshots of the UI 
 Home/Login Page | Signup Page 
:---:|:---:
 ![](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Screenshots/login.png)  |  ![](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Screenshots/signup.png) 
 
 Prediction | News Section 
 :---:|:---:
 ![](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Screenshots/prediction.png)  |  ![](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Screenshots/news.png)  
---
