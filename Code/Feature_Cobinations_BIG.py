# WeatherPredict_BIG.py
#  Title: WeatherPredict
# Author: Bae InGyu

import pandas as pd
import sklearn.metrics as metrics
import string 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from pandas import DataFrame as df
from itertools import combinations

 
newcolumn = string.ascii_uppercase     #To change the column name to the alphabet
i = 0                                  #Index of newcolumn list
cs = 3                                 #Column index start
ce = 24                                #Column index end
lst = [c for c in range(cs,ce)]        #Generate a list of indexes from cs to ce
feature_count = 1                      #Random Forest Parameter max_features
score = []                             #List to save score



#Read data
Weather = pd.read_csv('../Data/pWeather2.csv', encoding='euc-kr')

#Rename column to alphabet
while cs < ce:
    Weather.rename(columns = {Weather.columns[cs] : newcolumn[i]}, inplace =True)
    cs +=1    
    i +=1

#Generate a list of combinations of columns    
while feature_count < 22:
    print(feature_count)
    comblist = list(combinations(lst,feature_count))
    
    #Repeat column combination list length
    for cnt in range(len(comblist)): 
        
        #Create object(randomforest)
        rfc = RandomForestClassifier(n_estimators=10,max_features=feature_count)
    
        #Split data(train,test)
        print(cnt+1,Weather.iloc[:,list(comblist[cnt])].columns.tolist())
        x_train, x_test, y_train, y_test = train_test_split(Weather.iloc[:,list(comblist[cnt])], Weather.iloc[:,-1:], test_size = 0.2)
        
        #Train
        rfc.fit(x_train, y_train.values.ravel())
    
        #Target data predict
        predTrain = rfc.predict(x_train)
        predTest  = rfc.predict(x_test)
    
        #Score append to list
        score.append([Weather.iloc[:,list(comblist[cnt])].columns.tolist(),metrics.accuracy_score(y_train, predTrain),metrics.f1_score(y_train, predTrain),
                      metrics.accuracy_score(y_test, predTest),metrics.f1_score(y_test, predTest)])


        #Dataframe columns
        columns = ['Weather.iloc[:,list(comblist[cnt])].columns.tolist()','accuracy_score(train)','f1_score(train)',
                   'accuracy_score(test)','f1_score(test)']
        
    feature_count +=1
    
    
    
#Convert list to dataframe
dataFrame = df(score,columns=columns)

#Save as dataframe csv file
dataFrame.to_csv('../Doc/Bae InGyu.csv')

