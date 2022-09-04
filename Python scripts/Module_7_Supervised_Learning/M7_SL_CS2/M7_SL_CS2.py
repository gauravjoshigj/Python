# Author: Gaurav
# Domain – Animal husbandry - Horse survival

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from pprint import pprint
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt
#Importing Confusion Matrix to describe the performance of a classification model
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV

columns = ['surgery','Age','Hospital ID','rectal temperature','pulse','respiratory rate','temperature of extremities','peripheral pulse',"mucous membranes",'capillary refill time','pain','peristalsis','abdominal distension','nasogastric tube','nasogastric reflux','nasogastric reflux PH','rectal examination - feces','abdomen',' packed cell volume','total protein','abdominocentesis appearance','abdomcentesis total protein','outcome','surgical lesion?','1','2','3','path']
df = pd.read_csv('horse.csv', header = 0, na_values='?', names = columns)
df.fillna(0)
dfs = df
print(df.head())

#Dropping columns having significant number of NaN values
df.drop('nasogastric reflux PH', axis=1, inplace = True)
df.drop('abdomcentesis total protein', axis=1, inplace = True)
df.drop('abdominocentesis appearance', axis=1, inplace = True)
df.drop('nasogastric tube', axis=1, inplace = True)
df.drop('abdomen', axis=1, inplace = True)
df.drop('rectal examination - feces', axis=1, inplace = True)

df['Age'].replace({9:2}, inplace = True)
df['outcome'].replace({1:'lived', 2:'died', 3:'euthenized'}, inplace = True)
df['Age'].replace({1:'Adult', 2:'Young'}, inplace = True)
df['pain'].replace({1:'No Pain', 2:'Depressed', 3:'Mild pain', 4:'Severe Pain', 5:'Greaterthansevere'}, inplace = True)

# dfs = df
f, ax = plt.subplots(figsize=(12, 10))

sns.heatmap(df.isnull(),cmap='Blues')
plt.show()

null = df.isnull().sum()

plt.figure(figsize=(20,10))
plt.bar(range(len(null)),null)
plt.xlabel('Features')
plt.ylabel('missing')
plt.xticks(list(range(len(df.columns))), list(df.columns.values), rotation='vertical')
plt.show()

#Columns containing NaN values
null = pd.concat([df.isnull().sum()], axis = 1, keys = ['NA'] )
null.loc[(null.NA>0)]

#Filtering columns having continous variables
for col in df.columns.values:
    if (len(df[col].value_counts())> 5) and (df[col].isnull().sum() > 0):
        print(col)

#Filling columns containing continous variables with MEAN
df['surgery'].fillna(df['surgery'].mode()[0], inplace = True)
df['rectal temperature'].fillna(df['rectal temperature'].mean(), inplace = True)
df['pulse'].fillna(df['pulse'].mean(), inplace = True)
df['respiratory rate'].fillna(df['pulse'].mean(), inplace = True)
df['mucous membranes'].fillna(df['pulse'].mean(), inplace = True)
df[' packed cell volume'].fillna(df['pulse'].mean(), inplace = True)
df['total protein'].fillna(df['total protein'].mean(), inplace = True)

##Filling columns containing categorical variables with MODE
for col in df.columns.values:
    if (df[col].isnull().sum()>0):
        if (df[col].dtype == 'float64'):
            df[col].fillna(df[col].mode()[0], inplace = True)

null = pd.concat([df.isnull().sum()], axis = 1, keys = ['NA'])
null.loc[(null['NA']>0)]

sns.countplot(data=df, x="outcome");
print(df.outcome.value_counts())

#Finding relations between features and taget variable(outcome) by visualising data
#Relation between outcome and degree of pain experienced by the horse
sns.countplot(data=df, x='outcome', hue = 'pain')

#Relation between outcome and degree of age of the horse

sns.countplot(data=df, x='outcome', hue = 'Age')
# plt.show()

#Converting variables to categorical datatype for better analysis
df['outcome'] = df['outcome'].astype('category').cat.codes
df['Age'] = df['Age'].astype('category').cat.codes
df['pain'] = df['pain'].astype('category').cat.codes

#Finding correlation between features and target variables
corr= df.corr()

core = abs(corr.outcome.sort_values(ascending = False))
core.sort_values(ascending = False)

#Heatmap of correlations
sns.heatmap(corr, vmax=0.85)
# plt.show()

