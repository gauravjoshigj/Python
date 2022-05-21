# By Gaurav
# Problem : Write a program that accepts a sentence and calculate the number of letters and digits.
################################################
# Pseudo Code:
#   1. Take string as Input, count digits and letters
################################################
# Complexity :
#   1. Search : O(n)
#   2. Space :  O(2)

def count_dig_alpha(var):
    var_result = [0,0]
    for i in var:
        if i.isdigit():
            var_result[0] = var_result[0]+1
        else: #i.isalpha():
            var_result[1] = var_result[1]+1

    return var_result

var_list = input("Enter a alphanumeric sentence : ")

res = count_dig_alpha(var_list)

print ('Total digits :',res[0] , '| Total charactes :' , res[1])
