# Author : Gaurav
# Business challenge/requirementBank of Portugal runs marketing campaign to offer loans to clients.
# Loan is offered to only clients withparticular professions. List of successful campaigns(withclientdata) is given in attached dataset.
# You have to come up with program which reads the file and builds a set of unique profession list and
# given input profession of client –system tells whether client is eligible to be approached for marketing campaign
###################################
# Pseudo Code
# 1. Read CSV using pandas
# 2. Convert professions to a set of unique values
# 3. Accept input and validate against above set
#############################################

import pandas as pd
import Pass


data= pd.read_csv("bank-data.csv")
df = pd.DataFrame(data)
set_job = set(df.job.unique())
exit_flag  = ' '

while exit_flag.upper() != "END":
    exit_flag = input("Enter profession (enter END to exit) : ")
    if  exit_flag.upper() in set_job:
        print("Eligible")
    elif exit_flag.upper() == "END":
        print("Thank you.")
    else:
        print("Not eligible")



