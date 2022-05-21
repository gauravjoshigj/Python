# Author: Gaurav
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

inp = 'Y'
var_str = ''

while inp == 'Y':
    var_str += input("Enter a string: ")
    inp = input("Add more lines (y/n) ?: ")
    inp = inp.upper()
    var_str += "\n"

print(var_str.upper())

