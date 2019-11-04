# WeatherForecast_LSJ.py
#  Title: Weather Forecast
# AUTHOR: LEE SEOKJUNE
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import sklearn.metrics as metrics 

# 전처리 된 데이터 가져오기
#Weather = pd.read_csv('../Data/pWeather.csv', encoding='euc-kr')
Weather = pd.read_csv('../Data/pWeather2.csv', encoding='euc-kr')

# 데이터를 Train, Test 데이터로 분할
X_train, X_test, Y_train, Y_test = train_test_split(Weather.iloc[:,4:-1],
                                                    Weather.iloc[:,-1:],
                                                    test_size = 0.2)

# print(X_train)    # 2629 / 20
# print(Y_train)    # 2629 /  1
# print(X_test)     #  658 / 20
# print(Y_test)     #  658 /  1

# 랜덤포레스트 객체 생성
rfc = RandomForestClassifier(n_estimators=10)

# 결과 반환 리스트
result = []
# 반복 횟수
count = 1000

for cnt in range(0, count):
    print(cnt + 1)
    # 훈련
    rfc.fit(X_train, Y_train.values.ravel())
    # train과 test에 해당하는 예측결과
    trainPred = rfc.predict(X_train)
    testPred = rfc.predict(X_test)
    #
    result.append([metrics.accuracy_score(Y_train, trainPred),
                   metrics.precision_score(Y_train, trainPred),
                   metrics.recall_score(Y_train, trainPred),
                   metrics.f1_score(Y_train, trainPred),
                   metrics.accuracy_score(Y_test, testPred),
                   metrics.precision_score(Y_test, testPred),
                   metrics.recall_score(Y_test, testPred),
                   metrics.f1_score(Y_test, testPred)])
# 리스트를 데이터프레임으로 변환
pd = pd.DataFrame(result, columns=['accuracy_score(train)',
                                   'precision_score(train)',
                                   'recall_score(train)',
                                   'f1_score(train)',
                                   'accuracy_score(test)',
                                   'precision_score(test)',
                                   'recall_score(test)',
                                   'f1_score(test)'])
#데이터프레임 저장
pd.to_csv('../Doc/LSJ.csv')
