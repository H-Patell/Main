#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.svm import LinearSVC
from sklearn import metrics
import pickle


#loading trained model from pickle object
with open('model_pickle','rb')as f:
    tf=pickle.load(f)

# predicting on newly generated csv
def func2(data):    
    data2=data    
    X_test = data2.Sentence
    
    pred = tf.predict(X_test)

    data2['label'] = np.array(pred)
    data2.to_csv(r'C:\\Users\\Admin\\capstone\\14-10-2022\\OLD\\label.csv',index = False)
    return(data2)

#concatenating newly generated csv files(pasta)
def concat_file():
    TEST = pd.DataFrame()
    for i in range(1, 4):
        
        try:
            df = pd.read_csv(f"C:\\Users\\Admin\\capstone\\14-10-2022\\OLD\\{i}.csv") 
            TEST = pd.concat([TEST, df])
            TEST.to_csv('combined.csv')
            
        except FileNotFoundError:
            continue
    return TEST     

