# By Gaurav
# Problem :
# A website requires a user to input username and password to register.
# Write a program to check the validity of password given by user.
# Following are the criteria for checking password:
#     1. At least 1 letter between [a-z]
#     2. At least 1 number between [0-9]
#     3. At least 1 letter between [A-Z]
#     4. At least 1 character from [$#@]
#     5. Minimum length of transaction password: 6
#     6. Maximum length of transaction password: 12
################################################
# Pseudo Code:
#   1. Loop over string, apply length validation then rest using case
##########################################
# Complexity :
#   1. Search : O(N)
#   2. Space :  O(1)

import re

def verify(var_list):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$!#%*?&]{6,12}$"

    # compiling regex
    pat = re.compile(regex)

    # searching regex
    mat = re.search(pat, var_list)

    # validating conditions
    if mat:
        print("Password is valid.")
        return True
    else:
        print("""Password invalid !! :  
                    Following is the criteria for valid password:
                     1. At least 1 letter between [a-z]
                     2. At least 1 number between [0-9]
                     3. At least 1 letter between [A-Z]
                     4. At least 1 character from [$#@]
                     5. Minimum length of transaction password: 6
                     6. Maximum length of transaction password: 12 """)
        return False
