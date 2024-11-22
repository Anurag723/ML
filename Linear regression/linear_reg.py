import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("workspaces\\ML\\Linear regression\\area.csv")
# print(df)

plt.xlabel('area')
plt.ylabel('price')

plt.scatter(df.area,df.price,color='Red',marker='*')
# plt.show()

newdf = df.drop('price',axis='columns')
# print(newdf)

reg = linear_model.LinearRegression()
reg.fit(newdf,df.price)

# print(reg.predict([[3300]]))
# print(reg.coef_)
# print(reg.intercept_)

plt.plot(df.area,reg.predict(df[['area']]),color='blue')
# plt.show()

#``````````````````````````````````````````````upto this part the model is trained````````````````````````````````````````

pre = pd.read_csv('prediction.csv')
print(pre)

pre['prices'] = reg.predict(pre)
print(pre)

pre.to_csv('prediction.csv')