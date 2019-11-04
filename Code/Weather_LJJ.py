import pandas as pd
import warnings
warnings.filterwarnings(action='ignore') 
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
Weather=pd.read_csv("pWeather_.csv", encoding='euc-kr')
x_train, x_test, y_train, y_test = train_test_split(Weather.iloc[:,4:-1],Weather.iloc[:,-1:], test_size = 0.3)
rfc = RandomForestClassifier(n_estimators=10)
from sklearn import preprocessing
lab_enc = preprocessing.LabelEncoder()
yy_train = lab_enc.fit_transform(y_train)
rfc.fit(x_train, y_train)
import sklearn.metrics as metrics
prediction = rfc.predict(x_test)

train1=[]
train2=[]
train3=[]
train4=[]
test1=[]
test2=[]
test3=[]
test4=[]

for i in range(0,1000): 
    rfc.fit(x_train,y_train)
    pred1 = rfc.predict(x_train)
    
    
    train1.append(accuracy_score(pred1,y_train))
    train2.append(recall_score(pred1,y_train))
    train3.append(precision_score(pred1,y_train))
    train4.append(f1_score(pred1,y_train))
    
    pred2 = rfc.predict(x_test)
    test1.append(accuracy_score(pred2,y_test))
    test2.append(recall_score(pred2,y_test))
    test3.append(precision_score(pred2,y_test))
    test4.append(f1_score(pred2,y_test))
    
pd1 =  pd.DataFrame(train1,columns=["train_accuracy_score"])
pd2 =  pd.DataFrame(train2,columns=["train_reccall_score"])
pd3 =  pd.DataFrame(train3,columns=["train_precision_score"])
pd4 =  pd.DataFrame(train4,columns=["train_f1_score"])

pd5 =  pd.DataFrame(test1,columns=["test_accuracy_score"])
pd6 =  pd.DataFrame(test2,columns=["test_reccall_score"])
pd7 =  pd.DataFrame(test3,columns=["test_precision_score"])
pd8 =  pd.DataFrame(test4,columns=["test_f1_score"])

pda= pd.concat([pd1,pd2,pd3,pd4],axis=1)
pdb= pd.concat([pd5,pd6,pd7,pd8],axis=1)
pdc =pd.concat([pda,pdb],axis=1)
pdc.to_csv(path_or_buf =r"C:/Users/User/Desktop/66.csv", 
      encoding = 'euc-kr')