#Removing columns which have insignificant impact on our target variable "outcome" (corr<0.1)
df.drop('path',axis = 1 , inplace = True)
df.drop('3',axis = 1 , inplace = True)
df.drop('rectal temperature',axis = 1 , inplace = True)
df.drop('pain',axis = 1 , inplace = True)
df.drop('mucous membranes',axis = 1 , inplace = True)

#Cleaned and processed train dataset
print(df.head())
print(df.shape)

#Visualising missing data
sns.heatmap(dfs.isnull(),cbar='Blues', cmap='Pastel1')

# plt.show()

null = dfs.isnull().sum()

plt.figure(figsize=(20,10))
plt.bar(range(len(null)),null)
plt.xlabel('Features')
plt.ylabel('missing')
plt.xticks(list(range(len(dfs.columns))), list(dfs.columns.values), rotation='vertical')
# plt.show()

###########################################################
dfs = pd.read_csv('horse.csv', header = 0, na_values='?', names = columns)

print('here : ')
print(dfs.head())
print(dfs.columns)

# Encode String to number

df['surgery'] = df['surgery'].map({'yes':1,'no':0})
df['surgical lesion?'] = df['surgical lesion?'].map({'yes':1,'no':0})
df['temperature of extremities'] = df['temperature of extremities'].map({'normal':1,'warm':2,'cool':3,'cold':4,'':0})
df['peripheral pulse'] = df['peripheral pulse'].map({'normal':1,'increased':2,'reduced':3,'absent':4,'':0})
df['capillary refill time'] = df['capillary refill time'].map({'more_3_sec':2,'less_3_sec':1,'NA':0})
df['peristalsis'] = df['peristalsis'].map({'hypermotile':1,'normal':2,'hypomotile':3,'absent':4,'NA':0})
df['abdominal distension'] = df['abdominal distension'].map({'none':1,'slight':2,'moderate':3,'severe':4,'NA':0})
df['nasogastric reflux'] = df['nasogastric reflux'].map({'none':1,'more_1_liter':2,'less_1_liter':3,'NA':0})

dfs['surgery'] = dfs['surgery'].map({'yes':1,'no':0})
dfs['surgical lesion?'] = dfs['surgical lesion?'].map({'yes':1,'no':0})
dfs['temperature of extremities'] = dfs['temperature of extremities'].map({'normal':1,'warm':2,'cool':3,'cold':4})
dfs['peripheral pulse'] = dfs['peripheral pulse'].map({'normal':1,'increased':2,'reduced':3,'absent':4})
dfs['capillary refill time'] = dfs['capillary refill time'].map({'more_3_sec':2,'less_3_sec':1})
dfs['peristalsis'] = dfs['peristalsis'].map({'hypermotile':1,'normal':2,'hypomotile':3,'absent':4})
dfs['abdominal distension'] = dfs['abdominal distension'].map({'none':1,'slight':2,'moderate':3,'severe':4})
dfs['nasogastric reflux'] = dfs['nasogastric reflux'].map({'none':1,'more_1_liter':2,'less_1_liter':3})

df = df.replace(np.nan, 0)
dfs = dfs.replace(np.nan, 0)

#Dropping columns with significant number of missing values
dfs.drop('nasogastric reflux PH', axis=1, inplace = True)
dfs.drop('abdomcentesis total protein', axis=1, inplace = True)
dfs.drop('abdominocentesis appearance', axis=1, inplace = True)
dfs.drop('nasogastric tube', axis=1, inplace = True)
dfs.drop('abdomen', axis=1, inplace = True)
dfs.drop('rectal examination - feces', axis=1, inplace = True)

dfs.drop('path',axis = 1 , inplace = True)
dfs.drop('3',axis = 1 , inplace = True)
dfs.drop('rectal temperature',axis = 1 , inplace = True)
dfs.drop('pain',axis = 1 , inplace = True)
dfs.drop('mucous membranes',axis = 1 , inplace = True)

dfs['Age'].replace({9:2}, inplace = True)
dfs['outcome'].replace({1:'lived', 2:'died', 3:'euthenized'}, inplace = True)
dfs['Age'].replace({1:'Adult', 2:'Young'}, inplace = True)

null = pd.concat([dfs.isnull().sum()], axis = 1, keys = ['NA'] )
null.loc[(null.NA>0)]

