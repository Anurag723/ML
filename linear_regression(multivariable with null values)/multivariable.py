import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import math

df = pd.read_csv('multivariate.csv')

bdrooms = math.floor(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(bdrooms)

print(df)

reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)

print(reg.predict([[3000,3,40]]))
print(reg.coef_)
print(reg.intercept_)