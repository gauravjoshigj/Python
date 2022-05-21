# By Gaurav
# Problem : Check if an array list is palindrome or not
# Pseudo Code:
#   1. Compare values at both ends upto mid point
#   2. Break when value does not match
#   3. Return true when end_index at mid
##########################################
# Complexity :
#   1. Search : O(N)
#   2. Space :  O(1)

import math

def verify ():
    list_to_check =  [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    # list_to_check = ['A','B','C','B','A','z']
    start_idx = 0
    end_idx = len(list_to_check) -1
    mid = math.ceil((start_idx + end_idx) / 2)
    print(start_idx, '|', end_idx)
    for i in range (1,len(list_to_check)):


        if list_to_check[start_idx] == list_to_check[end_idx]:
            if start_idx == end_idx or end_idx == mid:
                return 'Palindrome'
            start_idx += 1
            end_idx -= 1
            print(start_idx, '|', end_idx)

        else:
            return 'Not a valid Palindrome'

    return 'Palindrome'

result = verify()

print (result)

