# By Gaurav
# Problem : Write a program, whichwill find all the numbers between 1000 and 3000 (both included)
# such that each digit of a number is an even number.
# The numbers obtained should be printed in a comma separated sequence on a single line
################################################
# Pseudo Code:
#   1. Take list as Input, Sort list
##########################################
# Complexity :
#   1. Search : O(1)
#   2. Space :  O(1)


def print_evens(m  ,n  ):
    for i in range(m,n):
        var_list = list(str(i))
        # print(var_list)
        all_even = 'Y'
        for x in var_list:
            # print (x)
            if int(x) % 2 == 0:
                continue;
            else:
                all_even = 'N'
                break

        if all_even == 'Y':
            print('' ,i)

begin = input("Enter start number: ")
end = input("Enter end number: ")
print ( 'Numbers with all digits even are :')
print_evens (int(begin),int(end))


