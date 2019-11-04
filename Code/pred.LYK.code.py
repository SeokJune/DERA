import pandas as pd
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import numpy as np
Weather=pd.read_csv("pWeather_.csv", encoding='utf-8')

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(Weather.iloc[ :2000,4:-1],Weather.iloc[ :2000,-1:], test_size = 0.2)
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=10)

from sklearn import preprocessing
lab_enc = preprocessing.LabelEncoder()
yy_train = lab_enc.fit_transform(y_train)
prediction = rfc.predict(x_test)


train1 = []
train2 = []
train3 = []
train4 = []
test1 = []
test2 = []
test3 = []
test4 = []
for i in range(1, 1001):
    rfc.fit(x_train, y_train) 
    
    pred1 = rfc.predict(x_train)
    
    train1.append(accuracy_score(pred1, y_train))
    train2.append(recall_score(pred1, y_train))
    train3.append(precision_score(pred1, y_train))
    train4.append(f1_score(pred1, y_train))
    
    pred2 = rfc.predict(x_test)
        
    test1.append(accuracy_score(pred2, y_test))
    test2.append(recall_score(pred2, y_test))
    test3.append(precision_score(pred2, y_test))
    test4.append(f1_score(pred2, y_test))
    
print(train1)
pd1 = pd.DataFrame(train1, columns=['train_accuray'])
pd2 = pd.DataFrame(train2, columns=['train_recall'])
pd3 = pd.DataFrame(train3, columns=['train_precision'])
pd4 = pd.DataFrame(train4, columns=['train_f1_score'])
pd5 = pd.DataFrame(test1, columns=['test_accuray'])
pd6 = pd.DataFrame(test2, columns=['test_recall'])
pd7 = pd.DataFrame(test3, columns=['test_precision'])
pd8 = pd.DataFrame(test4, columns=['test_f1_score'])

pd1.to_csv('t1', index=False)
pd2.to_csv('t2', index=False)
pd3.to_csv('t3', index=False)
pd4.to_csv('t4', index=False)
pd5.to_csv('t5', index=False)
pd6.to_csv('t6', index=False)
pd7.to_csv('t7', index=False)
pd8.to_csv('t8', index=False)

