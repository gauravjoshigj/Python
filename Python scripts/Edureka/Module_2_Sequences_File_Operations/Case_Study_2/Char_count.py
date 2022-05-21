# By Gaurav
# Problem :count occurance of each characters in a string
#

import pandas as pd

var_list = input(" Enter a string")
print(pd.Series(list(var_list)).value_counts())