import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import sklearn.metrics as metrics 

# 전처리 된 데이터 가져오기
#Weather = pd.read_csv('../Data/pWeather.csv', encoding='euc-kr')
Weather = pd.read_csv('pWeather5.csv', encoding='euc-kr')

# 데이터를 Train, Test 데이터로 분할
X_train, X_test, Y_train, Y_test = train_test_split(Weather.iloc[:,3:-1],
                                                    Weather.iloc[:,-1:],
                                                    test_size = 0.2)




# 결과 반환 리스트
result = []
# 반복 횟수
count = 1
#while i < 1 :
    # 랜덤포레스트 객체 생성
rfc = RandomForestClassifier(n_estimators=150,min_samples_leaf=10,n_jobs= -1,max_features=12)
    
for cnt in range(0, count):
        #print(cnt + 1)
        # 훈련
        rfc.fit(X_train, Y_train.values.ravel())
        # train과 test에 해당하는 예측결과
        trainPred = rfc.predict(X_train)
        testPred = rfc.predict(X_test)
        
        
        result.append([metrics.f1_score(Y_train, trainPred),
                       metrics.f1_score(Y_test, testPred)])


print(result)
    #i +=1
'''def feature_importances():
    col = Weather.iloc[:1,cols].columns
    fi = rfc.feature_importances_
    for i in range(0, len(cols)):
        print('%s:%s' % (col[i], fi[i]))
    print(col)

feature_importances()
        '''
# 리스트를 데이터프레임으로 변환
#pd = pd.DataFrame(result, columns=['f1_score(train)',
 #                                  'f1_score(test)',
  #                                 'max_leaf_nodes[i]'])

#데이터프레임 저장
#pd.to_csv('LJJ3.csv')
