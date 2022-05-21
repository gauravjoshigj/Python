# By Gaurav
# Problem : Write a for loop that prints all elements of a list and their position in the list.a = [4,7,3,2,5,9]
################################################
# Pseudo Code:
#   1. Loop over and print index, duh
##########################################
# Complexity :
#   1. Search : O(N)
#   2. Space :  O(1)

def Print(var_list, even_flag ):
    ret_val = []
    for i in range(0,len(var_list)):
        if even_flag == 'Y':
            if i % 2 == 0:
                ret_val.append(var_list[i])
        else:
            print('Value ', var_list[i], 'at index', i)

    # convert to string
    ret_val = ''.join(map(str, ret_val))

    return ret_val

ret_val= Print("H1e2l3l4o5w6o7r8l9d",'Y')

print (str(ret_val))