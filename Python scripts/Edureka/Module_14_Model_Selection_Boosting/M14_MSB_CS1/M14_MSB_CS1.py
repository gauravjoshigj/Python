# Author: Gaurav
# Domain – Chemical Industry
# IMP : Encode and Scale data

from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing


data = pd.read_csv("bio-degradabale-data.csv", sep=';', header = None)
df = pd.DataFrame(data)
print(df.head())

df.columns = range(42)
print(df.head())

# Encode data to convert col 41 to number from string.
label_encoder = preprocessing.LabelEncoder()
df[41] = label_encoder.fit_transform(df[41])
print(df.head())

# Scale data to fix lbfgs failed to converge error.
df[:]=preprocessing.MinMaxScaler().fit_transform(df)
print(df.head())


X = data.iloc[:, 0:41]
Y = data[41]

# Begin Test Train Split
train_x, test_x, train_y, test_y = train_test_split(X, Y, random_state=5, test_size=.30)

# print('Here')

log_model = LogisticRegression()
log_model.fit(train_x, train_y)
predicted = log_model.predict(test_x)

print(metrics.accuracy_score(predicted, test_y))
print(cross_val_score(log_model, X, Y, cv=10, scoring='accuracy').mean())