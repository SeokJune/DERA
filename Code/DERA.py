# Import List
import pandas as pd
import numpy as np

# Read csv file
def readCSV(num = 1):
    if num == 0:
        weather = pd.read_csv('../Data/weather.csv', encoding='euc-kr')
        stnInfo = pd.read_csv('../Data/stnInfo.csv', encoding='euc-kr')

        return weather, stnInfo
    else:
        weather = pd.read_csv('../Data/pWeather.csv', encoding='euc-kr')
        return weather
    
# Drop Unnecessary Columns
def dropCols(dataFrame, num):
    if num == 0:
        dataFrame1 = dataFrame.drop([#'지점',
                                     #'일시',
                                     #'평균기온(°C)',
                                     #'최저기온(°C)',
                                     '최저기온 시각(hhmi)',
                                     #'최고기온(°C)',
                                     '최고기온 시각(hhmi)',
                                     '강수 계속시간(hr)',
                                     '10분 최다 강수량(mm)',
                                     '10분 최다강수량 시각(hhmi)',
                                     '1시간 최다강수량(mm)',
                                     '1시간 최다 강수량 시각(hhmi)',
                                     #'일강수량(mm)',
                                     '최대 순간 풍속(m/s)',
                                     '최대 순간 풍속 풍향(16방위)',
                                     '최대 순간풍속 시각(hhmi)',
                                     '최대 풍속(m/s)',
                                     '최대 풍속 풍향(16방위)',
                                     '최대 풍속 시각(hhmi)',
                                     '평균 풍속(m/s)',
                                     '풍정합(100m)',
                                     '최다풍향(16방위)',
                                     #'평균 이슬점온도(°C)',
                                     #'최소 상대습도(%)',
                                     '최소 상대습도 시각(hhmi)',
                                     #'평균 상대습도(%)',
                                     #'평균 증기압(hPa)',
                                     #'평균 현지기압(hPa)',
                                     #'최고 해면기압(hPa)',
                                     '최고 해면기압 시각(hhmi)',
                                     #'최저 해면기압(hPa)',
                                     '최저 해면기압 시각(hhmi)',
                                     #'평균 해면기압(hPa)',
                                     #'가조시간(hr)',
                                     #'합계 일조 시간(hr)',
                                     '1시간 최다일사 시각(hhmi)',
                                     '1시간 최다일사량(MJ/m2)',
                                     #'합계 일사(MJ/m2)',
                                     #'일 최심신적설(cm)',
                                     '일 최심신적설 시각(hhmi)',
                                     #'일 최심적설(cm)',
                                     '일 최심적설 시각(hhmi)',
                                     '합계 3시간 신적설(cm)',
                                     #'평균 전운량(1/10)',
                                     #'평균 중하층운량(1/10)',
                                     #'평균 지면온도(°C)',
                                     #'최저 초상온도(°C)',
                                     '평균 5cm 지중온도(°C)',
                                     '평균 10cm 지중온도(°C)',
                                     '평균 20cm 지중온도(°C)',
                                     '평균 30cm 지중온도(°C)',
                                     '0.5m 지중온도(°C)',
                                     '1.0m 지중온도(°C)',
                                     '1.5m 지중온도(°C)',
                                     '3.0m 지중온도(°C)',
                                     '5.0m 지중온도(°C)',
                                     '합계 대형증발량(mm)',
                                     '합계 소형증발량(mm)',
                                     '9-9강수(mm)',
                                     '기사',
                                     '안개 계속시간(hr)'], axis=1)
        #
        dataFrame2 = dataFrame
        dataFrame2['Rain'] = dataFrame2['일강수량(mm)'].notnull().astype(int)
        dataFrame2 = dataFrame2[['일강수량(mm)','Rain']]
        dataFrame2 = dataFrame2.drop([0])
        #
        dataFrame3 = pd.DataFrame({'일강수량(mm)':[np.nan],'Rain':[0]})
        #
        dataFrame4 = pd.concat([dataFrame2, dataFrame3], ignore_index=True)
        #
        dataFrame = pd.concat([dataFrame1, dataFrame4['Rain']], axis=1)
    elif num == 1:
        dataFrame = dataFrame[dataFrame['종료일'].isnull() == True]
        dataFrame = dataFrame[['지점', '지점명']]
        dataFrame = dataFrame.drop_duplicates()
    return dataFrame

#Merge Data
def mergeDataFrame(weather, stnInfo):
    Data = pd.merge(weather, stnInfo, on='지점', how='left')
    Data = Data[['지점', '지점명', '일시', '평균기온(°C)', '최저기온(°C)',
                '최고기온(°C)', '일강수량(mm)', '평균 이슬점온도(°C)', '최소 상대습도(%)', '평균 상대습도(%)',
                '평균 증기압(hPa)', '평균 현지기압(hPa)', '최고 해면기압(hPa)', '최저 해면기압(hPa)', '평균 해면기압(hPa)',
                '가조시간(hr)', '합계 일조 시간(hr)', '합계 일사(MJ/m2)', '일 최심신적설(cm)', '일 최심적설(cm)',
                '평균 전운량(1/10)', '평균 중하층운량(1/10)', '평균 지면온도(°C)', '최저 초상온도(°C)', 'Rain']]
    return Data

# Run
def run(job = 1):
    if job == 0:
        weather, stnInfo = readCSV(0)
        weather = dropCols(weather, 0)
        stnInfo = dropCols(stnInfo, 1)
        pWeather = mergeDataFrame(weather, stnInfo)
        # Save csv file
        pWeather.to_csv('../Data/pWeather_.csv', index=False, na_rep=0, encoding='euc-kr')
    else:
        print('---')


# Start(0 - Data Preprocessing, 1 - random Forest)
run(0)
