# By Gaurav
#


var_list = [12,24,35,24,88,120,155]

############################# Problem 1
#By usinglist comprehension, please write a program to print the list
# after removing the value 24 in [12,24,35,24,88,120,155].
#
def remove_item ():
  while var_list.count(24) != 0:
     var_list.remove(24)
  print ('Remove all 24 :', var_list)

remove_item()
############################# Problem 2
#By using list comprehension, please write a program to print the list
# after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]
# Run reverse order as index changes when you pop

var_list = [12,24,35,70,88,120,155]

var_list.pop(5)
var_list.pop(4)
var_list.pop(0)
print('Remove from index 0,4,5 :', var_list)


############################# Problem 3
#  By using list comprehension, please write a program to print the list
#  after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]

var_list = [12,24,35,70,88,120,155]

for i in var_list:
    if i % 5 == 0 or i % 7 == 0:
        var_list.remove(i)

print('Removed multiples of 5 and 7 :' , var_list)




