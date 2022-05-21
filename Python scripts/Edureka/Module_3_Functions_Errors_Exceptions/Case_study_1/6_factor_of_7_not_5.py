# Author: Gaurav
#  Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#  between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line


def get_nums(m  ,n  ):
    ret_val = []
    for i in range(m,n+1):
         if i% 7 ==0 and i%5 != 0:
             ret_val.append(str(i))
    return ret_val

begin = input("Enter start number: ")
end = input("Enter end number: ")
print(get_nums (int(begin),int(end)))
