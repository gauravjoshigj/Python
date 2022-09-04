# Author: Gaurav
# Domain – Finance- Loans - Lower NPA (Non Performing Asset)

import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt

columns = ['surgery','Age','Hospital ID','rectal temperature','pulse','respiratory rate','temperature of extremities','peripheral pulse',"mucous membranes",'capillary refill time','pain','peristalsis','abdominal distension','nasogastric tube','nasogastric reflux','nasogastric reflux PH','rectal examination - feces','abdomen',' packed cell volume','total protein','abdominocentesis appearance','abdomcentesis total protein','outcome','surgical lesion?','1','2','3','path']
df = pd.read_csv('loan_borowwer_data.csv')
df.fillna(0)
print(df.head())

plt.figure(figsize=(10,6))
df[df['credit.policy']==0]['fico'].hist(bins=30,alpha=0.5,label='credit policy 0')
df[df['credit.policy']==1]['fico'].hist(color='red',bins=30,alpha=0.5,label='credit policy 1')
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
df[df['not.fully.paid']==0]['fico'].hist(color='green',bins=30,alpha=0.5,label='not full paid 0')
df[df['not.fully.paid']==1]['fico'].hist(color='red',bins=30,alpha=0.5,label='not full paid 1')
plt.legend()
plt.show()

plt.figure(figsize=(15,7))
sns.countplot(x=df['purpose'],hue=df['not.fully.paid'])
plt.show()

data = pd.get_dummies(df,columns=['purpose'],drop_first=True)

final_data = data[:]
final_data.drop(['inq.last.6mths'], axis=1, inplace=True)
final_data.drop(['not.fully.paid'], axis=1, inplace=True)
predict_var = final_data.columns
print (list(predict_var))

x = final_data
y = data['not.fully.paid']
x_train,x_test,y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)

model = tree.DecisionTreeClassifier()
model.fit(x_train,y_train)
prediction = model.predict(x_test)

print ('here')
print (metrics.accuracy_score(y_test, prediction))
print (metrics.confusion_matrix(prediction,y_test))

classifier = RandomForestClassifier(n_estimators=100)
classifier.fit(x_train, y_train)
pred = classifier.predict(x_test)
print (metrics.accuracy_score(pred, y_test))

print (metrics.confusion_matrix(pred,y_test))
