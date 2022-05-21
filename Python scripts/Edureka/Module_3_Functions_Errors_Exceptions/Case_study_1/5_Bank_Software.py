# Author : Gaurav
#Design a software for bank system. There should be options like cash withdraw, cash credit and change password.
# According to user input, the software should provide required output

import pandas as pd
from os.path import exists
import Pass

# if not exists('D\Python\SoftBank.csv'):
hdr = ["Username , Password ,Account_no, Balance"]
df = pd.DataFrame(hdr)
# df.loc[](["Username","Password","Account_no","Balance"])
df.to_csv('SoftBank.csv')
    # print(df)
#
# var_u_name = input("Enter username: ")
# var_token = input("Enter Password :")
#
# if pd
#
# if p.verify((var_token):
#     exit_flag = "N"
#     while exit_flag =="N":
#
#
#
#         data= pd.read_csv("tSoftBank.csv")
#         df = pd.DataFrame(data)
