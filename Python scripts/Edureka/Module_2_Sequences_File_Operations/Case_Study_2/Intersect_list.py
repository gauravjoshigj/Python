# By Gaurav
# Problem : With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the above given lists.
#

var_set_1 = set([1,3,6,78,35,55])
var_Set_2 = set([3,12,24,35,24,88,120,155])
print (var_set_1|var_Set_2)