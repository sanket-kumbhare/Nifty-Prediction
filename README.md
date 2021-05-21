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
### 1. [Documents Folder](https://github.com/Sanket-Kumbhare/Nifty-Prediction/tree/master/Documents)
Contains Reports, PPT and Project diaries of 7<sup>th</sup> and 8<sup>th</sup> semester.
> Documents Directory
```
Documents
|   7th sem project diary smpp.pdf
|   PPT Sem8 Stock Market Prediction.pdf
|   Project Report Stock Market Prediction.pdf
|   Sem 8 Project Diary.pdf
|   Sem8 report stock Price Prediction.pdf
|   Stock Market Prediction PPT-converted.pptx 
```
### 2. [Nifty-50-Prediction Folder](https://github.com/Sanket-Kumbhare/Nifty-Prediction/tree/master/Nifty-50-Prediction)
Contains following Django Project files and folders.
> Nifty-50-Prediction Directory
```
Nifty-50-Prediction
└───Stock_Prediction
└───lstm
└───stock
|   db.sqlite3
|   manage.py
|   nifty50Companies.csv 
```
  - #### [Stock_Prediction](https://github.com/Sanket-Kumbhare/Nifty-Prediction/tree/master/Nifty-50-Prediction/Stock_Prediction)
  > The Django project holds some configurations that apply to the project as a whole, such as project settings, URLs, shared templates and static files. Each application can have its own database and has its own functions to control how the data is displayed to the user in HTML templates.\
  > Stock_Prediction Directory
 ```
 Stock_Prediction
 |   __init__.py
 |   asgi.py
 |   settings.py
 |   urls.py
 |   wsgi.py
 ```
  - #### [lstm](https://github.com/Sanket-Kumbhare/Nifty-Prediction/tree/master/Nifty-50-Prediction/lstm)
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
  - #### [stock](https://github.com/Sanket-Kumbhare/Nifty-Prediction/tree/master/Nifty-50-Prediction/stock)
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
  - #### [db.sqlite3](https://github.com/Sanket-Kumbhare/Nifty-Prediction/tree/master/Nifty-50-Prediction/db.sqlite)
  > SQLite3 is a software library that provides a relational database management system. The lite in SQLite means lightweight in terms of setup, database administration, and required resources. SQLite has the following noticeable features: self-contained, serverless, zero-configuration, transactional.\
  > We are using sqlite3 for manageing User Authentication
<img src="https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Screenshots/myapp_models.png" width="800px;"/>

  - #### [manage.py](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Nifty-50-Prediction/manage.py)
  > A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py. The inner mysite/ directory is the actual Python package for your project.
  - #### [nifty50Companies.csv](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Nifty-50-Prediction/nifty50Companies.csv)
  > Csv file containing the list of nifty 50 companies with their respective symbol
### 3. [models Folder](https://github.com/Sanket-Kumbhare/Nifty-Prediction/tree/master/models)
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
 ![](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Screenshots/login.gif)  |  ![](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Screenshots/signup.png) 
 
 Prediction | News Section 
 :---:|:---:
 ![](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Screenshots/prediction.gif)  |  ![](https://github.com/Sanket-Kumbhare/Nifty-Prediction/blob/master/Screenshots/news.gif)  
---
## Required Libraries
- `django` Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- `nsepy` NSEpy is a library to extract historical and realtime data from NSE’s website.
- `sklearn` Simple and efficient tools for predictive data analysis
- `tenserflow` TensorFlow is an end-to-end open source platform for machine learning.
- `keras` Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow.
- `datetime` The datetime module supplies classes for manipulating dates and times.
---
## Contributors
| [<img src="https://avatars.githubusercontent.com/u/58529304?v=4" width="100px;"/><br /><sub><b>Sanket-Kumbhare</b></sub>](https://github.com/Sanket-Kumbhare) | [<img src="https://avatars.githubusercontent.com/u/31096252?v=4" width="100px;"/><br /><sub><b>swankhede</b></sub>](https://github.com/swankhede) | [<img src="https://avatars.githubusercontent.com/u/80164927?v=4" width="100px;"/><br /><sub><b>nihalbhopatrao</b></sub>](https://github.com/nihalbhopatrao) | [<img src="https://avatars.githubusercontent.com/u/83209588?v=4" width="100px;"/><br /><sub><b>kgce-git</b></sub>](https://github.com/kgce-git) | 
:---: | :---: | :---: |:---:
---
