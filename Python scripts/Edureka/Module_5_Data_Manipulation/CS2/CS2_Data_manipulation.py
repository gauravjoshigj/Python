# Author: Gaurav
# Domain –HR

import pandas as pd

pd.options.display.float_format = '{:.2f}'.format

data = pd.read_csv("Salaries.csv",low_memory=False)  # not a good practice
df = pd.DataFrame(data)
print(df.dtypes)

#############################################################
# Problem 1 :
# Compute how much total salary cost has increased from year 2011 to 2014
# Id,EmployeeName,  JobTitle,    BasePay,  OvertimePay,OtherPay,Benefits,TotalPay, TotalPayBenefits,Year,Notes,Agency,       Status
# 1, NATHANIEL FORD,GENERAL MA<>,167411.18,0,          400184.25,,       567595.43, 567595.43,      2011,,     San Francisco,
print("########################## Problem 1 ##########################")
# df2 = pd.DataFrame(pd.DataFrame(df.loc[(df['Year'].isin([2011,2014]))])[['Year','TotalPayBenefits']].groupby("Year", as_index= False ).sum())


df2 = pd.DataFrame(pd.DataFrame(df.loc[(df['Year'].isin([2011,2014]))]).groupby("Year", as_index= False ).sum())

rup = 'a'
# df2 = df2.groupby("Year", as_index= False ).sum()
print(df2)

# print(df2.loc[1]['TotalPayBenefits'])
diff = abs(df2.iloc[1]['TotalPayBenefits'] - df2.iloc[0]['TotalPayBenefits'])

print('Total Salary increase from 2011 to 2014 : ',diff)

