import numpy as np
import pandas as pd
from sklearn import linear_model
from word2number import w2n
import math

df = pd.read_csv('exercise.csv')

df.experience = df.experience.fillna('zero')

df.experience = df.experience.apply(w2n.word_to_num)

df.test_score = df.test_score.fillna(math.floor(df.test_score.mean()))

reg = linear_model.LinearRegression()
reg.fit(df[['experience','test_score','interview_score']],df.salary)

print(reg.predict([[2,9,6]]))