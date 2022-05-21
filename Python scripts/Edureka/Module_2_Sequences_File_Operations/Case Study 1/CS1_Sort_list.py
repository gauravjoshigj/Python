# By Gaurav
# Problem : Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
################################################
# Pseudo Code:
#   1. Take list as Input, Sort list
##########################################
# Complexity :
#   1. Search : O(1)
#   2. Space :  O(1)

def sort_list():
    var_str = input("Enter your string: ")
    val = list(var_str)
    val.sort()
    print (val)

sort_list()