# By Gaurav
# Problem : Write a program which will find factors of given number and find whether the factor is even or odd
################################################
# Pseudo Code:
#   1. Loop n items,print Factors
##########################################
# Complexity :
#   1. Search : O(N)
#   2. Space :  O(1)

def factors(n):
    print("The factors of", n, "are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

num = 320

factors(num)

######################