for col in dfs.columns.values:
    if (len(dfs[col].value_counts())> 5) and (dfs[col].isnull().sum() > 0):
        print(col)

dfs['surgery'].fillna(dfs['surgery'].mode()[0], inplace = True)
dfs['pulse'].fillna(dfs['pulse'].mean(), inplace = True)
dfs['respiratory rate'].fillna(dfs['pulse'].mean(), inplace = True)
dfs[' packed cell volume'].fillna(dfs['pulse'].mean(), inplace = True)
dfs['total protein'].fillna(dfs['total protein'].mean(), inplace = True)

for col in dfs.columns.values:
    if (dfs[col].isnull().sum()>0):
        if (dfs[col].dtype == 'float64'):
            dfs[col].fillna(df[col].mode()[0], inplace = True)

null = pd.concat([dfs.isnull().sum()], axis = 1, keys = ['NA'])
(null.loc[(null['NA']>0)])

dfs.dropna(axis=0, inplace =True)

dfs['outcome'] = dfs['outcome'].astype('category').cat.codes
dfs['Age'] = dfs['Age'].astype('category').cat.codes

print(dfs.head())
df.to_csv('Test.csv', index=False)

#Separating features and target variable from both test and train dataset
xtrain = df.drop("outcome", axis=1)
ytrain = df["outcome"]
xtest  = dfs.drop("outcome", axis=1)
ytest  = dfs["outcome"]

#RandomForestClassifier Model

rf = RandomForestClassifier(random_state=14 , n_jobs= -1)
pprint(rf.get_params())

# #RandomizedSearchCV for best hyperparameter range

n_est=[100,140,180,220]
bootstrap = [True,False]
msl = [2,3,4]
mss=[1,2,3]
mf=[.5,1,'auto']
criterion = ['gini', 'entropy']
maxd=[10,15,20,30,40,None]
# #
random_grid = {'n_estimators': n_est,
               'max_features': mf,
               'max_depth': maxd,
               'min_samples_split': mss,
               'min_samples_leaf': msl,
               'bootstrap': bootstrap,
               'criterion' : criterion}

pprint(random_grid)

rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 5, verbose=2, random_state=14, n_jobs = -1)
# #
rf_random.fit(xtrain, ytrain)

rf_random.best_params_

#GridSearchCV for finding better hyperparameters
from sklearn.model_selection import GridSearchCV
grid_param= {'n_estimators':[150, 180, 200,300,500],
             'min_samples_split':[2,4,6],
             'min_samples_leaf': [1,2,3,4],
             'max_features': [0.5, 'auto'],
             'max_depth': [10,15,20],
             'criterion': ['entropy'],
             'bootstrap': [True]}

rf = RandomForestClassifier()

grid_search =  GridSearchCV(estimator = rf, param_grid = grid_param,
                          cv = 3, n_jobs = -1, verbose = 2)

grid_search.fit(xtrain, ytrain)

grid_search.best_params_

#Random Forest Classifier Model
rf = RandomForestClassifier(n_estimators=300, criterion='entropy', min_samples_leaf=2,
                            min_samples_split=4,
                            max_depth=10)
rf.fit(xtrain, ytrain)
rf.score(xtrain, ytrain)

pred = rf.predict(xtest)
#Confusion Matrix for Random Forest
actual = ytest
predicted = pred
result = confusion_matrix(actual,predicted)


print ('Confusion Matrix :')
print(result)
print('Accuracy Score :',accuracy_score(actual, predicted))
print ('Report : ')
print (classification_report(actual, predicted))

#Decision tree Classifier Model

dt = DecisionTreeClassifier(max_depth = 3)
dt.fit(xtrain, ytrain)

prediction = dt.predict(xtest)
#Confusion Matrix for Decision Tree
actual = ytest
predicted = prediction
result = confusion_matrix(actual,predicted)

print ('Confusion Matrix :')
print(result)
print('Accuracy Score :',accuracy_score(actual, predicted))
print ('Report : ')
print (classification_report(actual, predicted) )

accuracy_dt= round(dt.score(xtrain, ytrain) * 100, 2)
accuracy_rf= round(rf.score(xtrain, ytrain) * 100, 2)
print("Train accuracy of Random Forest Classifier is ",accuracy_rf,"%")
print("Train accuracy of Decision Tree Classifier is ",accuracy_dt,"%")