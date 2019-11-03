# WeatherPredict_BIG.py
#  Title: WeatherPredict
# Author: Bae InGyu

import pandas as pd
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from pandas import DataFrame as df

#create score list 
score = []

#number of repetitions
i = 0
count = 1000

#read data
Weather = pd.read_csv('../Data/pWeather.csv', encoding='euc-kr')

#split data(train,test)
x_train, x_test, y_train, y_test = train_test_split(Weather.iloc[:,4:-1], Weather.iloc[:,-1:], test_size = 0.2)

#create object(randomforest)
rfc = RandomForestClassifier(n_estimators=10)

while i < count:
    #train
    rfc.fit(x_train, y_train)
    #target data predict
    predTrain = rfc.predict(x_train)
    predTest  = rfc.predict(x_test)
    #score append to list
    score.append([metrics.precision_score(y_train, predTrain),metrics.recall_score(y_train, predTrain),metrics.accuracy_score(y_train, predTrain),metrics.f1_score(y_train, predTrain),
                  metrics.precision_score(y_test, predTest),metrics.recall_score(y_test, predTest),metrics.accuracy_score(y_test, predTest),metrics.f1_score(y_test, predTest)])
    i += 1

#dataframe columns
columns = ['precision_score(train)','recall_score(train)','accuracy_score(train)','f1_score(train)',
          'precision_score(test)','recall_score(test)','accuracy_score(test)','f1_score(test)']

#convert list to dataframe
dataFrame = df(score,columns=columns)

#dataframe save
dataFrame.to_csv('../Doc/Bae InGyu.csv')
