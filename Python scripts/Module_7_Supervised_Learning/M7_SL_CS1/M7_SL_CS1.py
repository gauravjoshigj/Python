# Author: Gaurav
# Domain – Voice

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:.2f}'.format
data = pd.read_csv("voice.csv", low_memory=False, header=0)   # not a good practice

data['label'] = data['label'].map({'male':1,'female':0})
df = pd.DataFrame(data)

print(df.head())
label_encoder = preprocessing.LabelEncoder()
df["label"] = label_encoder.fit_transform(df["label"])

df[:]=preprocessing.MinMaxScaler().fit_transform(df) # Scale data to fix lbfgs failed to converge error
df.head()

X = df.drop(["label"], axis = 1 )
y = df["label"]

print(y)

# train_x,test_x,train_y, test_y = train_test_split(X,y,test_size=0.20, random_state = 42)

train,test = train_test_split(df,test_size=0.20, random_state = 42)

x_train = train.iloc[:, :-1]
y_train = train["label"]
x_test = test.iloc[:, :-1]
y_test = test["label"]

print(x_train.head())
# print(train_y.head())
print("Train test split done")

logistic = LogisticRegression()

logistic.fit(x_train , y_train)

temp = logistic.predict(x_test)

print(metrics.accuracy_score(temp,y_test))


#############################################################
# Problem 3 : Compute the correlation matrix that describes the dependence between all predictors and identify the predictors
# that are highly correlated. Plot the correlation matrix using seaborn heatmap.
# [Hint: Explore dataframe methods to identify appropriate method]

matrix = df.corr()

# print correlation matrix
print("Correlation Matrix is : ")
print(matrix)

corr = df.corr()
#
# Set up the matplotlib plot configuration
#
f, ax = plt.subplots(figsize=(12, 10))
#
#
# Draw the heatmap
#
sns.heatmap(corr, annot=True, cmap='Blues')

plt.show()
