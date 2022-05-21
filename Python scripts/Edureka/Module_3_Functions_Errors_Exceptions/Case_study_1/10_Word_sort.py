# Author: Gaurav
# Program to sort alphabetically the words form a string provided by the user

var_str = input("Enter a string: ")
words = [word for word in var_str.split(',')]
words.sort()
print(words)