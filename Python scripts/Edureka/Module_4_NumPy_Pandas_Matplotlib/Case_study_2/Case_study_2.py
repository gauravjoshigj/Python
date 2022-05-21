# Author : Gaurav
# Case Study 2
# Domain –Education

import pandas as pd


data = pd.read_csv("DSScoreTerm1.csv", usecols= ['ID','Score','Subject'])
df = pd.DataFrame(data)
# print(df.shape)
# print(df.head())
data  = pd.read_csv("MathScoreTerm1.csv",  usecols= ['ID','Score','Subject'])
# df2 = pd.DataFrame(data)
df = pd.merge(df, pd.DataFrame(pd.read_csv("MathScoreTerm1.csv",    usecols= ['ID','Score','Subject'])), on="ID", how = "inner")
df = pd.merge(df, pd.DataFrame(pd.read_csv("PhysicsScoreTerm1.csv", usecols= ['ID','Score','Subject'])), on="ID", how = "inner")

df= df[['ID','Subject','Score','Subject_x','Score_x','Subject_y','Score_y']].fillna(0)
# print(df.tail())
df.to_csv("Merged.csv",index=False)

