import pandas as pd
import numpy as np

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# FireBase
def FIREBASECONFIG():
    cred = credentials.Certificate("C:/Users/teufe/Downloads/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    
    return firestore.client()

# COLD_SIDO
def COLD_SIDO(db):
    cold_sido = pd.read_csv('./COLD/SIDO.csv', encoding='utf-8')
    
    for index in cold_sido.index:
        doc_ref = db.collection(u'COLD_SIDO').document()
        
        doc_ref.set({
            cold_sido.columns[0]: str(cold_sido.loc[index, cold_sido.columns[0]]),
            cold_sido.columns[1]: str(cold_sido.loc[index, cold_sido.columns[1]])
        })
    
    print('COLD_SIDO SUCCESS')

# COLD_PATIENT
def COLD_PATIENT(db):
    cold_patient = pd.read_csv('./COLD/PATIENT.csv', encoding='utf-8')
    
    for index in cold_patient.index:
        doc_ref = db.collection(u'COLD_PATIENT').document()
        
        doc_ref.set({
           cold_patient.columns[0]: str(cold_patient.loc[index, cold_patient.columns[0]]),
           cold_patient.columns[1]: str(cold_patient.loc[index, cold_patient.columns[1]]),
           cold_patient.columns[2]: str(cold_patient.loc[index, cold_patient.columns[2]])
        })
    
    print('COLD_PATIENT SUCCESS')

# KMA_SIDO
def KMA_SIDO(db):
    kma_sido = pd.read_csv('./KMA/SIDO.csv', encoding='utf-8')
    
    for index in kma_sido.index:
        doc_ref = db.collection(u'KMA_SIDO').document()
        
        doc_ref.set({
           kma_sido.columns[0]: str(kma_sido.loc[index, kma_sido.columns[0]]),
           kma_sido.columns[1]: str(kma_sido.loc[index, kma_sido.columns[1]]),
           kma_sido.columns[2]: str(kma_sido.loc[index, kma_sido.columns[2]])
        })
    
    print('KMA_SIDO SUCCESS')

# KMA_WEATHER
def KMA_WEATHER(db):
    kma_weather = pd.read_csv('./KMA/WEATHER.csv', encoding='utf-8')
    
    for index in kma_sido.index:
        doc_ref = db.collection(u'KMA_WEATHER').document()
        
        doc_ref.set({
           kma_weather.columns[0]: str(kma_weather.loc[index, kma_weather.columns[0]]),
           kma_weather.columns[1]: str(kma_weather.loc[index, kma_weather.columns[1]]),
           kma_weather.columns[2]: str(kma_weather.loc[index, kma_weather.columns[2]]),
           kma_weather.columns[3]: str(kma_weather.loc[index, kma_weather.columns[3]]),
           kma_weather.columns[4]: str(kma_weather.loc[index, kma_weather.columns[4]]),
           kma_weather.columns[5]: str(kma_weather.loc[index, kma_weather.columns[5]]),
           kma_weather.columns[6]: str(kma_weather.loc[index, kma_weather.columns[6]]),
           kma_weather.columns[7]: str(kma_weather.loc[index, kma_weather.columns[7]]),
           kma_weather.columns[8]: str(kma_weather.loc[index, kma_weather.columns[8]]),
           kma_weather.columns[9]: str(kma_weather.loc[index, kma_weather.columns[9]]),
           kma_weather.columns[10]: str(kma_weather.loc[index, kma_weather.columns[10]]),
           kma_weather.columns[11]: str(kma_weather.loc[index, kma_weather.columns[11]]),
           kma_weather.columns[12]: str(kma_weather.loc[index, kma_weather.columns[12]]),
           kma_weather.columns[13]: str(kma_weather.loc[index, kma_weather.columns[13]]),
           kma_weather.columns[14]: str(kma_weather.loc[index, kma_weather.columns[14]]),
           kma_weather.columns[15]: str(kma_weather.loc[index, kma_weather.columns[15]]),
           kma_weather.columns[16]: str(kma_weather.loc[index, kma_weather.columns[16]]),
           kma_weather.columns[17]: str(kma_weather.loc[index, kma_weather.columns[17]]),
           kma_weather.columns[18]: str(kma_weather.loc[index, kma_weather.columns[18]]),
           kma_weather.columns[19]: str(kma_weather.loc[index, kma_weather.columns[19]]),
           kma_weather.columns[20]: str(kma_weather.loc[index, kma_weather.columns[20]]),
           kma_weather.columns[21]: str(kma_weather.loc[index, kma_weather.columns[21]]),
           kma_weather.columns[22]: str(kma_weather.loc[index, kma_weather.columns[22]]),
           kma_weather.columns[23]: str(kma_weather.loc[index, kma_weather.columns[23]]),
           kma_weather.columns[24]: str(kma_weather.loc[index, kma_weather.columns[24]]),
           kma_weather.columns[25]: str(kma_weather.loc[index, kma_weather.columns[25]]),
           kma_weather.columns[26]: str(kma_weather.loc[index, kma_weather.columns[26]]),
           kma_weather.columns[27]: str(kma_weather.loc[index, kma_weather.columns[27]]),
           kma_weather.columns[28]: str(kma_weather.loc[index, kma_weather.columns[28]]),
           kma_weather.columns[29]: str(kma_weather.loc[index, kma_weather.columns[29]]),
           kma_weather.columns[20]: str(kma_weather.loc[index, kma_weather.columns[30]]),
           kma_weather.columns[31]: str(kma_weather.loc[index, kma_weather.columns[31]]),
           kma_weather.columns[32]: str(kma_weather.loc[index, kma_weather.columns[32]]),
           kma_weather.columns[33]: str(kma_weather.loc[index, kma_weather.columns[33]]),
           kma_weather.columns[34]: str(kma_weather.loc[index, kma_weather.columns[34]]),
           kma_weather.columns[35]: str(kma_weather.loc[index, kma_weather.columns[35]]),
           kma_weather.columns[36]: str(kma_weather.loc[index, kma_weather.columns[36]]),
           kma_weather.columns[37]: str(kma_weather.loc[index, kma_weather.columns[37]]),
           kma_weather.columns[38]: str(kma_weather.loc[index, kma_weather.columns[38]]),
           kma_weather.columns[39]: str(kma_weather.loc[index, kma_weather.columns[39]]),
           kma_weather.columns[40]: str(kma_weather.loc[index, kma_weather.columns[40]]),
           kma_weather.columns[41]: str(kma_weather.loc[index, kma_weather.columns[41]]),
           kma_weather.columns[42]: str(kma_weather.loc[index, kma_weather.columns[42]]),
           kma_weather.columns[43]: str(kma_weather.loc[index, kma_weather.columns[43]]),
           kma_weather.columns[44]: str(kma_weather.loc[index, kma_weather.columns[44]]),
           kma_weather.columns[45]: str(kma_weather.loc[index, kma_weather.columns[45]]),
           kma_weather.columns[46]: str(kma_weather.loc[index, kma_weather.columns[46]]),
           kma_weather.columns[47]: str(kma_weather.loc[index, kma_weather.columns[47]]),
           kma_weather.columns[48]: str(kma_weather.loc[index, kma_weather.columns[48]]),
           kma_weather.columns[49]: str(kma_weather.loc[index, kma_weather.columns[49]]),
           kma_weather.columns[50]: str(kma_weather.loc[index, kma_weather.columns[50]]),
           kma_weather.columns[51]: str(kma_weather.loc[index, kma_weather.columns[51]]),
           kma_weather.columns[52]: str(kma_weather.loc[index, kma_weather.columns[52]]),
           kma_weather.columns[53]: str(kma_weather.loc[index, kma_weather.columns[53]]),
           kma_weather.columns[54]: str(kma_weather.loc[index, kma_weather.columns[54]]),
           kma_weather.columns[55]: str(kma_weather.loc[index, kma_weather.columns[55]]),
           kma_weather.columns[56]: str(kma_weather.loc[index, kma_weather.columns[56]]),
           kma_weather.columns[57]: str(kma_weather.loc[index, kma_weather.columns[57]]),
           kma_weather.columns[58]: str(kma_weather.loc[index, kma_weather.columns[58]]),
           kma_weather.columns[59]: str(kma_weather.loc[index, kma_weather.columns[59]]),
           kma_weather.columns[60]: str(kma_weather.loc[index, kma_weather.columns[60]])
        })
    
    print('KMA_WEATHER SUCCESS')

### RUN
#COLD_SIDO(FIREBASECONFIG())
COLD_PATIENT(FIREBASECONFIG())
#KMA_SIDO(FIREBASECONFIG())
#KMA_WEATHER(FIREBASECONFIG())
