# Author: Gaurav
# Domain – Veribrates- Animal classification
#


from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics


data = pd.read_csv("zoo.csv")
df = pd.DataFrame(data)
df.drop(["animal_name"], axis = 1, inplace=True)  # remove string columns
print(df.head())

# Find Unique class types
unique_classtypes = np.unique(df["class_type"].values)

# Initialize Agglomerative Clustering
agglo = AgglomerativeClustering(n_clusters=4)
predicted_values = agglo.fit_predict(df.iloc[:, 0:16])

# Accuracy Score
print("Accuracy Score")
print(metrics.accuracy_score(predicted_values, df["class_type"].values))

# Mean Square Error value
print("Mean Squared Error value")
print(metrics.mean_squared_error(predicted_values, data["class_type"].values))