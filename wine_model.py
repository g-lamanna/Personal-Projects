import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.metrics import accuracy_score
import numpy as np

df = pd.read_csv("winequality-red.csv")

df.isnull().sum()

# wine_cols = []
# for col in df.columns:
#     wine_cols.append(col)
# print(wine_cols)

x = df[['fixed acidity', 'volatile acidity', 'citric acid', 
        'residual sugar', 'chlorides', 'free sulfur dioxide', 
        'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',]]

y = df[['quality']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=4)

mlr = LinearRegression()

model=mlr.fit(x_train, y_train)

y_predict = mlr.predict(x_test)

print(mlr.coef_)

print(mlr.score(x_train,y_train))

print(mlr.score(x_test,y_test))

#Test
test = [[3.4,1.7,1.0,1.5,0.036,13.0,32.0,0.9578,3.31,0.36,10.4]]

prediction = model.predict(test)

print("I predict a %.1f "%prediction)