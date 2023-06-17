import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('cpp.csv')
print(df)

plt.xlabel('year')
plt.ylabel('per_capita_income')

plt.scatter(df.year,df.per_capita_income,color='red',marker='D')

newdf = df.drop('per_capita_income',axis='columns')
print(newdf)

reg = linear_model.LinearRegression()
reg.fit(newdf,df.per_capita_income)

plt.plot(df.year,reg.predict(df[['year']]),color='black')
plt.show()

print(reg.predict([[2020]]))
print(reg.coef_)
print(reg.intercept_)