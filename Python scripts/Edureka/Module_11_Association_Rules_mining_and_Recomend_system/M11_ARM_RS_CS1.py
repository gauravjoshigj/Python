# Author: Gaurav
# Domain – Book recommendation engine
# Useful Links :
# https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-recommendation-engine-python/

import numpy as np
import pandas as pd
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.preprocessing import LabelEncoder

# Root mean square error
def rmse(pred, test):
    pred = pred[test.nonzero()].flatten()
    test = test[test.nonzero()].flatten()
    return sqrt(mean_squared_error(pred, test))


def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        # We use np.newaxis so that mean_user_rating has same format as ratings
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(
            ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'book':
        pred = ratings.dot(similarity) / \
            np.array([np.abs(similarity).sum(axis=1)])
    return pred


# Data is  huge so that taking only x rows
data = pd.read_csv("BX-Book-Ratings.csv")
df_ratings = pd.DataFrame(data)
df_ratings = df_ratings.head(10000)

#### Label Encoding is mandatory to encode string data into int64 dtype  ####
labelencoder = LabelEncoder()
df_ratings["isbn"] = labelencoder.fit_transform(df_ratings["isbn"])
print(df_ratings.head())

df_ratings.sort_values(["user_id", "isbn"], inplace=True)
df_ratings.reset_index()
print(df_ratings.head())
print(df_ratings.dtypes)


n_users = df_ratings["user_id"].unique().shape[0]
print("Total Users : ", n_users)

n_books = df_ratings["isbn"].unique().shape[0]
print("Total Books : ", n_books)

data_matrix = np.zeros((n_users, n_books))
print(data_matrix)

# Populate the Matrix
for line in df_ratings.head().itertuples():
    print('line is: ' ,  line[1], '   --  ',  line[1]-1,  '   --  ', line[2]-1 ,  '   --  ', line[3])
    data_matrix[line[1] - 1, line[2] - 1] = line[3]

print(data_matrix.shape)

user_similarity = pairwise_distances(data_matrix, metric='cosine')
item_similarity = pairwise_distances(data_matrix.T, metric='cosine')

user_prediction = predict(data_matrix, user_similarity, type='user')
book_prediction = predict(data_matrix, item_similarity, type='book')

print("Root mean square error of user prediction : ", rmse(user_prediction, data_matrix))
print("Root mean square error of book prediction", rmse(book_prediction, data_matrix))
