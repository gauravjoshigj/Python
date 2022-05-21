# Author : Gaurav
# Problem 5 :How  do  you  Count  The  Number  Of  Times  Each  Value  Appears  In  An  Array  Of Integers?
#

import numpy as np


print("########################## Problem 5 ##########################")
arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
count_arr = np.bincount(arr)
print(count_arr)


#############################################################
# Problem 6 :
# Create a numpyarray [[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]]) and filter the elements greater than 5

print("########################## Problem 6 ##########################")
arr = np.array([[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]])
print(arr[np.where(arr >5)])


#############################################################
# Problem 7 :
# Create a numpy array having NaN (Not a Number) and print it

print("########################## Problem 7 ##########################")
a = np.array([np.nan, 1,2,np.nan,3,4,5])
print(a)
print(a[~np.isnan(a)])


#############################################################
# Problem 8 :#
# Create  a  10x10  array  with  random  values  and  find  the  minimum  and  maximum values

print("########################## Problem 8 ##########################")
a = np.random.randint(1, 1000, size=(10, 10))
print(a)
print("Min :" , np.min(a), ' Max :' , np.max(a))


#############################################################
# Problem 9 :#
# Create a random vector of size 30 and find the mean value.

print("########################## Problem 9 ##########################")
a = np.random.randint(1, 1000, size = (1,30))
print(a,' The mean is ' , np.mean(a))


#############################################################
# Problem 10 :#
# Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9

print("########################## Problem 10 ##########################")
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11])
# a= a[a>=3]  *-1
a[ (a >= 3) & (a <=9) ] *=  -1
print(a)


#############################################################
# Problem 11 :
# Create a random array of 3 rows and 3 columns and sort it according to 1stcolumn, 2ndcolumn or 3rdcolumn
print("########################## Problem 11 ##########################")
#
a = np.random.randint(1, 100,  (3,3))
print('Original array : ',a)
a= np.array(sorted(a, key=lambda x: x[0]))
print('Sorted array :', a)


#############################################################
# Problem 12 :
# Create a random array of 3 rows and 3 columns and sort it according to 1stcolumn, 2ndcolumn or 3rdcolumn
print("########################## Problem 12 ##########################")
#
a = np.random.randint(1, 100,  (4,4,4,4))
print('Input array :',a)
print('Sum' ,a.sum(axis=2),a.sum(axis=3))


#############################################################
# Problem 13 :#
# Create a random array and swap two rows of an array
print("########################## Problem 13 ##########################")
#
a = np.random.randint(1, 100,  (4,3))
print('Input array :',a)
a[[0,2]] = a[[2,0]]
print('Post row swap: ',a)


#############################################################
# Problem 14 :
# Create a random array and swap two rows of an array
print("########################## Problem 14 ##########################")
print('Rank of above array: ',np.linalg.matrix_rank(a))