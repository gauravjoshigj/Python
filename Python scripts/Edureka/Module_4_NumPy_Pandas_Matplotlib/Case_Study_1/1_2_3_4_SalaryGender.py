# Author : Gaurav
# Extract data from the givenSalaryGender CSV file and store the data from each column in a separate NumPy array
#

import pandas as pd
import numpy

data= pd.read_csv("../Dataset/SalaryGender.csv")
df = pd.DataFrame(data)
npy_sal_array = df[['Salary']].to_numpy()
npy_sex_arr = df[['Gender']].to_numpy()
npy_age_arr = df[['Age']].to_numpy()
npy_phd_arr = df[['PhD']].to_numpy()
# print(npy_sal_array,npy_sex_arr)

#############################################################
# Problem 2 :
# Find:1. The number of men with a PhD
# 2. The number of women with a PhD3

# print(df['PhD'] == '1')
# df.info()
# print(df[df['PhD'] == 1])

# df_grp_by_gender = df.query('PhD  == 1').groupby('Gender')['PhD'].count()

# df_grp_by_gender = df.query('PhD  == 1').groupby('Gender')['PhD']
print("########################## Problem 2 ##########################")
print('Count of Phds grouped by :', df.query('PhD  == 1').groupby('Gender')['PhD'].count())


#############################################################
# Problem 3 :
# Use SalaryGender CSV file. Store the “Age” and “PhD” columns in one DataFrame and
# delete the data of all people who don’t have a PhD


print("########################## Problem 3 ##########################")
df2 = df[['Age','PhD']]
print('Count of Phds in df2 :', df2.query('PhD  == 0').groupby('PhD')['PhD'].count() )
df2 = df2.drop(df2[df2.PhD == 0].index)
# print('Count of Phds in df2 :', df2.query('PhD  == 1').count())
print(df2)


#############################################################
# Problem 4 :
# Calculate the total number of people who have a PhD degreefrom SalaryGender CSV file

print("########################## Problem 4 ##########################")
print('Count of people with Phds in df :', df.query('PhD  == 1')['PhD'].count())

# print(df.loc[0])
df2 = pd.DataFrame(df.loc[0])
# print(type(df2))


df.query('PhD  == 1')